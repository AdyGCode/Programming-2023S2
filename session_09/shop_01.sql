
USE `shop`;

INSERT INTO categories(id, name, description)
    VALUE (1, 'unknown', null);

INSERT INTO categories(name, description)
VALUES ('toys', null),
       ('games', null),
       ('electronics', null);


SELECT *
FROM categories;


INSERT INTO products(id, name, description, category_id)
    VALUE (1, 'unknown', null, 1);

INSERT INTO products(name, description, category_id)
VALUES ('A-Wing vs TIE Silencer 75196', 'Lego Microfighters', 2),
       ('Ski Speeder v First Order Walker 75195', 'Lego Microfighters', 2),
       ('Argon One M.2', 'Raspberry Pi 4 case with M.2 SATA', 4);

INSERT INTO products(name, description, category_id)
VALUES ('Banana', null, 7),
       ('SenseCap K1101', 'IoT Course for Beginners', 4),
       ('T-16 Skyhopper vs Bantha 75265', 'Lego Microfighters', 2),
       ('SenseCap K110', 'Sensor prototype kit with LoRa® and AI', 4)
;

SELECT *
FROM products;


SELECT DISTINCT products.name, categories.name
FROM categories,
     products;

SELECT products.name, categories.name
FROM categories,
     products
WHERE products.category_id = categories.id;

SELECT products.name, categories.name
FROM categories
         LEFT JOIN products
                   ON categories.id = products.category_id;

SELECT products.name, categories.name
FROM products
         RIGHT JOIN categories
                    ON categories.id = products.category_id;

SELECT products.name, categories.name
FROM products
         LEFT JOIN categories
                   ON categories.id = products.category_id;

SELECT products.name, categories.name
FROM products
         INNER JOIN categories
                    ON categories.id = products.category_id;

SELECT products.name, categories.name
FROM products
         CROSS JOIN categories
                    ON categories.id = products.category_id;

SELECT products.name AS product_name
FROM products
UNION
SELECT categories.name AS category_name
FROM categories;

SELECT DISTINCT products.name
FROM products
WHERE products.category_id IN (SELECT categories.id
                               FROM categories
                               WHERE categories.name LIKE 'to%');

/* Show the categories with more than X products in them */
SELECT name AS category_name
FROM categories
WHERE id IN (SELECT category_id
             FROM products
             GROUP BY category_id
             HAVING COUNT(id) >= 4)
ORDER BY category_name;

# Using JOIN and HAVING

SELECT c.name AS category_name, COUNT(p.id) as Number
FROM categories c
         JOIN products p ON c.id = p.category_id
GROUP BY c.name
HAVING COUNT(p.id) >= 2;

SELECT c.name, item_count
FROM (SELECT count(1)    AS item_count,
             category_id AS id
      FROM products
      GROUP BY category_id
      HAVING item_count >= 3) AS t
         JOIN categories c ON (c.id = t.id);
