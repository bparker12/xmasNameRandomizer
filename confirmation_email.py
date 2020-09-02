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

# this email is the key for the gift exchange.  takes the dictionary and changes into a list of strings, then joins the strings
def buildKeyEmail(lst, email):
    msg = []
    for person_id, person_info in lst.items():
        msg.append(person_info['giver'] + ' is getting a gift for ' + person_info['receiver'] + '\n')
    emailMsg = ' '.join(msg)
    mimeMessage = MIMEMultipart("alternative")
    mimeMessage['to'] = email
    mimeMessage['subject'] = 'Christmas {} - Parker gift exchange Key'.format(year)
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
 
    return service.users().messages().send(userId='me', body={'raw': raw_string}).execute()

