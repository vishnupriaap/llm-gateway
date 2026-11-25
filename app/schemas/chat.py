
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    model: str
    prompt: str


class ChatResponse(BaseModel):
    text: str
    prompt_tokens: int
    completion_tokens: int
    model: str
