
-- VGERIFICA SI EXISTE LA BASE SINO LA CREA--
IF NOT EXISTS (SELECT [name] FROM sys.databases WHERE [name] = N'Basept1')
BEGIN
    CREATE DATABASE Basept1;
END;
GO

USE Basept1;
GO
--tablas portafolio--

IF OBJECT_ID(N'PersonalMedico', N'U') IS NULL
BEGIN
    CREATE TABLE PersonalMedico (
        Especialidad varchar(255),
        Experiencia varchar(255),
        Correo varchar(255),
        Numero int,
        Nombre varchar(255),
        Apaterno varchar(255),
        Amaterno varchar(255)
    );
END;

IF OBJECT_ID(N'Paciente', N'U') IS NULL
BEGIN
	CREATE TABLE Paciente (
		Nombre varchar(255),
		Apaterno varchar(255),
		Amaterno varchar(255),
		Carnet varchar(255),
		Sexo char(1)
	);
END;
IF OBJECT_ID(N'Tratamiento', N'U') IS NULL
BEGIN
	CREATE TABLE Tratamiento (
		NombreMedicamento varchar(255),
		Dosis varchar(50),
		Tipo varchar(50),
		EfectosSecundarios text, --El text guarda cualquier cantidad de cadenas--
		ObjetivoTratamiento varchar(255),
		Duracion int
	);
END;

IF OBJECT_ID(N'Cita', N'U') IS NULL
BEGIN
	CREATE TABLE Cita (
		Motivo text,
		Fecha date,
		Resultado text
	);
END;

IF OBJECT_ID(N'HistorialMedico', N'U') IS NULL
BEGIN
CREATE TABLE HistorialMedico (
    --vacio porque pidio no meter las pk--
    --en mi mente es una tabla intermedia--
    Paciente varchar(255) --y este da error si no escribo nada
);
END;
