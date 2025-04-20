from utils.groq_api import groq_chat_response

def handle_tenancy_faq(user_text):
    prompt = f"""You are an expert in rental and tenancy laws. Answer the user's question: "{user_text}".
If possible, ask for the user's location for more accurate advice."""

    return groq_chat_response(prompt)
