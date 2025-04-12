from modules.iam_audit import audit_iam_policies
from modules.s3_scan import check_public_buckets
from alerts.slack_alert import send_slack_alert

def main():
    findings = []
    findings += audit_iam_policies()
    findings += check_public_buckets()
    
    if findings:
        send_slack_alert(f"{len(findings)} security issues found!")
        generate_html_report(findings)