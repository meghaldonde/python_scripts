import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Meghal Donde'
email['to'] = 'meghaldeveloper@gmail.com'
email['subject'] = 'cool program'

email.set_content(html.substitute({'name': 'Meghal'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('meghaltests@gmail.com', '')
  smtp.send_message(email)
  print('Sent email successfully!')