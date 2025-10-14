-- Drop tables if exist
DROP TABLE IF EXISTS Product;

-- Create tables
CREATE TABLE Product(
	id int NOT NULL,
	name varchar(50),
	price int,
	details varchar(500),
	currency varchar(5),
	PRIMARY KEY (id)
);

-- Insert data into tables
LOCK TABLES Product WRITE;

INSERT INTO Product VALUES
    (1, 'ADIDAS ORIGINAL', 11500, 'Adidas shoes for Men', '$'),
    (2, 'ZARA COAT 3', 11500, 'Zara coat for Women and girls', '$'),
    (3, 'IPHONE 13 PRO', 55000, 'Latest Apple Iphone13 pro with 200mp front camera', '$');

UNLOCK TABLES;
