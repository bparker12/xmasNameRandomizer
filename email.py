from emailSetup import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
client_secret_file = 'app_cred.json'
api_name = 'gmail'
api_verson = 'v1'
scopes = ['https://mail.google.com/']
year = 2020
 
service = Create_Service(client_secret_file, api_name, api_verson, scopes)

def buildEmail(giver, receiver): 
    emailMsg = """/
    <html>
        <head></head>
        <body>
            <p>Hey {giver['name']},<br>
            For the {year} Parker Christmas gift exchange, you have been given <strong>{receiver}</strong> as the person whom you will buy a christmas present for! <br>
            <br>
            Best of luck finding <strong>{receiver}</strong> a present!
            </p>
        </body>
    </html>
    """
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = {giver['email']}
    mimeMessage['subject'] = 'Christmas {year} - Parker gift exchange'
    mimeMessage.attach(MIMEText(emailMsg, 'html'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
 
    print(emailMsg)
    return service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
