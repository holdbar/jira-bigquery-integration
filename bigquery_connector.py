from google.cloud import bigquery
from google.api_core.exceptions import NotFound, Conflict


class BigQuery:
    def __init__(self, dataset_name='jira'):
        self.client = bigquery.Client()
        self.dataset_name = dataset_name
        self.dataset_ref = self._get_dataset_reference()

    def _get_dataset_reference(self):
        try:
            self.dataset = self.client.get_dataset(self.dataset_name)
        except NotFound:
            self.dataset = self.client.create_dataset(self.dataset_name)
            print(f"Created dataset {self.dataset.full_dataset_id}")

        return self.dataset.reference

    def create_partitioned_table(self, schema, table_name='issues'):
        table_ref = self.dataset_ref.table(table_name)
        table = bigquery.Table(table_ref, schema=schema)

        try:
            table.time_partitioning = bigquery.TimePartitioning(
                type_=bigquery.TimePartitioningType.DAY)
            table = self.client.create_table(table)
            print(f"Created table {table.full_table_id}")
        except Conflict:
            print('Already Exists: Table {table.full_table_id}')
        except Exception as error:
            print(error)
