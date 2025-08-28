"""
FastAPI endpoints for Industrial Automation Chatbot
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os

# Initialize FastAPI app
app = FastAPI(
    title="Industrial Automation AI Assistant API",
    description="API for accessing LLM-based industrial automation assistant",
    version="0.1.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development, restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define data models
class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    temperature: Optional[float] = 0.7
    model: Optional[str] = "gpt-3.5-turbo"

class ChatResponse(BaseModel):
    response: str
    sources: Optional[List[str]] = None

# Routes
@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "online", "service": "Industrial Automation AI Assistant"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Process chat messages with industrial automation context"""
    try:
        # In a real implementation, this would call the LLM service
        # For now, we'll just return a dummy response
        return {
            "response": "This is a placeholder response from the Industrial Automation AI Assistant API",
            "sources": ["Documentation 1", "Technical Specification 2"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/industrial-topics")
async def get_industrial_topics():
    """Get list of available industrial automation topics"""
    return {
        "topics": [
            "PLC Programming",
            "SCADA Systems",
            "Industrial IoT",
            "Building Automation",
            "Manufacturing Execution Systems",
            "Smart Factory Solutions"
        ]
    }

# Run with: uvicorn src.api.endpoints:app --reload
