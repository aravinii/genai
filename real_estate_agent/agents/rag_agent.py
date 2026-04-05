from utils.load_prompt import load_prompt
from utils.embedding import search_neighborhood_context
from google.genai import types
from utils.config import CLIENT, MODEL

def rag_agent(target_neighborhood: str) -> dict:
    """
    Runs the real estate research agent (RAG).

    The agent analyzes the investment potential of a given neighborhood
    using a predefined system prompt and returns a structured report
    highlighting positive investment factors and living characteristics.

    Args:
        target_neighborhood (str): Name of the neighborhood to analyze.

    Returns:
        dict: A dictionary containing:
            - "result" (str): The generated research report about the analyzed neighborhood.
            - "metadata": Aggregated total_token_count across chat turn(s), or None if unavailable.
    """
    rag_tool = types.FunctionDeclaration.from_callable(client=CLIENT, callable=search_neighborhood_context)
    rag_tool = types.Tool(function_declarations=[rag_tool])
    system_prompt = load_prompt("research_agent_v2")

    chat = CLIENT.chats.create(
        model=MODEL,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[rag_tool],
            temperature=0.2,
            tool_config = types.ToolConfig(
                function_calling_config=types.FunctionCallingConfig(
                    mode="AUTO"
                )
            )
        )
    )
    response = chat.send_message(
        f"TARGET NEIGHBORHOOD: {target_neighborhood}"
    )
    total_tokens = getattr(response.usage_metadata, "total_token_count", None)
    while True:
        parts = response.candidates[0].content.parts
        function_calls = [p.function_call for p in parts if p.function_call]

        if not function_calls:
            break

        for fn_call in function_calls:
            args = dict(fn_call.args)
            tool_result = search_neighborhood_context(**args)
            response = chat.send_message(
                types.Part.from_function_response(
                    name=fn_call.name,
                    response={"result": tool_result}
                )
            )
            total_tokens += getattr(response.usage_metadata, "total_token_count", None)

    return {
        "result": response.text,
        "metadata": total_tokens
    }