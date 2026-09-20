# Scalable Event-Driven Ingestion & Analytics Engine

Reference dual-path streaming/batch analytics platform using Python, Kafka, Spark Structured Streaming, Airflow, S3 and Redshift.

Kafka -> Spark streaming -> watermark/dedup -> window aggregation -> S3 curated -> Redshift marts  
S3 batch -> Airflow -> Spark batch -> Redshift

Includes runnable local transformation semantics, PySpark streaming/batch jobs, Airflow DAG, Redshift DDL, Docker Kafka and CI.

```bash
pip install -e ".[dev]"
pytest -q
```

Local tests validate deduplication and aggregation semantics. Kafka/Spark/Airflow/AWS end-to-end execution requires those services/credentials. No throughput claims are made without benchmarks.
