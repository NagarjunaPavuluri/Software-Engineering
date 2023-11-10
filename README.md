# Software-Engineering


1.Write the serverless,frontend and back end files for the delete-property

2. Create a DynamoDB table:
   - Go to the AWS Management Console and navigate to the DynamoDB service.
   - Click on "Create table" and provide a table name, such as "properties".
   - Set the primary key as "pid" of type String.
   - Leave the other settings as default and click on "Create".

3. Create a Lambda function:
   - Go to the AWS Management Console and navigate to the Lambda service.
   - Click on "Create function" and choose "Author from scratch".
   - Provide a function name, such as "deletePropertyLambda".
   - Select the runtime as "Python 3.8".
   - Under "Permissions", choose an existing or create a new execution role with appropriate permissions for DynamoDB.
   - Click on "Create function".

4. Upload the Lambda function code:
   - In the Lambda function configuration page, scroll down to the "Function code" section.
   - Choose the "Upload a .zip file" option and click on "Upload".
   - Select the ZIP file containing your Lambda function code (e.g., deleteProperty.zip).
   - Click on "Save" to upload the code and update the Lambda function.

5. Create a REST API:
   - Go to the AWS Management Console and navigate to the API Gateway service.
   - Click on "Create API" and choose "REST API".
   - Select the "New API" option and provide a name for your API.
   - Click on "Create API".

6. Create a resource and method:
   - In the API Gateway configuration page, click on "Actions" and choose "Create Resource".
   - Provide a resource name, such as "delete-property".
   - Click on "Create Resource".
   - On the newly created resource, click on "Actions" and choose "Create Method".
   - Select the DELETE method and choose the Lambda function integration type.
   - Select the region where your Lambda function is deployed.
   - Enter the Lambda function name and click on "Save".

7. Deploy the API:
   - In the API Gateway configuration page, click on "Actions" and choose "Deploy API".
   - Select the "New Stage" option and provide a stage name, such as "dev".
   - Click on "Deploy" to deploy the API.

8. Test the application:
   - In the API Gateway configuration page, navigate to the "Dashboard" tab.
   - Copy the "Invoke URL" for your deployed API.
   - Open the Cloud9 IDE and upload index.html.
   - Replace the API endpoint URL in the front-end code with the copied "Invoke URL".
   - Save the index.html file.
   - Right-click on the index.html file in Cloud9 and choose "Preview".
   - Click on the preview link to open the front-end application in a new tab.
   - Enter a property ID and click "Delete" to test the delete functionality.


9. Debug and verify the result:
   - In the Lambda function configuration page, go to the "Monitoring" tab.
   - Review the logs and any error messages to debug any issues.
   - Verify that the property is deleted from the DynamoDB table.
   - Check if the response from the API is as expected in the front-end application.




