from notification import Notification
from ppadb.client import Client as AdbClient
from adb_server import ADBServer


class NotificationReader:
    """
    A class to interact with an Android device via ADB and retrieve notifications.
    This class uses the `dumpsys notification` command to fetch and parse notification data.

    Attributes:
        server (ADBServer): An instance of the ADBServer class to connect to the ADB server.
    """

    def __init__(self, server: ADBServer) -> None:
        """
        Initializes the NotificationReader instance and connects to the specified Android device.

        Args:
            server (ADBServer): An instance of the ADBServer class to connect to the A
        """
        self._server = server

    def read_notifications(self) -> list[Notification]:
        """
        Reads and displays the notifications from the connected Android device.

        Returns:
            list: A list of Notification objects representing the notifications.
        """
        output = self._fetch_notifications()
        notifications = self._parse_notifications(output)
        return notifications

    def _fetch_notifications(self) -> str:
        """
        Fetches the notification data from the connected Android device.

        Returns:
            str: Raw output from the `dumpsys notification --noredact` command.
        """
        return self._server.fetch_notifications()

    def _parse_notifications(self, output: str) -> list[Notification]:
        """
        Parses the raw notification output from the `dumpsys notification` command.

        Args:
            output (str): The raw output from the dumpsys command.

        Returns:
            list: A list of parsed Notification objects.
        """
        notifications: list[Notification] = []
        lines = output.splitlines()
        current_notification = Notification()
        prev_field = ""

        # Define the notification fields and their corresponding keys
        fields = [
            ("android.title=", "title"),
            ("android.appInfo=", "app_info"),
            ("android.text=", "text"),
            ("android.subtext=", "subtext"),
            ("android.bigText=", "big_text"),
            ("android.messages=", "messages"),
        ]

        for line in lines:
            content = line.lstrip()
            line_is_continued = content == line
            line_is_message = (
                len(content) > 0
                and content[0] == "["
                and "text=" in line
                and prev_field == "messages"
            )

            if (line_is_continued or line_is_message) and prev_field:
                # Continue the previous field if the line is a continuation
                setattr(
                    current_notification,
                    prev_field,
                    getattr(current_notification, prev_field) + "\n" + line,
                )
            else:
                for field, key in fields:
                    if field in line:
                        # If the line contains a title, start a new notification
                        if key == "title" and current_notification.title:
                            notifications.append(current_notification)
                            current_notification = Notification()

                        # Extract the field's value and update the notification object
                        setattr(current_notification, key, line.split("=", 1)[1])
                        prev_field = key
                        break  # Exit the loop once we match a field
                else:
                    prev_field = ""  # Reset if no field matches

        # Append the last notification if it exists
        if current_notification.title:  # Only append if it has a title
            notifications.append(current_notification)

        return notifications

    def display_notifications(self, notifications: list[Notification]) -> None:
        """
        Displays the parsed notifications in a human-readable format.

        Args:
            notifications (list): List of parsed Notification objects.
        """
        for i, notification in enumerate(notifications, start=1):
            print(f"Notification {i}:")
            print(notification)
            print()
