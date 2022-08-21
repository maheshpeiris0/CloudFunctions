
from google.cloud import bigquery


def hello_world(request):


    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("EMPLOYEE_ID", "INTEGER"),
        bigquery.SchemaField("FIRST_NAME", "STRING"),
        bigquery.SchemaField("LAST_NAME", "STRING"),
        bigquery.SchemaField("EMAIL", "STRING"),
        bigquery.SchemaField("PHONE_NUMBER", "STRING"),
        bigquery.SchemaField("HIRE_DATE", "STRING"),
        bigquery.SchemaField("JOB_ID", "STRING"),
        bigquery.SchemaField("SALARY", "FLOAT"),
        bigquery.SchemaField("MANAGER_ID", "STRING"),
        bigquery.SchemaField("DEPARTMENT_ID", "STRING"),


    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
    )

    table_id = "my-website-308711.cloud_functions.employee"


    uri = "gs://cloud_functions_dataset/employees.csv"

    load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
    )


    load_job.result()  # Waits for the job to complete.

    destination_table = client.get_table(table_id)


    print("Loaded {} rows.".format(destination_table.num_rows))
    return f'check the results in the logs'


