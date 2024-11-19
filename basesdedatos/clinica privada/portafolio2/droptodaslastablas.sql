
use Basept1
go
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
IF OBJECT_ID(N'Medicamento', N'U') IS NOT NULL
BEGIN
    DROP TABLE Medicamento;
END;
GO

