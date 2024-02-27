import json
from datetime import datetime


def schedule_notification():
    notification_number = 1  # Start numbering from 1
    while True:
        title = input("Title: ")
        body = input("Body: ")
        date = input("Date (YYYY-MM-DD): ")
        time = input("Time in 24-hour notation (HH:MM): ")

        # Ensure formatting is correct
        try:
            notification_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        except ValueError as e:
            print(f"Error in date/time format: {e}")
            continue

        # Creates dictionary, this is
        notification = {
            "title": title,
            "body": body,
            "datetime": notification_datetime.isoformat()
        }

        with open("notification_list.txt", "a") as file:
            file.write(json.dumps(notification) + "\n")

        print(f"\nA notification will appear on {date} {time}\n")


if __name__ == "__main__":
    schedule_notification()
