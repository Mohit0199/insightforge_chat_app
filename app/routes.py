from flask import Blueprint, render_template, request, jsonify
import re
from app.utils import format_response
from app.chat import ChatManager


# Create a Blueprint for the main application
main = Blueprint('main', __name__)

chat_manager = ChatManager()


@main.route('/')
def index():
    """Render the chat interface."""
    return render_template('chat.html')


@main.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages from users."""
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    # Get AI response using updated ChatManager logic
    ai_response = chat_manager.get_response(user_message)

    # Format the response if necessary (e.g., replace newlines)
    formatted_response = format_response(ai_response)

    return jsonify({"response": formatted_response})  # Return the formatted AI's response as JSON