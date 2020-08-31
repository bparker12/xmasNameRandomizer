from email_setup import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
client_secret_file = 'app_cred.json'
api_name = 'gmail'
api_verson = 'v1'
scopes = ['https://mail.google.com/']
year = 2020
 
service = Create_Service(client_secret_file, api_name, api_verson, scopes)

def buildEmail(giver, email, receiver): 
    emailMsg = open("index.html").read().format(giver=giver, year=year, receiver=receiver)
    mimeMessage = MIMEMultipart("alternative")
    mimeMessage['to'] = email
    mimeMessage['subject'] = 'Christmas {} - Parker gift exchange'.format(year)
    mimeMessage.attach(MIMEText(emailMsg, 'html'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
 
    return service.users().messages().send(userId='me', body={'raw': raw_string}).execute()

