from pathlib import Path

def load_prompt(prompt_name: str) -> str:
    """
    Load a prompt from the prompts directory.
    """

    base_dir = Path(__file__).resolve().parent.parent  # real_state_agent
    prompt_path = base_dir / "prompts" / f"{prompt_name}.txt"

    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt {prompt_name} not found")

    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()