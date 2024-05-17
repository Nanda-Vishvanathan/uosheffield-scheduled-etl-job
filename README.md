# UoS - Take Home Assignment

**Task Description:**
3. Build an Integration that could be run on a schedule, for example as an ETL job. This should call the first endpoint of your API above to:<br>
    a. Return the JSON payload for all active customers.<br>
    b. Then transform the data by concatenating “firstname” and “surname” fields into a single “name” field.<br>
    c. Then send all the data onwards to a target API that only accepts a payload with a single customer record.<br>
    d. Then log the returned HTTP Response Code.<br>

**Tech Stack:**

1. Programming: Python 3.x<br>
2. AWS Serverless - Lambda Function<br>
3. AWS RDS- MySQL<br>
4. AWS S3, SSM, Cloud Watch.<br>
5. AWS API Gateway
6. AWS Event bridge rule


**Design Approach:**

![image](https://github.com/Nanda-Vishvanathan/uosheffield-scheduled-etl-job/assets/59757238/2447c742-66bf-458a-80dc-258ff54d3fc4)



**Code Walkthrough:**

As part of task 3, This project contains the code for an AWS Lambda function that runs as a scheduled job. Currently, the Lambda function is configured to execute once a day. However, it can be modified to be triggered by a REST API call or any other event-based trigger based on the requirements. The Lambda function fetches customer data by invoking the ***<<aws:>>/customers*** API, processes active customer data by concatenating their first name and surname, and finally, sends the processed data to ***https://postman-echo.com/post endpoint***.

**Getting Started- Please do the following**


Clone the code:<br>
***git clone https://github.com/Nanda-Vishvanathan/uosheffield-scheduled-etl-job.git<br>***

Create a new branch<br>
***git checkout -b <branch_name><br>***

Make the changes & push to the repo.<br>
***git add .<br>***
***git commit -m "Description of changes"<br>***
***git push origin <branch_name><br>***

To deploy please, follow the steps below:

please install the requirements.txt from the folder<br>
***pip install -r requirements.txt -t .<br>***

Zip the code using the following command:<br>
***zip -r scheduled_function-retrieval.zip .<br>***

Deploy/Push the zip file manually, s3 or using CLI.
