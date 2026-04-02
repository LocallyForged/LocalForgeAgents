"""
LocalForgeAgents - ReAct Loop Example
Simple ReAct-style reasoning loop for local Ollama models.
Optimized for local hardware: clear steps, minimal tokens, basic retry.

ReAct = Reason → Act → Observe → Repeat
"""

import json
from typing import List, Dict

def react_step(prompt: str, model_name: str = "llama3.2", max_steps: int = 5) -> str:
    """Basic ReAct loop - no heavy dependencies."""
    print(f"Starting ReAct loop with model: {model_name}")
    print(f"Goal: {prompt[:100]}...\n")
    
    history = []
    for step in range(max_steps):
        print(f"Step {step+1}/{max_steps}: Thinking...")
        
        # In real use, you would call Ollama here with the history
        # This is a simulation of the pattern
        thought = f"Thought: I need to break this down. Current context has {len(history)} previous steps."
        action = "No tool needed yet - gathering information."
        
        print(f"  Thought: {thought}")
        print(f"  Action: {action}")
        
        observation = "Observation: Local model responded correctly. Continuing."
        history.append({"thought": thought, "action": action, "observation": observation})
        
        if "final answer" in prompt.lower():  # simple stopping condition for demo
            break
    
    final_answer = f"Final Answer: Task completed in {len(history)} steps using local model."
    print(f"\n{final_answer}")
    return final_answer

def main():
    test_prompt = "How can I automate a daily research summary using only local AI?"
    react_step(test_prompt)

if __name__ == "__main__":
    main()
