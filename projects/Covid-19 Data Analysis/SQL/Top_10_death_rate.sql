SELECT 
  country_name,
  MAX(cumulative_deceased) / MAX(cumulative_confirmed) AS deceased_rate
FROM
  `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE cumulative_confirmed > 100000
GROUP BY country_name
ORDER BY deceased_rate DESC
LIMIT 10;