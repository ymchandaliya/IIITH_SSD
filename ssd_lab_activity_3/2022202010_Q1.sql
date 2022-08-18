USE COMPANY;
select Essn,sum(Hours) from WORKS_ON group by Essn having sum(Hours)<40;
#select * from temp;
#select Dno from EMPLOYEE where Ssn=(
#create view tempWork as 