
import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
from google.generativeai.types import HarmCategory, HarmBlockThreshold

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Create the model
generation_config = {
  "temperature": 0.1,
  "top_p": 0.95,
  "top_k": 12,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

def final_response(response):
    """
    Final response function to generate a markdown response using the Gemini
    model. This function takes a response string, sends it to the Gemini model
    to generate a markdown response, and then returns the response text.

    Args:
        response (str): The response string to send to the Gemini model.

    Returns:
        str: The markdown response generated by the Gemini model.
    """
    
    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-002",
    
    generation_config=generation_config,
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        }
    )
    
    chat_session = model.start_chat(
        history=[
        ]
    )

    response = chat_session.send_message(f"{response}  use every bit of given resource to come up with a information dense  output also don't missout any important point,OVERSHARING is OK.Respond in MARKDOWN format")
    return response.text
    # print(response.text)
