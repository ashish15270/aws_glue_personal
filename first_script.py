import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import os

## @params: [JOB_NAME]
#args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
#job.init(args['JOB_NAME'], args)


path = 's3://sampledata9873/project/src/main/python/staging/fact/jf.parquet'

spark.read.parquet(path).show(5,0)


job.commit()