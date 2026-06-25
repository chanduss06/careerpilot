"""
CareerPilot Jailbreak Detector

Phase 4
"""

from src.security.base_detector import BaseDetector
from src.security.security_rules import JAILBREAK_RULES


class JailbreakDetector(BaseDetector):
    """
    Detects jailbreak attempts.
    """

    CATEGORY = "JAILBREAK"

    def __init__(self):
        super().__init__(JAILBREAK_RULES)