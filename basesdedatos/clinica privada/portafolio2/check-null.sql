-- VERIFICA SI EXISTE LA BASE SINO LA CREA--
IF NOT EXISTS (SELECT [name] FROM sys.databases WHERE [name] = N'Basept1')
BEGIN
    CREATE DATABASE Basept1;
END;
GO

USE Basept1;
GO

-- Crear tablas portafolio --

IF OBJECT_ID(N'PersonalMedico', N'U') IS NULL
BEGIN
    CREATE TABLE PersonalMedico (
        Cedula int not null,
        Correo varchar(255)not null,
        Numero int not null,
        Nombre varchar(255)not null,
        Apaterno varchar(255)not null,
        Amaterno varchar(255)not null,
        Profesion varchar(255)not null,
        PRIMARY KEY (Cedula)
    );
END;

IF OBJECT_ID(N'Paciente', N'U') IS NULL
BEGIN
    CREATE TABLE Paciente (
        Nombre varchar(255)not null ,
        Apaterno varchar(255)not null,
        Amaterno varchar(255)not null,
        Carnet varchar(255)not null,
        Sexo char(1)CHECK (Sexo IN ('M', 'F'))not null,
        correo varchar(255)not null,
        Grupo_sanguineo varchar(255)CHECK (Grupo_sanguineo IN ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'))not null,
        cedula int CHECK (LEN(Cedula) = 9)not null,
        PRIMARY KEY (cedula)
    );
END;

IF OBJECT_ID(N'Cita', N'U') IS NULL
BEGIN
    CREATE TABLE Cita (
        cedulapaciente int not null,
        Motivo text not null,
        Fecha_hora datetime not null,
        Resultado text not null,
        profecionalcedula int not null,
        PRIMARY KEY (cedulapaciente, Fecha_hora, profecionalcedula),
        FOREIGN KEY (cedulapaciente) REFERENCES Paciente(cedula),
        FOREIGN KEY (profecionalcedula) REFERENCES PersonalMedico(Cedula)
    );
END;

IF OBJECT_ID(N'Tratamiento', N'U') IS NULL
BEGIN
    CREATE TABLE Tratamiento (
        cedula int not null,
        profecionalcedula int not null,
        Fecha_hora datetime not null,
        Tratamiento varchar(255) not null,
        PRIMARY KEY (cedula, Fecha_hora, profecionalcedula, Tratamiento),
        FOREIGN KEY (cedula, Fecha_hora, profecionalcedula) REFERENCES Cita(cedulapaciente, Fecha_hora, profecionalcedula)
    );
END;

IF OBJECT_ID(N'Padecimiento', N'U') IS NULL
BEGIN
    CREATE TABLE Padecimiento (
        cedulapaciente int not null,
        tipo varchar(255) not null,
        Padecimiento varchar(255) not null,
        sintomas varchar(255)not null,
        PRIMARY KEY (cedulapaciente, Padecimiento),
        FOREIGN KEY (cedulapaciente) REFERENCES Paciente(cedula)
    );
END;

IF OBJECT_ID(N'Afectacion', N'U') IS NULL
BEGIN
    CREATE TABLE Afectacion (
        cedulapaciente int not null,
        Afectacion varchar(255) not null,
        Padecimiento varchar(255) not null,
        gravedad varchar(255)not null,
        PRIMARY KEY (cedulapaciente, Padecimiento, Afectacion),
        FOREIGN KEY (cedulapaciente, Padecimiento) REFERENCES Padecimiento(cedulapaciente, Padecimiento)
    );
END;

IF OBJECT_ID(N'ResultadoCita', N'U') IS NULL
BEGIN
    CREATE TABLE ResultadoCita (
        cedulaPaciente int not null,
        cedulaProfecional int not null,
        fecha_hora datetime not null,
        Resultado varchar(255) not null,
        PRIMARY KEY (cedulaPaciente, cedulaProfecional, fecha_hora, Resultado),
        FOREIGN KEY (cedulaPaciente, fecha_hora, cedulaProfecional) REFERENCES Cita(cedulapaciente, Fecha_hora, profecionalcedula)
    );
END;

IF OBJECT_ID(N'Medicamento', N'U') IS NULL
BEGIN
    CREATE TABLE Medicamento (
        Nombre varchar(255) not null,
        ComponenteActivo varchar(255) not null,
        Patogeno varchar(255) not null,
        PRIMARY KEY (Nombre) 
       
    );
END;

IF OBJECT_ID(N'Medicamentocita', N'U') IS NULL
BEGIN
    CREATE TABLE Medicamentocita (
        cedulaPaciente int not null,
        cedulaProfecional int not null,
        fecha_hora datetime not null,
        medicamento varchar(255) not null,
        duracion varchar(255)CHECK (duracion>0)not null,
        PRIMARY KEY (cedulaPaciente, cedulaProfecional, fecha_hora, medicamento),
        FOREIGN KEY (cedulaPaciente, fecha_hora, cedulaProfecional) REFERENCES Cita(cedulapaciente, Fecha_hora, profecionalcedula),
		FOREIGN KEY (medicamento) REFERENCES Medicamento(Nombre)
		
    );
END;



IF OBJECT_ID(N'EfectoSecundario', N'U') IS NULL
BEGIN
    CREATE TABLE EfectoSecundario (
        Medicamento varchar(255) not null,
        Efecto varchar(255) not null,
        PRIMARY KEY (Medicamento, Efecto) ,
        FOREIGN KEY (Medicamento) REFERENCES Medicamento(Nombre)
    );
END;

IF OBJECT_ID(N'Procedimiento', N'U') IS NULL
BEGIN
    CREATE TABLE Procedimiento (
       cedulapaciente int not null,
        Motivo text not null,
        Fecha_hora datetime not null,
        Duracion text not null,
		epicrisis text,
        profecionalcedula int,
        PRIMARY KEY (cedulapaciente, Fecha_hora, profecionalcedula),
        FOREIGN KEY (cedulapaciente) REFERENCES Paciente(cedula),
        FOREIGN KEY (profecionalcedula) REFERENCES PersonalMedico(Cedula)
    );
END;

IF OBJECT_ID(N'MedicamentoProcedimiento', N'U') IS NULL
BEGIN
    CREATE TABLE MedicamentoProcedimiento (
       cedulapaciente int not null,
        Medicamento varchar(255) not null,
        Fecha_hora datetime not null,
        Duracion text,
		dosisis text ,
        profecionalcedula int not null,
        PRIMARY KEY (cedulapaciente, Fecha_hora, profecionalcedula,Medicamento),
    
        FOREIGN KEY (cedulapaciente, Fecha_hora, profecionalcedula) REFERENCES Procedimiento(cedulapaciente, Fecha_hora, profecionalcedula),
        FOREIGN KEY (Medicamento) REFERENCES Medicamento(Nombre)
		
    );
END;
-- Eliminar tabla MedicamentoProcedimiento --
IF OBJECT_ID(N'MedicamentoProcedimiento', N'U') IS NOT NULL
BEGIN
    DROP TABLE MedicamentoProcedimiento;
END;
GO

-- Eliminar tabla TratamientoProcedimiento --
IF OBJECT_ID(N'TratamientoProcedimiento', N'U') IS NOT NULL
BEGIN
    DROP TABLE TratamientoProcedimiento;
END;
GO

-- Eliminar tabla Procedimiento --
IF OBJECT_ID(N'Procedimiento', N'U') IS NOT NULL
BEGIN
    DROP TABLE Procedimiento;
END;
GO

-- Eliminar tabla EfectoSecundario --
IF OBJECT_ID(N'EfectoSecundario', N'U') IS NOT NULL
BEGIN
    DROP TABLE EfectoSecundario;
END;
GO

-- Eliminar tabla Medicamentocita --
IF OBJECT_ID(N'Medicamentocita', N'U') IS NOT NULL
BEGIN
    DROP TABLE Medicamentocita;
END;
GO

-- Eliminar tabla ResultadoCita --
IF OBJECT_ID(N'ResultadoCita', N'U') IS NOT NULL
BEGIN
    DROP TABLE ResultadoCita;
END;
GO

-- Eliminar tabla Afectacion --
IF OBJECT_ID(N'Afectacion', N'U') IS NOT NULL
BEGIN
    DROP TABLE Afectacion;
END;
GO

-- Eliminar tabla Tratamiento --
IF OBJECT_ID(N'Tratamiento', N'U') IS NOT NULL
BEGIN
    DROP TABLE Tratamiento;
END;
GO

-- Eliminar tabla Cita --
IF OBJECT_ID(N'Cita', N'U') IS NOT NULL
BEGIN
    DROP TABLE Cita;
END;
GO

-- Eliminar tabla Padecimiento --
IF OBJECT_ID(N'Padecimiento', N'U') IS NOT NULL
BEGIN
    DROP TABLE Padecimiento;
END;
GO

-- Eliminar tabla Paciente --
IF OBJECT_ID(N'Paciente', N'U') IS NOT NULL
BEGIN
    DROP TABLE Paciente;
END;
GO

-- Eliminar tabla PersonalMedico --
IF OBJECT_ID(N'PersonalMedico', N'U') IS NOT NULL
BEGIN
    DROP TABLE PersonalMedico;
END;
GO
