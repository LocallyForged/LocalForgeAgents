"""
LocalForgeAgents - Simple Multi-Step Agent Example
Minimal multi-step agent (Researcher → Writer) for local Ollama.
No heavy dependencies — just clear sequential steps.
"""

def researcher_step(query: str) -> str:
    """Simulates a researcher agent gathering info."""
    print(f"Researcher: Gathering information on '{query}' using local model...")
    # In real use: call Ollama with a research-focused prompt
    return f"Key facts found: Local AI is fast on consumer hardware. Token limits matter. Tool calling is key."

def writer_step(research: str, goal: str) -> str:
    """Simulates a writer agent turning research into output."""
    print(f"Writer: Creating summary for goal '{goal}'...")
    return f"Final Summary: {research[:150]}... This pattern works well on local setups because steps are short and clear."

def run_multi_step_agent(query: str = "Benefits of running agents locally"):
    print("Starting multi-step agent (Researcher → Writer)\n")
    
    research = researcher_step(query)
    print(f"Research output: {research}\n")
    
    summary = writer_step(research, "Create a short benefit summary")
    print(f"\nFinal Output:\n{summary}")
    
    print("\n✅ Multi-step pattern complete. Easy to extend with more agents.")

if __name__ == "__main__":
    run_multi_step_agent()
