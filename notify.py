import notify2
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
ICON_PATH = BASE_DIR +'/assets/logo.png'

def showNotification(message):
    # Initialize the notification system
    notify2.init("Tube Fetch")

    # Create a new notification with icon
    notification = notify2.Notification(
        "Download Complete",
        f"<b>{message}</b>",
        ICON_PATH
    )

    # Optionally, you can set the urgency level (LOW, NORMAL, CRITICAL)
    notification.set_urgency(notify2.URGENCY_NORMAL)

    # Optionally, you can set the timeout for the notification (in milliseconds)
    notification.set_timeout(5000)  # 5 seconds

    # Show the notification
    notification.show()

