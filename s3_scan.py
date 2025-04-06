def check_public_buckets():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']
    public_buckets = []
    
    for bucket in buckets:
        try:
            acl = s3.get_bucket_acl(Bucket=bucket['Name'])
            if any(grant['Grantee'].get('URI') == 'http://acs.amazonaws.com/groups/global/AllUsers' 
                   for grant in acl['Grants']):
                public_buckets.append(bucket['Name'])
        except Exception as e:
            print(f"Error checking {bucket['Name']}: {str(e)}")
    
    return public_buckets