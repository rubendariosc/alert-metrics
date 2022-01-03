import os

from google.cloud import monitoring_v3

PROJECT_ID = 'metrics-streaming-poc'
json_account_service = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

queries = monitoring_v3.services.query_service.QueryServiceClient()
queries.from_service_account_file(filename=json_account_service)

types = monitoring_v3.types.QueryTimeSeriesRequest()
types.name = 'projects/'+PROJECT_ID
types.query = """
                fetch dataflow_job
                | metric 'dataflow.googleapis.com/job/system_lag'
                | filter (resource.job_name == 'datadog-normalization-0-2-1')
                | group_by 5m, [value_system_lag_mean: mean(value.system_lag)]
                | every 5m
                | condition val() > 7 's'
              """

for q in queries.query_time_series(request=types):
    print(q)
