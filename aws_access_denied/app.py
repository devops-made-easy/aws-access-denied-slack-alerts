import json
import requests
import os

def send_slack_message(content):
    webhook = os.environ['SLACK_WEBHOOK_URL']
    payload = {
        "attachments": content
    }
    requests.post(webhook,
                  json.dumps(payload),
                  headers={'content-type': 'application/json'})
    

def lambda_handler(event, context):
    slack_payload = {
        "attachments": [
            {
                "fallback": "AWS Access Denied Event Notification",
                "color": "danger",
                "author_name": "DEVOPS-MADE-EASY",
                "title": event['detail']['eventName'] + " Operation attempted on " + event['source'],
                "text": event['detail']['errorMessage'],
                "fields": [
                    {
                        "title": "ErrorCode",
                        "value": event['detail']['errorCode'],
                        "short": True
                    },
                    {
                        "title": "Account ID",
                        "value": event['detail']['userIdentity']['accountId'],
                        "short": True
                    },
                    {
                        "title": "Region",
                        "value": event['detail']['awsRegion'],
                        "short": True

                    },
                    {
                        "title": "Prinicpal",
                        "value": event['detail']['userIdentity']['principalId'],
                        "short": True

                    }
                ],
                "footer": "DEVOPS MADE EASY ALERTS"
            }
        ]
    }
    send_slack_message(slack_payload)


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
