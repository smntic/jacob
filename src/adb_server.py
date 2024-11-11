from ppadb.client import Client as ADBClient
from ppadb.device import Device
from typing import Optional


class ADBServer:
    def __init__(self, adb_host: str = "127.0.0.1", adb_port: int = 5037):
        """
        Initializes the ADBServer instance and connects to the specified ADB server.

        Args:
            adb_host (str): Host address for the ADB server (default is localhost).
            adb_port (int): Port for the ADB server (default is 5037).
        """
        self._client = ADBClient(host=adb_host, port=adb_port)
        self._device: Optional[Device] = None

    def select_device(self) -> None:
        """Select a device to connect to from the list of connected devices."""
        while True:
            # List all devices connected to the ADB server
            self._list_devices()
            num_devices = self._num_devices()

            # If there are no devices, prompt the user to connect a device
            if num_devices == 0:
                print("No devices found. Please connect a device to continue.")
                input("Press Enter to refresh the device list.")
            else:
                try:
                    # Prompt the user to select a device
                    index = int(input("Select a device: "))
                    # Connect to the selected device
                    if self._connect_device(index):
                        print(f"Connected to device: {self._device.serial}")
                        break
                    else:
                        print("Invalid device. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid device index.")


    def _list_devices(self) -> None:
        """Print a list of all devices connected to the ADB server."""
        devices = self._client.devices()
        for index, device in enumerate(devices):
            print(f"{index}: {device.serial}")
        
    def _num_devices(self) -> int:
        """Return the number of devices connected to the ADB server."""
        return len(self._client.devices())

    def _connect_device(self, index: int) -> bool:
        """
        Connects to a specific device based on the index in the list of connected devices.

        Args:
            index (int): The index of the device to connect to.

        Returns:
            bool: True if the device was successfully connected, False otherwise.
        """
        # Get the device from the list of connected devices
        devices = self._client.devices()
        if index < len(devices) and index >= 0:
            self._device = devices[index]
            return True
        return False

    def fetch_notifications(self) -> str:
        """
        Fetches the notification data from the connected Android device.

        Returns:
            str: Raw output from the `dumpsys notification --noredact` command.
        """
        return self._device.shell("dumpsys notification --noredact")
