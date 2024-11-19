

create database portafolio4;
go

use portafolio4; 
go

CREATE SCHEMA Port4 AUTHORIZATION dbo;
go

-- Crear la tabla 'Pacientes' si no existe
if not exists (select * from sys.tables where [name] = N'Pacientes' and [schema_id] = SCHEMA_ID(N'Port4'))
begin
    create table Port4.Pacientes (
        N_carnet nvarchar(100) not null,
        Nombre nvarchar(100) not null,
        apellido_1 nvarchar(100) not null,
        apellido_2 nvarchar(100),
        telefono nvarchar(100) not null,
        correo nvarchar(100) not null,
        Sexo nvarchar(50) check (Sexo in ('Masculino', 'Femenino', 'Otro')) not null,
        grupo_Sanguineo nvarchar(50) check (grupo_Sanguineo in ('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-')),
        FechaNacimiento date not null,
        Direccion nvarchar(200),
        primary key (N_carnet)
    )
end;
go

-- Crear la tabla 'Padecimiento' si no existe
if not exists (select * from sys.tables where [name] = N'Padecimiento' and [schema_id] = SCHEMA_ID(N'Port4'))
begin
    create table Port4.Padecimiento (
        Paciente nvarchar(100) not null,
        Padecimiento nvarchar(100) not null primary key,
        tipo nvarchar(100),
        inicio_sintomas nvarchar(100),
        foreign key (Paciente) references Port4.Pacientes(N_carnet)
    )
end;
go

CREATE ROLE Rol1;
CREATE ROLE Rol2;
grant insert,delete, update on Port4.Pacientes to Rol1;
grant insert,delete, update on Port4.Padecimiento to Rol1;
grant connect to Rol1;
grant select on Port4.Pacientes to Rol2;
grant select on Port4.Padecimiento to Rol2;
grant connect to Rol2;

create login Rol1Log with password = '0000';
create user Rol1U for login Rol1Log;
alter role Rol1 add member Rol1U; 

create login Rol2Log with password = '0000';
create user Rol2U for login Rol2Log;
alter role Rol2 add member Rol2U; 


INSERT INTO Port4.Pacientes (
    N_carnet,
    Nombre,
    apellido_1,
    apellido_2,
    telefono,
    correo,
    Sexo,
    grupo_Sanguineo,
    FechaNacimiento,
    Direccion
) VALUES (
    '123456',              
    'Juan',                 
    'Pérez',              
    'López',               
    '123456789',            
    'juan.perez@email.com', 
    'Masculino',           
    'O+',                  
    '1990-05-15',         
    '123 Calle Principal' 
);
select * from Port4.Pacientes ;
