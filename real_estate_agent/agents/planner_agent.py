from google import genai
from google.genai import types
import time

from agents.research_agent import research_agent
from agents.pricing_agent import pricing_agent
from utils.load_prompt import load_prompt
from utils.render import render_block
from utils.config import CLIENT, MODEL, ANSI_USER_COLOR, ANSI_RESET_COLOR

def save_chat(history: dict, text: str, role: str, type: str = "text") -> dict:
    """
    Append a chat iteraction to the history.

    Args:
        history (dict): The chat history to save.

    Returns:
        dict: The saved chat history.
    """
    content = text if isinstance(text, dict) else {"result": text}
    history["chat"].append({
        "role": role,
        "type": type,
        "content": content
    })
    return history

def planner_agent(model: str = MODEL, return_object: bool = False) -> None | dict:
    """
    Planner Agent: autonomously decides which agent to call based on user input.

    The agent receives a user prompt and a list of available agent functions,
    and uses the model to determine which agent to invoke, calling it automatically.

    Args:
        model (str): The model identifier to use for planning and decision-making.

    Returns:
        None | dict: Displays the agent's response in markdown or returns the history as a dictionary.
    """
    system_prompt = load_prompt("planner_agent_v2")
    history = {"model_name": MODEL, "total_tokens": [], "latency": [], "chat": []}

    research_agent_def = types.FunctionDeclaration.from_callable(client = CLIENT, callable = research_agent)
    pricing_agent_def = types.FunctionDeclaration.from_callable(client = CLIENT, callable = pricing_agent)

    tools = [
        types.Tool(
            function_declarations=[
                research_agent_def,
                pricing_agent_def
            ]
        )
    ]

    tool_map = {
        "research_agent": research_agent,
        "pricing_agent": pricing_agent
    }
    
    chat = CLIENT.chats.create(
        model=MODEL,
        config = types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=tools,
            temperature=0.2,
            tool_config = types.ToolConfig(
                function_calling_config=types.FunctionCallingConfig(
                    mode="AUTO"
                )
            )
        )
    )

    while True:
        print(ANSI_USER_COLOR, end="")
        user_input = input("USER: ")
        print(ANSI_RESET_COLOR, end="")

        if user_input.lower() in ["exit"]:
            if return_object:
                return history
            break

        start = time.perf_counter()
        render_block("USER", user_input)
        
        resp = chat.send_message(user_input)
        history = save_chat(history, user_input, "user", "text")
        total_tokens = getattr(resp.usage_metadata, "total_token_count", None)
        if total_tokens > 0:
            history["total_tokens"].append(total_tokens)

        while True:
            parts = resp.candidates[0].content.parts
            tool_called = False

            for part in parts:
                if part.text:
                    render_block("AGENT", part.text)
                    history = save_chat(history, part.text, "planner_agent", "text")

                elif part.function_call:
                    fn = part.function_call
                    name = fn.name
                    args = dict(fn.args)

                    render_block("FUNCTION", f"🛠 Calling {name}({args})")
                    history = save_chat(history, {"tool_name": name, "args": args}, "planner_agent", "tool_call")

                    result = tool_map[name](**args)
                    payload = result.get("result", result)
                    resp = chat.send_message(
                        types.Part.from_function_response(
                            name=name,
                            response={"result": payload}
                        )
                    )
                    history = save_chat(history, payload, name, "tool_response")
                    history["total_tokens"].append(result['metadata'])
                    total_tokens = getattr(resp.usage_metadata, "total_token_count", None)
                    if total_tokens > 0:
                        history["total_tokens"].append(total_tokens)
                    
                    tool_called = True
                    break

            if not tool_called:
                latency = time.perf_counter() - start
                history["latency"].append(latency)
                break