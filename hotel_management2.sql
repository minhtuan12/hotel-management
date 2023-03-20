-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: hotel_management2
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `amusement_bill`
--

DROP TABLE IF EXISTS `amusement_bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amusement_bill` (
  `Room_no` int NOT NULL,
  `Num_Waterpolo` int DEFAULT '0',
  `Num_Bumpingcar` int DEFAULT '0',
  `Num_4Dmovie` int DEFAULT '0',
  `Num_GoKart` int DEFAULT '0',
  `Num_F1sim` int DEFAULT '0',
  `Amusement_Bill` int DEFAULT '0',
  PRIMARY KEY (`Room_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amusement_bill`
--

LOCK TABLES `amusement_bill` WRITE;
/*!40000 ALTER TABLE `amusement_bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `amusement_bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bar_bill`
--

DROP TABLE IF EXISTS `bar_bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bar_bill` (
  `Room_no` int NOT NULL,
  `Num_Water` int DEFAULT '0',
  `Num_Pinacolada` int DEFAULT '0',
  `Num_Fruitpunch` int DEFAULT '0',
  `Num_Scotchwhiskey` int DEFAULT '0',
  `Num_Vodkashots` int DEFAULT '0',
  `Bar_Bill` int DEFAULT '0',
  PRIMARY KEY (`Room_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bar_bill`
--

LOCK TABLES `bar_bill` WRITE;
/*!40000 ALTER TABLE `bar_bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `bar_bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carrent_bill`
--

DROP TABLE IF EXISTS `carrent_bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrent_bill` (
  `Room_no` int NOT NULL,
  `Num_Jeep` int DEFAULT '0',
  `Num_Landrover` int DEFAULT '0',
  `Num_Volkswagen` int DEFAULT '0',
  `Num_Mercedes` int DEFAULT '0',
  `Num_RollsRoyce` int DEFAULT '0',
  `CarRent_Bill` int DEFAULT '0',
  PRIMARY KEY (`Room_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrent_bill`
--

LOCK TABLES `carrent_bill` WRITE;
/*!40000 ALTER TABLE `carrent_bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `carrent_bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cust_data`
--

DROP TABLE IF EXISTS `cust_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cust_data` (
  `Room_no` int NOT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Address` varchar(20) DEFAULT NULL,
  `Number_Of_days` int DEFAULT NULL,
  `Room_Type` varchar(12) DEFAULT NULL,
  `Total_Room_Cost` int DEFAULT NULL,
  PRIMARY KEY (`Room_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cust_data`
--

LOCK TABLES `cust_data` WRITE;
/*!40000 ALTER TABLE `cust_data` DISABLE KEYS */;
/*!40000 ALTER TABLE `cust_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food_bill`
--

DROP TABLE IF EXISTS `food_bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `food_bill` (
  `Room_no` int NOT NULL,
  `Num_Water` int DEFAULT '0',
  `Num_Tea` int DEFAULT '0',
  `Num_BreakfastCombo` int DEFAULT '0',
  `Num_LunchCombo` int DEFAULT '0',
  `Num_DinnerCombo` int DEFAULT '0',
  `Food_Bill` int DEFAULT '0',
  PRIMARY KEY (`Room_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food_bill`
--

LOCK TABLES `food_bill` WRITE;
/*!40000 ALTER TABLE `food_bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `food_bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_bill`
--

DROP TABLE IF EXISTS `game_bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_bill` (
  `Room_no` int NOT NULL,
  `Num_Tabletennis` int DEFAULT '0',
  `Num_Bowling` int DEFAULT '0',
  `Num_Snooker` int DEFAULT '0',
  `Num_Videogames` int DEFAULT '0',
  `Num_Pool` int DEFAULT '0',
  `Game_bill` int DEFAULT '0',
  PRIMARY KEY (`Room_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_bill`
--

LOCK TABLES `game_bill` WRITE;
/*!40000 ALTER TABLE `game_bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `game_bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `laundry_bill`
--

DROP TABLE IF EXISTS `laundry_bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `laundry_bill` (
  `Room_no` int NOT NULL,
  `Num_Shorts` int DEFAULT '0',
  `Num_Trousers` int DEFAULT '0',
  `Num_Shirt` int DEFAULT '0',
  `Num_Jeans` int DEFAULT '0',
  `Num_Girlsuit` int DEFAULT '0',
  `Laundry_Bill` int DEFAULT '0',
  PRIMARY KEY (`Room_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `laundry_bill`
--

LOCK TABLES `laundry_bill` WRITE;
/*!40000 ALTER TABLE `laundry_bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `laundry_bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `services_bill`
--

DROP TABLE IF EXISTS `services_bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `services_bill` (
  `Room_no` int NOT NULL,
  `Num_Hairspa` int DEFAULT '0',
  `Num_bodyspa` int DEFAULT '0',
  `Num_hotwaterbath` int DEFAULT '0',
  `Num_indoorgym` int DEFAULT '0',
  `Num_outdoorgym` int DEFAULT '0',
  `Services_bill` int DEFAULT '0',
  PRIMARY KEY (`Room_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `services_bill`
--

LOCK TABLES `services_bill` WRITE;
/*!40000 ALTER TABLE `services_bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `services_bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `statuss`
--

DROP TABLE IF EXISTS `statuss`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `statuss` (
  `Room_no` int DEFAULT NULL,
  `status_room` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statuss`
--

LOCK TABLES `statuss` WRITE;
/*!40000 ALTER TABLE `statuss` DISABLE KEYS */;
INSERT INTO `statuss` VALUES (101,0),(102,0),(103,0),(104,0);
/*!40000 ALTER TABLE `statuss` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t1`
--

DROP TABLE IF EXISTS `t1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t1` (
  `Room_no` int NOT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Total_Room_Cost` int DEFAULT NULL,
  `Food_bill` int DEFAULT NULL,
  `Laundry_bill` int DEFAULT NULL,
  `bar_bill` int DEFAULT NULL,
  `carrent_bill` int DEFAULT NULL,
  `game_bill` int DEFAULT NULL,
  `Services_bill` int DEFAULT NULL,
  `amusement_bill` int DEFAULT NULL,
  `Cost` int DEFAULT NULL,
  PRIMARY KEY (`Room_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t1`
--

LOCK TABLES `t1` WRITE;
/*!40000 ALTER TABLE `t1` DISABLE KEYS */;
/*!40000 ALTER TABLE `t1` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-20 18:03:17
