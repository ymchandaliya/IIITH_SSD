USE CUSTOMER_DB;
DELIMITER $$
DROP procedure if exists addNumbers;
create procedure `addNumbers`(IN `num1` int, IN `num2` int, OUT `ans` int)

	BEGIN
     -- declare 
		set ans = num1 + num2;
        #print @ans
	END$$
    
-- declare @ans number
Call addNumbers(15,7,@ans);
select @ans;
 