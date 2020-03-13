from pyspark.sql import SparkSession

def write_file():
	
	spark = SparkSession.builder.appName("write file to S3").getOrCreate()

	#TODO get your file path from s3
	input_path = ""
	df = spark.read.load(input_path)

	# investigate what columns you have
	col_list = df.columns
	print(col_list)
	agg_df = df.groupby("city_name")

	# TODO get your output path - should be different than your input path
	output_path = ""
	agg_df.write.mode("overwrite").parquet(output_path)

if __name__ == "__main__":
	write_file()