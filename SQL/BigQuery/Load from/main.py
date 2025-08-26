# import bq_to_csv
#
sql = "SELECT * FROM kaggle-bq-249420.ecom_data_mart.warehouse"
project_id = "kaggle-bq-24940"
#
# if __name__ == '__main__':
#     bq_to_csv.BigQueryCsvLoader(
#     file_path="warehouse.csv",
#     sql=sql,
#     project_id=project_id)
#
import pandas_gbq

df = pandas_gbq.read_gbq(sql, project_id)

df.head()
df.info()