import json
import os

def schedule_notification(title, body, date, time):
    notification_details = {
        "title": title,
        "body": body,
        "date": date,
        "time": time,  
    }
    with open("notification_list.txt", "a") as file:
        file.write(json.dumps(notification_details) + "\n")

def main():
    while True:
        title = input("Title: ")
        body = input("Body: ")
        date = input("Date (YYYY-MM-DD): ")
        time = input("Time (HH:MM): ")
        schedule_notification(title, body, date, time)
        print(f"\n A notification will appear on {date} {time}\n")

if __name__ == "__main__":
    main()

