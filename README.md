Cloud Sentinel
=======
AWS Cloud Security Monitoring and Hardening Toolkit
    Cloud Sentinel is a modular, Python-based toolkit that helps organizations scan and secure their AWS cloud environment. It performs automated detection of common security misconfigurations and generates detailed reports for review or compliance purposes.
>>>>>>> d60cb94eafb6eed9b8670feedf914d6366732fac

# 🌩️ Cloud Sentinel

**Cloud Sentinel** is an AWS Cloud Security Monitoring and Hardening Toolkit that helps detect misconfigurations, insecure deployments, and risky IAM policies in real-time. It scans IAM, S3, and EC2, sends alerts, and generates compliance-friendly reports.

🔗 [GitHub Repository](https://github.com/Ninadjos/Cloud-Sentinel)

---

## 🚀 Features

- ✅ IAM Audit:
  - Detects overly permissive roles (`*:*`)
  - Flags users without MFA
  - Identifies risky inline policies

- 🪣 S3 Security Scan:
  - Checks public access
  - Ensures encryption at rest
  - Verifies versioning is enabled

- 🖥️ EC2 Risk Check:
  - Flags instances with public IPs
  - Detects insecure AMIs (against a safe list)
  - Audits IAM roles on instances

- 📝 Report Generation:
  - HTML reports using Jinja2
  - Optional PDF output via `xhtml2pdf`

- 🔔 Slack Alerts:
  - Sends a Slack notification if security issues are found

---

## 🏗️ Project Structure

```
Cloud-Sentinel/
├── modules/
│   ├── iam_audit.py
│   ├── s3_scan.py
│   └── ec2_check.py
├── alerts/
│   └── slack_alert.py
├── reports/
├── templates/
│   └── report_template.html
├── main.py
├── report_generator.py
├── tests/
│   └── test_iam_audit.py
└── .github/workflows/deploy.yml
```

---

## 📦 Installation

```bash
git clone https://github.com/Ninadjos/Cloud-Sentinel.git
cd Cloud-Sentinel
pip install -r requirements.txt
```

---

## ⚙️ Usage

Run the full audit with:

```bash
python main.py
```

Or run modules individually:

```bash
python modules/iam_audit.py
python modules/s3_scan.py
python modules/ec2_check.py
```

Reports will be saved in the `/reports/` directory.

---

## ☁️ CI/CD Deployment

Cloud Sentinel can be automatically deployed using GitHub Actions:

- On every push to `main`
- Deploys a CloudFormation stack (`cloud-sentinel`)
- Uses secrets for AWS credentials

See: `.github/workflows/deploy.yml`

---

## 🔔 Slack Integration

To receive Slack alerts:

1. Generate a [Slack Incoming Webhook URL](https://api.slack.com/messaging/webhooks)
2. Add it to `alerts/slack_alert.py`:

```python
WEBHOOK_URL = "https://hooks.slack.com/services/XXX/YYY/ZZZ"
```

---

## ✅ Testing

Includes unit tests for core functions:

```bash
pytest tests/
```

---

## 📄 License

MIT License © [Ninad Joshi](https://github.com/Ninadjos)

---

## 🙌 Contributions Welcome

Have ideas, found a bug, or want to improve Cloud Sentinel?  
Open a PR or start a discussion!

Let's make the cloud safer together. ☁️🔐
Usage - 
python iam_audit.py
python s3_scan.py
python ec2_check.py
python report_generator.py
