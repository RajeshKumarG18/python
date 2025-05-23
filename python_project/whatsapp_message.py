import pywhatkit as pwk

# Define the recipient's phone number (with country code) and the message
phone_number = "+917975044149"
message = "Hello, this is an automated message sent using Python Hi Vachan C!"

# Send the message
pwk.sendwhatmsg(phone_number, message, 17, 10)