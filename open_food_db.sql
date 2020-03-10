
CREATE TABLE category (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(150) NOT NULL,
                PRIMARY KEY (id)
);
CREATE TABLE product (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(150) NOT NULL,
                nutrition_grades VARCHAR(1) NOT NULL,
                energy_100 SMALLINT NOT NULL,
                category_id INT NOT NULL,
                subtitute_id INT,
                PRIMARY KEY (id)
);


ALTER TABLE product ADD CONSTRAINT category_product_fk
FOREIGN KEY (category_id)
REFERENCES category (id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE product ADD CONSTRAINT product_product_fk
FOREIGN KEY (subtitute_id)
REFERENCES product (id)
ON DELETE CASCADE
ON UPDATE CASCADE;
