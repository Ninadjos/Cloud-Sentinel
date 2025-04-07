from slack_sdk import WebClient

def send_slack_alert(message):
    client = WebClient(token=os.getenv('SLACK_TOKEN'))
    response = client.chat_postMessage(
        channel="#security-alerts",
        text=f"🚨 Cloud Security Alert: {message}"
    )
    return response