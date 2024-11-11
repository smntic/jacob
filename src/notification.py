from typing import Optional


class Notification:
    """
    A class to represent a single notification.

    Attributes:
        title (str): The title of the notification.
        app_info (str): Information about the app generating the notification.
        text (str): The main text content of the notification.
        subtext (str): Any additional subtext associated with the notification.
        big_text (str): A longer version of the notification text, if available.
        messages (str): Any additional message content, if available.
    """

    def __init__(
        self,
        title: Optional[str] = None,
        app_info: Optional[str] = None,
        text: Optional[str] = None,
        subtext: Optional[str] = None,
        big_text: Optional[str] = None,
        messages: Optional[str] = None,
    ) -> None:
        """
        Initializes a Notification object with optional attributes.

        Args:
            title (str, optional): The title of the notification.
            app_info (str, optional): The app info of the notification.
            text (str, optional): The main text of the notification.
            subtext (str, optional): Subtext of the notification.
            big_text (str, optional): The big text of the notification.
            messages (str, optional): Additional message contents of the notification.
        """
        self.title = title
        self.app_info = app_info
        self.text = text
        self.subtext = subtext
        self.big_text = big_text
        self.messages = messages

    def __repr__(self) -> str:
        """String representation for displaying notification contents."""
        return (
            f"Notification(title={self.title}, app_info={self.app_info}, text={self.text}, "
            f"subtext={self.subtext}, big_text={self.big_text}, messages={self.messages})"
        )
