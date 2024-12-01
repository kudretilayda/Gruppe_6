CREATE DATABASE  IF NOT EXISTS `digital_wardrobe` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `digital_wardrobe`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: digital_wardrobe
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `binary_constraint`
--

DROP TABLE IF EXISTS `binary_constraint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `binary_constraint` (
  `constraint_id` varchar(36) NOT NULL,
  `reference_object1_id` varchar(36) NOT NULL,
  `reference_object2_id` varchar(36) NOT NULL,
  PRIMARY KEY (`constraint_id`),
  KEY `reference_object1_id` (`reference_object1_id`),
  KEY `reference_object2_id` (`reference_object2_id`),
  CONSTRAINT `binary_constraint_ibfk_1` FOREIGN KEY (`constraint_id`) REFERENCES `constraint_rule` (`id`) ON DELETE CASCADE,
  CONSTRAINT `binary_constraint_ibfk_2` FOREIGN KEY (`reference_object1_id`) REFERENCES `clothing_type` (`id`),
  CONSTRAINT `binary_constraint_ibfk_3` FOREIGN KEY (`reference_object2_id`) REFERENCES `clothing_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `binary_constraint`
--

LOCK TABLES `binary_constraint` WRITE;
/*!40000 ALTER TABLE `binary_constraint` DISABLE KEYS */;
/*!40000 ALTER TABLE `binary_constraint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clothing_item`
--

DROP TABLE IF EXISTS `clothing_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clothing_item` (
  `id` varchar(36) NOT NULL,
  `wardrobe_id` varchar(36) NOT NULL,
  `type_id` varchar(36) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `color` varchar(50) DEFAULT NULL,
  `brand` varchar(100) DEFAULT NULL,
  `season` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wardrobe_id` (`wardrobe_id`),
  KEY `idx_clothing_type` (`type_id`),
  CONSTRAINT `clothing_item_ibfk_1` FOREIGN KEY (`wardrobe_id`) REFERENCES `wardrobe` (`id`) ON DELETE CASCADE,
  CONSTRAINT `clothing_item_ibfk_2` FOREIGN KEY (`type_id`) REFERENCES `clothing_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clothing_item`
--

LOCK TABLES `clothing_item` WRITE;
/*!40000 ALTER TABLE `clothing_item` DISABLE KEYS */;
INSERT INTO `clothing_item` VALUES ('1','1','1','Blue Jeans','Blau','Levi\'s','Winter'),('2','2','2','Red T-Shirt','Rot','Nike','Sommer');
/*!40000 ALTER TABLE `clothing_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clothing_type`
--

DROP TABLE IF EXISTS `clothing_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clothing_type` (
  `id` varchar(36) NOT NULL,
  `type_name` varchar(255) NOT NULL,
  `type_description` text,
  `category` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clothing_type`
--

LOCK TABLES `clothing_type` WRITE;
/*!40000 ALTER TABLE `clothing_type` DISABLE KEYS */;
INSERT INTO `clothing_type` VALUES ('1','Hose','Bequeme Jeans','unterteile'),('2','T-Shirt','Rotes Baumwoll-T-Shirt','oberteile');
/*!40000 ALTER TABLE `clothing_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `constraint_rule`
--

DROP TABLE IF EXISTS `constraint_rule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `constraint_rule` (
  `id` varchar(36) NOT NULL,
  `style_id` varchar(36) NOT NULL,
  `constraint_type` enum('binary','unary','implikation','mutex','kardinalitaet') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_constraint_style` (`style_id`),
  CONSTRAINT `constraint_rule_ibfk_1` FOREIGN KEY (`style_id`) REFERENCES `style` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `constraint_rule`
--

LOCK TABLES `constraint_rule` WRITE;
/*!40000 ALTER TABLE `constraint_rule` DISABLE KEYS */;
/*!40000 ALTER TABLE `constraint_rule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outfit`
--

DROP TABLE IF EXISTS `outfit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `outfit` (
  `id` varchar(36) NOT NULL,
  `outfit_name` varchar(255) NOT NULL,
  `style_id` varchar(36) DEFAULT NULL,
  `created_by` varchar(36) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `created_by` (`created_by`),
  KEY `idx_outfit_style` (`style_id`),
  CONSTRAINT `outfit_ibfk_1` FOREIGN KEY (`style_id`) REFERENCES `style` (`id`),
  CONSTRAINT `outfit_ibfk_2` FOREIGN KEY (`created_by`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outfit`
--

LOCK TABLES `outfit` WRITE;
/*!40000 ALTER TABLE `outfit` DISABLE KEYS */;
INSERT INTO `outfit` VALUES ('1','Casual Outfit','1','1','2024-11-30 09:49:55'),('2','Sport Outfit','2','2','2024-11-30 09:49:55');
/*!40000 ALTER TABLE `outfit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outfit_items`
--

DROP TABLE IF EXISTS `outfit_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `outfit_items` (
  `outfit_id` varchar(36) NOT NULL,
  `clothing_item_id` varchar(36) NOT NULL,
  PRIMARY KEY (`outfit_id`,`clothing_item_id`),
  KEY `clothing_item_id` (`clothing_item_id`),
  CONSTRAINT `outfit_items_ibfk_1` FOREIGN KEY (`outfit_id`) REFERENCES `outfit` (`id`) ON DELETE CASCADE,
  CONSTRAINT `outfit_items_ibfk_2` FOREIGN KEY (`clothing_item_id`) REFERENCES `clothing_item` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outfit_items`
--

LOCK TABLES `outfit_items` WRITE;
/*!40000 ALTER TABLE `outfit_items` DISABLE KEYS */;
INSERT INTO `outfit_items` VALUES ('1','1'),('2','2');
/*!40000 ALTER TABLE `outfit_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `id` varchar(36) NOT NULL,
  `google_id` varchar(255) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `nickname` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `google_id` (`google_id`),
  KEY `idx_person_google_id` (`google_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES ('1','google_12345','Max','Mustermann','Maxi','2024-11-30 09:49:54'),('2','google_67890','Erika','Musterfrau','Eri','2024-11-30 09:49:54');
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `style`
--

DROP TABLE IF EXISTS `style`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `style` (
  `id` varchar(36) NOT NULL,
  `style_name` varchar(255) NOT NULL,
  `style_description` text,
  `created_by` varchar(36) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `created_by` (`created_by`),
  CONSTRAINT `style_ibfk_1` FOREIGN KEY (`created_by`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `style`
--

LOCK TABLES `style` WRITE;
/*!40000 ALTER TABLE `style` DISABLE KEYS */;
INSERT INTO `style` VALUES ('1','Casual Style','Lässiger Look für den Alltag','1'),('2','Sportlich','Sportlicher Look für Aktivitäten','2');
/*!40000 ALTER TABLE `style` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unary_constraint`
--

DROP TABLE IF EXISTS `unary_constraint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unary_constraint` (
  `constraint_id` varchar(36) NOT NULL,
  `reference_object_id` varchar(36) NOT NULL,
  PRIMARY KEY (`constraint_id`),
  KEY `reference_object_id` (`reference_object_id`),
  CONSTRAINT `unary_constraint_ibfk_1` FOREIGN KEY (`constraint_id`) REFERENCES `constraint_rule` (`id`) ON DELETE CASCADE,
  CONSTRAINT `unary_constraint_ibfk_2` FOREIGN KEY (`reference_object_id`) REFERENCES `clothing_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unary_constraint`
--

LOCK TABLES `unary_constraint` WRITE;
/*!40000 ALTER TABLE `unary_constraint` DISABLE KEYS */;
/*!40000 ALTER TABLE `unary_constraint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wardrobe`
--

DROP TABLE IF EXISTS `wardrobe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wardrobe` (
  `id` varchar(36) NOT NULL,
  `person_id` varchar(36) NOT NULL,
  `owner_name` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `person_id` (`person_id`),
  KEY `idx_wardrobe_person` (`person_id`),
  CONSTRAINT `wardrobe_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wardrobe`
--

LOCK TABLES `wardrobe` WRITE;
/*!40000 ALTER TABLE `wardrobe` DISABLE KEYS */;
INSERT INTO `wardrobe` VALUES ('1','1','Max\'s Wardrobe','2024-11-30 09:49:54'),('2','2','Erika\'s Wardrobe','2024-11-30 09:49:54');
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

-- Dump completed on 2024-11-30 10:50:56
