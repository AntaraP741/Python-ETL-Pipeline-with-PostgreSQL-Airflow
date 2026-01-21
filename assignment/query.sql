CREATE TABLE orders_raw (
    order_id INT,
    customer_name VARCHAR(100),
    product VARCHAR(100),
    amount DECIMAL(10,2),
    order_date DATE,
    created_at TIMESTAMP
);

CREATE TABLE orders_clean (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    product VARCHAR(100),
    amount DECIMAL(10,2),
    order_date DATE,
    created_at TIMESTAMP,
    order_value_category VARCHAR(20)
);

INSERT INTO orders_raw VALUES
(1, 'Alice', 'Laptop', 45000, '2026-01-20', NOW()),
(2, 'Bob', 'Mouse', 500, '2026-01-20', NOW()),
(3, 'Charlie', 'Phone', -100, '2026-01-21', NOW()),
(4, 'Mary', 'Keyboard', 1000, '2026-01-24', NOW()),
(5, '%%$', 'Bottle', -5600, '2026-01-26', NOW()),
(6, 'Aditi', 'PlayStation', 56100, '2026-01-01', NOW()),
(7, 'Akansha', 'Book', 67777700, '2026-01-02', NOW());

SELECT * FROM ORDERS_RAW
SELECT * FROM ORDERS_CLEAN
