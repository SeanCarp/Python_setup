# This library sends a text to the specified phone num
#
# It does not have specified email and password, that needs to be
# created through the google set-up

# This import uses the MIMEText library to format the text
from email.mime.text import MIMEText

# This import uses smtplib as the connection between the Gmail server
import smtplib

class Email():
    email = None
    password = None
    server = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

        # Setup server connection
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)

        self.server = server
        print('Login successful')


    def send_text(self, subject, body, *to):
        print(self.email, self.server)

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


if __name__ == '__main__':


