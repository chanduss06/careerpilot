"""
CareerPilot PII Masker

Masks sensitive information detected by PIIDetector.

Phase 4 - Step 3
"""

from src.security.pii_detector import PIIDetector


class PIIMasker:
    """
    Masks detected PII while preserving enough context
    for resume analysis.
    """

    def __init__(self):
        self.detector = PIIDetector()

    # -------------------------------------------------
    # Individual Masking Methods
    # -------------------------------------------------

    def _mask_email(self, email: str) -> str:
        username, domain = email.split("@")
        return "*" * len(username) + "@" + domain

    def _mask_phone(self, phone: str) -> str:
        digits = "".join(filter(str.isdigit, phone))
        return "*" * (len(digits) - 4) + digits[-4:]

    def _mask_aadhaar(self, aadhaar: str) -> str:
        digits = aadhaar.replace(" ", "")
        return "*" * 8 + digits[-4:]

    def _mask_pan(self, pan: str) -> str:
        return "*" * 5 + pan[5:]

    def _mask_github(self, url: str) -> str:
        username = url.rstrip("/").split("/")[-1]
        return url.replace(username, "*" * len(username))

    def _mask_linkedin(self, url: str) -> str:
        username = url.rstrip("/").split("/")[-1]
        return url.replace(username, "*" * len(username))

    def _mask_ip(self, ip: str) -> str:
        parts = ip.split(".")
        return "***.***.***." + parts[-1]

    def _mask_credit_card(self, card: str) -> str:
        digits = "".join(filter(str.isdigit, card))
        return "*" * (len(digits) - 4) + digits[-4:]

    # -------------------------------------------------
    # Main Masking Function
    # -------------------------------------------------

    def mask(self, text: str) -> str:
        """
        Detect and mask all supported PII.
        """

        findings = self.detector.detect(text)

        masked_text = text

        handlers = {
            "email": self._mask_email,
            "phone": self._mask_phone,
            "aadhaar": self._mask_aadhaar,
            "pan": self._mask_pan,
            "github": self._mask_github,
            "linkedin": self._mask_linkedin,
            "ip_address": self._mask_ip,
            "credit_card": self._mask_credit_card,
        }

        for pii_type, values in findings.items():

            if pii_type not in handlers:
                continue

            mask_function = handlers[pii_type]

            for value in values:
                masked_text = masked_text.replace(
                    value,
                    mask_function(value)
                )

        return masked_text