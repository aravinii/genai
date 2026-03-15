from IPython.display import display, HTML
import markdown
from IPython import get_ipython
from utils.config import USER_COLOR, AGENT_COLOR, FUNCTION_COLOR, ANSI_USER_COLOR, ANSI_AGENT_COLOR, ANSI_FUNCTION_COLOR, ANSI_RESET_COLOR

def _in_notebook():
    try:
        shell = get_ipython()
        if shell is None:
            return False
        return shell.__class__.__name__ == "ZMQInteractiveShell"
    except NameError:
        return False

def _get_color(role: str, notebook: bool):
    if notebook:
        return USER_COLOR if role == "USER" else AGENT_COLOR if role == "AGENT" else FUNCTION_COLOR
    else:
        return ANSI_USER_COLOR if role == "USER" else ANSI_AGENT_COLOR if role == "AGENT" else ANSI_FUNCTION_COLOR

def render_block(role: str, message: str):
    if _in_notebook():
        message_ = markdown.markdown(message)
        html = f"""
        <div style="
            background-color: {_get_color(role, True)};
            color: black; 
            padding: 10px;
            border-radius: 8px;
            margin: 5px 0px;
            font-family: Arial, sans-serif;
        ">
            <strong>{role}:</strong><br>
            {message_.replace('\n', '')}
        </div>
        """
        display(HTML(html))
    else:
        if role == "USER":
            print()
        else:
            color = _get_color(role, False)
            msg = message.rstrip("\n")
            print(f"{color}{role}: {msg}{ANSI_RESET_COLOR}\n")