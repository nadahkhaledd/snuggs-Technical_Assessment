SELECT customer.name, customer.email
FROM customer 
JOIN (SELECT TOP 5 customerid, SUM(amount) AS total_amount
FROM orders
GROUP BY customerid
ORDER BY total_amount DESC) AS total
ON( total.customerid = customer.customerid)
