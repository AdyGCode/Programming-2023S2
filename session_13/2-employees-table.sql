# Table: employees
#
# Id	id	Big Integer		AI, PK	Primary key
# Given Name	given_name	Var Char	64		May be empty for people with ONE name only
# Family Name	family_name	Var Char	64	NN	Not null, Required
# Date of Birth	date_of_birth	Date		NN	Required in form YYYY-MM--DD
# Gender Identity	gender_identity	Character	1		May be empty
# Gross Salary	gross_salary	Big Integer		Default 0	Default to 0
# Supervisor ID	supervisor_id	Big integer			Has a default of 0.00
# Branch ID	branch_id	Big Integer			
# Created At	created_at	Timestamp		Default 2022-07-01	Default to 2022-07-01
# Updated At	updated_at	Timestamp			Nullable

drop table if exists employees;
create table employees(
	id bigint unsigned auto_increment primary key,
	given_name varchar(64),
	family_name varchar(64),
	date_of_birth date,
	gender_identity char(1),
	gross_salary bigint default(0),
	supervisor_id bigint unsigned default(0),
	branch_id bigint unsigned,
	created_at timestamp default('2022-07-01'),
	updated_at timestamp
);



insert into employees(
		id, given_name, family_name, date_of_birth, 
		gender_identity, gross_salary, supervisor_id, 
		branch_id, created_at, updated_at) 
values(
		100,	"David",	"Wallace",	"1967-11-17",	
	  "M",	25000,	null,	
	  1, now(), null);
	
select * from employees;

insert into employees(
		id, given_name, family_name, date_of_birth, 
		gender_identity, gross_salary, supervisor_id, 
		branch_id, created_at, updated_at) 
values
		(101,	'Jan',	'Levinson',	'1967-05-11',	'F',	110000,	100,	1, now(), null),
		(102,	'Michael',	'Scott',	'1964-03-15',	'M',	75000,	100,	2, now(), null),
		(103,	'Angela',	'Martin',	'1971-06-25',	'F',	63000,	102,	2, now(), null),
		(104,	'Kelly',	'Kapoor',	'1980-02-05',	'F',	55000,	102,	2, now(), null),
		(999, 'Jack', 'O''Reilly', '1970-01-01', 'O', 234000, 102, 2, now(), now()) ;
	  