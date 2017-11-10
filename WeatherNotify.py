import weatherCheck

#Must verify your phone number with twilio beforehand.
name = "[Your Name]"
phoneNumber = "[Your Phone Number]"
location = "[Your Location]"

start = weatherCheck.User(name,phoneNumber,location)
start.notifyUser()