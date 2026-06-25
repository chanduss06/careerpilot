"""
CareerPilot Prompt Injection Detector

Phase 4
"""

from src.security.base_detector import BaseDetector
from src.security.security_rules import PROMPT_INJECTION_RULES


class PromptInjectionDetector(BaseDetector):
    """
    Detects prompt injection attempts.
    """

    CATEGORY = "PROMPT_INJECTION"

    def __init__(self):
        super().__init__(PROMPT_INJECTION_RULES)