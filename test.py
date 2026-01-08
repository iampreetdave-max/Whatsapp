import pywhatkit as kit

# Use exception handling for potential errors
try:
    # Recipient's phone number with country code (e.g., +1234567890)
    phone_number = "+919081025277" 
    # Message to be sent
    message = "Hello, this is an automated message from Python!"
    # Time in 24-hour format (Hour, Minute)
    hour = 22  # e.g., 3 PM
    minute = 50 # e.g., 30 minutes

    # Send the message
    kit.sendwhatmsg(phone_number, message, hour, minute)
    print(f"Message scheduled to be sent to {phone_number} at {hour}:{minute}")

except Exception as e:
    print(f"An error occurred: {e}")
