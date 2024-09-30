
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Configure the API key from environment variables
genai.configure(api_key=os.getenv("API_KEY"))

def get_meaning_from_gemai(word: str) -> str:
    prompt = (
        f"What is the meaning of the word '{word}'? "
        "Write it in a single sentence. "
        "The number of words in the answer should not exceed 20."
    )

    # Generate content using the Gemini model
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    # Extract and return the generated content
    return response.text.strip()
