
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_grant_suggestions(grant_text):
    prompt = (
        "You are an expert in grant writing. Review the following grant proposal and provide "
        "clear, actionable suggestions to improve clarity, tone, and completeness. "
        "Focus on aligning the text with best practices for successful grant approval.\n\n"
        f"Grant Proposal:\n{grant_text}\n\nSuggestions:"
    )
    try:
        response = openai.Completion.create(
            engine="gpt-4", 
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if _name_ == "_main_": 
   
    print("Enter your grant proposal text (end input with Ctrl+D):")
    grant_text = ""
    try:
        while True:
            line = input()
            grant_text += line + "\n"
    except EOFError:
        pass

    suggestions = get_grant_suggestions(grant_text)
    print("\nGrant Suggestions by tool to make your text more clear\n")
    print(suggestions)
