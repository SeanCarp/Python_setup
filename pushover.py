import requests

class Pushover:
    user_key = None
    api_token = None

    def __init__(self, key, token):
        self.user_key = key
        self.api_token = token

    def send_notification(message, key=user_key, token=api_token, title=None, priority=None):
        """
        Sends a Push notifcation with the PushOver API
        
        Parameters:
            key (user_key): Pushover user key
            token (api_token): Pushover application API token
            message (string): Notification Message
            title (string): Notification title (optional)
            priority (string): Notification priority (optional)"""
        
        URL = 'https://api.pushover.net/1/messages.json'

        data = {
            'user': key,
            'token': token,
            'message': message,
            'title': title,
            'priority': priority
        }

        response = requests.post(URL, data=data)

        # Status RESPONSE
        # NOTE: make sure to read the documentation for the different error codes
        if response.status_code == 200:
            print("Notication sent successfully.")
        else:
            print("Failed to send notifcation. Err:", response.text)


    # Chat-GPT answer
    def send_pushover_notification(user_key, api_token, message, title=None, priority=None):
        """
        Send a push notification via Pushover API.
        
        :param user_key: User's Pushover user key
        :param api_token: Your Pushover application API token
        :param message: Notification message
        :param title: Notification title (optional)
        :param priority: Notification priority (optional)
        """
        url = 'https://api.pushover.net/1/messages.json'
        
        data = {
            'token': api_token,
            'user': user_key,
            'message': message,
            'title': title,
            'priority': priority
        }
        
        response = requests.post(url, data=data)
        
        if response.status_code == 200:
            print("Notification sent successfully.")
        else:
            print("Failed to send notification. Error:", response.text)