CREATE DATABASE IF NOT EXISTS digital_wardrobe;
USE digital_wardrobe;
SET FOREIGN_KEY_CHECKS=0;
-- SET FOREIGN_KEY_CHECKS=0 deaktiviert vorübergehend referenzielle Einschränkungen zwischen Tabellen.
-- Das erleichtert das Erstellen von neuen Tabellen und das Laden von Daten.

-- User Table
-- User muss in SQL als 'person' gespeichert werden, weil user schon ein built-in ist
DROP TABLE IF EXISTS person;
CREATE TABLE person (
    id INT AUTO_INCREMENT PRIMARY KEY,
    google_id VARCHAR(255) NOT NULL UNIQUE,
    lastname VARCHAR(255) NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    nickname VARCHAR(255),
    email VARCHAR(255) NOT NULL
);

-- Wardrobe
DROP TABLE IF EXISTS wardrobe;
CREATE TABLE wardrobe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    wardrobe_owner INT NOT NULL,
    FOREIGN KEY (wardrobe_owner) REFERENCES person(id) ON DELETE CASCADE
);

-- Clothing Item
DROP TABLE IF EXISTS clothing_item;
CREATE TABLE clothing_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    wardrobe_id INT NOT NULL,
    clothing_type_id INT NOT NULL,
    clothing_item_name VARCHAR(255) NOT NULL,
    FOREIGN KEY (wardrobe_id) REFERENCES wardrobe(id) ON DELETE CASCADE,
    FOREIGN KEY (clothing_type_id) REFERENCES clothing_type(id)
) ;

-- Outfit
DROP TABLE IF EXISTS outfit;
CREATE TABLE outfit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    outfit_name VARCHAR(255) NOT NULL,
    style_id INT NOT NULL,
    FOREIGN KEY (style_id) REFERENCES style(id)
);

-- Outfit Clothing Item Normalisierung
DROP TABLE IF EXISTS outfit_items;
CREATE TABLE outfit_items (
    outfit_id INT NOT NULL,
    clothing_item_id INT NOT NULL,
    PRIMARY KEY (outfit_id, clothing_item_id),
    FOREIGN KEY (outfit_id) REFERENCES outfit(id) ON DELETE CASCADE,
    FOREIGN KEY (clothing_item_id) REFERENCES clothing_item(id)
);

-- Clothing Type
DROP TABLE IF EXISTS clothing_type;
CREATE TABLE clothing_type (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(255) NOT NULL,
    type_usage VARCHAR(255)
);

-- Style
DROP TABLE IF EXISTS style;
CREATE TABLE style (
    id INT AUTO_INCREMENT PRIMARY KEY,
    style_features TEXT,
    style_constraints TEXT -- JSON oder serialisierte Constraints
);

-- Constraint
DROP TABLE IF EXISTS constraints;
CREATE TABLE constraints (
    id INT AUTO_INCREMENT PRIMARY KEY,
    constraint_type ENUM('Unary', 'Binary', 'Implication', 'Cardinality', 'Mutex') NOT NULL,
    description TEXT NOT NULL
);

-- Unary
DROP TABLE IF EXISTS unary_constraint;
CREATE TABLE unary_constraint (
    id INT AUTO_INCREMENT PRIMARY KEY,
    constraint_id INT NOT NULL,
    style_id INT NOT NULL,
    FOREIGN KEY (constraint_id) REFERENCES constraints(id) ON DELETE CASCADE,
    FOREIGN KEY (style_id) REFERENCES style(id) ON DELETE CASCADE
);

-- Binary
DROP TABLE IF EXISTS binary_constraint;
CREATE TABLE binary_constraint (
    id INT AUTO_INCREMENT PRIMARY KEY,
    constraint_id INT NOT NULL,
    item_1_id INT NOT NULL,
    item_2_id INT NOT NULL,
    FOREIGN KEY (constraint_id) REFERENCES constraints(id) ON DELETE CASCADE,
    FOREIGN KEY (item_1_id) REFERENCES clothing_item(id) ON DELETE CASCADE,
    FOREIGN KEY (item_2_id) REFERENCES clothing_item(id) ON DELETE CASCADE
);

-- Implication
DROP TABLE IF EXISTS implication_constraint;
CREATE TABLE implication_constraint (
    id INT AUTO_INCREMENT PRIMARY KEY,
    constraint_id INT NOT NULL,
    if_type_id INT NOT NULL,
    then_type_id INT NOT NULL,
    FOREIGN KEY (constraint_id) REFERENCES constraints(id) ON DELETE CASCADE,
    FOREIGN KEY (if_type_id) REFERENCES clothing_type(id),
    FOREIGN KEY (then_type_id) REFERENCES clothing_type(id)
);

-- Cardinality
DROP TABLE IF EXISTS cardinality_constraint;
CREATE TABLE cardinality_constraint (
    id INT AUTO_INCREMENT PRIMARY KEY,
    constraint_id INT NOT NULL,
    min_count INT NOT NULL,
    max_count INT NOT NULL,
    FOREIGN KEY (constraint_id) REFERENCES constraints(id) ON DELETE CASCADE
);

-- Mutex
DROP TABLE IF EXISTS mutex_constraint;
CREATE TABLE mutex_constraint (
    id INT AUTO_INCREMENT PRIMARY KEY,
    constraint_id INT NOT NULL,
    item_1_id INT NOT NULL,
    item_2_id INT NOT NULL,
    FOREIGN KEY (constraint_id) REFERENCES constraints(id) ON DELETE CASCADE,
    FOREIGN KEY (item_1_id) REFERENCES clothing_item(id) ON DELETE CASCADE,
    FOREIGN KEY (item_2_id) REFERENCES clothing_item(id) ON DELETE CASCADE
);

SET FOREIGN_KEY_CHECKS=1;