"""
Helper functions for Industrial Automation Chatbot
"""

import os
import json
from datetime import datetime
from typing import List, Dict, Any, Optional

def validate_api_key(api_key: str) -> bool:
    """Validate if an API key is in the correct format
    
    Args:
        api_key: The API key to validate
        
    Returns:
        True if the API key is valid, False otherwise
    """
    # Simple validation for OpenAI API key format (starts with 'sk-')
    return api_key and isinstance(api_key, str) and api_key.startswith("sk-")

def save_conversation(
    conversation_id: str,
    messages: List[Dict[str, str]],
    save_dir: str = None
) -> bool:
    """Save a conversation to a JSON file
    
    Args:
        conversation_id: Unique identifier for the conversation
        messages: List of conversation messages
        save_dir: Directory to save the conversation, defaults to ./conversations
        
    Returns:
        Success status
    """
    try:
        # Create directory if it doesn't exist
        save_dir = save_dir or os.path.join(os.getcwd(), "conversations")
        os.makedirs(save_dir, exist_ok=True)
        
        # Prepare filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{conversation_id}_{timestamp}.json"
        filepath = os.path.join(save_dir, filename)
        
        # Prepare data structure
        data = {
            "conversation_id": conversation_id,
            "timestamp": timestamp,
            "messages": messages
        }
        
        # Write to file
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
            
        return True
    except Exception as e:
        print(f"Error saving conversation: {e}")
        return False

def load_conversation(filepath: str) -> Optional[Dict[str, Any]]:
    """Load a conversation from a JSON file
    
    Args:
        filepath: Path to the conversation file
        
    Returns:
        Conversation data or None if error
    """
    try:
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            return None
            
        with open(filepath, "r") as f:
            data = json.load(f)
            
        return data
    except Exception as e:
        print(f"Error loading conversation: {e}")
        return None

def format_message_for_display(message: Dict[str, str]) -> Dict[str, Any]:
    """Format a message for display in the UI
    
    Args:
        message: Raw message dictionary
        
    Returns:
        Formatted message with UI-specific properties
    """
    role = message.get("role", "")
    content = message.get("content", "")
    
    # Format based on role
    if role == "user":
        return {
            "role": "user",
            "content": content,
            "avatar": "👨‍💼",  # User avatar
            "align": "left"
        }
    elif role == "assistant":
        return {
            "role": "assistant",
            "content": content,
            "avatar": "🤖",  # Assistant avatar
            "align": "right"
        }
    else:
        return {
            "role": role,
            "content": content,
            "avatar": "ℹ️",  # System/info avatar
            "align": "center"
        }

def get_industrial_topics() -> List[Dict[str, str]]:
    """Get list of industrial automation topics with descriptions
    
    Returns:
        List of topics with descriptions
    """
    return [
        {
            "name": "PLC Programming",
            "description": "Programming logic controllers for industrial automation",
            "icon": "🔧"
        },
        {
            "name": "SCADA Systems",
            "description": "Supervisory control and data acquisition for industrial processes",
            "icon": "📊"
        },
        {
            "name": "Industrial IoT",
            "description": "Internet of Things applications in industrial settings",
            "icon": "🌐"
        },
        {
            "name": "Building Automation",
            "description": "Smart building systems and controls",
            "icon": "🏢"
        },
        {
            "name": "Manufacturing Execution Systems",
            "description": "Systems for managing manufacturing operations",
            "icon": "🏭"
        },
        {
            "name": "Smart Factory Solutions",
            "description": "Advanced technologies for factory automation",
            "icon": "🤖"
        }
    ]
