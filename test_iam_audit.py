# tests/test_iam_audit.py
def test_overly_permissive_policy():
    test_policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }]
    }
    assert is_policy_permissive(test_policy) == True