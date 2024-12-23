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
  `id` int NOT NULL AUTO_INCREMENT,
  `constraint_id` int NOT NULL,
  `item_1_id` int NOT NULL,
  `item_2_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `constraint_id` (`constraint_id`),
  KEY `item_1_id` (`item_1_id`),
  KEY `item_2_id` (`item_2_id`),
  CONSTRAINT `binary_constraint_ibfk_1` FOREIGN KEY (`constraint_id`) REFERENCES `constraints` (`id`) ON DELETE CASCADE,
  CONSTRAINT `binary_constraint_ibfk_2` FOREIGN KEY (`item_1_id`) REFERENCES `clothing_item` (`id`) ON DELETE CASCADE,
  CONSTRAINT `binary_constraint_ibfk_3` FOREIGN KEY (`item_2_id`) REFERENCES `clothing_item` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `binary_constraint`
--

LOCK TABLES `binary_constraint` WRITE;
/*!40000 ALTER TABLE `binary_constraint` DISABLE KEYS */;
/*!40000 ALTER TABLE `binary_constraint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cardinality_constraint`
--

DROP TABLE IF EXISTS `cardinality_constraint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cardinality_constraint` (
  `id` int NOT NULL AUTO_INCREMENT,
  `constraint_id` int NOT NULL,
  `min_count` int NOT NULL,
  `max_count` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `constraint_id` (`constraint_id`),
  CONSTRAINT `cardinality_constraint_ibfk_1` FOREIGN KEY (`constraint_id`) REFERENCES `constraints` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cardinality_constraint`
--

LOCK TABLES `cardinality_constraint` WRITE;
/*!40000 ALTER TABLE `cardinality_constraint` DISABLE KEYS */;
/*!40000 ALTER TABLE `cardinality_constraint` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clothing_item`
--

LOCK TABLES `clothing_item` WRITE;
/*!40000 ALTER TABLE `clothing_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `clothing_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clothing_type`
--

DROP TABLE IF EXISTS `clothing_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clothing_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type_name` varchar(255) NOT NULL,
  `type_usage` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clothing_type`
--

LOCK TABLES `clothing_type` WRITE;
/*!40000 ALTER TABLE `clothing_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `clothing_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `constraints`
--

DROP TABLE IF EXISTS `constraints`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `constraints` (
  `id` int NOT NULL AUTO_INCREMENT,
  `constraint_type` enum('Unary','Binary','Implication','Cardinality','Mutex') NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `constraints`
--

LOCK TABLES `constraints` WRITE;
/*!40000 ALTER TABLE `constraints` DISABLE KEYS */;
/*!40000 ALTER TABLE `constraints` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `implication_constraint`
--

DROP TABLE IF EXISTS `implication_constraint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `implication_constraint` (
  `id` int NOT NULL AUTO_INCREMENT,
  `constraint_id` int NOT NULL,
  `if_type_id` int NOT NULL,
  `then_type_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `constraint_id` (`constraint_id`),
  KEY `if_type_id` (`if_type_id`),
  KEY `then_type_id` (`then_type_id`),
  CONSTRAINT `implication_constraint_ibfk_1` FOREIGN KEY (`constraint_id`) REFERENCES `constraints` (`id`) ON DELETE CASCADE,
  CONSTRAINT `implication_constraint_ibfk_2` FOREIGN KEY (`if_type_id`) REFERENCES `clothing_type` (`id`),
  CONSTRAINT `implication_constraint_ibfk_3` FOREIGN KEY (`then_type_id`) REFERENCES `clothing_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `implication_constraint`
--

LOCK TABLES `implication_constraint` WRITE;
/*!40000 ALTER TABLE `implication_constraint` DISABLE KEYS */;
/*!40000 ALTER TABLE `implication_constraint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mutex_constraint`
--

DROP TABLE IF EXISTS `mutex_constraint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mutex_constraint` (
  `id` int NOT NULL AUTO_INCREMENT,
  `constraint_id` int NOT NULL,
  `item_1_id` int NOT NULL,
  `item_2_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `constraint_id` (`constraint_id`),
  KEY `item_1_id` (`item_1_id`),
  KEY `item_2_id` (`item_2_id`),
  CONSTRAINT `mutex_constraint_ibfk_1` FOREIGN KEY (`constraint_id`) REFERENCES `constraints` (`id`) ON DELETE CASCADE,
  CONSTRAINT `mutex_constraint_ibfk_2` FOREIGN KEY (`item_1_id`) REFERENCES `clothing_item` (`id`) ON DELETE CASCADE,
  CONSTRAINT `mutex_constraint_ibfk_3` FOREIGN KEY (`item_2_id`) REFERENCES `clothing_item` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mutex_constraint`
--

LOCK TABLES `mutex_constraint` WRITE;
/*!40000 ALTER TABLE `mutex_constraint` DISABLE KEYS */;
/*!40000 ALTER TABLE `mutex_constraint` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outfit`
--

LOCK TABLES `outfit` WRITE;
/*!40000 ALTER TABLE `outfit` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `style`
--

LOCK TABLES `style` WRITE;
/*!40000 ALTER TABLE `style` DISABLE KEYS */;
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
  `constraint_id` int NOT NULL,
  `style_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `constraint_id` (`constraint_id`),
  KEY `style_id` (`style_id`),
  CONSTRAINT `unary_constraint_ibfk_1` FOREIGN KEY (`constraint_id`) REFERENCES `constraints` (`id`) ON DELETE CASCADE,
  CONSTRAINT `unary_constraint_ibfk_2` FOREIGN KEY (`style_id`) REFERENCES `style` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
  `id` int NOT NULL AUTO_INCREMENT,
  `wardrobe_owner` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wardrobe_owner` (`wardrobe_owner`),
  CONSTRAINT `wardrobe_ibfk_1` FOREIGN KEY (`wardrobe_owner`) REFERENCES `person` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wardrobe`
--

LOCK TABLES `wardrobe` WRITE;
/*!40000 ALTER TABLE `wardrobe` DISABLE KEYS */;
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

-- Dump completed on 2024-12-23  2:24:17
