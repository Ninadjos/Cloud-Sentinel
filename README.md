# Cloud Sentinel
  AWS Cloud Security Monitoring and Hardening Toolkit

iam_audit.py
    List IAM users, roles, and policies.

  Detect:
    Inline policies with *:*
    Users without MFA
    Overly permissive roles
    Output: List of insecure IAM entities.

s3_scan.py
    List all S3 buckets.

  Check:
    Public access settings
    Encryption at rest
    Versioning enabled
    Output: Vulnerable S3 buckets.

ec2_check.py
    List EC2 instances and check:
    Public IP exposure
    Insecure AMIs (check against a hardcoded safe list)
    IAM roles assigned
    Output: Risky EC2 instances.

report_generator.py
    Accepts results from other modules.

  Generate:
    HTML report using Jinja2 templates
    Optional: PDF via xhtml2pdf
    Output: Saved report in /reports/
    