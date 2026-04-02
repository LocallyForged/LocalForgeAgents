"""
LocalForgeAgents - Basic Evaluation Script
Simple way to test agent patterns on your local Ollama model.
Helps keep the repo useful as models improve.
"""

def run_eval_test(pattern_name: str = "basic_tool_call"):
    """Basic eval template — run this after testing any pattern."""
    print(f"Running basic eval for pattern: {pattern_name}")
    print("=== LocalForgeAgents Eval Template ===")
    print("1. Did the pattern run without errors on your hardware?")
    print("2. Was the output useful and clear?")
    print("3. How many tokens/steps did it use? (important for local inference speed)")
    print("4. Any improvements needed for your model (e.g. Llama 3.2 vs Qwen2.5)?")
    
    print("\n✅ Eval complete. Share results in Issues if you want to help improve the patterns.")
    print("This script makes the project evergreen — re-run when new models come out.")

    print("\nTip: For real testing, integrate with ollama python library.")

if __name__ == "__main__":
    run_eval_test()
    print("\nAll starter patterns added. LocalForgeAgents v0.1 is live!")
