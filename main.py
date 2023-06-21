from pyspark.sql import SparkSession
from pyspark.sql import functions as F

S3_SOURCE_DATA_PATH = 's3:<YOUR_BUCKET_NAME>/raw-data/sales-dataset.csv'
S3_DEST_DATA_PATH = 's3:<YOUR_BUCKET_NAME>/cleaned-raw/'


def main():
    spark = SparkSession.builder.appName("ETL sales App").getOrCreate()
    spark.sparkContext.setLogLevel('ERROR')

    # Spark Dataframe (Raw)- Transformation 
    df = spark.read.option("Header", True).option("InferSchema", True).csv(S3_SOURCE_DATA_PATH)
    
    replacements = {c:c.replace(' ','_') for c in df.columns if ' ' in c}
    selected_df = df.select([F.col(c).alias(replacements.get(c, c)) for c in df.columns])

    print('Total no. of records in the source data set is:%s' %selected_df.count())
    selected_df.write.mode('overwrite').parquet(S3_DEST_DATA_PATH)
    print('The cleaned data was successfully uploaded to S3:%s' %S3_DEST_DATA_PATH)


if __name__ == '__main__':
    main()


    