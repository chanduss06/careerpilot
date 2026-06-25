"""
CareerPilot Resume Sanitizer

Prepares resumes before they are sent to AI agents.

Phase 4
"""

import re

from src.security.pii_masker import PIIMasker


class ResumeSanitizer:
    """
    Cleans and sanitizes resume text.
    """

    def __init__(self):
        self.masker = PIIMasker()

    def normalize_whitespace(self, text: str) -> str:
        """
        Normalize whitespace while preserving paragraph breaks.
        """

        # Remove trailing spaces
        text = "\n".join(line.rstrip() for line in text.splitlines())

        # Collapse multiple blank lines into one
        text = re.sub(r"\n\s*\n+", "\n\n", text)

        return text.strip()

    def sanitize(self, resume_text: str) -> str:
        """
        Fully sanitize a resume.
        """

        cleaned = self.normalize_whitespace(resume_text)

        cleaned = self.masker.mask(cleaned)

        return cleaned