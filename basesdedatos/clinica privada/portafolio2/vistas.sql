USE Basept1;
GO


CREATE VIEW Pacientec AS
SELECT 
    Nombre,
    Carnet,
    Sexo,
    Grupo_sanguineo 
FROM 
    Paciente;
GO

CREATE VIEW IntervencionesDc AS
SELECT
    P.Nombre AS PacienteNombre,
    P.Carnet AS PacienteCarnet,
    PM.Nombre AS DoctorNombre,
    PM.profecionalcedula AS DoctorCedula, 
    Pr.Fecha_hora AS FechaProcedimiento,
    Pr.Motivo AS MotivoProcedimiento,
    Pr.Duracion AS DuracionProcedimiento,
    Pr.epicrisis AS EpicrisisProcedimiento
FROM
    Procedimiento Pr
    INNER JOIN Paciente P ON Pr.cedulapaciente = P.cedula
    LEFT JOIN PersonalMedico PM ON Pr.profecionalcedula = PM.profecionalcedula;
GO

CREATE VIEW vista_citas_pacientes AS
SELECT
    Paciente.Carnet AS PacienteCarnet,
    Paciente.Nombre + ' ' + Paciente.Apaterno + ' ' + Paciente.Amaterno AS NombrePaciente,
    PersonalMedico.profecionalcedula AS ProfesionalCedula,
    PersonalMedico.Nombre + ' ' + PersonalMedico.Apaterno + ' ' + PersonalMedico.Amaterno AS NombreProfesional,
    Cita.Fecha_hora AS FechaHoraCita,
    Cita.Motivo AS MotivoCita
FROM 
    Cita
JOIN 
    Paciente ON Cita.cedulapaciente = Paciente.cedula
JOIN 
    PersonalMedico ON Cita.profecionalcedula = PersonalMedico.profecionalcedula;
GO

select * from Pacientec;
select * from IntervencionesDc;
select * from vista_citas_pacientes;