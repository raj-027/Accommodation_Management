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
-- Table structure for table `person_master`
--

DROP TABLE IF EXISTS `person_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person_master` (
  `person_id` varchar(20) NOT NULL,
  `mobile_num` int DEFAULT NULL,
  `name` char(40) NOT NULL,
  `gender` char(10) NOT NULL,
  `dob` date DEFAULT NULL,
  `role` char(10) DEFAULT NULL,
  `place_name` varchar(45) NOT NULL,
  `I_F` char(1) NOT NULL,
  `visa_number` varchar(20) DEFAULT NULL,
  `visa_expiry` date DEFAULT NULL,
  PRIMARY KEY (`person_id`),
  KEY `place_name_idx` (`place_name`),
  KEY `person_id_idx` (`person_id`),
  CONSTRAINT `place_name` FOREIGN KEY (`place_name`) REFERENCES `country_state` (`place_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person_master`
--

LOCK TABLES `person_master` WRITE;
/*!40000 ALTER TABLE `person_master` DISABLE KEYS */;
INSERT INTO `person_master` VALUES ('78945612300',1234567899,'SUPER MAN','M',NULL,NULL,'ODISHA','I',NULL,NULL),('7898652002',321654987,'SPIDER MAN','M',NULL,NULL,'JHARKHAND','I',NULL,NULL);
/*!40000 ALTER TABLE `person_master` ENABLE KEYS */;
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
