
from fastapi import FastAPI

from app.api.routes import router
from app.providers.fake import FakeProvider


app = FastAPI(title="LLM Gateway")

# Create the provider when the application starts
app.state.provider = FakeProvider(
    latency=0.5,
    failure_rate=0.0
)

# Register our API routes
app.include_router(router, prefix="/v1")
