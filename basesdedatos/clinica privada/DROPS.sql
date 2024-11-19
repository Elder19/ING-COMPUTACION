-- Eliminar la tabla 'Tratamiento_Procedimiento' si existe
if exists (select * from sys.tables where [name] = N'Tratamiento_Procedimiento' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    drop table dbo.Tratamiento_Procedimiento
end;

-- Eliminar la tabla 'Medicamento_Procedimiento' si existe
if exists (select * from sys.tables where [name] = N'Medicamento_Procedimiento' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    drop table dbo.Medicamento_Procedimiento
end;

-- Eliminar la tabla 'Medicamento_Cita' si existe
if exists (select * from sys.tables where [name] = N'Medicamento_Cita' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    drop table dbo.Medicamento_Cita
end;

-- Eliminar la tabla 'tratamientos_Cita' si existe
if exists (select * from sys.tables where [name] = N'tratamientos_Cita' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    drop table dbo.tratamientos_Cita
end;

-- Eliminar la tabla 'Resultado_Cita' si existe
if exists (select * from sys.tables where [name] = N'Resultado_Cita' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    drop table dbo.Resultado_Cita
end;

-- Eliminar la tabla 'Efectos_Secundario' si existe
if exists (select * from sys.tables where [name] = N'Efectos_Secundario' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    drop table dbo.Efectos_Secundario
end;

-- Eliminar la tabla 'Medicamentos' si existe
if exists (select * from sys.tables where [name] = N'Medicamentos' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    drop table dbo.Medicamentos
end;

-- Eliminar la tabla 'Cita' si existe
if exists (select * from sys.tables where [name] = N'Cita' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    drop table dbo.Cita
end;


-- Eliminar la tabla 'Afectacion_Padecimiento' si existe
if exists (select * from sys.tables where [name] = N'Afectacion_Padecimiento' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    drop table dbo.Afectacion_Padecimiento
end;


-- Eliminar la tabla 'Pacientes' si existe
if exists (select * from sys.tables where [name] = N'Pacientes' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    drop table dbo.Pacientes
end;

-- Eliminar la tabla 'Procedimiento' si existe
if exists (select * from sys.tables where [name] = N'Procedimiento' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    drop table dbo.Procedimiento
end;

-- Eliminar la tabla 'Personal_Medico' si existe
if exists (select * from sys.tables where [name] = N'Personal_Medico' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    drop table dbo.Personal_Medico
end;
-- Eliminar la tabla 'Padecimiento' si existe
if exists (select * from sys.tables where [name] = N'Padecimiento' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    drop table dbo.Padecimiento
end;
if exists (select * from sys.tables where [name] = N'PacienteFrecuente' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    drop table dbo.PacienteFrecuente
end;
