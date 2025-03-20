DynamoDB Table and Index Creation Documentation
Step 1: Open DynamoDB in AWS Console
In the AWS Console search bar, type “DynamoDB” and select DynamoDB from the results.
Ensure that your selected region is US East (N. Virginia) by clicking on the region in the upper-right corner of the AWS console and selecting us-east-1.

Step 2: Create a DynamoDB Table
Click on Create table.
Enter Table Name: Employee
Set Partition Key:
Key Name: EmployeeID
Data Type: String
Leave all other settings as default.
Click Create table.
Wait for the table to be created (this may take a few minutes).

Step 3: Create a Secondary Index
In the DynamoDB console, navigate to:
Tables > Employee > Indexes > Create index
Define the index:
Partition Key: PhoneNumber
Index Name: (Automatically populated as PhoneNumber-index)
Click Create index.
Wait for the index to be created (this can take up to 10 minutes).

Step 4: Add an Employee Record to the Table
Navigate to DynamoDB > Tables > Employee > Explore table items.

Click Create item.

In the top-right corner, select JSON.

Enter the following JSON, replacing EmailAddress, EmployeeName, and PhoneNumber with your actual details:

json
Copy
Edit
{
    "EmployeeID": { "S": "101" },
    "EmployeePIN": { "S": "111" },
    "EmailAddress": { "S": "your-email@example.com" },
    "EmployeeName": { "S": "John Doe" },
    "PhoneNumber": { "S": "+1234567890" }
}
Notes:

Use the correct case sensitivity for all parameters.
Enter your PhoneNumber in E.164 format (e.g., +15551234567).
The PIN is stored in plaintext for simplicity, but in a production system, it should be encrypted.
Click Create item.

Wait for the item to be added successfully.


Step 5: Verify Table and Index
Navigate to DynamoDB > Tables > Employee > Explore table items.
Check if the Employee record exists.
To verify the PhoneNumber-index, query the index by selecting:
Indexes > PhoneNumber-index > Query
Enter your PhoneNumber to ensure it retrieves the correct employee details.



Amazon DynamoDB Configuration for Lex Bot Bookings
Step 1: Open DynamoDB in AWS Console
In the AWS Console search bar, type “DynamoDB” and select DynamoDB from the results.
Ensure that your selected region is US East (N. Virginia) (us-east-1) by clicking on the region in the upper-right corner of the AWS console and selecting us-east-1.

Step 2: Create a DynamoDB Table for Bookings
Navigate to DynamoDB > Tables.
Click on Create table.
Enter Table Name: LexBookHotel
Define Partition Key:
Key Name: TripID
Data Type: String
Leave all other settings as default.
Click Create table.
Wait for the table to be created (this process may take a few minutes).

Step 3: Verify the Table Creation
Navigate to DynamoDB > Tables.
Locate the LexBookHotel table.
Click on the table name to view its structure and configuration.
