from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "[YOUR ACC SID]"
# Your Auth Token from twilio.com/console
auth_token  = "[YOUR AUTH TOKEN]"

def createText(name,location,pop,low):
    rain = None
    cold = None

    if float(pop) >= 50:
        rain = pop
    if float(low) <= 0:
        cold = low

    if rain or cold:
        message = "\n\nHey, " + name + "! \n\nJust a friendly reminder to"
        if rain and cold:
            message += " bring both an umbrella and a jacket! \n\nHere's the forecast:\n"
            message += "A low of " + cold + '\u00b0' + "C"
            message += " with a "+ rain + "% chance of rain in " + location + "\n"
        elif rain:
            message += " bring an umbrella!\n\nHere's the forecast:\n"
            message += pop + "% chance of rain in " + location + "\n"
        elif cold:
            message += " bring a jacket!\n\nHere's the forecast:\n"
            message += cold + '\u00b0' + "C in " + location + "\n"

    return message

def SendText(message, recipient):
        client  = Client(account_sid, auth_token)
        message = client.messages.create(
         to     = recipient,
         from_  = "[PHONE NUMBER REGISTERED TO YOUR TWILIO]",
         body   = message)

