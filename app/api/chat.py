from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from ..services.chat_service import ChatService
from typing import List
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(
    title="Local Chat Service"
)

# Instantiate the ChatService
chat_service = ChatService(os.path.join(BASE_DIR, 'model/Dorna-Llama3-8B-Instruct'))

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    temperature: float = 0.3
    max_new_tokens: int = 512

@app.get(
    path="/",
    tags=["Chat Endpoints"]
)
async def root():
    return JSONResponse(
        {"message": "Service is up and running"}
    )


@app.post(
        path="/chat/",
        tags=["Chat Endpoints"]
)
async def chat_endpoint(request: ChatRequest):
    try:
        # Call the ChatService to process the chat
        response = chat_service.chat(
            messages=request.messages,
            temperature=request.temperature,
            max_new_tokens=request.max_new_tokens
        )
        return JSONResponse(
            {"role": "assistant", "response": response}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
