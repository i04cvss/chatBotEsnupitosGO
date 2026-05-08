-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: esnupitos
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

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
-- Table structure for table `costos_envio`
--

DROP TABLE IF EXISTS `costos_envio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `costos_envio` (
  `categoria` varchar(50) NOT NULL,
  `costo_envio_aprox` varchar(50) DEFAULT NULL,
  `costo_aduana_aprox` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `costos_envio`
--

LOCK TABLES `costos_envio` WRITE;
/*!40000 ALTER TABLE `costos_envio` DISABLE KEYS */;
INSERT INTO `costos_envio` VALUES ('Álbum','Envio: $7000 a $12000 pesos chilenos APROXIMADAMEN','Aduana: $3000 a $7000 pesos chilenos APROXIMADAMEN'),('Photocard/PC','Envio: $500 a $1000 pesos chilenos APROXIMADAMENTE','Aduana: $100 a $700 pesos chilenos APROXIMADAMENTE');
/*!40000 ALTER TABLE `costos_envio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faq`
--

DROP TABLE IF EXISTS `faq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faq` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pregunta` text DEFAULT NULL,
  `respuesta` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faq`
--

LOCK TABLES `faq` WRITE;
/*!40000 ALTER TABLE `faq` DISABLE KEYS */;
INSERT INTO `faq` VALUES (1,'cuanto demora el envio','El envío demora entre 1 mes a 3 meses aproximadamente. Esto depende de la empresa de envio y cuanto se demore la aduana.'),(2,'como se calcula el costo de envio','El costo depende del peso y la categoría del producto.'),(3,'que pasa si mi pedido se retrasa','Puede deberse a aduanas o transporte internacional.'),(4,'donde llegan los pedidos','Los pedidos llegan primero a una casilla en el país de origen y luego a Chile.'),(5,'como saber el estado de mi pedido','Debes ingresar el nombre del pedido en el sistema.');
/*!40000 ALTER TABLE `faq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedidos`
--

DROP TABLE IF EXISTS `pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos` (
  `id` varchar(20) NOT NULL,
  `nombre_producto` varchar(200) DEFAULT NULL,
  `estado` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidos`
--

LOCK TABLES `pedidos` WRITE;
/*!40000 ALTER TABLE `pedidos` DISABLE KEYS */;
INSERT INTO `pedidos` VALUES ('123456789','pedido 01: CH skz peluches (ex pedido 16)','viajando a Chile...'),('234567891','pedido 02: CH chobin (ex pedido 47)','viajando a Chile...'),('YT2541309007280','pedido 04: CH primer pedido en esnupitos','viajando a Chile...'),('YT2585514950371','pedido 03: Ch personal cami (ex pedido 52)','viajando a Chile...'),('YT7611358273792','pedido 05: CH cortisball ','viajando a Chile...');
/*!40000 ALTER TABLE `pedidos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-03 19:39:17
