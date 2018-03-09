import boto3
from botocore.exceptions import ClientError

## Turn on S3 AES-256 encryption
def run_action(rule,entity,params):
    bucket_name = entity['id']
    s3 = boto3.client('s3')

    try:
        result = s3.put_bucket_encryption(
            Bucket=bucket_name,
            ServerSideEncryptionConfiguration={
                'Rules': [
                    {
                        'ApplyServerSideEncryptionByDefault': {
                            'SSEAlgorithm': 'AES256'
                        }
                    },
                ]
            }
        )

        responseCode = result['ResponseMetadata']['HTTPStatusCode']
        if responseCode >= 400:
            text_output = "Unexpected error: %s \n" % str(result)
        else:
            text_output = "Bucket encryption enabled: %s \n" % bucket_name

    except ClientError as e:
        text_output = "Unexpected error: %s \n" % e

    return text_output 