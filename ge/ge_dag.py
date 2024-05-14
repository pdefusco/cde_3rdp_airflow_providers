"""
A DAG that demonstrates use of the operators in this provider package.
"""

from datetime import datetime
import pandas as pd
from airflow import DAG
from airflow.models.baseoperator import chain

from great_expectations_provider.operators.great_expectations import (
    GreatExpectationsOperator,
)
from include.great_expectations.object_configs.example_checkpoint_config import (
    example_checkpoint_config,
)
from include.great_expectations.object_configs.example_data_context_config import (
    example_data_context_config,
)
from include.great_expectations.object_configs.example_runtime_batch_request_for_plugin_expectation import (
    runtime_batch_request,
)

from airflow.operators.dummy_operator import DummyOperator


data_dir = "/app/mount"
data_file = data_dir / "yellow_tripdata_sample_2019-01.csv"


with DAG(
    dag_id="example_great_expectations_dag",
    start_date=datetime(2023, 12, 15),
    catchup=False,
    schedule_interval=None,
) as dag:

    start = DummyOperator(
        task_id="start",
        dag=intro_dag
    )

    ge_data_context_root_directory_no_checkpoint_pass = GreatExpectationsOperator(
        task_id="ge_data_context_root_directory_no_checkpoint_pass",
        data_context_root_dir=ge_root_dir,
        dataframe_to_validate=pd.read_csv(
            filepath_or_buffer=data_file,
            header=1,
            parse_dates=True,
            infer_datetime_format=True,
        ),
        expectation_suite_name="taxi.demo",
        data_asset_name="taxi_dataframe",
        execution_engine="PandasExecutionEngine",
    )

    end = DummyOperator(
        task_id="end",
        dag=intro_dag
    )


start >> ge_data_context_root_directory_no_checkpoint_pass >> end
