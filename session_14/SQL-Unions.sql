SELECT salary AS expenditure,"-" AS income FROM employees GROUP BY id
 union
SELECT "-" as expenditure, total_sales as income FROM works_with;

SELECT
    'Expenditure' AS transaction_type,
    e.id AS transaction_id,
    e.given_name AS employee_first_name,
    e.family_name AS employee_last_name,
    b.branch_name AS branch_name,
    bs.supplier_name AS supplier_name,
    bs.supply_type AS supply_type,
    -w.total_sales AS amount
FROM
    employees e
LEFT JOIN
    works_with w ON e.id = w.employee_id
LEFT JOIN
    branches b ON e.branch_id = b.id
LEFT JOIN
    branch_suppliers bs ON b.id = bs.branch_id
WHERE
    w.total_sales < 0

UNION

SELECT
    'Income' AS transaction_type,
    e.id AS transaction_id,
    e.given_name AS employee_first_name,
    e.family_name AS employee_last_name,
    b.branch_name AS branch_name,
    NULL AS supplier_name,
    NULL AS supply_type,
    w.total_sales AS amount
FROM
    employees e
LEFT JOIN
    works_with w ON e.id = w.employee_id
LEFT JOIN
    branches b ON e.branch_id = b.id
WHERE
    w.total_sales > 0;


SELECT
    'Expenditure' AS transaction_type,
    e.id AS transaction_id,
    e.given_name AS employee_first_name,
    e.family_name AS employee_last_name,
    b.branch_name AS branch_name,
    NULL AS supplier_name,
    NULL AS supply_type,
    e.salary AS amount
FROM
    employees e
LEFT JOIN
    branches b ON e.branch_id = b.id

UNION

SELECT
    'Income' AS transaction_type,
    e.id AS transaction_id,
    e.given_name AS employee_first_name,
    e.family_name AS employee_last_name,
    b.branch_name AS branch_name,
    NULL AS supplier_name,
    NULL AS supply_type,
    w.total_sales AS amount
FROM
    employees e
LEFT JOIN
    works_with w ON e.id = w.employee_id
LEFT JOIN
    branches b ON e.branch_id = b.id
WHERE
    w.total_sales > 0;

SELECT * FROM works_with;
SELECT * FROM clients;

SELECT
    'Expenditure' AS transaction_type,
    e.id AS transaction_id,
    e.given_name AS employee_first_name,
    e.family_name AS employee_last_name,
    b.branch_name AS branch_name,
    NULL AS client_name,
    e.salary AS amount
FROM
    employees e
LEFT JOIN
    branches b ON e.branch_id = b.id

UNION

SELECT
    'Income' AS transaction_type,
    e.id AS transaction_id,
    e.given_name AS employee_first_name,
    e.family_name AS employee_last_name,
    b.branch_name AS branch_name,
    c.client_name,
    w.total_sales AS amount
FROM
    employees e
LEFT JOIN
    works_with w ON e.id = w.employee_id
LEFT JOIN
    branches b ON e.branch_id = b.id
LEFT JOIN
    clients c ON w.client_id = c.id
WHERE
    w.total_sales > 0;
    
    
SELECT
    'Expenditure' AS transaction_type,
    e.id AS transaction_id,
    e.given_name AS employee_first_name,
    e.family_name AS employee_last_name,
    NULL AS client_name,
    -e.salary AS amount
FROM
    employees e

UNION

SELECT
    'Income' AS transaction_type,
    e.id AS transaction_id,
    e.given_name AS employee_first_name,
    e.family_name AS employee_last_name,
    c.client_name,
    w.total_sales AS amount
FROM
    employees e
LEFT JOIN
    works_with w ON e.id = w.employee_id
LEFT JOIN
    clients c ON w.client_id = c.id
WHERE
    w.total_sales > 0;

