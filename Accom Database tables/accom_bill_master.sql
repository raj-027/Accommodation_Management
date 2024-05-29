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
-- Table structure for table `bill_master`
--

DROP TABLE IF EXISTS `bill_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill_master` (
  `bill_id` int NOT NULL AUTO_INCREMENT,
  `visit_num` int NOT NULL,
  `room_number` varchar(10) NOT NULL,
  `G_F_S` char(10) NOT NULL,
  `amt_collected` decimal(10,2) DEFAULT NULL,
  `amt_due` decimal(10,2) DEFAULT NULL,
  `paymode` char(5) DEFAULT NULL,
  `closed_on` date DEFAULT NULL,
  `remark` varchar(45) DEFAULT NULL,
  `guest_from` varchar(45) DEFAULT NULL,
  `bill_type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`bill_id`),
  KEY `visit_master_idx` (`visit_num`),
  CONSTRAINT `visit_master` FOREIGN KEY (`visit_num`) REFERENCES `visit_master` (`visit_num`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill_master`
--

LOCK TABLES `bill_master` WRITE;
/*!40000 ALTER TABLE `bill_master` DISABLE KEYS */;
INSERT INTO `bill_master` VALUES (1,4,'S1-A2','G',120.00,NULL,'CASH',NULL,NULL,NULL,'DEVOTEES'),(2,5,'N1-B2','F',600.00,NULL,'CASH',NULL,NULL,NULL,'DEVOTEES');
/*!40000 ALTER TABLE `bill_master` ENABLE KEYS */;
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
