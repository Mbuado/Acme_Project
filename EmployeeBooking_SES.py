

import boto3
import json
import logging
from typing import Any, Dict
from botocore.exceptions import ClientError

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize SES client
ses = boto3.client('ses', region_name='us-east-1')

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, str]:
    """
    AWS Lambda handler for sending hotel booking confirmation emails.
    """
    logger.info(f"Incoming Event: {json.dumps(event)}")

    # Extract parameters from the event
    try:
        email_address = event['Details']['Parameters']['EmailAddress']
        booking_price = event['Details']['Parameters']['BookingPrice']
    except KeyError as e:
        logger.error(f"Missing required parameter: {e}")
        return {"lambdaResult": "Error"}

    # Construct the email message
    message = f"""
    <!DOCTYPE html>
    <html>
    <head></head>
    <body>
    <p>Hi</p>
    <p>Thank you for using our service to book a hotel. 
    Your account will be charged for <b>{booking_price} dollars</b>.</p>
    <p>Thank you,<br>The Employee Booking Line</p>
    </body>
    </html>
    """

    # Set up the email parameters
    email_params = {
        "Destination": {
            "ToAddresses": [email_address]
        },
        "Message": {
            "Body": {
                "Html": {
                    "Data": message
                }
            },
            "Subject": {
                "Data": "Your Hotel Booking"
            }
        },
        "Source": "michaelbuado99@gmail.com"
    }

    # Send the email
    try:
        response = ses.send_email(**email_params)
        logger.info(f"Email sent! Message ID: {response['MessageId']}")
        return {"lambdaResult": "Success"}
    except ClientError as e:
        logger.error(f"An error occurred: {e.response['Error']['Message']}")
        return {"lambdaResult": "Error"}
