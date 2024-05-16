from plyer import notification

# Send a notification
notification.notify(
    title="Title",
    message="Message",
    timeout=5,  # Notification will disappear after 5 seconds
    app_icon="/path/to/icon.ico",  # Path to the icon file
)
