
from fastapi import APIRouter, Depends, HTTPException

from app.providers.base import Provider, ProviderError
from app.providers.dependencies import get_provider
from app.schemas.chat import ChatRequest, ChatResponse


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    provider: Provider = Depends(get_provider)
):
    try:
        result = await provider.complete(
            model=request.model,
            prompt=request.prompt,
            timeout=10.0
        )

        return ChatResponse(
            text=result.text,
            prompt_tokens=result.prompt_tokens,
            completion_tokens=result.completion_tokens,
            model=result.model
        )

    except ProviderError:
        raise HTTPException(
            status_code=502,
            detail="LLM provider failed"
        )
