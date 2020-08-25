from twilio.rest import Client

account_sid = 'AC1d6ce76e91480dc7954a672c3beb4947'
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+14054671238',
    body='hi there!',
    to=''
)

print(message.sid)