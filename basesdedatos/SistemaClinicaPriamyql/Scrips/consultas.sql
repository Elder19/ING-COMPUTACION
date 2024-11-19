
DELIMITER //

CREATE PROCEDURE ObtenerAtenciones(IN FechaInicio DATE, IN FechaFin DATE)
BEGIN
    SELECT 
        p.CedulaP,
        p.Nombre,
        p.Apellidos,
        p.FechaNacimiento,
        p.Genero,
        p.Ntelefono,
        p.CorreoE,
        p.Direccion,
        p.GrupoSanguineo,
        p.CantidadPadecimientos,
        p.Intervenciones,
        p.CantidadMedicamentos,
        p.FechaUltimaCita,
        COUNT(DISTINCT cm.IdCita) AS CantidadAtenciones,
        COUNT(DISTINCT pq.IdProcedimiento) AS CantidadProcedimientos
    FROM 
        paciente p
    LEFT JOIN 
        CitasMedicas cm ON p.CedulaP = cm.CedulaP
        AND cm.Fecha BETWEEN FechaInicio AND FechaFin
    LEFT JOIN 
        ProcedimientosQuirurjicos pq ON p.CedulaP = pq.CedulaP 
            AND pq.Fecha BETWEEN FechaInicio AND FechaFin
    WHERE 
        cm.Fecha BETWEEN FechaInicio AND FechaFin
    GROUP BY 
        p.CedulaP
    ORDER BY 
        p.CedulaP;
END //

DELIMITER ;






# cosulta 2
CREATE VIEW consulta20 AS
SELECT 
    DATE_FORMAT(IFNULL(CitasMedicas.Fecha, ProcedimientosQuirurjicos.Fecha), '%Y-%m') AS MesAnio,
    Medicamento.Nombre,
    Medicamento.patogeno,
    Medicamento.EfectosSecundarios,
    SUM(Medicamentos.cantidad) AS CantidadUtilizada
FROM Medicamentos
LEFT JOIN 
    TratamientoPrescrito ON Medicamentos.IdTratamiento = TratamientoPrescrito.IdTratamiento
LEFT JOIN 
    CitasMedicas ON TratamientoPrescrito.IDCita = CitasMedicas.IdCita
LEFT JOIN 
    ProcedimientosQuirurjicos ON TratamientoPrescrito.IdProcedimiento = ProcedimientosQuirurjicos.IdProcedimiento
RIGHT JOIN 
    Medicamento ON Medicamentos.Nombre = Medicamento.Nombre
GROUP BY 
    MesAnio, Medicamento.Nombre;

------------------------------------------------------------------------------------
# cosulta 3
create view consulta3 as
select   DATE_FORMAT(hp.FechaInicio, '%Y') AS fecha, 
    count(hp.CedulaP) as cantidad ,hp.NombrePadecimiento
FROM HistorialPadecimientos hp
join Padecimiento pd on pd.NombrePadecimiento=hp.NombrePadecimiento
group by fecha,pd.NombrePadecimiento;

-----------------------------------------------------------------------------------
# cosulta 4
create view consulta4 as
select(COUNT(tp.IdCita) + COUNT(tp.IdProcedimiento)) AS Intevenciones,sum(md.cantidad) as CantidadMedicamento, M.Nombre as medico
from TratamientoPrescrito tp  
join Medicamentos md on md.IdTratamiento=tp.IdTratamiento
right join personalmedico M on M.CedulaM= tp.CedulaM
group by M.Nombre;


-------------------------------------------------
CREATE VIEW consulta5 AS
SELECT 
    p.*, 
    COUNT(DISTINCT hp.NombrePadecimiento) AS CantidadPadecimientos, 
    (COUNT(DISTINCT pc.IdProcedimiento) + COUNT(DISTINCT cm.IdCita)) AS Intervenciones, 
    SUM(m.cantidad) AS CantidadMedicamentos, 
    MAX(cm.Fecha) AS FechaUltimaCita 
FROM 
    paciente p 
LEFT JOIN 
    HistorialPadecimientos hp ON p.CedulaP = hp.CedulaP 
LEFT JOIN 
    ProcedimientosQuirurjicos pc ON p.CedulaP = pc.CedulaP 
LEFT JOIN 
    CitasMedicas cm ON p.CedulaP = cm.CedulaP 
LEFT JOIN 
    TratamientoPrescrito tp ON cm.IdCita = tp.IDCita 
LEFT JOIN 
    Medicamentos m ON tp.IdTratamiento = m.IdTratamiento 
GROUP BY 
    p.CedulaP, p.Nombre, p.Apellidos, p.fechaNacimiento, p.genero, p.Ntelefono, p.CorreoE, p.Direccion, p.GrupoSanguineo 
ORDER BY 
    p.CedulaP;


