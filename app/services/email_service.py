import os
import httpx
import logging
from typing import Optional, Dict, Any, List

logger = logging.getLogger(__name__)

class EmailConfigurationError(Exception):
    pass

class EmailDeliveryError(Exception):
    pass

class EmailService:
    def __init__(self):
        # Prefer MAILJET_ specific vars, fallback to the SMTP vars provided in instructions
        self.api_key = os.getenv("MAILJET_API_KEY") or os.getenv("NOTIFICATION_SMTP_USER")
        self.secret_key = os.getenv("MAILJET_SECRET_KEY") or os.getenv("NOTIFICATION_SMTP_PASSWORD")
        self.from_email = os.getenv("MAIL_FROM_EMAIL") or os.getenv("NOTIFICATION_EMAIL_FROM")
        self.from_name = os.getenv("MAIL_FROM_NAME") or "VigilAI Automated System"

        self._validate_config()
        self.api_url = "https://api.mailjet.com/v3.1/send"

    def _validate_config(self):
        missing = []
        if not self.api_key:
            missing.append("MAILJET_API_KEY")
        if not self.secret_key:
            missing.append("MAILJET_SECRET_KEY")
        if not self.from_email:
            missing.append("MAIL_FROM_EMAIL")

        if missing:
            logger.error(f"EmailService init failed. Missing env vars: {', '.join(missing)}")
            raise EmailConfigurationError(f"Missing required environment variables: {', '.join(missing)}")

    async def _send_via_mailjet(self, to_email: str, subject: str, text_part: Optional[str] = None, html_part: Optional[str] = None, to_name: str = "Recipient", attachments: Optional[List[Dict[str, str]]] = None) -> Dict[str, Any]:
        """Core method to dispatch the email via Mailjet REST API asynchronously."""
        
        message_payload = {
            "From": {
                "Email": self.from_email,
                "Name": self.from_name
            },
            "To": [
                {
                    "Email": to_email,
                    "Name": to_name
                }
            ],
            "Subject": subject
        }
        
        if text_part:
            message_payload["TextPart"] = text_part
        if html_part:
            message_payload["HTMLPart"] = html_part
        if attachments:
            message_payload["Attachments"] = attachments

        payload = {
            "Messages": [message_payload]
        }

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.post(
                    self.api_url,
                    auth=(self.api_key, self.secret_key),
                    json=payload
                )

            if response.status_code >= 400:
                logger.error(f"Mailjet API Error ({response.status_code}): {response.text}")
                raise EmailDeliveryError(f"Mailjet API returned {response.status_code}")
                
            return response.json()
            
        except httpx.RequestError as e:
            logger.error(f"Mailjet Network Error: {str(e)}")
            raise EmailDeliveryError(f"Network error while calling Mailjet: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error in email delivery: {str(e)}")
            raise EmailDeliveryError(str(e))

    async def send_email(self, to_email: str, subject: str, text_content: str) -> bool:
        """Send a plain text email."""
        try:
            await self._send_via_mailjet(to_email=to_email, subject=subject, text_part=text_content)
            return True
        except (EmailConfigurationError, EmailDeliveryError):
            return False

    async def send_html_mail(self, to_email: str, subject: str, html_content: str, text_fallback: str = "", attachments: Optional[List[Dict[str, str]]] = None) -> bool:
        """Send an HTML email with optional plain text fallback and attachments."""
        try:
            await self._send_via_mailjet(to_email=to_email, subject=subject, html_part=html_content, text_part=text_fallback, attachments=attachments)
            return True
        except (EmailConfigurationError, EmailDeliveryError):
            return False

    async def send_template_mail(self, to_email: str, subject: str, template_name: str, context: Dict[str, Any], attachments: Optional[List[Dict[str, str]]] = None) -> bool:
        """Send an email using a predefined template.
        Currently supports: 'lease_request'. 
        Can be expanded for Welcome, OTP, etc.
        """
        from app.services.templates import get_lease_request_template
        
        html_content = ""
        if template_name == "lease_request":
            html_content = get_lease_request_template(
                asset_name=context.get("asset_name", "Asset"),
                owner_name=context.get("owner_name", "Owner"),
                requester_name=context.get("requester_name", "A user")
            )
        else:
            logger.error(f"Unknown email template requested: {template_name}")
            return False
            
        return await self.send_html_mail(to_email, subject, html_content, attachments=attachments)

# Export a singleton instance getter or factory
def get_email_service() -> EmailService:
    return EmailService()
