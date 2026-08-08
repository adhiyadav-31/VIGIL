import datetime

def get_base_template(content: str) -> str:
    """Base HTML wrapper matching VIGIL branding."""
    current_year = datetime.datetime.now().year
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
                background-color: #0f172a;
                color: #f1f5f9;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                background-color: #1e293b;
                border: 1px solid #334155;
                border-radius: 8px;
                overflow: hidden;
            }}
            .header {{
                background-color: #0f172a;
                padding: 24px;
                text-align: center;
                border-bottom: 1px solid #334155;
            }}
            .header h1 {{
                display: inline-block;
                margin: 0;
                color: #38bdf8;
                font-size: 24px;
                font-weight: 700;
                vertical-align: middle;
            }}
            .content {{
                padding: 32px 24px;
                color: #cbd5e1;
                font-size: 16px;
                line-height: 1.6;
            }}
            .content h2 {{
                color: #f8fafc;
                margin-top: 0;
                margin-bottom: 16px;
                font-size: 20px;
            }}
            .cta-button {{
                display: inline-block;
                background-color: #3b82f6;
                color: #ffffff;
                text-decoration: none;
                padding: 12px 24px;
                border-radius: 6px;
                font-weight: 600;
                margin-top: 24px;
                margin-bottom: 24px;
            }}
            .cta-button:hover {{
                background-color: #2563eb;
            }}
            .footer {{
                background-color: #0f172a;
                padding: 24px;
                text-align: center;
                font-size: 14px;
                color: #64748b;
                border-top: 1px solid #334155;
            }}
            .footer a {{
                color: #38bdf8;
                text-decoration: none;
            }}
        </style>
    </head>
    <body>
        <div style="padding: 40px 20px;">
            <div class="container">
                <div class="header">
                    <h1>VigilAI</h1>
                </div>
                <div class="content">
                    {content}
                </div>
                <div class="footer">
                    <p>Need help? Contact us at <a href="mailto:support@vigilai.com">support@vigilai.com</a></p>
                    <p>&copy; {current_year} VigilAI Systems. All rights reserved.</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

def get_lease_request_template(asset_name: str, owner_name: str, requester_name: str = "A user", date: str = None) -> str:
    if date is None:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        
    content = f"""
    <h2>New Lease Request</h2>
    <p>Hi {owner_name},</p>
    <p><strong>{requester_name}</strong> is interested in leasing your asset:</p>
    <div style="background-color: #334155; padding: 16px; border-radius: 6px; margin: 16px 0;">
        <strong style="color: #f8fafc; font-size: 18px;">{asset_name}</strong>
    </div>
    <p>Date Requested: {date}</p>
    <p>Please find the attached PDF containing the comprehensive summary of this product.</p>
    <p>Best regards,<br>The VigilAI Team</p>
    """
    return get_base_template(content)
