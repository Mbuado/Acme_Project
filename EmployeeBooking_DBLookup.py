

import boto3
import json
from typing import Dict, Any

dynamodb = boto3.client('dynamodb')

EMPLOYEE_TABLE = "Employee"
UNKNOWN = 0
AUTHENTICATED = 1
PIN_REQUIRED = 2
INCORRECT_PIN = 3

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    print(f'Received event: {json.dumps(event, indent=2)}')

    params = event['Details']['Parameters']
    phone_number = params.get('PhoneNumber')
    employee_id = params.get('EmployeeID')
    employee_pin = params.get('EmployeePIN')

    if phone_number:
        query_params = {
            'TableName': EMPLOYEE_TABLE,
            'IndexName': 'PhoneNumber-index',
            'KeyConditionExpression': 'PhoneNumber = :varNumber',
            'ExpressionAttributeValues': {':varNumber': {'S': phone_number}}
        }
    elif employee_id:
        query_params = {
            'TableName': EMPLOYEE_TABLE,
            'KeyConditionExpression': 'EmployeeID = :varNumber',
            'ExpressionAttributeValues': {':varNumber': {'S': employee_id}}
        }
    else:
        return create_return_result()

    return query_employee(query_params, employee_pin)

def query_employee(params: Dict[str, Any], employee_pin: str) -> Dict[str, Any]:
    try:
        response = dynamodb.query(**params)
        print(f"Query succeeded: {json.dumps(response, indent=2)}")
        
        if 'Items' in response and len(response['Items']) == 1:
            item = response['Items'][0]
            return create_return_result(
                item['EmployeeID']['S'],
                item['EmployeeName']['S'],
                item['EmailAddress']['S'],
                item.get('EmployeePIN', {}).get('S'),
                employee_pin
            )
        else:
            return create_return_result()
    except Exception as e:
        print(f"Unable to read item. Error: {str(e)}")
        return create_return_result()

def create_return_result(employee_id=None, employee_name='Unknown', email_address='Unknown', stored_pin=None, provided_pin=None) -> Dict[str, Any]:
    result = {
        'EmployeeID': employee_id,
        'EmployeeName': employee_name,
        'EmailAddress': email_address,
        'EmployeePIN': None
    }
    
    if not employee_id:
        result['EmployeeType'] = UNKNOWN
    elif stored_pin and stored_pin == provided_pin:
        result['EmployeeType'] = AUTHENTICATED
    elif provided_pin:
        result['EmployeeType'] = INCORRECT_PIN
    else:
        result['EmployeeType'] = PIN_REQUIRED
    
    print(f"Returning result: {json.dumps(result)}")
    return result