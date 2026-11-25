
import asyncio
import random

from app.providers.base import Provider, Completion, ProviderError


class FakeProvider(Provider):

    def __init__(
        self,
        latency: float = 0.5,
        failure_rate: float = 0.0
    ):
        self.latency = latency
        self.failure_rate = failure_rate

    async def complete(
        self,
        model: str,
        prompt: str,
        timeout: float
    ) -> Completion:

        if self.latency > timeout:
            raise ProviderError(
                "Provider request timed out",
                retryable=True
            )

        await asyncio.sleep(self.latency)

        if random.random() < self.failure_rate:
            raise ProviderError(
                "Simulated provider failure",
                retryable=True
            )

        return Completion(
            text=f"Fake response to: {prompt}",
            prompt_tokens=len(prompt.split()),
            completion_tokens=len(f"Fake response to: {prompt}".split()),
            model=model
        )
