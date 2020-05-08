from pyspark.sql import SparkSession

def repartition():
    spark = SparkSession.builder.appName("Repartition Example").getOrCreate()

    # TODO Path to your file
    df = spark.read.format('csv').load()


    #TODO explore & do some transformations and actions and see how Spark works,
    # especially on the executor tab
    # for example.. write is an action
    # fill it in with your desired path and look at the executor tab
    df.write.partitionBy('year').csv("")

    # Now, try doing repartition
    # TODO Add the number of your workers
    # Write another path, and take a look at Executor tab. What changed?
    df.repartition().write.csv("")

    
if __name__ == "__main__":
    repartition()
