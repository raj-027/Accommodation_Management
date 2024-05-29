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
-- Table structure for table `visit_master`
--

DROP TABLE IF EXISTS `visit_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visit_master` (
  `visit_num` int NOT NULL AUTO_INCREMENT,
  `I_F` char(1) NOT NULL,
  `room_number` varchar(10) NOT NULL,
  `person_id` varchar(45) NOT NULL,
  `bill_id` int DEFAULT NULL,
  `vacated_date` date DEFAULT NULL,
  `from_date` datetime NOT NULL,
  `to_date` datetime DEFAULT NULL,
  `no_of_days` int NOT NULL,
  `male_num` int DEFAULT NULL,
  `female_num` int DEFAULT NULL,
  `child_num` int DEFAULT NULL,
  `total` int NOT NULL,
  `A_D` char(1) DEFAULT NULL,
  `remark` text,
  `visit_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`visit_num`),
  KEY `room_number_idx` (`room_number`),
  KEY `person_id_idx` (`person_id`),
  KEY `visit_num_idx` (`visit_num`),
  KEY `bill_id_idx` (`bill_id`),
  CONSTRAINT `bill_id` FOREIGN KEY (`bill_id`) REFERENCES `bill_master` (`bill_id`),
  CONSTRAINT `person_id` FOREIGN KEY (`person_id`) REFERENCES `person_master` (`person_id`),
  CONSTRAINT `room_number` FOREIGN KEY (`room_number`) REFERENCES `flat_master` (`room_number`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visit_master`
--

LOCK TABLES `visit_master` WRITE;
/*!40000 ALTER TABLE `visit_master` DISABLE KEYS */;
INSERT INTO `visit_master` VALUES (4,'I','S1-A2','78945612300',1,NULL,'2024-03-16 00:00:00','2024-03-18 00:00:00',2,1,1,1,3,'D','GOOD','I4'),(5,'I','N1-B2','7898652002',2,NULL,'2024-03-16 00:00:00','2024-03-18 00:00:00',2,1,2,1,4,'D','GOOD','I5');
/*!40000 ALTER TABLE `visit_master` ENABLE KEYS */;
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
