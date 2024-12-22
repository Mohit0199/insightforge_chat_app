import os
from groq import Groq
from logger import CustomLogger
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class GroqClient:
    """Class to interact with the Groq API"""

    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.client = Groq(api_key = self.api_key)
        self.logger = CustomLogger().get_logger()

    def get_response(self, messages):
        """Send messages to groq api API and return the response."""

        try:
            self.logger.info("Sending messages to Groq API...")
            chat_completion = self.client.chat.completions.create(
                messages=messages,
                model="llama3-70b-8192"  #using llama3 LLM
            )
            response = chat_completion.choices[0].message.content
            self.logger.info("Received response from Groq API...")

            return response
        
        except Exception as e:
            self.logger.error(f"Error communicating with Groq API: {e}")
            return "Sorry, I couldn't get a response at this time."
        
