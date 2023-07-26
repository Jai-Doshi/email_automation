import time
import datetime as dt
import smtplib, ssl
from email.message import EmailMessage
from email.header import Header
from email.utils import formataddr


gmailaddress = 'portfolio4cv@gmail.com'
gmailpassword = 'Badshah2001'

my_friends = {
    0:{
        'name': 'jai doshi',
        'date': '22',
        'month': '10',
        'year': '2001',
        'gmail': 'jaidoshi18@gmail.com'
    },
    1:{
        'name': 'jai viral doshi',
        'date': '22',
        'month': '10',
        'year': '2001',
        'gmail': 'jaiviraldoshi@gmail.com'
    }
}

smtp_server = 'smtp.gmail.com'
port = 587

context = ssl.create_default_context()


with smtplib.SMTP(smtp_server, port) as email:
    email.starttls(context=context)
    email.login(gmailaddress,gmailpassword)
    for i in my_friends:
        time1 = str(dt.datetime.fromtimestamp(time.time()).strftime('%d-%m'))       
        time2 = str(dt.datetime.fromtimestamp(time.time()).strftime('%I:%M:%S:%p'))
        dob = '{}-{}'.format(my_friends[i]['date'], my_friends[i]['month'])
        if time1 == dob:
            email_server = EmailMessage()
            email_server['From'] = formataddr((str(Header('Jai Doshi', 'utf-8')), 'portfolio4cv@gmail.com'))
            email_server['To'] = my_friends[i]['gmail']
            email_server['Subject'] = 'Python Automated System'
            email_server.set_content('Happy Birthday !!!')
            email.send_message(email_server)

            print('Sent!!!')
