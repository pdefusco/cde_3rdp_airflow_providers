#****************************************************************************
# (C) Cloudera, Inc. 2020-2024
#  All rights reserved.
#
#  Applicable Open Source License: GNU Affero General Public License v3.0
#
#  NOTE: Cloudera open source products are modular software products
#  made up of hundreds of individual components, each of which was
#  individually copyrighted.  Each Cloudera open source product is a
#  collective work under U.S. Copyright Law. Your license to use the
#  collective work is as provided in your written agreement with
#  Cloudera.  Used apart from the collective work, this file is
#  licensed for your use pursuant to the open source license
#  identified above.
#
#  This code is provided to you pursuant a written agreement with
#  (i) Cloudera, Inc. or (ii) a third-party authorized to distribute
#  this code. If you do not have a written agreement with Cloudera nor
#  with an authorized and properly licensed third party, you do not
#  have any rights to access nor to use this code.
#
#  Absent a written agreement with Cloudera, Inc. (“Cloudera”) to the
#  contrary, A) CLOUDERA PROVIDES THIS CODE TO YOU WITHOUT WARRANTIES OF ANY
#  KIND; (B) CLOUDERA DISCLAIMS ANY AND ALL EXPRESS AND IMPLIED
#  WARRANTIES WITH RESPECT TO THIS CODE, INCLUDING BUT NOT LIMITED TO
#  IMPLIED WARRANTIES OF TITLE, NON-INFRINGEMENT, MERCHANTABILITY AND
#  FITNESS FOR A PARTICULAR PURPOSE; (C) CLOUDERA IS NOT LIABLE TO YOU,
#  AND WILL NOT DEFEND, INDEMNIFY, NOR HOLD YOU HARMLESS FOR ANY CLAIMS
#  ARISING FROM OR RELATED TO THE CODE; AND (D)WITH RESPECT TO YOUR EXERCISE
#  OF ANY RIGHTS GRANTED TO YOU FOR THE CODE, CLOUDERA IS NOT LIABLE FOR ANY
#  DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, PUNITIVE OR
#  CONSEQUENTIAL DAMAGES INCLUDING, BUT NOT LIMITED TO, DAMAGES
#  RELATED TO LOST REVENUE, LOST PROFITS, LOSS OF INCOME, LOSS OF
#  BUSINESS ADVANTAGE OR UNAVAILABILITY, OR LOSS OR CORRUPTION OF
#  DATA.
#
# #  Author(s): Paul de Fusco
#***************************************************************************/

from dateutil import parser
from datetime import datetime, timedelta
from datetime import timezone
from airflow import DAG
from cloudera.cdp.airflow.operators.cde_operator import CDEJobRunOperator
from airflow.providers.amazon.aws.operators.s3 import S3ListOperator
from airflow.operators.dummy_operator import DummyOperator
import pendulum

with DAG(
    dag_id='s3_bucket_tagging_dag',
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    default_args={"bucket_name": BUCKET_NAME},
    max_active_runs=1,
    tags=['example'],
) as dag:

    create_bucket = S3CreateBucketOperator(task_id='s3_bucket_tagging_dag_create', region_name='us-east-1')

    delete_bucket = S3DeleteBucketOperator(task_id='s3_bucket_tagging_dag_delete', force_delete=True)

    get_tagging = S3GetBucketTaggingOperator(task_id='s3_bucket_tagging_dag_get_tagging')

    put_tagging = S3PutBucketTaggingOperator(
        task_id='s3_bucket_tagging_dag_put_tagging', key=TAG_KEY, value=TAG_VALUE
    )

    delete_tagging = S3DeleteBucketTaggingOperator(task_id='s3_bucket_tagging_dag_delete_tagging')

    create_bucket >> put_tagging >> get_tagging >> delete_tagging >> delete_bucket
