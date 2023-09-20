CREATE DATABASE IF NOT EXISTS shop;

CREATE USER IF NOT EXISTS shop_user@localhost
    IDENTIFIED BY 'Password1';

GRANT ALL ON shop.* TO shop_user@localhost;
GRANT USAGE ON *.* TO shop_user@localhost;



USE shop;

DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS products;

CREATE TABLE IF NOT EXISTS categories
(
    id          BIGINT UNSIGNED AUTO_INCREMENT,
    name        VARCHAR(32)  NOT NULL,
    description VARCHAR(255) NULL,

    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS products
(
    id          BIGINT UNSIGNED AUTO_INCREMENT,
    name        VARCHAR(64)  NOT NULL,
    description VARCHAR(255) NULL,
    category_id BIGINT UNSIGNED, # FK

    PRIMARY KEY (id)
);
