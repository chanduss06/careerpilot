"""
CareerPilot Security Middleware

Runs all security checks before
allowing an input to reach an AI agent.

Phase 4
"""

from src.security.pii_detector import PIIDetector
from src.security.pii_masker import PIIMasker
from src.security.prompt_injection import PromptInjectionDetector
from src.security.jailbreak_detector import JailbreakDetector
from src.security.resume_sanitizer import ResumeSanitizer
from src.security.output_validator import OutputValidator


class SecurityMiddleware:
    """
    Central security pipeline.
    """

    def __init__(self):

        self.pii_detector = PIIDetector()
        self.pii_masker = PIIMasker()

        self.prompt_detector = PromptInjectionDetector()
        self.jailbreak_detector = JailbreakDetector()

        self.resume_sanitizer = ResumeSanitizer()
        self.output_validator = OutputValidator()

    def inspect_input(self, text: str) -> dict:
        """
        Run every security check.
        """

        prompt_result = self.prompt_detector.detect(text)

        jailbreak_result = self.jailbreak_detector.detect(text)

        findings = self.pii_detector.detect(text)

        cleaned_text = self.resume_sanitizer.sanitize(text)

        security_report = {
            "pii_detected": bool(findings),
            "pii_types": list(findings.keys()),
            "prompt_injection": not prompt_result["allowed"],
            "jailbreak": not jailbreak_result["allowed"],
        }

        if not jailbreak_result["allowed"]:
            return {
                "allowed": False,
                "reason": jailbreak_result,
                "security_report": security_report,
            }

        if not prompt_result["allowed"]:
            return {
                "allowed": False,
                "reason": prompt_result,
                "security_report": security_report,
            }

        return {
            "allowed": True,
            "clean_text": cleaned_text,
            "security_report": security_report,
        }

    def inspect_output(self, text: str) -> dict:
        """
        Validate LLM output before returning it
        to the user.
        """

        result = self.output_validator.detect(text)

        if not result["allowed"]:
            return {
                "allowed": False,
                "reason": result,
            }

        return {
            "allowed": True,
            "clean_text": text,
        }