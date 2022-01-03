import os

from google.cloud import monitoring_v3

PROJECT_ID = 'metrics-streaming-poc'
json_account_service = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

client = monitoring_v3.services.alert_policy_service.AlertPolicyServiceClient()
client.from_service_account_file(filename=json_account_service)

list_policies = client.list_alert_policies(name='projects/'+PROJECT_ID)

print(list_policies)

