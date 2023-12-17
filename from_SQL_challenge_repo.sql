---Q4.How many days on average are customers reallocated 
--    to a different node?

WITH tnd AS (
  SELECT 
    SUM(end_date - start_date) AS total_node_days,
	customer_id, 
    node_id
  FROM customer_nodes
  WHERE end_date != '9999-12-31'
  GROUP BY customer_id, 
		   node_id, 
		   start_date, 
		   end_date
			)
SELECT 
	ROUND(
		  AVG(total_node_days),
		  2)	
			AS node_days_average
FROM tnd;
