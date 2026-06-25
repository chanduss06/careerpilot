"""
CareerPilot Base Security Detector

Provides reusable detection logic for all
rule-based security detectors.

Phase 4
"""

from src.security.security_response import SecurityResponse


class BaseDetector:
    """
    Base class for all rule-based detectors.
    """

    CATEGORY = "GENERIC"

    def __init__(self, rules: dict):
        self.rules = rules

    def normalize(self, text: str) -> str:
        """
        Normalize text before scanning.
        """

        return " ".join(text.lower().split())

    def detect(self, text: str) -> dict:
        """
        Scan text using configured rules.
        """

        normalized = self.normalize(text)

        for rule_name, phrases in self.rules.items():

            for phrase in phrases:

                if phrase in normalized:

                    return SecurityResponse.block(
                        category=self.CATEGORY,
                        rule=rule_name,
                        matched_phrase=phrase,
                        message=f"{self.CATEGORY.replace('_', ' ').title()} detected."
                    )

        return SecurityResponse.allow(
            category=self.CATEGORY
        )