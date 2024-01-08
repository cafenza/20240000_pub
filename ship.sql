-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        11.2.2-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- user maria 생성
-- CREATE user maria@'%' IDENTIFIED BY '1234';
-- 
-- GRANT USAGE ON *.* TO maria@'%';
-- GRANT ALL PRIVILEGES ON python_db.* TO maria@'%';
-- FLUSH PRIVILEGES;	
-- 
-- python_db 데이터베이스 구조 내보내기
-- CREATE DATABASE IF NOT EXISTS `python_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
-- USE `python_db`;

-- 테이블 python_db.user_list 구조 내보내기
CREATE TABLE IF NOT EXISTS `user_list` (
--  `CODE` int(11) NOT NULL,
  `ID` varchar(100) NOT NULL,
  `PW` varchar(15) DEFAULT NULL,
  `DEPT` varchar(20) DEFAULT NULL,
  `TEL` varchar(20) DEFAULT NULL,
  `E_MAIL` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 python_db.user_list:~10 rows (대략적) 내보내기
INSERT INTO `user_list` (`ID`, `PW`, `DEPT`, `TEL`,`E_MAIL`) VALUES
	('KCC', '0000', '관리부', '010-1234-5671', 'kcc@kcc.co.kr'),
	('MADEIRA', '0000', '관리부', '010-1234-5672', 'madeira@madeira.co.kr'),
	('SMLINE', '0000', '관리부', '010-1234-5673', 'smline@smline.co.kr'),
	('SHI', '0000', '관리부', '010-1234-5674', 'shi@shi.co.kr');



-- 테이블 python_db.ship_list 구조 내보내기
CREATE TABLE IF NOT EXISTS `ship_list` (
  `CODE` int(11) NOT NULL,
  `NAME` varchar(200) NOT NULL,
  `OWNER` varchar(20) DEFAULT NULL,
  `TYPE` varchar(30) DEFAULT NULL,
  `LENGTH` int(11) DEFAULT NULL,
  `HEIGHT` int(11) DEFAULT NULL,
  `WIDTH` int(11) DEFAULT NULL,
  `WATERLINE` int(11) DEFAULT NULL,
  PRIMARY KEY (`CODE`),
  KEY `FK1` (`OWNER`),
  CONSTRAINT `FK1` FOREIGN KEY (`OWNER`) REFERENCES `user_list` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 python_db.ship_list:~24 rows (대략적) 내보내기
INSERT INTO `ship_list` (`CODE`, `NAME`, `OWNER`, `TYPE`, `LENGTH`,`HEIGHT`,`WIDTH`, `WATERLINE`) VALUES
	(1, 'Morning Prosperity', 'KCC', 'VehicleCarrier', '000','00','00','0'),
	(2, 'PASSAMA','MADEIRA','Bulk Carrier','000','00','00','0'),
	(3, 'MUMBAI','SMLINE','CNT','000','00','00','0'),
	(4, 'QINGDAO','SMLINE','CNT','000','00','00','0'),
	(5, 'TIANJIN','SMLINE','CNT','000','00','00','0'),
	(6, 'DrillShip','SHI','DrillShip','000','00','00','0'),
	(7, 'SN2307','SHI','LNG','000','00','00','0'),
	(8, 'SN2336','SHI','LNGC','000','00','00','0'),
	(9, 'SN2350','SHI','COT','000','00','00','0'),
	(10, 'SN2351','SHI','COT','000','00','00','0'),
	(11, 'SN2352','SHI','COT','000','00','00','0'),
	(12, 'SN2353','SHI','COT','000','00','00','0'),
	(13, 'SN2355','SHI','LNGC','000','00','00','0'),
	(14, 'SN2359','SHI','CNT','000','00','00','0'),
	(15, 'SN2360','SHI','CNT','000','00','00','0'),
	(16, 'SN2361','SHI','CNT','000','00','00','0');



/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
