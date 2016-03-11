from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACbd533d1e7ff5c5d273a813c5e0641703"
auth_token  = "cd1d506bffd692488651c9e0567d7829"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="HEYO",
    to="+2012130126",    # Replace with your phone number
    from_="+8622608990") # Replace with your Twilio number
print message.sid
