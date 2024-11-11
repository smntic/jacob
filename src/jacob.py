from adb_server import ADBServer
from notification_reader import NotificationReader
from model import Model
from typing import Optional

EXIT_COMMAND = '<EXIT>'
FETCH_COMMAND = '<FETCH>'

def initialize_model() -> tuple[Model, str]:
    """Initialize the model and handle setup responses."""
    model = Model()
    response = model.initialize()
    return model, response

def process_response(response: str) -> tuple[str, Optional[str]]:
    """
    Process the model's response to check for special commands.
    Returns:
        A tuple of the cleaned response and the action to perform, if any.
    """
    if EXIT_COMMAND in response:
        return response.replace(EXIT_COMMAND, '').strip(), 'exit'
    elif FETCH_COMMAND in response:
        return response.replace(FETCH_COMMAND, '').strip(), 'fetch'
    return response, None

def fetch_notifications(reader: NotificationReader, model: Model) -> None:
    """Fetch notifications and process them with the model."""
    print("Fetching notifications...")
    notifications = reader.read_notifications()
    model.read_notifications(notifications)

def main_loop(reader: NotificationReader) -> None:
    """Main interactive loop to handle model responses and user input."""
    model, response = initialize_model()

    while True:
        response, action = process_response(response)
        print(response)

        if action == 'exit':
            print("Exiting program...")
            break
        elif action == 'fetch':
            fetch_notifications(reader, model)

        user_input = input('>>> ')
        response = model.respond(user_input)

if __name__ == '__main__':
    server = ADBServer()
    server.select_device()
    reader = NotificationReader(server)

    main_loop(reader)
