-- Write your query below
SELECT name FROM customers where id NOT IN(Select customer_id FROM orders);  