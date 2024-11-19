
use Basept1
go 
 select distinct UPPER(nombre)as  PC , Grupo_sanguineo as GS  from Paciente 
 where Grupo_sanguineo <> 'A-'
 
 SELECT p.Nombre, p.Apaterno, p.Amaterno 
FROM Paciente p
WHERE p.cedula = ALL (SELECT a.cedulapaciente 
                      FROM Afectacion a
                      WHERE a.Padecimiento = 'Diabetes'
                      AND a.cedulapaciente = p.cedula);

 SELECT p.cedula, p.Nombre FROM Paciente p
WHERE RIGHT(CAST(p.cedula AS VARCHAR(10)), 1) = '3';
                     

SELECT 
    Fecha_hora,
    Motivo,
    cedulapaciente,
    profecionalcedula,
    Resultado
FROM Cita
WHERE DATEDIFF(DAY,Fecha_hora, GETDATE()) > 8
