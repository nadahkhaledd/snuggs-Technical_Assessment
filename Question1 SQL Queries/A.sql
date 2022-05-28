SELECT product.productid, product.productname
FROM  product 
JOIN (SELECT TOP 5 productid, COUNT(*) AS product_sales
FROM sales
GROUP BY productid
ORDER BY product_sales DESC) AS s
ON (s.productid = product.productid)
