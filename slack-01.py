from slack_webhook import Slack

slack = Slack(url='<Slack Webhook URL>')
slack.post(text="Hello, world.")