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

![image](https://github.com/Nanda-Vishvanathan/uosheffield-scheduled-etl-job/assets/59757238/2ec99f02-8fac-4af0-8ade-1a7451fe1473)


**Code Walkthrough:**

As part of task 2, this project contains the code for an AWS Lambda function that is a scheduled job. As of now this lambda is scheduled to run once a day. However, based on the requirements it can be modified to be invoked by a REST API or based on any other trigger.This Lambda function invokes ***<aws:>/customers*** api to query all the active customers, concatenates their firstname and surname and returns the processed data to the target API i.e., ***https://postman-echo.com/post*** <br>

**Code Use**

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

Deploy manually, s3 or using CLI.
