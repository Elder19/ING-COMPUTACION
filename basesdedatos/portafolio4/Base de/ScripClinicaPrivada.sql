-- Verificar si la base de datos 'Clinica_Privada' existe, si no, crearla
if not exists (select [name] from sys.databases where [name] = N'Clinica_Privada')
begin
    create database Clinica_Privada
end;
use Clinica_Privada;
-- Crear la tabla 'Pacientes' si no existe
if not exists (select * from sys.tables where [name] = N'Pacientes' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    create table dbo.Pacientes (
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
-- Crear la tabla 'PacienteFrecuente' si no existe
if not exists (select * from sys.tables where [name] = N'PacienteFrecuente' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    create table dbo.PacienteFrecuente (
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

-- Crear la tabla 'Padecimiento' si no existe
if not exists (select * from sys.tables where [name] = N'Padecimiento' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    create table dbo.Padecimiento (
        Paciente nvarchar(100) not null,
        Padecimiento nvarchar(100) not null primary key,
        tipo nvarchar(100),
        inicio_sintomas nvarchar(100),
        foreign key (Paciente) references Pacientes(N_carnet)
    )
end;

-- Crear la tabla 'Afectacion_Padecimiento' si no existe
if not exists (select * from sys.tables where [name] = N'Afectacion_Padecimiento' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    create table dbo.Afectacion_Padecimiento (
        Padecimiento nvarchar(100) not null,
        afectacion nvarchar(100) not null,
        gravedad nvarchar(100) check (gravedad in ('Baja', 'Media', 'Alta')) not null,
        foreign key (Padecimiento) references Padecimiento(Padecimiento)
    )
end;

-- Crear la tabla 'Personal_Medico' si no existe
if not exists (select * from sys.tables where [name] = N'Personal_Medico' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    create table dbo.Personal_Medico (
        N_cedula nvarchar(100) not null,
        Nombre nvarchar(100) not null,
        apellido_1 nvarchar(100) not null,
        apellido_2 nvarchar(100),
        telefono nvarchar(100) not null,
        correo nvarchar(100) not null,
        profesion nvarchar(50),
        especialidad nvarchar(50),
        primary key (N_cedula)
    )
end;

-- Crear la tabla 'Cita' si no existe
if not exists (select * from sys.tables where [name] = N'Cita' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    create table dbo.Cita (
        IdCita int identity(1,1) primary key,
        Paciente nvarchar(100) not null,
        profesional nvarchar(100) not null,
        fecha date not null,
        motivo nvarchar(100) not null,
        Duracion time not null,
        Resultados nvarchar(200),
        foreign key (Paciente) references Pacientes(N_carnet),
        foreign key (profesional) references Personal_Medico(N_cedula) 
    )
end;
ALTER TABLE dbo.Cita
ADD Activo nvarchar(10) DEFAULT 'activo' CHECK (Activo IN ('activo', 'inactivo'));
-- Crear la tabla 'Medicamentos' si no existe
if not exists (select * from sys.tables where [name] = N'Medicamentos' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    create table dbo.Medicamentos (
        nombre nvarchar(100) not null,
        patogeno nvarchar(100),
        primary key (nombre)
    )
end;

-- Crear la tabla 'Efectos_Secundario' si no existe
if not exists (select * from sys.tables where [name] = N'Efectos_Secundario' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    create table dbo.Efectos_Secundario (
        medicamento nvarchar(100) not null,
        efecto nvarchar(100) not null,
        primary key (medicamento),
        foreign key (medicamento) references Medicamentos(nombre)
    )
end;

-- Crear la tabla 'Resultado_Cita' si no existe
if not exists (select * from sys.tables where [name] = N'Resultado_Cita' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    create table dbo.Resultado_Cita (
        IdCita int not null, 
        resultado nvarchar(200) not null,
        foreign key (IdCita) references Cita(IdCita)
    )
end;


if not exists (select * from sys.tables where [name] = N'tratamientos_Cita' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    create table dbo.tratamientos_Cita (
        IdCita int not null, 
        tratamiento nvarchar(200) not null,
        foreign key (IdCita) references Cita(IdCita)
    )
end;

if not exists (select * from sys.tables where [name] = N'Medicamento_Cita' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    create table dbo.Medicamento_Cita (
        IdCita int not null,
        medicamentos nvarchar(100) not null,
        duracion time not null,
        primary key (IdCita), 
        foreign key (IdCita) references Cita(IdCita),
        foreign key (medicamentos) references Medicamentos(nombre)
    )
end;
-- Crear la tabla 'Procedimiento' si no existe
if not exists (select * from sys.tables where [name] = N'Procedimiento' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    create table dbo.Procedimiento (
        IdProcedimiento int identity(1,1) not null, 
        N_carnet nvarchar(100) not null, 
        N_cedula nvarchar(100) not null, 
        fecha date not null,
        Duracion time not null,
        epicrisis nvarchar(200) not null,
        primary key (IdProcedimiento), 
        foreign key (N_carnet) references Pacientes(N_carnet),
        foreign key (N_cedula) references Personal_Medico(N_cedula)
    )
end;

-- Crear la tabla 'Tratamiento_Procedimiento' si no existe
if not exists (select * from sys.tables where [name] = N'Tratamiento_Procedimiento' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    create table dbo.Tratamiento_Procedimiento (
        IdTratamiento int identity(1,1) not null, 
        IdProcedimiento int not null, 
        tratamiento nvarchar(100) not null,
        primary key (IdTratamiento), 
        foreign key (IdProcedimiento) references Procedimiento(IdProcedimiento)
    )
end;

-- Crear la tabla 'Medicamento_Procedimiento' si no existe
if not exists (select * from sys.tables where [name] = N'Medicamento_Procedimiento' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    create table dbo.Medicamento_Procedimiento (
        IdMedicamento int identity(1,1) not null, 
        IdProcedimiento int not null, 
        medicamentos nvarchar(100) not null,
        duracion time not null,
        primary key (IdMedicamento), 
        foreign key (IdProcedimiento) references Procedimiento(IdProcedimiento),
        foreign key (medicamentos) references Medicamentos(nombre)
    )
end;
if not exists (select * from sys.tables where [name] = N'PacientesVIP' and [schema_id] = SCHEMA_ID(N'dbo'))
begin
    create table dbo.PacientesVIP (
        N_carnet nvarchar(100) not null,
        Nombre nvarchar(100) not null,
        apellido_1 nvarchar(100) not null,
        apellido_2 nvarchar(100),
        telefono nvarchar(100) not null,
        correo nvarchar(100) not null,
        Sexo nvarchar(50) not null,
        grupo_Sanguineo nvarchar(50),
        FechaNacimiento date not null,
        Direccion nvarchar(200),
        primary key (N_carnet)
    )
end;



INSERT INTO dbo.Pacientes (N_carnet, Nombre, apellido_1, apellido_2, telefono, correo, Sexo, grupo_Sanguineo, FechaNacimiento, Direccion)
VALUES 
('C001', 'Juan', 'Pérez', 'González', '123456789', 'juan.perez@email.com', 'Masculino', 'O+', '1990-01-15', 'Calle 123, Ciudad'),
('C002', 'María', 'López', 'Hernández', '987654321', 'maria.lopez@email.com', 'Femenino', 'A+', '1985-03-22', 'Avenida 456, Ciudad'),
('C003', 'Luis', 'García', 'Martínez', '456789123', 'luis.garcia@email.com', 'Masculino', 'B+', '2000-07-10', 'Boulevard 789, Ciudad'),
('C004', 'Ana', 'Torres', 'Sánchez', '321654987', 'ana.torres@email.com', 'Femenino', 'AB+', '1995-12-05', 'Plaza 321, Ciudad'),
('C005', 'Ricardo', 'Jiménez', 'Pineda', '123123123', 'ricardo.jimenez@email.com', 'Masculino', 'O-', '1982-08-20', 'Calle 202, Ciudad'),
('C006', 'Verónica', 'Cruz', 'Salazar', '321321321', 'veronica.cruz@email.com', 'Femenino', 'AB+', '1993-12-11', 'Avenida 303, Ciudad'),
('C007', 'Andrés', 'Morales', 'Pérez', '456456456', 'andres.morales@email.com', 'Masculino', 'B-', '1979-06-30', 'Boulevard 404, Ciudad'),
('C008', 'Gabriela', 'Fernández', 'Díaz', '654654654', 'gabriela.fernandez@email.com', 'Femenino', 'A+', '1995-04-14', 'Plaza 505, Ciudad');

INSERT INTO dbo.PacienteFrecuente (N_carnet, Nombre, apellido_1, apellido_2, telefono, correo, Sexo, grupo_Sanguineo, FechaNacimiento, Direccion)
VALUES 
('C0011', 'Juan', 'Pérez', 'González', '123456789', 'juan.perez@email.com', 'Masculino', 'O+', '1990-01-15', 'Calle 123, Ciudad'),
('C0020', 'María', 'López', 'Hernández', '987654321', 'maria.lopez@email.com', 'Femenino', 'A+', '1985-03-22', 'Avenida 456, Ciudad'),
('C0030', 'Luis', 'García', 'Martínez', '456789123', 'luis.garcia@email.com', 'Masculino', 'B+', '2000-07-10', 'Boulevard 789, Ciudad'),
('C0040', 'Ana', 'Torres', 'Sánchez', '321654987', 'ana.torres@email.com', 'Femenino', 'AB+', '1995-12-05', 'Plaza 321, Ciudad'),
('C0050', 'Ricardo', 'Jiménez', 'Pineda', '123123123', 'ricardo.jimenez@email.com', 'Masculino', 'O-', '1982-08-20', 'Calle 202, Ciudad'),
('C0060', 'Verónica', 'Cruz', 'Salazar', '321321321', 'veronica.cruz@email.com', 'Femenino', 'AB+', '1993-12-11', 'Avenida 303, Ciudad'),
('C0070', 'Andrés', 'Morales', 'Pérez', '456456456', 'andres.morales@email.com', 'Masculino', 'B-', '1979-06-30', 'Boulevard 404, Ciudad'),
('C0080', 'Gabriela', 'Fernández', 'Díaz', '654654654', 'gabriela.fernandez@email.com', 'Femenino', 'A+', '1995-04-14', 'Plaza 505, Ciudad'),
('C0090', 'Fernando', 'Ramírez', 'García', '789789789', 'fernando.ramirez@email.com', 'Masculino', 'O+', '1988-11-01', 'Calle 606, Ciudad'),
('C0100', 'Lucía', 'Torres', 'Martínez', '321654987', 'lucia.torres@email.com', 'Femenino', 'AB-', '1990-05-20', 'Avenida 707, Ciudad'),
('C0110', 'Carlos', 'Vega', 'López', '987654321', 'carlos.vega@email.com', 'Masculino', 'B+', '1982-09-15', 'Plaza 808, Ciudad');

-- Inserciones corregidas en la tabla Padecimiento
INSERT INTO dbo.Padecimiento (Paciente, Padecimiento, tipo, inicio_sintomas)
VALUES 
('C001', 'Diabetes', 'Crónico', '2021-01-10'),
('C002', 'Hipertensión', 'Crónico', '2020-05-20'),
('C003', 'Asma', 'Agudo', '2022-06-15'),
('C004', 'Alérgico', 'Agudo', '2023-03-22'),
('C005', 'Cáncer', 'Crónico', '2022-02-25'),
('C006', 'Migraña', 'Agudo', '2023-09-12'),
('C007', 'Artritis', 'Crónico', '2020-03-18'),
('C008', 'Eczema', 'Agudo', '2024-05-20');

-- Inserciones en la tabla Afectacion_Padecimiento
INSERT INTO dbo.Afectacion_Padecimiento (Padecimiento, afectacion, gravedad)
VALUES 
('Diabetes', 'Fatiga constante', 'Alta'),
('Hipertensión', 'Dolor de cabeza', 'Media'),
('Asma', 'Dificultad para respirar', 'Alta'),
('Alérgico', 'Estornudos frecuentes', 'Baja'),
('Cáncer', 'Pérdida de peso', 'Alta'),
('Migraña', 'Dolor intenso de cabeza', 'Alta'),
('Artritis', 'Dolor en las articulaciones', 'Media'),
('Eczema', 'Irritación en la piel', 'Baja');

-- Inserciones en la tabla Personal_Medico
INSERT INTO dbo.Personal_Medico (N_cedula, Nombre, apellido_1, apellido_2, telefono, correo, profesion, especialidad)
VALUES 
('P001', 'Dr. Carlos', 'Mendoza', 'López', '555111222', 'carlos.mendoza@email.com', 'Médico', 'Cardiología'),
('P002', 'Dra. Laura', 'Ramírez', 'Sánchez', '555222333', 'laura.ramirez@email.com', 'Médico', 'Dermatología'),
('P003', 'Dr. Javier', 'Cifuentes', 'González', '555333444', 'javier.cifuentes@email.com', 'Médico', 'Pediatría'),
('P004', 'Dra. Ana', 'Martínez', 'Cruz', '555444555', 'ana.martinez@email.com', 'Médico', 'Psiquiatría'),
('P005', 'Dra. Carolina', 'Acuña', 'Torres', '555111222', 'carolina.acuna@email.com', 'Médico', 'Pediatría'),
('P006', 'Dr. Fernando', 'Rojas', 'Martín', '555222333', 'fernando.rojas@email.com', 'Médico', 'Ginecología'),
('P007', 'Dra. Patricia', 'Peña', 'Morales', '555333444', 'patricia.pena@email.com', 'Médico', 'Psicología'),
('P008', 'Dr. Alberto', 'Salas', 'González', '555444555', 'alberto.salas@email.com', 'Médico', 'Traumatología');

-- Inserciones en la tabla Cita
INSERT INTO dbo.Cita (Paciente, profesional, fecha, motivo, Duracion, Resultados)
VALUES 
('C001', 'P001', '2024-10-15', 'Chequeo general', '01:00:00', NULL),
('C002', 'P002', '2024-10-18', 'Consulta de piel', '00:45:00', NULL),
('C003', 'P003', '2024-10-20', 'Chequeo pediátrico', '01:30:00', NULL),
('C004', 'P004', '2024-10-22', 'Consulta psicológica', '01:00:00', NULL),
('C005', 'P005', '2024-11-10', 'Chequeo de rutina', '01:00:00', NULL),
('C006', 'P006', '2024-11-15', 'Consulta ginecológica', '01:00:00', NULL),
('C007', 'P007', '2024-11-20', 'Consulta psicológica', '01:00:00', NULL),
('C008', 'P008', '2024-12-05', 'Chequeo traumatológico', '01:00:00', NULL);

-- Inserciones en la tabla Medicamentos
INSERT INTO dbo.Medicamentos (nombre, patogeno)
VALUES 
('Paracetamol', NULL),
('Ibuprofeno', NULL),
('Amoxicilina', NULL),
('Aspirina', NULL);

-- Inserciones en la tabla Efectos_Secundario
INSERT INTO dbo.Efectos_Secundario (Medicamento, efecto)
VALUES 
('Paracetamol', 'Náuseas'),
('Ibuprofeno', 'Dolor de estómago'),
('Amoxicilina', 'Erupciones cutáneas'),
('Aspirina', 'Dificultad para respirar');

-- Inserciones en la tabla Resultado_Cita
INSERT INTO dbo.Resultado_Cita (IdCita, resultado)
VALUES 
(1, 'Todo en orden' ),
(2, 'Erupción leve' ),
(3, 'Chequeo normal'),
(4, 'Recomendación de terapia');

-- Inserciones en la tabla Tratamientos_Cita
INSERT INTO dbo.Tratamientos_Cita (IdCita, tratamiento)
VALUES 
(1, 'Control de azúcar'),
(2, 'Crema para la piel'),
(3, 'Revisión pediátrica'),
(4, 'Sesiones de terapia');

-- Inserciones en la tabla Medicamento_Cita
INSERT INTO dbo.Medicamento_Cita (IdCita, medicamentos, duracion)
VALUES 
(1, 'Paracetamol', '02:00:00'), 
(2, 'Ibuprofeno', '03:00:00'),  
(3, 'Amoxicilina', '01:30:00'), 
(4, 'Aspirina', '02:30:00');     

-- Inserciones en la tabla Procedimiento
INSERT INTO dbo.Procedimiento (N_carnet, N_cedula, fecha, Duracion, epicrisis)
VALUES 
('C001', 'P001', '2024-10-15', '01:30:00', 'Procedimiento realizado con éxito.'),
('C002', 'P002', '2024-10-18', '02:00:00', 'Revisión y seguimiento necesario.'),
('C003', 'P003', '2024-10-20', '00:45:00', 'Sin complicaciones, todo en orden.'),
('C004', 'P004', '2024-10-22', '01:15:00', 'Procedimiento finalizado, revisar informes.');
-- Inserciones en la tabla Procedimiento

INSERT INTO dbo.Procedimiento (N_carnet, N_cedula, fecha, Duracion, epicrisis)
VALUES 
('C002', 'P001', '2024-10-15', '01:30:00', 'Procedimiento realizado con éxito.'),
('C001', 'P001', '2023-10-15', '01:30:00', 'Procedimiento realizado con éxito.');
  

-- Inserciones en la tabla Tratamiento_Procedimiento
INSERT INTO dbo.Tratamiento_Procedimiento (IdProcedimiento, tratamiento)
VALUES 
(1, 'Chequeo general'),
(2, 'Consulta de piel'),
(3, 'Chequeo pediátrico'),
(4, 'Consulta psicológica');

-- Inserciones en la tabla Medicamento_Procedimiento
INSERT INTO dbo.Medicamento_Procedimiento (IdProcedimiento, medicamentos, duracion)
VALUES 
(1, 'Paracetamol', '01:00:00'), 
(2, 'Ibuprofeno', '02:00:00'), 
(3, 'Amoxicilina', '00:30:00'), 
(4, 'Aspirina', '01:15:00'); 

