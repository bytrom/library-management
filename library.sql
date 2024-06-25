-- MySQL dump 10.13  Distrib 5.1.73, for Win32 (ia32)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	5.1.73-community

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `id` int(11) NOT NULL DEFAULT '0',
  `name` varchar(500) DEFAULT NULL,
  `author` varchar(500) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `catalouge` varchar(100) DEFAULT NULL,
  `genre` varchar(100) DEFAULT NULL,
  `holder` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (357,'Murder on the orient express','Agatha Christie',496,'R2S4E','Crime-Fiction','Sai Kiran'),(708,'A Short History of World','H G Wells',300,'R2S4A','Sci-Fi','Sameer'),(920,'My Days','R K Narayan',635,'R4S1A','Drama','Mukesh'),(926,'Pradyumna','Usha Narayanan',456,'R3S4E','Mythical-Fiction','Abhiram'),(965,'Arise Awake','Rashmi Bansal',145,'R2S2C','Non-Fiction',NULL),(981,'Long walk to Freedom','Nelson Mandela',369,'R2S3B','Auto Biography',NULL),(1013,'Waiting for the Mahatma','R K Narayan',754,'R4S2E','Semi-Biography',NULL),(1115,'The Trails of Apollo:The Dark Proplecy','Rick Riordan',122,'R2S2D','Fantasy','Tejus'),(1138,'Gone with the Wind','Margaret Mitchaell',235,'R2S2E','Romance','Pranav'),(1354,'The Davinci Code','Dan Brown',345,'R2S3D','Thriller',NULL),(1355,'The Namesake','Jhumpa Lahiri',500,'R2S2B','Fantasy','Prasad'),(1407,'Mighter than the Sword','Jeffrey Archer',195,'R1S3D','Fiction','Bhargav'),(1438,'The Hobbit','JRR Tolken',456,'R1S1B','Fantasy','Sandeep'),(1456,'The Secret','Rhonda Byrne',458,'R1S2A','Non-Fiction',NULL),(1495,'Where Have All Leaders Gone','Lee Jacocca',320,'R3S1C','Non-Fiction',NULL),(1518,'Panchatantra','Vishnu Sharma',368,'R1S3E','Fiction','Sai'),(1536,'Frankstein','Mary Shelly',412,'R3S2A','Sci-Fi',NULL),(1564,'The Throne of Fire','Rick Riordan',438,'R4S1D','Fantasy',NULL),(1573,'Harry Potter And the Prisnor of Azkaben','J K Rowling',800,'R1S2C','Fantasy','Ranga'),(1686,'Famous Five:Five go to demons rocks','Enid Blyton',369,'R1S1A','Mystery','Pranav Sai'),(1721,'Heroes of Olympus:The Demigod Diaries','Rick Riordan',451,'R4S2C','Fantasy',NULL),(1755,'Sita:Warrrior of Mithila','Amish',250,'R4S3B','Mythical Fiction','Akash'),(1774,'The Shakespeare Mask','Frohlich',678,'R4S4D','Detective','Abhishek'),(1950,'Aleph','Paulo Coelho',126,'R1S4C','Drama','Kalim'),(1991,'Sense and Sensibility','Jane Austen',651,'R3S1D','Romance',NULL),(2511,'61 Hours','Lee Child',245,'R1S2D','Crime',NULL),(2512,'Make Me','Lee Child',100,'R3S1E','Crime','Vasanth'),(2732,'The Vampire Diaries:The Compelled','L.J.Smith',541,'R1S4B','Fiction','Mustaq'),(3032,'Capital','John Lance',710,'R2S1A','Non-Fiction','None'),(3200,'Wings of Fire: The Hidden Kingdom','Sutherland',365,'R3S2C','Fantasy','Saketh');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `magazines`
--

DROP TABLE IF EXISTS `magazines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `magazines` (
  `name` varchar(100) NOT NULL,
  `genre` varchar(100) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `magazines`
--

LOCK TABLES `magazines` WRITE;
/*!40000 ALTER TABLE `magazines` DISABLE KEYS */;
INSERT INTO `magazines` VALUES ('Better Photography','Photography',9),('Biology Today','Subject Oriented',9),('Champak','Entertainment',8),('Competition Success Review','GK & GA',10),('Current Science','Science',7),('Digital','Technology',6),('Down To Earth','Current Awareness',6),('Economic Political','Poilitics',5),('Electronics For You','Technology',4),('Front Line','Current Topics',4),('Gobar Times','Political',5),('Health','Health',5),('Highlights Champs','Entertainment',5),('MGT CHemistry','Subject oriented',7),('MGT Maths','Subject oriented',5),('MGT Physics','Subject oriented',6),('National Geography Kids','Wildlife',6),('National Geography Magazine','Wildlife',2),('Outlook','Current Topics',6),('Outlook Spotlight','Current Awareness',6),('Parent Edge','Guidance',3),('PC Quest','Current Awareness',7),('Pratiyogita Darpan(E)','GK & GA',10),('Pratiyogita Darpan(H)','GK & GA',4),('Sanctuary Asia','Wildlife',5),('Science Reporter','Science',3),('Sports Star','Sports',4),('Tell Me Why','GK & GA',3),('The Week','Current Awareness',2),('TIME','Current Affairs',3),('Tinkle','Entertainment',4),('Wisdom','Entertainment',8),('World Focus','Political',4);
/*!40000 ALTER TABLE `magazines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `name` varchar(100) DEFAULT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('Priyadarshini','priya','library');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-28 10:28:35
