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
-- Table structure for table `guest_diary`
--

DROP TABLE IF EXISTS `guest_diary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guest_diary` (
  `name` char(40) NOT NULL,
  `department` char(10) NOT NULL,
  `on_payment` char(3) NOT NULL,
  `from_date` datetime NOT NULL,
  `to_date` datetime DEFAULT NULL,
  `room_number` varchar(10) NOT NULL,
  `bill_id` int DEFAULT NULL,
  `remark` text,
  `visit_num` int DEFAULT NULL,
  KEY `room_number_idx` (`room_number`),
  KEY `fk_bill_id_guest_idx` (`bill_id`),
  KEY `fk_visit_num_guest_idx` (`visit_num`),
  CONSTRAINT `fk_bill_id_guest` FOREIGN KEY (`bill_id`) REFERENCES `bill_master` (`bill_id`),
  CONSTRAINT `fk_room_number_guest` FOREIGN KEY (`room_number`) REFERENCES `flat_master` (`room_number`),
  CONSTRAINT `fk_visit_num_guest` FOREIGN KEY (`visit_num`) REFERENCES `visit_master` (`visit_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guest_diary`
--

LOCK TABLES `guest_diary` WRITE;
/*!40000 ALTER TABLE `guest_diary` DISABLE KEYS */;
INSERT INTO `guest_diary` VALUES ('RAJJ','sssihl','yes','2024-03-20 00:00:00',NULL,'N2-A1',NULL,'',NULL),('RAJJ','sssihl','yes','2024-03-20 00:00:00',NULL,'N2-A1',NULL,'',NULL),('RITICK','sssihms','yes','2024-03-20 00:00:00',NULL,'N1-C2',NULL,'/',NULL),('HYRT','ssshss','yes','2024-03-20 00:00:00',NULL,'N2-C2',NULL,'ju',NULL),('HYRT','ssshss','no','2024-03-20 00:00:00',NULL,'N2-B2',NULL,'ju',NULL),('GUEST12','sssihl','no','2024-03-24 00:00:00',NULL,'N2-A2',NULL,'//',NULL);
/*!40000 ALTER TABLE `guest_diary` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-29 10:15:55
