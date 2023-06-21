# etl-data-pipeline-using-aws-EMR-spark-Glue-Athena

In this project, we build an ETL (Extract, Transform, and Load) pipeline for batch processing using [Amazon EMR (Amazon Elastic MapReduce)](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html) and [Spark](https://spark.apache.org/). During this process we will  learn about few of the use case of batch ETL process and how EMR can be leveraged to solve such problems. 

Batch ETL is a common use case across many organizations and this use case implementation learning will provide us a starting point that we can use to build more complex data pipelines in AWS using Amazon EMR.

We are going to use [PySpark](https://spark.apache.org/docs/latest/api/python/) to interact with the Spark cluster. PySpark allows you to write Spark applications using Python APIs. 

## What you will learn

In this guide, you will learn:
- How to create and setup an Amazon EMR cluster 
- How to submit a PySpark job on EMR 
- How to integrate EMR with Amazon S3 
- How to integrate S3 bucket  with Amazon Athena 

## Requirements 

Before Starting this guide, you will need:

- An AWS account (if you don't yet have one, please create one and [set up your environment](https://aws.amazon.com/getting-started/guides/setup-environment/))
- An IAM user that has the access and create AWS resources. 
- Basic understanding of Python

## Use case and problem statement

For this project, let's assume you have a vendor who provides incremental sales data at the end of every month. And the data arrives into S3 bucket as `CSV`file  and it needs to be processed and made available for data analysts or scientists for querying and analysis. 

We need to build a data pipeline  that it will take this new sales file from the S3 bucket, processes it with required transformations using Amazon EMR, and would save the cleaned and transformed data into the target S3 bucket, which will be used later on for querying. 
