In the folder are two Python programs. 
"implement_notifications.py" is the actual microservice, it must be continuously run in the background until the specified date of the notification to function properly.
"call_notifications.py" is a program that gives an example on how to call the microservice.

Make sure you enable notifications from apps and other senders on your computer for this to work.
I did not have it enabled initially and was not getting notifications.

An outside program must write into "notification_list.txt" a dictionary onto 1 line.
This dictionary must contain 4 key:value pairs, with the keys being: "title", "body", "date", and "time".
The value for "title" should be the header you want to appear with the notification.
The value for "body" should be a longer more detailed message.
The value for "date" should be in YYYY-MM-DD format.
The value for "time" should be in HH:MM format.

This is an example of 2 different notifications that can be accepted when written into "notification_list.txt".
{"title": "Assignment 1", "body": "For Biology", "date": "2024-02-26", "time": "23:59"}
{"title": "Assignment 2", "body": "Don't forget the quiz as well.", "date": "2024-02-28", "time": "21:00"}

If the date or time is given in an inappropriate format, an error will be given.
If there are no errors, then you should receive a print statement confirming that a notification will be sent.

![UML_sequence](https://github.com/Brianb98/Microservice/assets/122406696/0ed49648-7954-44ba-9524-6036102fc179)
