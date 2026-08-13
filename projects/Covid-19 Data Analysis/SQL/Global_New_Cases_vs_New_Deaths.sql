SELECT 
  date,
  SUM(new_confirmed) AS Total_New_Cases,
  SUM(new_deceased) AS Total_New_Deaths
FROM 
  `bigquery-public-data.covid19_open_data.covid19_open_data` 
GROUP BY date
ORDER BY date;
