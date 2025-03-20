Acme Travel Contact Center Implementation Documentation

Project Overview

Acme Travel, a travel company based in San Diego, California, specializes in supporting corporate events such as conferences, seminars, and internal meetings in multiple U.S. cities. To enhance customer service, Acme Travel engaged our team to implement a cloud-based contact center that allows employees to book their travel accommodations for company-sponsored events.

Project Requirements

Implement a self-service application that recognizes an employee’s phone number and authenticates via their previously provided PIN.

If the phone number is unrecognized, prompt the employee to enter their Employee ID and PIN.

Separate queues for authenticated and unknown employees, with priority for authenticated employees.

Personalized greetings for verified employees.

Hotel accommodation booking using a Natural Language Understanding (NLU) chatbot.

Collect location, check-in date, and number of nights for booking, and store this information in a database.

Offer email confirmation of the booking with total reservation costs.

Enable agent-assisted service, ensuring agents greet employees by name.

AWS Services Used

1. Amazon Connect

Implemented the contact flow to manage customer interactions.

Configured call routing based on authentication status.

Integrated with AWS Lambda for dynamic interactions and data retrieval.

2. Amazon Lex

Designed an NLU chatbot to facilitate hotel booking.

Collected and processed user input for location, check-in date, and number of nights.

3. AWS Lambda

Authenticated employees by validating phone numbers and PINs.

Queried and stored booking data in Amazon DynamoDB.

Triggered email confirmations via Amazon Simple Email Service (SES).

4. Amazon DynamoDB

Stored employee authentication details.

Maintained booking information, including hotel selection, check-in date, and duration of stay.

5. Amazon Simple Email Service (SES)

Sent booking confirmation emails with reservation details and total costs.

6. Amazon S3

Stored call recordings and chat transcripts for monitoring and compliance.

Hosted the Agent Contact Control Panel (CCP) webpage for handling customer interactions.

7. Amazon CloudWatch

Monitored system performance and gathered operational metrics.

8. AWS IAM

Managed user roles and permissions for secure access to AWS services.

9. Amazon CloudFront

Delivered the web-based Agent CCP securely and efficiently.

Solution Architecture

The solution follows a structured workflow:

Employee Authentication:

Employee calls into the contact center.

Amazon Connect routes the call and triggers AWS Lambda to validate the phone number and PIN.

If the number is unrecognized, the employee is prompted to enter their Employee ID and PIN.

Successfully authenticated employees are prioritized in the queue.

Booking Process:

The Amazon Lex chatbot assists employees with hotel reservations.

AWS Lambda processes user inputs and stores the booking in DynamoDB.

Confirmation & Assistance:

Upon successful booking, the employee is offered an email confirmation via SES.

If an agent is required, Amazon Connect transfers the call, ensuring the agent greets the employee by name.

Conclusion

The implemented AWS-based contact center solution enables Acme Travel to provide efficient and automated customer service for corporate travel bookings. By leveraging Amazon Connect, Lex, Lambda, and other AWS services, the system delivers seamless authentication, automated booking, and personalized agent interactions, ensuring a superior customer experience.