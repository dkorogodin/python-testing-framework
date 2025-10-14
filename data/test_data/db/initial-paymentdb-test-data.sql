-- Drop tables if exist
DROP TABLE IF EXISTS Payment;
DROP TABLE IF EXISTS CreditCard;
DROP TABLE IF EXISTS ShippingInfo;

-- Create tables
CREATE TABLE ShippingInfo(
	id int NOT NULL,
	email varchar(50),
	country varchar(50),
	PRIMARY KEY (id)
);
create table CreditCard(
	id int NOT NULL,
	number varchar(50),
	expiry_date date,
	cvv varchar(3),
	name_on_card varchar(50),
	PRIMARY KEY (id)
);
create table Payment(
	id int NOT NULL,
	credit_card_id int,
	coupon varchar(50),
	shipping_info_id int,
	PRIMARY KEY (id),
	FOREIGN KEY (credit_card_id) REFERENCES CreditCard(id),
	FOREIGN KEY (shipping_info_id) REFERENCES ShippingInfo(id)
);

-- Insert data into tables
LOCK TABLES ShippingInfo WRITE;

LOCK TABLES ShippingInfo WRITE;
INSERT INTO ShippingInfo VALUES
    (1, 'tester_aqa_946@mail.com', 'United Kingdom'),
    (2, 'tester_aqa_888@mail.com', 'United Kingdom');

LOCK TABLES CreditCard WRITE;
INSERT INTO CreditCard VALUES
    (1, '5203013923806946', '2028-11-12', '946', 'Tester_946'),
    (2, '5203013923806888', '2028-12-01', '888', 'Tester_888');

LOCK TABLES Payment WRITE;
INSERT INTO Payment VALUES
    (1, 1, null, 1),
    (2, 2, null, 2);

UNLOCK TABLES;
