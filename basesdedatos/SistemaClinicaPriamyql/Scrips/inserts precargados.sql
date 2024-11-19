use sistema_clinica_privada; 

-- Insertar 15 pacientes
INSERT INTO paciente (CedulaP, Nombre, Apellidos, fechaNacimiento, genero, Ntelefono, CorreoE, Direccion, GrupoSanguineo)
VALUES
(101, 'Juan', 'Pérez', '1985-01-15', 'M', 88881111, 'juan.perez@example.com', 'Calle 1', 'O+'),
(102, 'Ana', 'Gómez', '1990-02-20',  'F', 88882222, 'ana.gomez@example.com', 'Calle 2', 'A+'),
(103, 'Luis', 'Martínez', '1982-07-05',  'M', 88883333, 'luis.martinez@example.com', 'Calle 3', 'B+'),
(104, 'María', 'Rodríguez', '1975-09-12', 'F', 88884444, 'maria.rodriguez@example.com', 'Calle 4', 'O-'),
(105, 'Carlos', 'Fernández', '1995-10-22',  'M', 88885555, 'carlos.fernandez@example.com', 'Calle 5', 'A-'),
(106, 'Lucía', 'Sánchez', '1988-04-14', 'F', 88886666, 'lucia.sanchez@example.com', 'Calle 6', 'AB+'),
(107, 'Jorge', 'López', '1978-12-30',  'M', 88887777, 'jorge.lopez@example.com', 'Calle 7', 'B-'),
(108, 'Claudia', 'García', '1993-03-18', 'F', 88888888, 'claudia.garcia@example.com', 'Calle 8', 'AB-'),
(109, 'Pedro', 'Ramírez', '1981-06-22', 'M', 88889999, 'pedro.ramirez@example.com', 'Calle 9', 'O+'),
(110, 'Sara', 'Torres', '1985-08-01', 'F', 88880000, 'sara.torres@example.com', 'Calle 10', 'A+'),
(111, 'Esteban', 'Castro', '1980-11-25',  'M', 88881112, 'esteban.castro@example.com', 'Calle 11', 'B+'),
(112, 'Laura', 'Vargas', '1992-05-13', 'F', 88882223, 'laura.vargas@example.com', 'Calle 12', 'O-'),
(113, 'Diego', 'Mora', '1987-02-18', 'M', 88883334, 'diego.mora@example.com', 'Calle 13', 'A-'),
(114, 'Patricia', 'Herrera', '1991-06-28',  'F', 88884445, 'patricia.herrera@example.com', 'Calle 14', 'AB+'),
(115, 'Ricardo', 'Cruz', '1979-09-08',  'M', 88885556, 'ricardo.cruz@example.com', 'Calle 15', 'AB-');

-- Insertar 5 padecimientos
INSERT INTO Padecimiento (NombrePadecimiento, Sintomas)
VALUES
('Diabetes', 'Sed excesiva, fatiga'),
('Hipertensión', 'Dolor de cabeza, fatiga'),
('Asma', 'Dificultad para respirar, tos'),
('Gripe', 'Fiebre, dolor de cuerpo, tos'),
('Migraña', 'Dolor de cabeza intenso, náuseas');

-- Insertar historial de padecimientos para los pacientes
INSERT INTO HistorialPadecimientos (NombrePadecimiento, CedulaP, FechaInicio, Sintomas)
VALUES
('Diabetes', 101, '2015-05-10', 'Sed excesiva, fatiga'),
('Hipertensión', 101, '2018-03-15', 'Dolor de cabeza, fatiga'),
('Asma', 102, '2019-07-20', 'Dificultad para respirar, tos'),
('Gripe', 102, '2022-11-10', 'Fiebre, dolor de cuerpo, tos'),
('Migraña', 103, '2021-01-25', 'Dolor de cabeza intenso, náuseas'),
('Asma', 104, '2019-09-10', 'Dificultad para respirar, tos'),
('Gripe', 105, '2022-08-20', 'Fiebre, dolor de cuerpo, tos');
-- (Agregar más registros similares para los otros pacientes).


-- Insertar especialidades médicas
INSERT INTO Especialidad (NombreEspecialidad)
VALUES
('Cardiología'),
('Endocrinología'),
('Pediatría'),
('Neurología'),
('Gastroenterología'),
('Dermatología'),
('Neumología'),
('Psiquiatría'),
('Urología'),
('Cirugía General');
-- Insertar 10 médicos
INSERT INTO PersonalMedico (CedulaM, Nombre, Apellidos, genero, Experiencia, Ntelefono, CorreoE, NombreEspecialidad)
VALUES
(201, 'Carlos', 'Rodríguez', 'M', '10 años', 88883333, 'carlos.rodriguez@example.com', 'Cardiología'),
(202, 'Laura', 'Fernández', 'F', '8 años', 88884444, 'laura.fernandez@example.com', 'Endocrinología'),
(203, 'Mario', 'Gómez', 'M', '5 años', 88885555, 'mario.gomez@example.com', 'Pediatría'),
(204, 'Ana', 'López', 'F', '12 años', 88886666, 'ana.lopez@example.com', 'Neurología'),
(205, 'José', 'Martínez', 'M', '15 años', 88887777, 'jose.martinez@example.com', 'Gastroenterología'),
(206, 'Sofía', 'Ramírez', 'F', '7 años', 88888888, 'sofia.ramirez@example.com', 'Dermatología'),
(207, 'Daniel', 'Sánchez', 'M', '6 años', 88889999, 'daniel.sanchez@example.com', 'Neumología'),
(208, 'Paula', 'Torres', 'F', '9 años', 88880000, 'paula.torres@example.com', 'Psiquiatría'),
(209, 'Javier', 'Mora', 'M', '11 años', 88881112, 'javier.mora@example.com', 'Urología'),
(210, 'Carolina', 'Vargas', 'F', '4 años', 88882223, 'carolina.vargas@example.com', 'Cirugía General');
-- Insertar 10 medicamentos
INSERT INTO Medicamento (Nombre, patogeno, EfectosSecundarios)
VALUES
('Metformina', 'Control de la glucosa', 'Náuseas, dolor de estómago'),
('Lisinopril', 'Control de la presión arterial', 'Tos, mareos'),
('Ibuprofeno', 'Antiinflamatorio', 'Mareos, indigestión'),
('Amoxicilina', 'Antibiótico', 'Diarrea, erupciones'),
('Paracetamol', 'Antipirético', 'Reacciones alérgicas, náuseas'),
('Omeprazol', 'Protector gástrico', 'Dolor de cabeza, mareos'),
('Furosemida', 'Diurético', 'Deshidratación, calambres musculares'),
('Aspirina', 'Analgésico', 'Problemas gastrointestinales, sangrado'),
('Clorfenamina', 'Antihistamínico', 'Somnolencia, boca seca'),
('Prednisona', 'Corticosteroide', 'Aumento de peso, insomnio');
