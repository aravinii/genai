from google import genai
from google.genai import types

from agents.research_agent import research_agent
from agents.pricing_agent import pricing_agent
from utils.load_prompt import load_prompt
from utils.render import render_block
from utils.config import CLIENT, MODEL, USER_COLOR, AGENT_COLOR, FUNCTION_COLOR

def planner_agent(model: str = MODEL) -> None:
    """
    Planner Agent: autonomously decides which agent to call based on user input.

    The agent receives a user prompt and a list of available agent functions,
    and uses the model to determine which agent to invoke, calling it automatically.

    Args:
        model (str): The model identifier to use for planning and decision-making.

    Returns:
        None: Displays the agent's response in markdown.
    """
    system_prompt = load_prompt("planner_agent_v2")

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
        user_input = input("USER: ")
        if user_input.lower() in ["exit"]:
            break

        render_block("USER", user_input, USER_COLOR)

        resp = chat.send_message(user_input)

        while True:

            parts = resp.candidates[0].content.parts
            tool_called = False

            for part in parts:

                if part.text:
                    render_block("AGENT", part.text, AGENT_COLOR)

                elif part.function_call:

                    fn = part.function_call
                    name = fn.name
                    args = dict(fn.args)

                    render_block("FUNCTION", f"🛠 Calling {name}({args})", FUNCTION_COLOR)

                    result = tool_map[name](**args)

                    resp = chat.send_message(
                        types.Part.from_function_response(
                            name=name,
                            response={"result": result}
                        )
                    )

                    tool_called = True
                    break

            if not tool_called:
                break