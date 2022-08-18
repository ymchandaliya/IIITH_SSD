USE COMPANY;
select DEPENDENT.Essn,v.Dnumber,count(Relationship) from DEPENDENT where essn IN (select Mgr_ssn,v.Dnumber from DEPARTMENT,(select Dnumber,count(distinct Dlocation) as c from DEPT_LOCATIONS group by Dnumber having c>1) as v where DEPARTMENT.Dnumber=v.Dnumber) group by DEPENDENT.Essn,v.Dnumber;
#select DEPENDENT.Essn,count(Dependent_name) from DEPENDENT,x group by DEPENDENT.Essn having DEPENDENT.Essn=x.Mgr_ssn;
#select Mgr_ssn,Dnumber,count(Dependent_name) from DEPENDENT,(  ) as x group by DEPENDENT.Essn HAVING DEPENDENT.Essn=x.Mgr_ssn;
#select Mgr_ssn from DEPARTMENT where Dnumber
#select mgr_ssn from DEPARTMENT 