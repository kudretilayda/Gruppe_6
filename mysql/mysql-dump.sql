CREATE DATABASE IF NOT EXISTS digital_wardrobe;
USE digital_wardrobe;
SET FOREIGN_KEY_CHECKS=0;

-- User
DROP TABLE IF EXISTS person;
CREATE TABLE person (
    id INT AUTO_INCREMENT PRIMARY KEY,
    google_id VARCHAR(255) NOT NULL UNIQUE,
    lastname VARCHAR(255) NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    nickname VARCHAR(255),
    email VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Wardrobe
DROP TABLE IF EXISTS wardrobe;
CREATE TABLE wardrobe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    wardrobe_owner INT NOT NULL, -- 'Eigentuemer' verweist auf 'User'
    FOREIGN KEY (wardrobe_owner) REFERENCES person(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Clothing Item
DROP TABLE IF EXISTS clothing_item;
CREATE TABLE clothing_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    wardrobe_id INT NOT NULL, -- Verbindung zu Kleiderschrank
    clothing_type_id INT NOT NULL, -- Verbindung zu Kleidungstyp
    clothing_item_name VARCHAR(255) NOT NULL,
    FOREIGN KEY (wardrobe_id) REFERENCES wardrobe(id) ON DELETE CASCADE,
    FOREIGN KEY (clothing_type_id) REFERENCES clothing_type(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Outfit
DROP TABLE IF EXISTS outfit;
CREATE TABLE outfit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    outfit_name VARCHAR(255) NOT NULL,
    style_id INT NOT NULL,
    FOREIGN KEY (style_id) REFERENCES style(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Outfit Clothing Item Connection (vllt nicht nötig)
DROP TABLE IF EXISTS outfit_items;
CREATE TABLE outfit_items (
	outfit_id INT NOT NULL,
    clothing_item_id INT NOT NULL,
    PRIMARY KEY (outfit_id, clothing_item_id),
    FOREIGN KEY (outfit_id) REFERENCES outfit(id) ON DELETE CASCADE,
	FOREIGN KEY (clothing_item_id) REFERENCES clothing_item(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Clothing Type
DROP TABLE IF EXISTS clothing_type;
CREATE TABLE clothing_type (
	id INT AUTO_INCREMENT PRIMARY KEY,
	type_name VARCHAR(255) NOT NULL,
	type_usage VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Style
DROP TABLE IF EXISTS style;
CREATE TABLE style (
	id INT AUTO_INCREMENT PRIMARY KEY,
	style_features TEXT,
	style_constraints TEXT -- Constraint-Daten vorhalten
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Constraint
DROP TABLE IF EXISTS constraint_rule;
CREATE TABLE constraint_rule (
    id INT AUTO_INCREMENT PRIMARY KEY,
    style_id INT NOT NULL, -- Bezug zu Style
    constraint_type ENUM('binary', 'unary', 'implikation', 'mutex', 'kardinalitaet') NOT NULL,
    attribute VARCHAR(255), -- z. B. color oder size
    constrain VARCHAR(255), -- z. B. "NOT EQUAL", "EQUAL", "IN"
    val VARCHAR(255), -- Wert wie "Gelb", "Sommer", "42"
    FOREIGN KEY (style_id) REFERENCES style(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Unary Constraint
DROP TABLE IF EXISTS unary_constraint;
CREATE TABLE unary_constraint (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reference_object_id INT NOT NULL, -- Bezug zu einem clothing_type
    attribute VARCHAR(255), -- Attribut, das eingeschränkt wird (z. B. "season")
    constrain VARCHAR(255), -- Bedingung (z. B. "EQUAL", "NOT EQUAL")
    val VARCHAR(255), -- Wert (z. B. "Sommer", "Winter")
    FOREIGN KEY (id) REFERENCES constraint_rule(id) ON DELETE CASCADE,
    FOREIGN KEY (reference_object_id) REFERENCES clothing_type(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Binary Constraint
DROP TABLE IF EXISTS binary_constraint;
CREATE TABLE binary_constraint (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reference_object1_id INT NOT NULL, -- Verbindung zu clothing_type (z. B. Jacke)
    reference_object2_id INT NOT NULL, -- Verbindung zu clothing_type (z. B. Chino)
    FOREIGN KEY (id) REFERENCES constraint_rule(id) ON DELETE CASCADE,
    FOREIGN KEY (reference_object1_id) REFERENCES clothing_type(id),
    FOREIGN KEY (reference_object2_id) REFERENCES clothing_type(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



-- Testdaten für die Person-Tabelle
INSERT INTO person (google_id, lastname, firstname, nickname, email)
VALUES 
('google123', 'Müller', 'Hans', 'hansm', 'hans.mueller@example.com'),
('google456', 'Schmidt', 'Anna', 'annas', 'anna.schmidt@example.com');

-- Testdaten für die Kleiderschrank-Tabelle
INSERT INTO wardrobe (wardrobe_owner)
VALUES 
(1), -- Kleiderschrank von Hans
(2); -- Kleiderschrank von Anna

-- Testdaten für die Kleidungstyp-Tabelle
INSERT INTO clothing_type (type_name, type_usage)
VALUES 
('Jacke', 'Winterjacke'),
('Hose', 'Chino'),
('T-Shirt', 'Sommerbekleidung'),
('Schuhe', 'Sportschuhe');

-- Testdaten für die Kleidungsstück-Tabelle
INSERT INTO clothing_item (wardrobe_id, clothing_type_id, clothing_item_name)
VALUES 
(1, 1, 'Gelbe Jacke'), -- Gelbe Jacke im Kleiderschrank von Hans
(1, 2, 'Beige Chino'), -- Beige Chino im Kleiderschrank von Hans
(2, 3, 'Rotes T-Shirt'), -- Rotes T-Shirt im Kleiderschrank von Anna
(2, 4, 'Weiße Sportschuhe'); -- Weiße Sportschuhe im Kleiderschrank von Anna

-- Testdaten für die Style-Tabelle
INSERT INTO style (style_features, style_constraints)
VALUES 
('Sommerbekleidung', 'Nur Sommersachen kombinieren'),
('Business Casual', 'Keine gelbe Jacke mit Chino-Hose');

-- Testdaten für die Outfit-Tabelle
INSERT INTO outfit (outfit_name, style_id)
VALUES 
('Sommerliches Outfit', 1),
('Business Outfit', 2);

-- Testdaten für die Outfit-Kleidungsstück-Verbindungstabelle
INSERT INTO outfit_items (outfit_id, clothing_item_id)
VALUES 
(1, 3), -- Sommerliches Outfit enthält Rotes T-Shirt
(1, 4), -- Sommerliches Outfit enthält Weiße Sportschuhe
(2, 1), -- Business Outfit enthält Gelbe Jacke
(2, 2); -- Business Outfit enthält Beige Chino

-- Testdaten für die Constraint-Regeln
INSERT INTO constraint_rule (style_id, constraint_type, attribute, constrain, val)
VALUES 
(1, 'unary', 'season', 'EQUAL', 'Sommer'), -- Sommersachen kombinieren
(2, 'binary', 'color', 'NOT EQUAL', 'Gelb'); -- Keine gelbe Jacke mit Chino-Hose

-- Testdaten für Unary Constraints
INSERT INTO unary_constraint (reference_object_id, attribute, constrain, val)
VALUES 
(3, 'season', 'EQUAL', 'Sommer'); -- Rotes T-Shirt nur für Sommerbekleidung

-- Testdaten für Binary Constraints
INSERT INTO binary_constraint (reference_object1_id, reference_object2_id)
VALUES 
(1, 2); -- Gelbe Jacke (ID 1) darf nicht mit Chino (ID 2) kombiniert werden


SET FOREIGN_KEY_CHECKS=1;