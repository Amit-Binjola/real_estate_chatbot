from utils.blip_model import generate_caption
from utils.groq_api import groq_chat_response

def handle_image_issue(image_file, user_text):
    caption = ""
    if image_file:
        caption = generate_caption(image_file)
    
    prompt = f"""You are a real estate maintenance assistant.

Analyze the following:
- Image description: "{caption}"
- User comment: "{user_text}"

Identify any visible property issues and suggest appropriate troubleshooting or professional help if needed."""
    
    return groq_chat_response(prompt)
