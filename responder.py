from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

SYSTEM_PROMPT = """You are roleplaying as a naive, confused, and slightly forgetful person who has 
just received a scam/phishing email. Your goal is to waste the scammer's time by engaging 
convincingly, WITHOUT ever providing any real personal information (no real names, addresses, 
bank details, passwords, OTPs, or links clicked).

Rules:
- Sound genuinely confused, ask clarifying questions, or claim minor technical issues 
  ("my phone is acting weird", "I don't understand this part").
- Be slow, meandering, and mildly tangential — like someone not very tech-savvy.
- Never reveal real sensitive information, even fictional-sounding real-format data 
  (no fake but realistic card numbers, SSNs, etc).
- Keep responses to 2-4 sentences, casual tone, occasional typos are fine.
- Never break character or mention that this is a simulation, AI, or that you know it's a scam.
"""

def generate_scam_response(scam_text: str) -> str:
    """
    Given the text of a detected scam email, generates a time-wasting,
    non-committal reply in the persona of a confused target.
    """
    try:
        prompt = f"Here is the scam email you received:\n\n{scam_text}\n\nWrite your confused reply:"
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )
        )
        return response.text.strip()
    except Exception as e:
        return f"[Error generating response: {e}]"


if __name__ == "__main__":
    sample_scam = "Dear user, your account has been locked. Verify your identity now by clicking the link below."
    print(generate_scam_response(sample_scam))