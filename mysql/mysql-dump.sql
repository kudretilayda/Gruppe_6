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

<<<<<<< HEAD
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
=======
DROP TABLE IF EXISTS `binary_constraint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `binary_constraint` (
  `id` int NOT NULL AUTO_INCREMENT,
  `reference_object1_id` int NOT NULL,
  `reference_object2_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reference_object1_id` (`reference_object1_id`),
  KEY `reference_object2_id` (`reference_object2_id`),
  CONSTRAINT `binary_constraint_ibfk_1` FOREIGN KEY (`id`) REFERENCES `constraint_rule` (`id`) ON DELETE CASCADE,
  CONSTRAINT `binary_constraint_ibfk_2` FOREIGN KEY (`reference_object1_id`) REFERENCES `clothing_type` (`id`),
  CONSTRAINT `binary_constraint_ibfk_3` FOREIGN KEY (`reference_object2_id`) REFERENCES `clothing_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
>>>>>>> cb40ce594841218d73ecccfcb843f3b4c9718885

-- Outfit
DROP TABLE IF EXISTS outfit;
CREATE TABLE outfit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    outfit_name VARCHAR(255) NOT NULL,
    style_id INT NOT NULL,
    FOREIGN KEY (style_id) REFERENCES style(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

<<<<<<< HEAD
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

=======
LOCK TABLES `binary_constraint` WRITE;
/*!40000 ALTER TABLE `binary_constraint` DISABLE KEYS */;
INSERT INTO `binary_constraint` VALUES (1,1,2);
/*!40000 ALTER TABLE `binary_constraint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clothing_item`
--

DROP TABLE IF EXISTS `clothing_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clothing_item` (
  `id` int NOT NULL AUTO_INCREMENT,
  `wardrobe_id` int NOT NULL,
  `clothing_type_id` int NOT NULL,
  `clothing_item_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wardrobe_id` (`wardrobe_id`),
  KEY `clothing_type_id` (`clothing_type_id`),
  CONSTRAINT `clothing_item_ibfk_1` FOREIGN KEY (`wardrobe_id`) REFERENCES `wardrobe` (`id`) ON DELETE CASCADE,
  CONSTRAINT `clothing_item_ibfk_2` FOREIGN KEY (`clothing_type_id`) REFERENCES `clothing_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
>>>>>>> cb40ce594841218d73ecccfcb843f3b4c9718885


<<<<<<< HEAD
-- Testdaten für die Person-Tabelle
INSERT INTO person (google_id, lastname, firstname, nickname, email)
VALUES 
('google123', 'Müller', 'Hans', 'hansm', 'hans.mueller@example.com'),
('google456', 'Schmidt', 'Anna', 'annas', 'anna.schmidt@example.com');
=======
LOCK TABLES `clothing_item` WRITE;
/*!40000 ALTER TABLE `clothing_item` DISABLE KEYS */;
INSERT INTO `clothing_item` VALUES (1,1,1,'Gelbe Jacke'),(2,1,2,'Beige Chino'),(3,2,3,'Rotes T-Shirt'),(4,2,4,'Weiße Sportschuhe');
/*!40000 ALTER TABLE `clothing_item` ENABLE KEYS */;
UNLOCK TABLES;
>>>>>>> cb40ce594841218d73ecccfcb843f3b4c9718885

-- Testdaten für die Kleiderschrank-Tabelle
INSERT INTO wardrobe (wardrobe_owner)
VALUES 
(1), -- Kleiderschrank von Hans
(2); -- Kleiderschrank von Anna

<<<<<<< HEAD
-- Testdaten für die Kleidungstyp-Tabelle
INSERT INTO clothing_type (type_name, type_usage)
VALUES 
('Jacke', 'Winterjacke'),
('Hose', 'Chino'),
('T-Shirt', 'Sommerbekleidung'),
('Schuhe', 'Sportschuhe');
=======
DROP TABLE IF EXISTS `clothing_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clothing_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type_name` varchar(255) NOT NULL,
  `type_usage` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
>>>>>>> cb40ce594841218d73ecccfcb843f3b4c9718885

-- Testdaten für die Kleidungsstück-Tabelle
INSERT INTO clothing_item (wardrobe_id, clothing_type_id, clothing_item_name)
VALUES 
(1, 1, 'Gelbe Jacke'), -- Gelbe Jacke im Kleiderschrank von Hans
(1, 2, 'Beige Chino'), -- Beige Chino im Kleiderschrank von Hans
(2, 3, 'Rotes T-Shirt'), -- Rotes T-Shirt im Kleiderschrank von Anna
(2, 4, 'Weiße Sportschuhe'); -- Weiße Sportschuhe im Kleiderschrank von Anna

<<<<<<< HEAD
-- Testdaten für die Style-Tabelle
INSERT INTO style (style_features, style_constraints)
VALUES 
('Sommerbekleidung', 'Nur Sommersachen kombinieren'),
('Business Casual', 'Keine gelbe Jacke mit Chino-Hose');
=======
LOCK TABLES `clothing_type` WRITE;
/*!40000 ALTER TABLE `clothing_type` DISABLE KEYS */;
INSERT INTO `clothing_type` VALUES (1,'Jacke','Winterjacke'),(2,'Hose','Chino'),(3,'T-Shirt','Sommerbekleidung'),(4,'Schuhe','Sportschuhe');
/*!40000 ALTER TABLE `clothing_type` ENABLE KEYS */;
UNLOCK TABLES;
>>>>>>> cb40ce594841218d73ecccfcb843f3b4c9718885

-- Testdaten für die Outfit-Tabelle
INSERT INTO outfit (outfit_name, style_id)
VALUES 
('Sommerliches Outfit', 1),
('Business Outfit', 2);

<<<<<<< HEAD
-- Testdaten für die Outfit-Kleidungsstück-Verbindungstabelle
INSERT INTO outfit_items (outfit_id, clothing_item_id)
VALUES 
(1, 3), -- Sommerliches Outfit enthält Rotes T-Shirt
(1, 4), -- Sommerliches Outfit enthält Weiße Sportschuhe
(2, 1), -- Business Outfit enthält Gelbe Jacke
(2, 2); -- Business Outfit enthält Beige Chino
=======
DROP TABLE IF EXISTS `constraint_rule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `constraint_rule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `style_id` int NOT NULL,
  `constraint_type` enum('binary','unary','implikation','mutex','kardinalitaet') NOT NULL,
  `attribute` varchar(255) DEFAULT NULL,
  `constrain` varchar(255) DEFAULT NULL,
  `val` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `style_id` (`style_id`),
  CONSTRAINT `constraint_rule_ibfk_1` FOREIGN KEY (`style_id`) REFERENCES `style` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
>>>>>>> cb40ce594841218d73ecccfcb843f3b4c9718885

-- Testdaten für die Constraint-Regeln
INSERT INTO constraint_rule (style_id, constraint_type, attribute, constrain, val)
VALUES 
(1, 'unary', 'season', 'EQUAL', 'Sommer'), -- Sommersachen kombinieren
(2, 'binary', 'color', 'NOT EQUAL', 'Gelb'); -- Keine gelbe Jacke mit Chino-Hose

<<<<<<< HEAD
-- Testdaten für Unary Constraints
INSERT INTO unary_constraint (reference_object_id, attribute, constrain, val)
VALUES 
(3, 'season', 'EQUAL', 'Sommer'); -- Rotes T-Shirt nur für Sommerbekleidung

-- Testdaten für Binary Constraints
INSERT INTO binary_constraint (reference_object1_id, reference_object2_id)
VALUES 
(1, 2); -- Gelbe Jacke (ID 1) darf nicht mit Chino (ID 2) kombiniert werden


SET FOREIGN_KEY_CHECKS=1;
=======
LOCK TABLES `constraint_rule` WRITE;
/*!40000 ALTER TABLE `constraint_rule` DISABLE KEYS */;
INSERT INTO `constraint_rule` VALUES (1,1,'unary','season','EQUAL','Sommer'),(2,2,'binary','color','NOT EQUAL','Gelb');
/*!40000 ALTER TABLE `constraint_rule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outfit`
--

DROP TABLE IF EXISTS `outfit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `outfit` (
  `id` int NOT NULL AUTO_INCREMENT,
  `outfit_name` varchar(255) NOT NULL,
  `style_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `style_id` (`style_id`),
  CONSTRAINT `outfit_ibfk_1` FOREIGN KEY (`style_id`) REFERENCES `style` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outfit`
--

LOCK TABLES `outfit` WRITE;
/*!40000 ALTER TABLE `outfit` DISABLE KEYS */;
INSERT INTO `outfit` VALUES (1,'Sommerliches Outfit',1),(2,'Business Outfit',2);
/*!40000 ALTER TABLE `outfit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outfit_items`
--

DROP TABLE IF EXISTS `outfit_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `outfit_items` (
  `outfit_id` int NOT NULL,
  `clothing_item_id` int NOT NULL,
  PRIMARY KEY (`outfit_id`,`clothing_item_id`),
  KEY `clothing_item_id` (`clothing_item_id`),
  CONSTRAINT `outfit_items_ibfk_1` FOREIGN KEY (`outfit_id`) REFERENCES `outfit` (`id`) ON DELETE CASCADE,
  CONSTRAINT `outfit_items_ibfk_2` FOREIGN KEY (`clothing_item_id`) REFERENCES `clothing_item` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outfit_items`
--

LOCK TABLES `outfit_items` WRITE;
/*!40000 ALTER TABLE `outfit_items` DISABLE KEYS */;
INSERT INTO `outfit_items` VALUES (2,1),(2,2),(1,3),(1,4);
/*!40000 ALTER TABLE `outfit_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `id` int NOT NULL AUTO_INCREMENT,
  `google_id` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `nickname` varchar(255) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `google_id` (`google_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES (1,'google123','Müller','Hans','hansm','hans.mueller@example.com'),(2,'google456','Schmidt','Anna','annas','anna.schmidt@example.com');
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `style`
--

DROP TABLE IF EXISTS `style`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `style` (
  `id` int NOT NULL AUTO_INCREMENT,
  `style_features` text,
  `style_constraints` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `style`
--

LOCK TABLES `style` WRITE;
/*!40000 ALTER TABLE `style` DISABLE KEYS */;
INSERT INTO `style` VALUES (1,'Sommerbekleidung','Nur Sommersachen kombinieren'),(2,'Business Casual','Keine gelbe Jacke mit Chino-Hose');
/*!40000 ALTER TABLE `style` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unary_constraint`
--

DROP TABLE IF EXISTS `unary_constraint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unary_constraint` (
  `id` int NOT NULL AUTO_INCREMENT,
  `reference_object_id` int NOT NULL,
  `attribute` varchar(255) DEFAULT NULL,
  `constrain` varchar(255) DEFAULT NULL,
  `val` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `reference_object_id` (`reference_object_id`),
  CONSTRAINT `unary_constraint_ibfk_1` FOREIGN KEY (`id`) REFERENCES `constraint_rule` (`id`) ON DELETE CASCADE,
  CONSTRAINT `unary_constraint_ibfk_2` FOREIGN KEY (`reference_object_id`) REFERENCES `clothing_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unary_constraint`
--

LOCK TABLES `unary_constraint` WRITE;
/*!40000 ALTER TABLE `unary_constraint` DISABLE KEYS */;
INSERT INTO `unary_constraint` VALUES (1,3,'season','EQUAL','Sommer');
/*!40000 ALTER TABLE `unary_constraint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wardrobe`
--

DROP TABLE IF EXISTS `wardrobe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wardrobe` (
  `id` int NOT NULL AUTO_INCREMENT,
  `wardrobe_owner` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wardrobe_owner` (`wardrobe_owner`),
  CONSTRAINT `wardrobe_ibfk_1` FOREIGN KEY (`wardrobe_owner`) REFERENCES `person` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wardrobe`
--

LOCK TABLES `wardrobe` WRITE;
/*!40000 ALTER TABLE `wardrobe` DISABLE KEYS */;
INSERT INTO `wardrobe` VALUES (1,1),(2,2);
/*!40000 ALTER TABLE `wardrobe` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-08 23:37:07
>>>>>>> cb40ce594841218d73ecccfcb843f3b4c9718885
