import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

import get_all_variables as gav
from validations import get_curr_date
import logging

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

MSG_FORMAT = '%(asctime)s %(levelname)s %(name)s: %(message)s'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(format=MSG_FORMAT, datefmt=DATETIME_FORMAT)
logger = logging.getLogger('spark_app_logs')

logger.setLevel(logging.DEBUG)

def main():
    ## validate spark object
    try:
        logger.info('main() method has started')
        get_curr_date(spark)
        
        
        
    except Exception as exp:
        logger.error('Error occured in main method: '+ str(exp), exc_info=True)
        sys.exit(1)
    
    
    
if __name__ == '__main__':
    main()



job.commit()