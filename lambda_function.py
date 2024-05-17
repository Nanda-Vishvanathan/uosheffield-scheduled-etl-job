import requests
import json
import boto3
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    # Initializing AWS boto3 client to access parameters
    logger.info("Schedule ETL Lambda to process active customer being invoked!")
    ssm_client = boto3.client('ssm')
    customer_processing_url = ssm_client.get_parameter(Name='api_url', WithDecryption=True)['Parameter']['Value']
    target_url = ssm_client.get_parameter(Name='target_url', WithDecryption=True)['Parameter']['Value']
    try:
        # Get request to the API endpoint
        response = requests.get(customer_processing_url)
        # Checking for success response
        if response.status_code == 200:
            logger.info("Successfully invoked Customer & Order processing API")
            customer_list = []
            json_data = response.json()
            # Processing Json response.
            for customer in json_data:
                # Concatenating the first name and surname
                if customer['status'] == 'active':
                    full_name = customer['firstname'] + " " + customer['surname']
                    customer_dict = {'full_name': full_name,
                                     'id': customer['customer_id'],
                                     'email': customer['email'],
                                     'address': customer['address'],
                                     'zip_code': customer['zip_code'],
                                     'region': customer['region'],
                                     'status': customer['status'],
                                     'order_id': customer['order_id'],
                                     'date': customer['date'],
                                     'amount': customer['amount']}
                    customer_list.append(customer_dict)
            logger.info(f"Processed Customer & Order data: {json.dumps(customer_list)}")
            data = json.dumps(customer_list)
            # Invoking the target url
            response = requests.post(target_url, data=data, headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                logger.info("Successfully sent data to the target API : %s", response.status_code)
                return {
                         'statusCode': response.status_code,
                         'body': 'Successfully sent data to the target API'
                }
            else:
                logger.info("Error: Failed to send details to target API: %s", response.status_code)
                return {
                         'statusCode': response.status_code,
                         'body': 'Error: Failed to send data to the target API'
                }

        else:
            logger.info("Error while invoking Customer & Order processing API")
            return {
                     'statusCode': response.status_code,
                     'body': 'API request failed'
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
