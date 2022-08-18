USE COMPANY;
select Super_ssn,count(Ssn) from EMPLOYEE group by Super_ssn having Super_ssn=Ssn;