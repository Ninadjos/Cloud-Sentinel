# Cloud Sentinel
  AWS Cloud Security Monitoring and Hardening Toolkit
    
  Cloud Sentinel is a modular, Python-based toolkit that helps organizations scan and secure their AWS cloud environment. It performs automated detection of common security misconfigurations and generates detailed reports for review or compliance purposes.

cloud-sentinel/
├── iam_audit.py           # IAM users, roles, and policy audit
├── s3_scan.py             # S3 bucket security check
├── ec2_check.py           # EC2 instance exposure analysis
├── report_generator.py    # Report generation (HTML + optional PDF)
├── templates/             # Jinja2 templates for reports
└── reports/               # Output reports are saved here

🛡️ Features
iam_audit.py
🔍 Lists IAM users, roles, and policies.

🚨 Detects:

Inline policies with wildcards (*:*)

Users without MFA enabled

Overly permissive IAM roles

📤 Outputs a list of insecure IAM entities.

s3_scan.py
🪣 Lists all S3 buckets.

🔎 Checks for:

Public access configuration

Encryption at rest

Versioning status

📤 Outputs a list of vulnerable S3 buckets.

ec2_check.py
🖥️ Lists EC2 instances.

🧪 Verifies:

Public IP exposure

Use of insecure AMIs (validated against a safe list)

Assigned IAM roles

📤 Outputs a list of risky EC2 instances.

report_generator.py
📝 Accepts JSON/dictionary input from scan modules.

🖨️ Generates:

HTML report using Jinja2

(Optional) PDF report using xhtml2pdf

💾 Saves reports to /reports/

Usage - 
python iam_audit.py
python s3_scan.py
python ec2_check.py
python report_generator.py
