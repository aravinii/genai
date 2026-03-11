from IPython.display import display, HTML
import markdown

def render_block(role: str, message: str, color: str):
    message_ = markdown.markdown(message)
    html = f"""
    <div style="
        background-color: {color};
        color: black; 
        padding: 10px;
        border-radius: 8px;
        margin: 5px 0px;
        font-family: Arial, sans-serif;
    ">
        <strong>{role}:</strong><br>
        {message_.replace('\n', '<br>')}
    </div>
    """
    display(HTML(html))