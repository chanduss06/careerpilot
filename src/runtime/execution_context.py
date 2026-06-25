from dataclasses import dataclass, field


@dataclass(slots=True)
class ExecutionContext:
    """
    Stores request-specific runtime state.
    """

    session_id: str
    user_id: str = "default"

    metadata: dict = field(default_factory=dict)