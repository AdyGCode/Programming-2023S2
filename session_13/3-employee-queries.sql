select * from employees;

select given_name, family_name from employees;

select * from employees order by family_name, given_name;

select * from employees order by gross_salary;

select * from employees order by gross_salary desc;

select sum(gross_salary) from employees;

select sum(gross_salary) as "total salaries" from employees;

select e.given_name from employees as e;
select e.given_name from employees e;

select * from employees order by gross_salary limit 3;

update employees set gross_salary = gross_salary+1;
select * from employees;

update employees set gross_salary = gross_salary + gross_salary * 10 / 100 where gross_salary < 100000;
select * from employees;
update employees set gross_salary = gross_salary + gross_salary * 25 / 100 where id=999;
select * from employees;

select avg(gross_salary) as "mean salaries" from employees;

select * from employees where family_name = "Scott";
select * from employees where family_name like "W%";
select * from employees where family_name like "%or";
select * from employees where family_name like "%la%";

select * from employees where family_name like "K%" and given_name like "K%";

select * from employees where family_name like "K%" or family_name like "R%";

select * from employees where family_name like "T%" or given_name like "%A%";

select * from employees where gender_identity in ("M","O");

select * from employees where family_name like "%a%" xor given_name like "%a%";

# Write & run a SQL query to find all female employees born after 1969 or who has salary greater than 8000.
select * from employees where gender_identity = "F" and (year(date_of_birth) > 1969 or gross_salary > 8000);

# > = --> >= < = --> <=
select * from employees where Year(date_of_birth)>= 1960 and Year(date_of_birth) <= 1969;
select * from employees where Year(date_of_birth) between 1960 and 1969;

select * from employees where month(date_of_birth) = 11;

select * from employees where day(date_of_birth) = 15;

select given_name, monthname(date_of_birth) from employees;
