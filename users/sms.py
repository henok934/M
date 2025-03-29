import vonage
from django.conf import settings

def send_sms(phone, message):
    # Create a Vonage client using your API Key and Secret
    client = vonage.Client(key=settings.VONAGE_API_KEY, secret=settings.VONAGE_API_SECRET)

    # Prepare the SMS data
    response = client.sms.send(
        to=phone,                             # Recipient's phone number
        from_='+251907252775',                 # Your Vonage virtual number (replace with actual number)
        text=message                          # The message content
    )

    # Check if the SMS was sent successfully
    if response['messages'][0]['status'] == '0':
        return True  # SMS sent successfully
    else:
        print(f"Failed to send SMS: {response['messages'][0]['error-text']}")
        return False  # SMS failed to send
