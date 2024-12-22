from app.app_client import GroqClient


class ChatManager:
    """Class to manage chat interactions"""

    def __init__(self):
        self.client = GroqClient()
        self.conversation_history = []

    def add_message(self, role, content):
        """Add a message to the conversation history"""
        self.conversation_history.append({"role": role, "content": content})

    def get_response(self, user_message):
        """Get a concise or detailed response based on user input."""
        self.add_message("user", user_message)  # Add user's input to the history

        # Determine the type of response based on keywords in user input
        if any(keyword in user_message.lower() for keyword in ["what is", "define"]):
            prompt = f"Provide a concise definition of: {user_message}"
        elif "explain" in user_message.lower() or "code" in user_message.lower():
            prompt = f"Explain clearly with examples: {user_message}"
        else:
            prompt = f"Respond concisely to: {user_message}"

        # Send the conversation history with the generated prompt to the Groq API
        self.conversation_history[-1]["content"] = prompt  # Update the last user message
        ai_response = self.client.get_response(self.conversation_history)

        if not ai_response:  # Handle edge case where no response is received
            ai_response = "Sorry, I couldn't process your request at this time."

        # Add the AI's response to the conversation history
        self.add_message("assistant", ai_response)

        return ai_response
