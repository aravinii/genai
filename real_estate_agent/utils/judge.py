import re
import json

def format_judge_conversation(conversation: dict) -> str:
    turns = []
    chat = conversation.get("chat", [])
    for msg in chat:
        typ = msg.get("type")
        if typ == "text":
            role = msg.get("role")
            content = msg.get("content", {}).get("result", "")
            turn = f"""<turn><role>{role}</role><content>{content}</content></turn>""".strip()
            turns.append(turn)
    return "\n\n".join(turns)

def parse_judge_json(text: str) -> dict:
    t = text.strip()
    if t.startswith("```"):
        t = re.sub(r"^```(?:json)?\s*", "", t, flags=re.IGNORECASE)
        t = re.sub(r"\s*```\s*$", "", t)
    return json.loads(t)