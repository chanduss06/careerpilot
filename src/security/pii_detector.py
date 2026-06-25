"""
CareerPilot PII Detector

Detects Personally Identifiable Information (PII)
from user prompts and resumes.

Phase 4 - Step 2
"""

import re


class PIIDetector:
    """
    Detects common PII using regular expressions.
    """

    def __init__(self):
        self.patterns = {
            "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",

            "phone": r"(?:\+91[- ]?)?[6-9]\d{9}\b",

            "aadhaar": r"\b\d{4}\s?\d{4}\s?\d{4}\b",

            "pan": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",

            "github": r"https?://(?:www\.)?github\.com/[A-Za-z0-9_-]+/?",

            "linkedin": r"https?://(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+/?",

            "ip_address": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",

            "credit_card": r"\b(?:\d[ -]*?){13,16}\b",
        }

    def detect(self, text: str) -> dict:
        """
        Detect all supported PII types.

        Parameters
        ----------
        text : str

        Returns
        -------
        dict
        """

        findings = {}

        for pii_type, pattern in self.patterns.items():

            matches = re.findall(pattern, text)

            if matches:
                findings[pii_type] = matches

        return findings

    def contains_pii(self, text: str) -> bool:
        """
        Returns True if any PII exists.
        """

        return len(self.detect(text)) > 0