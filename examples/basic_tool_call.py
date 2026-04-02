"""
LocalForgeAgents - Basic Tool Call Example
Optimized for local Ollama models.

This is a minimal, standalone example of tool calling with Ollama.
No external frameworks required.
"""

import json
from typing import Dict, Any

# Example tool definition (model-agnostic JSON schema style)
TOOLS = [
    {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            },
            "required": ["location"]
        }
    }
]

def simple_tool_call_demo(model_name: str = "llama3.2"):
    """Demonstrates basic tool calling pattern for local models."""
    print(f"Running basic tool call demo with model: {model_name}")
    print("This example shows how to structure tool definitions for Ollama.")
    print("\nIn a real setup, you would send the tools to Ollama and parse the response.")
    print("Key pattern: Use clear JSON schemas and always validate tool outputs.")

    # Example of what the model might return
    example_response = {
        "tool_calls": [
            {
                "name": "get_current_weather",
                "arguments": json.dumps({"location": "Salt Lake City, UT", "unit": "fahrenheit"})
            }
        ]
    }
    
    print("\nExample tool call structure:")
    print(json.dumps(example_response, indent=2))
    
    print("\n✅ Pattern complete. This structure works across most open models.")

if __name__ == "__main__":
    simple_tool_call_demo()
