from twilio.rest import TwilioRestClient
#python 2.7
# inside twilio there's a folder called rest. Inside rest there's a class called "Twilio RestClient

account_sid = "ACad8d05d4c8455296d4c8c55d9644aeb5" # Your Account SID from www.twilio.com/console
auth_token  = "80ebd2c31762767bb1bdac6adf66b03c"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello, this is from Briceida. Today I learned how to write Python code to make HTTP requests to the Twilio API. This is a python script. Neato, eh?",
    to="+12532495659",    # Replace with your phone number
    from_="+12532631811") # Replace with your Twilio number

print(message.sid)
