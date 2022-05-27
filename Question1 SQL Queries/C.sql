SELECT customer.name, customer.email
FROM customer 
JOIN (SELECT TOP 5 customerid, COUNT(orderid) AS customer_orders
FROM orders
GROUP BY customerid
ORDER BY customer_orders DESC) as customers_orders
ON( customer.customerid = customers_orders.customerid)