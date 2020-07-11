
CREATE TABLE category (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(150) NOT NULL,
                PRIMARY KEY (id)
)ENGINE=InnoDB;
CREATE TABLE product (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(150) NOT NULL,
                nutrition_grades VARCHAR(1) NOT NULL,
                energy_100 SMALLINT NOT NULL,
                stores VARCHAR(200) NOT NULL,
                url VARCHAR(300) NOT NULL,
                category_id INT NOT NULL,
                substitute_id INT,
                PRIMARY KEY (id)
)ENGINE=InnoDB;


ALTER TABLE product ADD CONSTRAINT category_product_fk
FOREIGN KEY (category_id)
REFERENCES category (id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE product ADD CONSTRAINT product_product_fk
FOREIGN KEY (substitute_id)
REFERENCES product (id)
ON DELETE CASCADE
ON UPDATE CASCADE;
