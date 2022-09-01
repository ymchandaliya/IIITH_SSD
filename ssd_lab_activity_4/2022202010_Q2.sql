USE CUSTOMER_DB
DELIMITER $$
DROP procedure if exists getNames;
CREATE PROCEDURE `getNames`(IN `city` varchar(100))
	BEGIN
		SELECT CUST_NAME from customer where WORKING_AREA=city;
	END$$

call getNames("Bangalore");