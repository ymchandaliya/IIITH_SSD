USE CUSTOMER_DB;

DROP table if exists tempData;
create table tempData(
	cname varchar(50), city varchar(60), country varchar(50), cgrade varchar(60)
);
DELIMITER $$
DROP procedure if exists getCustDetails;
CREATE PROCEDURE `getCustDetails`()
	BEGIN
        declare done INT default 0;
		DECLARE cname,city,country,cgrade varchar (50);
		DECLARE getDetails cursor for select CUST_NAME, CUST_CITY, CUST_COUNTRY, GRADE from customer where AGENT_CODE like 'A00%';
		DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
        
        OPEN getDetails;
        comeHere: LOOP
        FETCH getDetails into cname, city, country, cgrade;
        IF done = 1	
        then leave comeHere;
        end if;
        insert into tempData values(cname, city, country, cgrade);

        end loop;
        close getDetails;
	END$$
DELIMITER ;

call getCustDetails;
select * from tempData;
