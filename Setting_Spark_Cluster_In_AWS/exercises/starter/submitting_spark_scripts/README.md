# Exercise: Submitting Spark Scripts

### Instructions: 
1. Download the `cities.csv` dataset to your local machine.
2. Upload the dataset into an S3 location using the AWS S3 console, or you can use the AWS CLI command, like `aws s3 cp <your current file location>/<filename>.csv s3://<bucket_name>`.
3. Create an EMR instance.
4. Create a python program to process the dataset.
5. Copy the program to your EMR instance, preferably in your home directory of EMR instance.
6. Execute the file using `spark-submit <filename>.py`.
