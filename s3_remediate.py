def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = event['detail']['bucketName']
    
    # Block public access
    s3.put_public_access_block(
        Bucket=bucket_name,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        }
    )
    return f"Remediated public access for {bucket_name}"