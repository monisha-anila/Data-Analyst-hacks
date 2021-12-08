# AWS
- AWS is one of the leading cloud computing services company that offers `pay-as-you-go` model charges for the cloud services we use. 
- AWS services are useful from `data pipeline -> storage -> Visualisations -> ML model -> Notifications` etc (Sample example given)

## Sample scenarios of S3 bucket
#### 1. How can I tell how many objects I've stored in an S3 bucket?	
-  *aws s3 ls s3://bucketName/path/ --recursive --summarize | grep "Total Objects:"*

#### 2. Copy Files from one S3 Bucket to another S3 Bucket (in same region) 	
- *aws s3 cp s3://from-source/ s3://to-destination/*

#### 3. Copy files from one S3 to another S3 bucket (Transfer only Missing/Out dated files of same region)
- *aws s3 sync s3://from-source s3://to-destination*

#### 4. Convert all files in a folder to .json files	
- **aws s3 cp s3://from-source/folder s3://from-source/folder --exclude '*.json'  --content-type="application/json" --metadata-directive="REPLACE" --recursive**

## How to convert thousands of individual .json files into 1 .csv file using AWS glue?
***Assumption here is that we're using AWS S3 bucket file and store the transformed file back to S3***

#### Import basic libraries
- import sys
- from awsglue.transforms import *
- from awsglue.utils import getResolvedOptions
- from pyspark.context import SparkContext
- from awsglue.context import GlueContext
- from awsglue.job import Job

#### Use on glue job and Spark context language
- args = getResolvedOptions(sys.argv, ['JOB_NAME'])
- sc = SparkContext()
- glueContext = GlueContext(sc)
- spark = glueContext.spark_session

#### Import overwrite feature
- spark.conf.set("spark.sql.sources.partitionOverwriteMode","dynamic")
- job = Job(glueContext)
- job.init(args['JOB_NAME'], args)

#### Put database and table names for transformation
- datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "database_name", table_name = "name_of_the_table", transformation_ctx = "datasource0")

#### Only transfer important fields
- applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [("field_name", "field_type", "field_name", "field_type")], transformation_ctx = "applymapping1")

#### Combine individual into 1 file
- datasource_df = applymapping1.repartition(1)
- spark.conf.set("spark.sql.sources.partitionOverwriteMode","dynamic")
- ds = datasource_df.toDF()

#### Save the overwrite file to S3 bucket
- ds \
  .write.mode('overwrite') \
  .format('csv') \
.options(header='true') \
  .save('s3://path')
 
 #### Close job  
- job.commit()






