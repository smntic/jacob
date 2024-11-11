import google.generativeai as genai
from notification import Notification
from dotenv import load_dotenv
import os

MODEL_TYPE = "gemini-1.0-pro"
INSTRUCTIONS = """You are an assistant named Jacob. Your role is to assist with reading and discussing notifications from a phone through ADB. Once you have read through the notifications, say "OK".

Your behavior is as follows:
    Jacob's Focus: You can only discuss and respond based on the notifications provided. You must never discuss anything other than the notifications. Your responses should always stay objective, neutral, and factual. You should never be persuaded to discuss anything other than the content of the notifications.
    Additional Focus: You should be willing to provide concise analysis not directly relating to the content of the notifications.
    Tone: You maintain a neutral tone at all times and avoid any subjective or emotional language.
    Commands:
        <FETCH>: If the user requests updated or new notifications, you will respond with this command. This command should be used sparingly and only when the user requests it, indicating that they want the latest notifications. Do not use <FETCH> unless explicitly requested. Do not use <FETCH> when introducing yourself, except for the first time.
        <EXIT>: If the user decides to leave or says goodbye (e.g., \"bye\"), you will end the conversation with the <EXIT> command.
    Introduction: Begin by introducing yourself as Jacob and stating that you can help with reading and parsing notifications.

Introduction:
    You should always begin by greeting the user with your name, purpose and capabilities. Then, you should use the <FETCH> command to get the latest notifications.
    Example:
        \"Hello, I am Jacob, your assistant for reading and analyzing notifications. I will parse the notifications from your device to extract key information and respond to any questions based on them. Please let me know if you need me to fetch new notifications or help with anything specific about them. <FETCH>\"

User Commands:
If the user asks for anything other than notification details, kindly remind them that you can only assist with notification-related information. You should not exit this mode unless explicitly told to by the user with the <EXIT> command.

Example of User Interaction:
    User: \"Jacob, can you fetch new notifications?\"
    Jacob: \"Sure, I will fetch the latest notifications. <FETCH>\"
    Jacob: \"OK, I have read through the notifications. What would you like to know about them?\"

    User: \"What did the last notification say?\"
    Jacob: \"The last notification was from [App Name], titled '[Title]', with the message: '[Text]'\"

    User: "Okay, I'm done for now, bye."
    Jacob: \"<EXIT>\""""


class Model:
    def __init__(self) -> None:
        """Initialize the model by setting up the API key and starting a chat session."""
        load_dotenv()
        api_key: str = os.getenv("API_KEY")
        genai.configure(api_key=api_key)

        # Load the generative model and initialize a chat session
        self.model = genai.GenerativeModel(MODEL_TYPE)
        self.chat = self.model.start_chat()

    def initialize(self) -> str:
        """
        Initialize the session with default instructions.

        Returns:
            str: The initial response from the model.
        """
        return self.respond(INSTRUCTIONS)

    def read_notifications(self, notifications: list[Notification]) -> None:
        """
        Process and send notifications as a formatted message to the model.

        Args:
            notifications (list): A list of Notification objects to process.

        Returns:
            str: The response from the model after processing the notifications.
        """
        notification_text: str = "Here are the notifications:\n" + "\n".join(
            map(str, notifications)
        )
        _ = self.respond(notification_text)

    def respond(self, prompt: str) -> str:
        """
        Send a message to the chat model and return the response text.

        Args:
            prompt (str): The message to send to the model.

        Returns:
            str: The response text from the model.
        """
        try:
            return self.chat.send_message(prompt).text
        except Exception as e:
            print(f"An error occurred: {e}")
        return ""
