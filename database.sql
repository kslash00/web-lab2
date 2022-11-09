-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: std-mysql    Database: std_1688_exam
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.16.04.1

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('04d88246e641');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_genre`
--

DROP TABLE IF EXISTS `book_genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_genre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) DEFAULT NULL,
  `genre_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_book_genre_book_id_books` (`book_id`),
  KEY `fk_book_genre_genre_id_genres` (`genre_id`),
  CONSTRAINT `fk_book_genre_book_id_books` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_book_genre_genre_id_genres` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_genre`
--

LOCK TABLES `book_genre` WRITE;
/*!40000 ALTER TABLE `book_genre` DISABLE KEYS */;
INSERT INTO `book_genre` VALUES (18,2,1),(19,2,5),(21,4,2),(23,3,3),(24,5,4),(25,6,5);
/*!40000 ALTER TABLE `book_genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `short_desc` text NOT NULL,
  `rating_sum` int(11) NOT NULL,
  `rating_num` int(11) NOT NULL,
  `year` year(4) NOT NULL,
  `publisher` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `vol_pages` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (2,'Кости Волхвов','В Кельнском соборе во время праздничной службы происходит массовое убийство: все прихожане погибают мучительной смертью. Преступники, облаченные в монашеские рясы, похищают бесценную реликвию, хранившуюся в соборе с XII века, – кости библейских волхвов. Из Вашингтона для расследования преступления послана группа спецагентов секретной организации «Сигма» во главе с Греем Пирсом. Совместно с учеными Ватикана группе удается установить, что в убийстве и похищении замешан Имперский орден дракона – тайное братство алхимиков, корни которого уходят в глубь веков.',0,0,2013,'ЭКСМО','Джеймс Пол Чайковски',1123),(3,'Гордость и предубеждение','Роман начинается с беседы мистера и миссис Беннет о приезде молодого мистера Бингли в Незерфилд-парк. Жена уговаривает мужа навестить соседа и свести с ним более тесное знакомство. Она надеется, что мистеру Бингли непременно понравится одна из их пяти дочерей. Мистер Беннет наносит визит молодому человеку, и тот через какое-то время наносит ответный.',0,0,2010,'ЭКСМО','Джейн Остин',356),(4,'Кости Пети','В Кельнском соборе во время праздничной службы происходит массовое убийство: все прихожане погибают мучительной смертью. Преступники, облаченные в монашеские рясы, похищают бесценную реликвию, хранившуюся в соборе с XII века, – кости библейских волхвов. Из Вашингтона для расследования преступления послана группа спецагентов секретной организации «Сигма» во главе с Греем Пирсом. Совместно с учеными Ватикана группе удается установить, что в убийстве и похищении замешан Имперский орден дракона – тайное братство алхимиков, корни которого уходят в глубь веков.',5,1,1995,'ЭКСМО','Вася Пупкин',257),(5,'Кости Псов','В Кельнском соборе во время праздничной службы происходит массовое убийство: все прихожане погибают мучительной смертью. Преступники, облаченные в монашеские рясы, похищают бесценную реликвию, хранившуюся в соборе с XII века, – кости библейских волхвов. Из Вашингтона для расследования преступления послана группа спецагентов секретной организации «Сигма» во главе с Греем Пирсом. Совместно с учеными Ватикана группе удается установить, что в убийстве и похищении замешан Имперский орден дракона – тайное братство алхимиков, корни которого уходят в глубь веков.',0,0,2000,'ЭКСМО','Джейн Остин Ип',523),(6,'Кости Волка','цкпмм цам цм уиее',0,0,2006,'ЭКСМО','Вася Пупкин Вова',257);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS `genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_genres_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genres`
--

LOCK TABLES `genres` WRITE;
/*!40000 ALTER TABLE `genres` DISABLE KEYS */;
INSERT INTO `genres` VALUES (2,'Детектив'),(3,'Исторический роман'),(1,'Научная фантастика'),(5,'Триллер'),(4,'Фэнтези');
/*!40000 ALTER TABLE `genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `images`
--

DROP TABLE IF EXISTS `images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `images` (
  `id` varchar(100) NOT NULL,
  `file_name` varchar(100) NOT NULL,
  `mime_type` varchar(100) NOT NULL,
  `md5_hash` varchar(100) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `book_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_images_md5_hash` (`md5_hash`),
  KEY `fk_images_book_id_books` (`book_id`),
  CONSTRAINT `fk_images_book_id_books` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `images`
--

LOCK TABLES `images` WRITE;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
INSERT INTO `images` VALUES ('6e38a99c-4787-4186-9856-e637c49e85d3','persi.jpg','image/jpeg','5768568b7224c76cbab682679f452c72','2022-11-09 13:03:24',5),('c774a843-c461-4029-8cc6-354959355645','player.jpg','image/jpeg','298e63580dd059bc367c15646d5b6711','2022-11-09 13:01:31',4),('cc288a29-abf8-46f2-8ced-c7c242b5905f','m-and-m1.jpg','image/jpeg','ae4d92a137e6328e2d479f548c59d119','2022-11-09 21:38:26',6),('de4aa916-6bfe-4d6d-99cb-9b226eb49820','bones.jpg','image/jpeg','3178df5ee780b4aec255d8774fb28b84','2022-11-09 12:47:17',2),('f8504e0c-65f0-473d-b81e-f3fb5af3553c','g-and-p.jpg','image/jpeg','9e25524fb36de18b419c813c383a3bb7','2022-11-09 12:56:10',3);
/*!40000 ALTER TABLE `images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` int(11) NOT NULL,
  `text` text NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `book_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_reviews_book_id_books` (`book_id`),
  KEY `fk_reviews_user_id_users` (`user_id`),
  CONSTRAINT `fk_reviews_book_id_books` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_reviews_user_id_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,5,'Книга класс','2022-11-09 13:11:29',4,2);
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `desciption` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'ADMIN','ADMIN'),(2,'MODER','MODER'),(3,'USER','USER');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `last_name` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) NOT NULL,
  `login` varchar(100) NOT NULL,
  `password_hash` varchar(200) NOT NULL,
  `role_id` int(11) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_users_login` (`login`),
  UNIQUE KEY `uq_users_password_hash` (`password_hash`),
  KEY `fk_users_role_id_roles` (`role_id`),
  CONSTRAINT `fk_users_role_id_roles` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'Иванов','Иван','Иванов','user','pbkdf2:sha256:260000$hqHwpU7k2kH5I070$642761bc99ea51409a5e01a7e5f97f5babdb86c5a9f2b90f42039f1102059f88',3,'2022-11-08 18:27:54'),(3,'Огурцова','Карина','Константиновна','admin','pbkdf2:sha256:260000$SgCEqpvDrABlLFuv$805bafb758f4c6b2caa36481e5976836ae8680d1b795552ae6138b90c6658a69',1,'2022-11-08 18:30:29'),(4,'Кукушкина','Ксюша','Ивановна','moder','pbkdf2:sha256:260000$bGrcM3V8FLDEa0az$52d2eef19e5b3638aac6fa7ca59fd6414506118039175423b21eb86d0a3f0c81',2,'2022-11-08 18:30:54');
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

-- Dump completed on 2022-11-09 21:52:08
