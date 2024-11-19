-- VERIFICA SI EXISTE LA BASE SINO LA CREA --
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
        profecionalcedula int CHECK (LEN(profecionalcedula) = 9) NOT NULL,
        Correo varchar(255) NOT NULL,
        Numero int NOT NULL,
        Nombre varchar(255) NOT NULL,
        Apaterno varchar(255) NOT NULL,
        Amaterno varchar(255) NOT NULL,
        Profesion varchar(255) NOT NULL,
        PRIMARY KEY (profecionalcedula)
    );
END;

IF OBJECT_ID(N'Paciente', N'U') IS NULL
BEGIN
    CREATE TABLE Paciente (
        Nombre varchar(255) NOT NULL,
        Apaterno varchar(255) NOT NULL,
        Amaterno varchar(255) NOT NULL,
        Carnet varchar(255) NOT NULL,
        Sexo char(1) CHECK (Sexo IN ('M', 'F')) NOT NULL,
        correo varchar(255) NOT NULL,
        Grupo_sanguineo varchar(255) CHECK (Grupo_sanguineo IN ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')) NOT NULL,
        cedula int CHECK (LEN(Cedula) = 9) NOT NULL,
        PRIMARY KEY (cedula)
    );
END;

IF OBJECT_ID(N'Cita', N'U') IS NULL
BEGIN
    CREATE TABLE Cita (
        cedulapaciente int NOT NULL,
        Motivo text NOT NULL,
        Fecha_hora datetime NOT NULL,
        Resultado text NOT NULL,
        profecionalcedula int NOT NULL,
        PRIMARY KEY (cedulapaciente, Fecha_hora, profecionalcedula),
        FOREIGN KEY (cedulapaciente) REFERENCES Paciente(cedula),
        FOREIGN KEY (profecionalcedula) REFERENCES PersonalMedico(profecionalcedula)
    );
END;

IF OBJECT_ID(N'Tratamiento', N'U') IS NULL
BEGIN
    CREATE TABLE Tratamiento (
        cedula int NOT NULL,
        profecionalcedula int NOT NULL,
        Fecha_hora datetime NOT NULL,
        Tratamiento varchar(255) NOT NULL,
        PRIMARY KEY (cedula, Fecha_hora, profecionalcedula, Tratamiento),
        FOREIGN KEY (cedula, Fecha_hora, profecionalcedula) REFERENCES Cita(cedulapaciente, Fecha_hora, profecionalcedula)
    );
END;

IF OBJECT_ID(N'Padecimiento', N'U') IS NULL
BEGIN
    CREATE TABLE Padecimiento (
        cedulapaciente int NOT NULL,
        tipo varchar(255) NOT NULL,
        Padecimiento varchar(255) NOT NULL,
        sintomas varchar(255) NOT NULL,
        PRIMARY KEY (cedulapaciente, Padecimiento),
        FOREIGN KEY (cedulapaciente) REFERENCES Paciente(cedula)
    );
END;

IF OBJECT_ID(N'Afectacion', N'U') IS NULL
BEGIN
    CREATE TABLE Afectacion (
        cedulapaciente int NOT NULL,
        Afectacion varchar(255) NOT NULL,
        Padecimiento varchar(255) NOT NULL,
        gravedad varchar(255) NOT NULL,
        PRIMARY KEY (cedulapaciente, Padecimiento, Afectacion),
        FOREIGN KEY (cedulapaciente, Padecimiento) REFERENCES Padecimiento(cedulapaciente, Padecimiento)
    );
END;

IF OBJECT_ID(N'ResultadoCita', N'U') IS NULL
BEGIN
    CREATE TABLE ResultadoCita (
        cedulaPaciente int NOT NULL,
        cedulaProfecional int NOT NULL,
        fecha_hora datetime NOT NULL,
        Resultado varchar(255) NOT NULL,
        PRIMARY KEY (cedulaPaciente, cedulaProfecional, fecha_hora, Resultado),
        FOREIGN KEY (cedulaPaciente, fecha_hora, cedulaProfecional) REFERENCES Cita(cedulapaciente, Fecha_hora, profecionalcedula)
    );
END;

IF OBJECT_ID(N'Medicamento', N'U') IS NULL
BEGIN
    CREATE TABLE Medicamento (
        Nombre varchar(255) NOT NULL,
        ComponenteActivo varchar(255) NOT NULL,
        Patogeno varchar(255) NOT NULL,
        PRIMARY KEY (Nombre)
    );
END;

IF OBJECT_ID(N'Medicamentocita', N'U') IS NULL
BEGIN
    CREATE TABLE Medicamentocita (
        cedulaPaciente int NOT NULL,
        cedulaProfecional int NOT NULL,
        fecha_hora datetime NOT NULL,
        medicamento varchar(255) NOT NULL,
        duracion varchar(255) NOT NULL,
        PRIMARY KEY (cedulaProfecional, fecha_hora, medicamento),
        FOREIGN KEY (cedulaPaciente, fecha_hora, cedulaProfecional) REFERENCES Cita(cedulapaciente, Fecha_hora, profecionalcedula),
        FOREIGN KEY (medicamento) REFERENCES Medicamento(Nombre)
    );
END;

IF OBJECT_ID(N'EfectoSecundario', N'U') IS NULL
BEGIN
    CREATE TABLE EfectoSecundario (
        Medicamento varchar(255) NOT NULL,
        Efecto varchar(255) NOT NULL,
        PRIMARY KEY (Medicamento, Efecto),
        FOREIGN KEY (Medicamento) REFERENCES Medicamento(Nombre)
    );
END;

IF OBJECT_ID(N'Procedimiento', N'U') IS NULL
BEGIN
    CREATE TABLE Procedimiento (
        cedulapaciente int NOT NULL,
        Motivo text NOT NULL,
        Fecha_hora datetime NOT NULL,
        Duracion decimal(5, 2) NOT NULL, 
        epicrisis text,
        profecionalcedula int,
        PRIMARY KEY (cedulapaciente, Fecha_hora, profecionalcedula),
        FOREIGN KEY (cedulapaciente) REFERENCES Paciente(cedula),
        FOREIGN KEY (profecionalcedula) REFERENCES PersonalMedico(profecionalcedula)
    );
END;


IF OBJECT_ID(N'MedicamentoProcedimiento', N'U') IS NULL
BEGIN
    CREATE TABLE MedicamentoProcedimiento (
        cedulapaciente int NOT NULL,
        Medicamento varchar(255) NOT NULL,
        Fecha_hora datetime NOT NULL,
        Duracion text,
        dosisis text,
        profecionalcedula int NOT NULL,
        PRIMARY KEY (cedulapaciente, Fecha_hora, profecionalcedula, Medicamento),
        FOREIGN KEY (cedulapaciente, Fecha_hora, profecionalcedula) REFERENCES Procedimiento(cedulapaciente, Fecha_hora, profecionalcedula),
        FOREIGN KEY (Medicamento) REFERENCES Medicamento(Nombre)
    );
END;

