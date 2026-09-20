# Scalable Event-Driven Ingestion & Analytics Engine

Reference dual-path streaming/batch analytics platform using Python, Kafka, Spark Structured Streaming, Airflow, S3 and Redshift.

Kafka -> Spark streaming -> watermark/dedup -> window aggregation -> S3 curated -> Redshift marts  
S3 batch -> Airflow -> Spark batch -> Redshift

Includes runnable local transformation semantics, PySpark streaming/batch jobs, Airflow DAG, Redshift DDL, Docker Kafka and CI.

```bash
pip install -e ".[dev]"
pytest -q
```

