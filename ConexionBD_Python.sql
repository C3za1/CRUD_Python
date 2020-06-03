create database ConexionBD_Python;

use ConexionBD_Python;

create table persona
(
id int primary key identity(1,1),
nombre nvarchar (50) not null,
pais nvarchar (50) not null,
);

insert into persona values('cesar','Mexico')
insert into persona values('mayra','Mexico')
insert into persona values('Ale','USA')
select * from persona



USE master ;  
GO  
DROP DATABASE ConexionBD_Python ;  
GO  
