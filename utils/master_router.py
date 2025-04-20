from utils.agent1_issue_detect import handle_image_issue
from utils.agent2_tenancy_faq import handle_tenancy_faq
from utils.groq_api import groq_chat_response

def route_to_agent(image_file, user_text, history=None):
    if image_file:
        return handle_image_issue(image_file, user_text)
    
    # Ask GROQ to classify the query
    classification_prompt = f"""You are a routing agent. Classify the following query into one of the following:
- 'issue' if it's related to a property issue (e.g., mold, cracks, plumbing)
- 'tenancy' if it's about rental laws or agreements

Query: "{user_text}"

Respond ONLY with one word: 'issue' or 'tenancy'
"""
    classification = groq_chat_response(classification_prompt).strip().lower()

    if classification == "issue":
        return handle_image_issue(None, user_text)
    elif classification == "tenancy":
        return handle_tenancy_faq(user_text)
    else:
        return "Sorry, I couldn't understand your question. Could you clarify if it's about a property issue or tenancy law?"
