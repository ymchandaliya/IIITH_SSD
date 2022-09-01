USE CUSTOMER_DB
DELIMITER $$
DROP procedure if exists getCustomerDetails;
CREATE PROCEDURE `getCustomerDetails`()
	BEGIN
		SELECT CUST_NAME, GRADE from customer where OPENING_AMT+RECEIVE_AMT>10000;
	END$$

call getCustomerDetails();