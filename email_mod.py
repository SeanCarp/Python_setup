""" This library sends a text to the specified phone num

It does not have specified email and password, that needs to be
created through the google set-up
"""

# This import uses the MIMEText library to format the text
from email.mime.text import MIMEText

# This import uses smtplib as the connection between the Gmail server
import smtplib

class Email():
    '''A class to hold the data for sending emails'''

    email = None
    password = None
    server = None

    def __init__(self, email, password):
        """
        Initializes the Email class

        Attributes:
            self (self)
            email (str): the email used to send out the text
            password (str): the password used to sign-in to the email
        """

        self.email = email
        self.password = password

        # Setup server connection
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)

        self.server = server
        print('Login successful')


    def send_text(self, subject, body, *to):
        """
        Sends the text to the required person

        Atributes:
            self (self)
            subject (str): the email of the text
            body (str): the body of the text
            *to (str, str): 
                first one is phone num
                second one is mobile provider

            to (str):
                first one is perfect phone email addr
        """

        if self.server is not None or self.email is not None:
            msg = MIMEText(body)
            msg['subject'] = subject
            msg['from'] = self.email

            if(len(to) == 2):
                mobile_providers = {'at&t': '@mms.att.net',
                                'cricket wireless': '@mms.att.net',
                                'metro pcs': '@metropcs.sms.us',
                                'tmobile': '@tmomail.net',
                                'us cellular': '@email.uscc.net',
                                'verizon': '@vtext.com'}
                msg['to'] = to[0] + mobile_providers.get(to[1].lower())
            else:
                msg['to'] = to[0] # You better make sure that is perfect
            
            self.server.send_message(msg)
            print('Sent')