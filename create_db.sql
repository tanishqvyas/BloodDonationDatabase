SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";



--
-- Table Site
--

CREATE TABLE `Site`(
  `sid` int(50) NOT NULL PRIMARY KEY,
  `sname` varchar(50) NOT NULL,
  `saddr` varchar(50) NOT NULL
);


--
-- Table Hospital
--

CREATE TABLE `Hospital` (
  `hid` int(50) NOT NULL PRIMARY KEY,
  `hname` varchar(50) NOT NULL,
  `haddr` varchar(100) NOT NULL,
  `hcontact` varchar(20) NOT NULL
);


--
-- Table Organization
--

CREATE TABLE `Organization` (
  `oid` int(50) NOT NULL PRIMARY KEY,
  `oname` varchar(50) NOT NULL,
  `oaddr` varchar(100) NOT NULL,
  `ocontact` varchar(20) NOT NULL
);


--
-- Table Donor
--

CREATE TABLE `Donor`(
  `did` int(50) NOT NULL PRIMARY KEY,
  `oid` int(50) NOT NULL,
  `dname` varchar(50) NOT NULL,
  `dblood` varchar(50) NOT NULL,
  `dage` int(50) NOT NULL,
  `dsex` char(10) NOT NULL,
  `dmail` varchar(50) NOT NULL UNIQUE,
  `dcount` int(40) NOT NULL,
  CONSTRAINT FK_Organization FOREIGN KEY (`oid`) REFERENCES `Organization`(`oid`),
  CONSTRAINT CHK_PersonAge CHECK (`dage`>=17 and `dage` < 80)
);


--
-- Table Volunteer  : Is a weak entity 
-- 

CREATE TABLE `Volunteer`(
  `vid` int(50) NOT NULL,
  `hid` int(50) NOT NULL,
  `vname` varchar(50) NOT NULL,
  PRIMARY KEY(`vid`, `hid`),
  CONSTRAINT FK_Hospital FOREIGN KEY (`hid`) REFERENCES `Hospital`(`hid`)

);



--
-- Table Donation
--

CREATE TABLE `Donation`(
  `did` int(50) NOT NULL,
  `vid` int(50) NOT NULL,
  `hid` int(50) NOT NULL,  
  `sid` int(50) NOT NULL,
  `date` DATE NOT NULL, -- YYYY-MM-DD format
  PRIMARY KEY(`did`, `date`),
  CONSTRAINT FK_Donor FOREIGN KEY (`did`) REFERENCES `Donor`(`did`),
  CONSTRAINT FK_VolunteerPresence FOREIGN KEY (`vid`,`hid`) REFERENCES `Volunteer`(`vid`,`hid`),
  CONSTRAINT FK_Site FOREIGN KEY (`sid`) REFERENCES `Site`(`sid`),
  CONSTRAINT CHK_Date CHECK (`date` >= CURDATE())
);


-- Triggers

-- Make dcount 0 if anything else entered


DELIMITER $$

CREATE TRIGGER `Donation_Count`
BEFORE INSERT
ON `Donor` FOR EACH ROW
BEGIN
  SET NEW.dcount = 0;
END$$

DELIMITER ;


-- Update the dcount

DELIMITER $$


CREATE trigger `Donation_Count_Incrementer`
AFTER INSERT
ON `Donation` FOR EACH ROW
BEGIN
  UPDATE `Donor` SET `dcount` = `dcount` + 1 WHERE `did` = NEW.did;
END$$

DELIMITER ;





COMMIT;