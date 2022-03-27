import time
from plyer import notification


def notify_me(title1, message1, timeout1, time_to_show):
    """
    This function notifies you about something you want to be notified about. Just enter the parameters correctly.
    """
    while True:
        n = int(timeout1)
        time.sleep(int(time_to_show))
        notification.notify(
            title = title1,
            message = message1,
            timeout = int(timeout1),
        )
        n = int(timeout1) + 1
        if n > int(timeout1):
            break
        else:
            continue

notify_me("this", "this is a test", "10", "1")