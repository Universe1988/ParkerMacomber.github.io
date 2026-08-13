SELECT
  country_name,
  MAX(cumulative_confirmed) AS total_cases
FROM
  `bigquery-public-data.covid19_open_data.covid19_open_data`
GROUP BY country_name
ORDER BY total_cases DESC
LIMIT 10;