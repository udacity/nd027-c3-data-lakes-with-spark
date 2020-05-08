from pyspark.sql import SparkSession

def explore_dataframe():
	
	spark = SparkSession.builder.appName("Skewness Introduction").getOrCreate()

	#TODO get your file path from s3 for parking_violation.csv
	input_path = ""
	df = spark.read.format("csv").option("header", True).load(input_path)

	# investigate what columns you have
	col_list = df.columns
	print(col_list)

    # TODO groupby month and year to get count
	year_df = df.groupby("")
    month_df = df.groupby("")

    # TODO write file partition by year, and study the executor in the spark UI
    # TODO use repartition function


if __name__ == "__main__":
	explore_dataframe()
