# Exercise: Submitting Spark Scripts

### Instructions: 
1. Download the `cities.csv` dataset to your local machine.
2. Upload a file into an S3 location using the AWS S3 console, or you can use the AWS CLI command, like `aws s3 cp <your current file location>/<filename> s3://<bucket_name>`.
3. Create an EMR instance.
4. Copy the file to your EMR instance, preferably in your home directory of EMR instance.
5. Execute the file using `spark-submit <filename>.py`.
