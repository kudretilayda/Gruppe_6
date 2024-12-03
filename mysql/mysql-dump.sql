CREATE DATABASE IF NOT EXISTS digital_wardrobe;
USE digital_wardrobe;

SET FOREIGN_KEY_CHECKS=0;

-- Nutzertabelle
DROP TABLE IF EXISTS person;
CREATE TABLE person (
    id VARCHAR(36) NOT NULL,  -- Korrekt als 'id' definiert
    google_id VARCHAR(255) NOT NULL UNIQUE,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    nick_name VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id) -- Primärschlüssel auf 'id'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Kleiderschranktabelle
DROP TABLE IF EXISTS wardrobe;
CREATE TABLE wardrobe (
    id VARCHAR(36) NOT NULL,  -- Korrekt als 'id' definiert
    person_id VARCHAR(36) NOT NULL,
    owner_name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (person_id) REFERENCES person(id) ON DELETE CASCADE -- Verweis auf 'id' in person
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Kleidungstyp-Tabelle
DROP TABLE IF EXISTS clothing_type;
CREATE TABLE clothing_type (
    id VARCHAR(36) NOT NULL,  -- Korrekt als 'id' definiert
    type_name VARCHAR(255) NOT NULL,
    type_description TEXT,
    category ENUM('oberteile', 'unterteile', 'schuhe') NOT NULL,
    PRIMARY KEY (id) -- Primärschlüssel auf 'id'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Kleidungsstücke-Tabelle
DROP TABLE IF EXISTS clothing_item;
CREATE TABLE clothing_item (
    id VARCHAR(36) NOT NULL,  -- Korrekt als 'id' definiert
    wardrobe_id VARCHAR(36) NOT NULL,
    clothing_type_id VARCHAR(36) NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    color VARCHAR(50),
    brand VARCHAR(100),
    season ENUM('Winter', 'Sommer', 'Frühling', 'Herbst'),
    PRIMARY KEY (id),
    FOREIGN KEY (wardrobe_id) REFERENCES wardrobe(id) ON DELETE CASCADE, -- Verweis auf 'id' in wardrobe
    FOREIGN KEY (clothing_type_id) REFERENCES clothing_type(id) -- Verweis auf 'id' in clothing_type
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Style-Tabelle
DROP TABLE IF EXISTS style;
CREATE TABLE style (
    id VARCHAR(36) NOT NULL,  -- Korrekt als 'id' definiert
    style_name VARCHAR(255) NOT NULL,
    style_description TEXT,
    created_by VARCHAR(36) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (created_by) REFERENCES person(id) -- Verweis auf 'id' in person
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Outfit-Tabelle
DROP TABLE IF EXISTS outfit;
CREATE TABLE outfit (
    id VARCHAR(36) NOT NULL,  -- Korrekt als 'id' definiert
    outfit_name VARCHAR(255) NOT NULL,
    style_id VARCHAR(36),
    created_by VARCHAR(36) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (style_id) REFERENCES style(id), -- Verweis auf 'id' in style
    FOREIGN KEY (created_by) REFERENCES person(id) -- Verweis auf 'id' in person
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Outfit-Kleidungsstücke-Verbindungstabelle
DROP TABLE IF EXISTS outfit_items;
CREATE TABLE outfit_items (
    outfit_id VARCHAR(36) NOT NULL, -- Verweis auf outfit.id
    clothing_item_id VARCHAR(36) NOT NULL, -- Verweis auf clothing_item.id
    PRIMARY KEY (outfit_id, clothing_item_id),
    FOREIGN KEY (outfit_id) REFERENCES outfit(id) ON DELETE CASCADE,
    FOREIGN KEY (clothing_item_id) REFERENCES clothing_item(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Constraint-Tabelle
DROP TABLE IF EXISTS constraint_rule;
CREATE TABLE constraint_rule (
    id VARCHAR(36) NOT NULL,  -- Korrekt als 'id' definiert
    style_id VARCHAR(36) NOT NULL,
    constraint_type ENUM('binary', 'unary', 'implikation', 'mutex', 'kardinalitaet') NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (style_id) REFERENCES style(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Binary Constraint-Tabelle
DROP TABLE IF EXISTS binary_constraint;
CREATE TABLE binary_constraint (
    id VARCHAR(36) NOT NULL,  -- Korrekt als 'id' definiert
    reference_object1_id VARCHAR(36) NOT NULL,
    reference_object2_id VARCHAR(36) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES constraint_rule(id) ON DELETE CASCADE,
    FOREIGN KEY (reference_object1_id) REFERENCES clothing_type(id),
    FOREIGN KEY (reference_object2_id) REFERENCES clothing_type(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Unary Constraint-Tabelle
DROP TABLE IF EXISTS unary_constraint;
CREATE TABLE unary_constraint (
    id VARCHAR(36) NOT NULL,  -- Korrekt als 'id' definiert
    reference_object_id VARCHAR(36) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES constraint_rule(id) ON DELETE CASCADE,
    FOREIGN KEY (reference_object_id) REFERENCES clothing_type(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

SET FOREIGN_KEY_CHECKS=1;