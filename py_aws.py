import boto3
from py_config import read_db_config

 

db_config = read_db_config(filename='config.ini', section='aws-work-lab')

# credential example - http://boto3.readthedocs.io/en/latest/guide/configuration.html
s3 = boto3.resource(
    's3',
    aws_access_key_id=db_config['aws_access_key_id'],
    aws_secret_access_key=db_config['aws_secret_access_key'],
    # aws_session_token=db_config['aws_session_token'],
)

#print(db_config['aws_access_key_id'])


#s3 = boto3.resource('s3')

# session = boto3.Session(profile_name='aws-fcs-dchang')
# Any clients created from this session will use credentials
# from the [dev] section of ~/.aws/credentials.
# s3 = session.resource('s3')
# s3 = boto3.resource('s3') # use default session, boto3
#print(s3.waiter_names)
for bucket in s3.buckets.all():
     print(bucket.name)



# # Upload a new file
# data = open('test.jpg', 'rb')
# s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)