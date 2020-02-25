
CREATE TABLE category (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(150) NOT NULL,
                PRIMARY KEY (id)
);
CREATE TABLE product (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(150) NOT NULL,
                nutrition_grades VARCHAR(1) NOT NULL,
                energy_100 DECIMAL(6,2) NOT NULL,
                category_id INT NOT NULL,
                PRIMARY KEY (id)
);


ALTER TABLE product ADD CONSTRAINT category_product_fk
FOREIGN KEY (category_id)
REFERENCES category (id)
ON DELETE CASCADE
ON UPDATE CASCADE;
