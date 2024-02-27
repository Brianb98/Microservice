from plyer import notification
from datetime import datetime
import json
import time


def send_notifications():
    while True:
        with open("notification_list.txt", "r") as infile:
            lines = infile.readlines()
            # Each notification is a line in the .txt
        
        current_datetime = datetime.now()
        updated_lines = []
        for line in lines:
            try:
                notification_details = json.loads(line)
                notification_datetime = datetime.fromisoformat(notification_details["datetime"])

                # If it's an approriate time (time in the future), then create the notification.
                if current_datetime >= notification_datetime:
                    notification.notify(
                        title=notification_details["title"],
                        message=notification_details["body"],
                        app_icon="notif_icon.ico"
                    )
                    print(f"The notification has appeared")
                    continue
            except Exception as error:
                print(f"Error: {error}")
            
            updated_lines.append(line)
        
        with open("notification_list.txt", "w") as outfile:
            outfile.writelines(updated_lines)
        
        # Checking the .txt every 5 seconds.
        time.sleep(5)

if __name__ == "__main__":
    send_notifications()


