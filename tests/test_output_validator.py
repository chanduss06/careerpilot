"""
CareerPilot Output Validator Tests

Phase 4
"""

from src.security.output_validator import OutputValidator


def test_safe_output():

    validator = OutputValidator()

    result = validator.detect(
        "Your resume shows strong Python and SQL skills."
    )

    assert result["allowed"] is True

    assert result["category"] == "OUTPUT_VALIDATION"


def test_api_key_exposure():

    validator = OutputValidator()

    result = validator.detect(
        "API_KEY = sk-123456789"
    )

    assert result["allowed"] is False

    assert result["rule"] == "API Key Exposure"


def test_bearer_token():

    validator = OutputValidator()

    result = validator.detect(
        "Authorization: Bearer abc123token"
    )

    assert result["allowed"] is False

    assert result["rule"] == "Bearer Token"


def test_password_exposure():

    validator = OutputValidator()

    result = validator.detect(
        "Password: admin123"
    )

    assert result["allowed"] is False

    assert result["rule"] == "Password Exposure"


def test_private_key():

    validator = OutputValidator()

    result = validator.detect(
        "-----BEGIN PRIVATE KEY-----"
    )

    assert result["allowed"] is False

    assert result["rule"] == "Private Key"


def test_system_prompt():

    validator = OutputValidator()

    result = validator.detect(
        "System Prompt: You are CareerPilot."
    )

    assert result["allowed"] is False

    assert result["rule"] == "System Prompt Leakage"