import csv

from pathlib import Path

from google.cloud import bigquery
from google.oauth2 import service_account

## create service account from BQ_CREDS file
credentials = service_account.Credentials.from_service_account_file('.secrets/BQ_CREDS.json')

client = bigquery.Client(credentials=credentials, project=credentials.project_id)


def get_monthly_stats(year, month):
    QUERY = (
        f"""
        SELECT
          COUNT(*) AS num_downloads,
          REGEXP_EXTRACT(file.project, r".*?-(.*?)-(?:.*-)?stubs") AS port,
          REGEXP_EXTRACT(file.project, r".*?-.*?-(?:(.*)-)?stubs") AS board,
          REGEXP_EXTRACT(file.version, r"(.*).post") AS version,
          DATE({year},{month},1) as report_date,
          file.project as project,
          file.version AS version_full,
          -- REGEXP_EXTRACT(file.version, r".*.post(.*)") AS post,
        FROM
          `bigquery-public-data.pypi.file_downloads`
        WHERE
          file.PROJECT LIKE 'micropython-%-stubs' -- Only query the previous month OF history
          AND DATE(timestamp) BETWEEN DATE({year},{month},1)
          AND DATE_ADD(DATE({year},{month},1), INTERVAL 1 MONTH)
          AND details.installer.name <> 'bandersnatch'
        GROUP BY
          port,
          board,
          version,
          project,
          version_full
          -- ,post
        ORDER BY
          `num_downloads` DESC
        """
    )
    query_job = client.query(QUERY)  # API request

    results = query_job.result()  # Waits for query to finish
    return results

stats_list = []

year = 2022
month = 10

for month in range(5,13):
    print(f"Processing {year}-{month} ... ", end="", flush=True)
    results = get_monthly_stats(year, month)
    field_names = [f.name for f in results.schema]
    # print(field_names)
    print(f"Retrieved {results.total_rows} download summaries")
    for row in results:
        stats_list.append(dict(row))

print("writing to csv")
keys = stats_list[0].keys()

with open(Path('./statistics')/'downloads.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()

    dict_writer.writerows(stats_list)

