"""
CareerPilot Security Response

Provides a standard response format for all
security components.

Phase 4
"""


class SecurityResponse:
    """
    Factory class for creating consistent security responses.
    """

    @staticmethod
    def allow(
        category: str,
        message: str = "No security issues detected.",
        metadata: dict | None = None,
    ) -> dict:

        return {
            "allowed": True,
            "risk_level": "LOW",
            "category": category,
            "rule": None,
            "matched_phrase": None,
            "message": message,
            "metadata": metadata or {},
        }

    @staticmethod
    def block(
        *,
        category: str,
        rule: str,
        matched_phrase: str,
        message: str,
        risk_level: str = "HIGH",
        metadata: dict | None = None,
    ) -> dict:

        return {
            "allowed": False,
            "risk_level": risk_level,
            "category": category,
            "rule": rule,
            "matched_phrase": matched_phrase,
            "message": message,
            "metadata": metadata or {},
        }