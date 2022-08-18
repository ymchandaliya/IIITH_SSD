USE COMPANY;
select Essn,count(Pno) from WORKS_ON group by Essn having Essn=(select Mgr_ssn from DEPARTMENT where Dnumber IN(select Dnum from PROJECT where Pname="ProductY"));