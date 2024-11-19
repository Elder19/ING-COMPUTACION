use Basept1
go 


IF OBJECT_ID(N'Tratamiento', N'U') IS NOT NULL
BEGIN
    DROP TABLE Tratamiento;
END;
GO

IF OBJECT_ID(N'ResultadoCita', N'U') IS NOT NULL
BEGIN
    DROP TABLE ResultadoCita;
END;
GO

IF OBJECT_ID(N'EfectoSecundario', N'U') IS NOT NULL
BEGIN
    DROP TABLE EfectoSecundario;
END;
GO


ALTER TABLE Paciente
ADD FechaNacimiento DATE;

ALTER TABLE Procedimiento
DROP COLUMN epicrisis;


ALTER TABLE PersonalMedico
ALTER COLUMN Correo VARCHAR(500) NULL;
