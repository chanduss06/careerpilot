"""
CareerPilot PII Tests

Phase 4
"""

from src.security.pii_detector import PIIDetector
from src.security.pii_masker import PIIMasker


def test_email_detection():

    detector = PIIDetector()

    result = detector.detect(
        "My email is test@gmail.com"
    )

    assert "email" in result


def test_phone_detection():

    detector = PIIDetector()

    result = detector.detect(
        "9876543210"
    )

    assert "phone" in result


def test_email_masking():

    masker = PIIMasker()

    masked = masker.mask(
        "Email: test@gmail.com"
    )

    assert "test@gmail.com" not in masked

    assert "@gmail.com" in masked


def test_phone_masking():

    masker = PIIMasker()

    masked = masker.mask(
        "9876543210"
    )

    assert "9876543210" not in masked

    assert "3210" in masked