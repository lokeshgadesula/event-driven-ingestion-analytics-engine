from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
with DAG("analytics_pipeline",start_date=datetime(2026,1,1),schedule="@hourly",catchup=False) as dag:
 validate=BashOperator(task_id="validate",bash_command="echo validate S3")
 spark=BashOperator(task_id="spark",bash_command="spark-submit /opt/jobs/batch_job.py")
 redshift=BashOperator(task_id="redshift",bash_command="echo COPY/MERGE curated data")
 validate>>spark>>redshift
