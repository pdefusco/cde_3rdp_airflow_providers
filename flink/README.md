## GitHub Provider Examples

### Installation

```
pip install apache-airflow-providers-apache-flink
```

### Instructions

Create pipeline resource:

```
cde resource create --name my_pipeline_resource   
```

Create files resource:

```
cde resource create --name my_file_resource
```

Upload files to resources:

```
cde resource upload --name my_file_resource --local-path flink/flinkjob.jar

cde resource upload --name my_pipeline_resource --local-path flink/flink_job_dag.py
```

Create & Run CDE Airflow Job:

```
cde job create --name my_pipeline --type airflow --dag-file flink_job_dag.py --mount-1-resource my_pipeline_resource --airflow-file-mount-1-resource my_file_resource

cde job run --name my_pipeline
```




### References

Official Documentation: https://airflow.apache.org/docs/apache-airflow-providers-amazon/6.0.0/index.html
