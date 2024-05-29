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
-- Table structure for table `flat_manager`
--

DROP TABLE IF EXISTS `flat_manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flat_manager` (
  `room_number` varchar(10) NOT NULL,
  `occupancy_status` char(3) NOT NULL,
  `visit_num` int DEFAULT NULL,
  KEY `room_number_idx` (`room_number`),
  KEY `flat_visit_num_idx` (`visit_num`),
  CONSTRAINT `fk_room_number` FOREIGN KEY (`room_number`) REFERENCES `flat_master` (`room_number`),
  CONSTRAINT `flat_visit_num` FOREIGN KEY (`visit_num`) REFERENCES `visit_master` (`visit_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flat_manager`
--

LOCK TABLES `flat_manager` WRITE;
/*!40000 ALTER TABLE `flat_manager` DISABLE KEYS */;
INSERT INTO `flat_manager` VALUES ('W1-A1','v',NULL),('W1-B1','v',NULL),('W1-C1','v',NULL),('W1-D1','v',NULL),('W1-A2','v',NULL),('W1-B2','v',NULL),('W1-C2','v',NULL),('W1-D2','v',NULL),('W2-A1','v',NULL),('W2-B1','v',NULL),('W2-C1','v',NULL),('W2-D1','v',NULL),('W2-A2','v',NULL),('W2-B2','v',NULL),('W2-C2','v',NULL),('W2-D2','v',NULL),('W3-A1','v',NULL),('W3-B1','v',NULL),('W3-C1','v',NULL),('W3-D1','v',NULL),('W3-A2','v',NULL),('W3-B2','v',NULL),('W3-C2','v',NULL),('W3-D2','v',NULL),('S1-A1','v',NULL),('S1-B1','v',NULL),('S1-C1','v',NULL),('S1-D1','v',NULL),('S1-A2','v',NULL),('S1-B2','v',NULL),('S1-C2','v',NULL),('S1-D2','v',NULL),('S2-A1','v',NULL),('S2-B1','v',NULL),('S2-C1','v',NULL),('S2-D1','v',NULL),('S2-A2','v',NULL),('S2-B2','v',NULL),('S2-C2','v',NULL),('S2-D2','v',NULL),('S3-A1','v',NULL),('S3-B1','v',NULL),('S3-C1','v',NULL),('S3-D1','v',NULL),('S3-A2','v',NULL),('S3-B2','v',NULL),('S3-C2','v',NULL),('S3-D2','v',NULL),('N1-A1','v',NULL),('N1-B1','v',NULL),('N1-C1','v',NULL),('N1-D1','v',NULL),('N1-A2','v',NULL),('N1-B2','v',NULL),('N1-C2','v',NULL),('N1-D2','v',NULL),('N2-A1','v',NULL),('N2-B1','v',NULL),('N2-C1','v',NULL),('N2-D1','v',NULL),('N2-A2','g',NULL),('N2-B2','g',NULL),('N2-C2','v',NULL),('N2-D2','v',NULL),('N3-A1','v',NULL),('N3-B1','v',NULL),('N3-C1','v',NULL),('N3-D1','v',NULL),('N3-A2','v',NULL),('N3-B2','v',NULL),('N3-C2','v',NULL),('N3-D2','v',NULL);
/*!40000 ALTER TABLE `flat_manager` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-29 10:15:56
