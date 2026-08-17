"""
Purpose: Initialize the Gemini LLM client, the Sentence-Transformers
         embedding model, and the trained risk-prediction model (XGBoost +
         scaler) ONCE at application startup, and expose them as
         module-level singletons for the rest of the app to import.
Inputs: GEMINI_API_KEY (via backend/config.py Settings)
        app/models/xgboost_model.pkl, app/models/scaler.pkl (trained artifacts)
Outputs: get_llm_client() -> genai.GenerativeModel
         get_embedding_model() -> SentenceTransformer
         get_risk_model() -> xgboost.XGBClassifier | None
         get_risk_scaler() -> sklearn scaler | None
Depends on: backend/config.py (Settings), google-generativeai, sentence-transformers, joblib
Called by: backend/main.py (at startup), rag/embeddings.py, agents/*_agent.py,
           app/ml/risk_prediction.py (via app/api/simulator.py, app/api/dashboard.py)
"""

import logging
from pathlib import Path

import google.generativeai as genai

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    SentenceTransformer = None

from backend.config import get_settings

logger = logging.getLogger(__name__)

GEMINI_MODEL_NAME = "gemini-1.5-pro"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

_MODELS_DIR = Path(__file__).resolve().parent
_RISK_MODEL_PATH = _MODELS_DIR / "xgboost_model.pkl"
_RISK_SCALER_PATH = _MODELS_DIR / "scaler.pkl"

_llm_client = None
_embedding_model = None
_risk_model = None
_risk_scaler = None
_initialized = False


def initialize() -> None:
    """Initialize Gemini + embedding model + risk model exactly once.
    Call at app startup (see backend/main.py lifespan)."""
    global _llm_client, _embedding_model, _risk_model, _risk_scaler, _initialized

    if _initialized:
        logger.info("model_loader.initialize() called again — skipping, already initialized.")
        return

    settings = get_settings()

    if not settings.gemini_api_key:
        logger.warning(
            "GEMINI_API_KEY is not set. Gemini LLM will be unavailable. "
            "AI agents will use deterministic fallback logic."
        )
        print("WARNING: GEMINI_API_KEY not set — LLM features disabled, using fallbacks.")
    else:
        logger.info("Initializing Gemini client with model=%s", GEMINI_MODEL_NAME)
        genai.configure(api_key=settings.gemini_api_key)
        _llm_client = genai.GenerativeModel(GEMINI_MODEL_NAME)

    logger.info("Loading embedding model=%s", EMBEDDING_MODEL_NAME)
    if SentenceTransformer is not None:
        _embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    else:
        logger.warning("sentence-transformers not installed — embedding model unavailable.")
        _embedding_model = None

    _risk_model, _risk_scaler = _load_risk_model()

    _initialized = True
    logger.info("model_loader initialization complete.")


def _load_risk_model():
    """Load the trained XGBoost risk model + scaler from disk.

    Returns (None, None) instead of raising if the .pkl files haven't been
    trained yet, so a missing risk model degrades the Risk/Simulator
    features gracefully instead of crashing the whole app at startup.
    """
    if not _RISK_MODEL_PATH.exists() or not _RISK_SCALER_PATH.exists():
        logger.warning(
            "Risk model artifacts not found at %s / %s — risk scoring will "
            "be unavailable until they are trained (see scripts/train_risk_model.py).",
            _RISK_MODEL_PATH, _RISK_SCALER_PATH,
        )
        return None, None

    import joblib

    try:
        model = joblib.load(_RISK_MODEL_PATH)
        scaler = joblib.load(_RISK_SCALER_PATH)
        logger.info("Risk model + scaler loaded from %s", _MODELS_DIR)
        return model, scaler
    except Exception as exc:  # noqa: BLE001
        logger.error("Failed to load risk model artifacts: %s", exc)
        return None, None


def get_llm_client():
    if _llm_client is None:
        raise RuntimeError(
            "LLM client not initialized. Call model_loader.initialize() "
            "at app startup before requesting the client."
        )
    return _llm_client


def get_embedding_model():
    if _embedding_model is None:
        raise RuntimeError(
            "Embedding model not initialized. Call model_loader.initialize() "
            "at app startup before requesting the model."
        )
    return _embedding_model


def get_risk_model():
    """Returns the trained XGBoost risk model, or None if not yet trained."""
    return _risk_model


def get_risk_scaler():
    """Returns the fitted scaler for the risk model, or None if not yet trained."""
    return _risk_scaler


def is_initialized() -> bool:
    return _initialized