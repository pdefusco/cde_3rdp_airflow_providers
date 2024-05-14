## AWS Provider Examples

### Installation

```
pip install airflow-provider-great-expectations
```

### Instructions

Create pipeline resource:

```
cde resource create --name my_pipeline_resource   
```

Create files resource:

```
cde resource create --name my_ge_resource
```

Upload files to resources:

```
cde resource upload --name my_ge_resource --local-path ge/yellow_tripdata_sample_2019.csv

cde resource upload --name my_pipeline_resource --local-path ge/ge_dag.py
```

Create & Run CDE Airflow Job:

```
cde job create --name my_pipeline --type airflow --dag-file ge_dag.py --mount-1-resource my_pipeline_resource --airflow-file-mount-1-resource my_ge_resource

cde job run --name my_pipeline
```


### References

Official Documentation: https://airflow.apache.org/docs/apache-airflow-providers-amazon/6.0.0/index.html
