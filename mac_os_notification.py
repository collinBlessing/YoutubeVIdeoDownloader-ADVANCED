import os


def send_notification(title, message):
    os.system(
        """
              osascript -e 'display notification "{}" with title "{}"'
              """.format(
            message, title
        )
    )


# Example usage:
send_notification("Title", "Message")
