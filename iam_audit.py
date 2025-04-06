import boto3
from policyuniverse.policy import Policy

def audit_iam_policies():
    iam = boto3.client('iam')
    findings = []
    
    # Get all IAM policies
    policies = iam.list_policies(Scope='Local')['Policies']
    
    for policy in policies:
        policy_version = iam.get_policy_version(
            PolicyArn=policy['Arn'],
            VersionId=policy['DefaultVersionId']
        )['PolicyVersion']
        
        document = policy_version['Document']
        policy_analysis = Policy(document)
        
        if policy_analysis.is_internet_accessible():
            findings.append({
                'type': 'IAM',
                'severity': 'HIGH',
                'policy': policy['PolicyName'],
                'issue': 'Overly permissive policy'
            })
    
    return findings