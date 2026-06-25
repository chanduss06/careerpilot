from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class RuntimeResponse:
    """
    Standard response object returned by the runtime.
    """

    success: bool
    message: str
    data: Any = None