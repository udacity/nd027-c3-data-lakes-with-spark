In this exercise, we'll be writing a parquet file to an S3 path you desire.
1. First, upload `city.csv` to any desired S3 pth. 
2. Then copy `file_util.py` into your EMR home.
3. Next, SSH into your EMR cluster.
4. Take a look at the `file_util.py` - the input and final paths are empty.
5. Fill in the right input path of `city.csv` (where you uploaded), then write the final path. 
+ If the directory does not yet exist, that is okay. 
+ If the directory doesn't exsit, AWS will create one for you as you write the file.

