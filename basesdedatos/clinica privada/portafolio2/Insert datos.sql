USE Basept1;
GO


INSERT INTO PersonalMedico (profecionalcedula, Correo, Numero, Nombre, Apaterno, Amaterno, Profesion)
VALUES
(123456789, 'medico1@example.com', 123456789, 'Juan', 'P�rez', 'G�mez', 'Cardi�logo'),
(234567890, 'medico2@example.com', 234567890, 'Ana', 'Mart�nez', 'Rivas', 'Dermat�logo'),
(345678901, 'medico3@example.com', 345678901, 'Luis', 'Garc�a', 'L�pez', 'Pediatra'),
(456789012, 'medico4@example.com', 456789012, 'Mar�a', 'Rodr�guez', 'Cruz', 'Cirujano');


INSERT INTO Paciente (Nombre, Apaterno, Amaterno, Carnet, Sexo, correo, Grupo_sanguineo, cedula)
VALUES
('Carlos', 'Alvarez', 'Soto', 'C001', 'M', 'carlos@example.com', 'O+', 111111111),
('Laura', 'Paredes', 'Vargas', 'L002', 'F', 'laura@example.com', 'A-', 222222222),
('Pedro', 'Ram�rez', 'G�mez', 'P003', 'M', 'pedro@example.com', 'B+', 333333333),
('Sof�a', 'Mendoza', 'L�pez', 'S004', 'F', 'sofia@example.com', 'AB-', 444444444),
('Carlos', 'Alvarez', 'Soto', 'c0000', 'M', 'carlos@example.com', 'O+', 703080520),
('Laura', 'Paredes', 'Vargas', 'c2222', 'F', 'laura@example.com', 'A-', 115420101),
('Pedro', 'Ram�rez', 'G�mez', 'c00005', 'M', 'pedro@example.com', 'B+', 701640696);



INSERT INTO Cita (cedulapaciente, Motivo, Fecha_hora, Resultado, profecionalcedula)
VALUES
(111111111, 'Consulta general', '2024-09-01 10:00:00', 'Sin novedad', 123456789),
(222222222, 'Chequeo dermatol�gico', '2024-09-02 11:00:00', 'Requiere tratamiento', 234567890),
(333333333, 'Consulta pedi�trica', '2024-09-03 09:00:00', 'Control satisfactorio', 345678901),
(444444444, 'Procedimiento quir�rgico', '2024-09-04 14:00:00', '�xito total', 456789012),
(703080520, 'Consulta general', '2024-09-05 10:00:00', 'Sin novedad', 123456789),
(115420101, 'Chequeo dermatol�gico', '2024-09-07 11:00:00', 'Requiere tratamiento', 234567890),
(701640696, 'Consulta pedi�trica', '2024-09-08 09:00:00', 'Control satisfactorio', 345678901);

INSERT INTO Tratamiento (cedula, profecionalcedula, Fecha_hora, Tratamiento)
VALUES
(111111111, 123456789, '2024-09-01 10:00:00', 'Antibi�ticos'),
(222222222, 234567890, '2024-09-02 11:00:00', 'Crema t�pica'),
(333333333, 345678901, '2024-09-03 09:00:00', 'Vitamina D'),
(444444444, 456789012, '2024-09-04 14:00:00', 'An�lisis postoperatorios');

INSERT INTO Padecimiento (cedulapaciente, tipo, Padecimiento, sintomas)
VALUES
(111111111, 'Cr�nico', 'Diabetes', 'Hiperglucemia, fatiga'),
(222222222, 'Agudo', 'Eczema', 'Picaz�n, enrojecimiento'),
(333333333, 'Cr�nico', 'Asma', 'Dificultad para respirar'),
(444444444, 'Agudo', 'Infecci�n', 'Dolor, fiebre');


INSERT INTO Afectacion (cedulapaciente, Padecimiento, Afectacion, gravedad)
VALUES
(111111111, 'Diabetes', 'Retinopat�a', 'Moderada'),
(222222222, 'Eczema', 'Dermatitis severa', 'Alta'),
(333333333, 'Asma', 'Crisis asm�tica', 'Alta'),
(444444444, 'Infecci�n', 'Sepsis', 'Cr�tica');


INSERT INTO ResultadoCita (cedulaPaciente, cedulaProfecional, fecha_hora, Resultado)
VALUES
(111111111, 123456789, '2024-09-01 10:00:00', 'Estable'),
(222222222, 234567890, '2024-09-02 11:00:00', 'Necesita seguimiento'),
(333333333, 345678901, '2024-09-03 09:00:00', 'Controlado'),
(444444444, 456789012, '2024-09-04 14:00:00', 'Exitoso');


INSERT INTO Medicamento (Nombre, ComponenteActivo, Patogeno)
VALUES
('Amoxicilina', 'Amoxicilina', 'Bacteria'),
('Prednisona', 'Prednisona', 'Ninguno'),
('Paracetamol', 'Paracetamol', 'Ninguno'),
('Ibuprofeno', 'Ibuprofeno', 'Ninguno');


INSERT INTO Medicamentocita (cedulaPaciente, cedulaProfecional, fecha_hora, medicamento, duracion)
VALUES
(111111111, 123456789, '2024-09-01 10:00:00', 'Amoxicilina', '7 d�as'),
(222222222, 234567890, '2024-09-02 11:00:00', 'Prednisona', '10 d�as'),
(333333333, 345678901, '2024-09-03 09:00:00', 'Paracetamol', '5 d�as'),
(444444444, 456789012, '2024-09-04 14:00:00', 'Ibuprofeno', '3 d�as');

INSERT INTO EfectoSecundario (Medicamento, Efecto)
VALUES
('Amoxicilina', 'N�useas'),
('Prednisona', 'Aumento de peso'),
('Paracetamol', 'Erupciones'),
('Ibuprofeno', 'Dolor de est�mago');


INSERT INTO Procedimiento (cedulapaciente, Motivo, Fecha_hora, Duracion, epicrisis, profecionalcedula)
VALUES
(111111111, 'Cirug�a de la vista', '2024-09-09 10:00:00', 2, '�xito total', 123456789),
(222222222, 'Examen dermatol�gico', '2024-10-09 11:00:00', 1 , 'Necesario tratamiento', 234567890),
(333333333, 'Consulta de control', '2024-09-03 09:00:00', 30 , 'Controlado', 345678901),
(444444444, 'Revisi�n postoperatoria', '2024-09-04 14:00:00', 1, 'Todo en orden', 456789012);


INSERT INTO MedicamentoProcedimiento (cedulapaciente, Medicamento, Fecha_hora, Duracion, dosisis, profecionalcedula)
VALUES
(111111111, 'Amoxicilina', '2024-09-01 10:00:00', '7 d�as', '500 mg cada 8 horas', 123456789),
(222222222, 'Prednisona', '2024-09-02 11:00:00', '10 d�as', '10 mg diarios', 234567890),
(333333333, 'Paracetamol', '2024-09-03 09:00:00', '5 d�as', '500 mg cada 6 horas', 345678901),
(444444444, 'Ibuprofeno', '2024-09-04 14:00:00', '3 d�as', '400 mg cada 8 horas', 456789012);
