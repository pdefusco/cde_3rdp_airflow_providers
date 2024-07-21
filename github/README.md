## GitHub Provider Examples

### Installation

```
pip install apache-airflow-providers-github
```

### Instructions

Create Airflow DAG resource:

```
cde resource create --name git_provider_resource   
```

Create files resource:

```
cde resource create --name my_file_resource
```

Upload files to resources:

```
cde resource upload --name my_file_resource --local-path github/my_file.txt

cde resource upload --name git_provider_resource --local-path github/git_list_repos_dag.py --local-path github/git_create_file_dag.py
```

Create & Run CDE Airflow Job:

```
cde job create --name git_list_repos_dag --type airflow --dag-file git_list_repos_dag.py --mount-1-resource git_provider_resource

cde job create --name git_create_file_dag --type airflow --dag-file git_create_file_dag.py --mount-1-resource git_provider_resource --airflow-file-mount-1-resource my_file_resource
```

### References

Official Documentation: https://airflow.apache.org/docs/apache-airflow-providers-amazon/6.0.0/index.html
