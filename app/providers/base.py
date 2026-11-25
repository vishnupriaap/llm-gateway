
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Completion:
    text: str
    prompt_tokens: int
    completion_tokens: int
    model: str


class ProviderError(Exception):

    def __init__(self, message: str, retryable: bool):
        super().__init__(message)
        self.retryable = retryable


class Provider(ABC):

    @abstractmethod
    async def complete(
        self,
        model: str,
        prompt: str,
        timeout: float
    ) -> Completion:
        pass
