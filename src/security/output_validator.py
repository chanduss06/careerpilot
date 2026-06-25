"""
CareerPilot Output Validator

Detects sensitive information that should
not be returned to the user.

Phase 4
"""

from src.security.base_detector import BaseDetector
from src.security.security_rules import OUTPUT_VALIDATION_RULES


class OutputValidator(BaseDetector):
    """
    Detect sensitive output leakage.
    """

    CATEGORY = "OUTPUT_VALIDATION"

    def __init__(self):
        super().__init__(OUTPUT_VALIDATION_RULES)