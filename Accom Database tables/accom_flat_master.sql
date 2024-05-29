-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: accom
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `flat_master`
--

DROP TABLE IF EXISTS `flat_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flat_master` (
  `room_number` varchar(10) NOT NULL,
  `category_id` int DEFAULT NULL,
  `remark` tinytext,
  PRIMARY KEY (`room_number`),
  KEY `category_id_idx` (`category_id`),
  KEY `room_number_idx` (`room_number`),
  CONSTRAINT `category_id` FOREIGN KEY (`category_id`) REFERENCES `flat_category_master` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flat_master`
--

LOCK TABLES `flat_master` WRITE;
/*!40000 ALTER TABLE `flat_master` DISABLE KEYS */;
INSERT INTO `flat_master` VALUES ('N1-A1',9,NULL),('N1-A2',9,NULL),('N1-B1',9,NULL),('N1-B2',9,NULL),('N1-C1',9,NULL),('N1-C2',10,NULL),('N1-D1',10,NULL),('N1-D2',10,NULL),('N2-A1',5,NULL),('N2-A2',5,NULL),('N2-B1',5,NULL),('N2-B2',6,NULL),('N2-C1',6,NULL),('N2-C2',6,NULL),('N2-D1',6,NULL),('N2-D2',5,NULL),('N3-A1',4,NULL),('N3-A2',4,NULL),('N3-B1',4,NULL),('N3-B2',4,NULL),('N3-C1',5,NULL),('N3-C2',10,NULL),('N3-D1',5,NULL),('N3-D2',6,NULL),('R1',5,NULL),('R2',5,NULL),('R3',5,NULL),('S1-A1',1,NULL),('S1-A2',1,NULL),('S1-B1',1,NULL),('S1-B2',1,NULL),('S1-C1',1,NULL),('S1-C2',1,NULL),('S1-D1',1,NULL),('S1-D2',1,NULL),('S2-A1',2,NULL),('S2-A2',2,NULL),('S2-B1',2,NULL),('S2-B2',2,NULL),('S2-C1',2,NULL),('S2-C2',2,NULL),('S2-D1',2,NULL),('S2-D2',2,NULL),('S3-A1',3,NULL),('S3-A2',3,NULL),('S3-B1',3,NULL),('S3-B2',3,NULL),('S3-C1',3,NULL),('S3-C2',3,NULL),('S3-D1',3,NULL),('S3-D2',3,NULL),('SBN-A1',8,NULL),('SBN-A2',8,NULL),('SBN-A3',8,NULL),('SBN-A4',8,NULL),('SBN-A5',7,NULL),('SBN-A6',7,NULL),('SBN-A7',7,NULL),('SBN-A8',7,NULL),('W1-A1',1,NULL),('W1-A2',1,NULL),('W1-B1',1,NULL),('W1-B2',1,NULL),('W1-C1',1,NULL),('W1-C2',1,NULL),('W1-D1',1,NULL),('W1-D2',1,NULL),('W2-A1',2,NULL),('W2-A2',2,NULL),('W2-B1',2,NULL),('W2-B2',2,NULL),('W2-C1',2,NULL),('W2-C2',2,NULL),('W2-D1',2,NULL),('W2-D2',2,NULL),('W3-A1',2,NULL),('W3-A2',2,NULL),('W3-B1',2,NULL),('W3-B2',1,NULL),('W3-C1',1,NULL),('W3-C2',1,NULL),('W3-D1',1,NULL),('W3-D2',2,NULL);
/*!40000 ALTER TABLE `flat_master` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-29 10:15:54
