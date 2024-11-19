



create view ConteoCitas as
select(COUNT(h.idCita) + COUNT(h.IdProcedimiento)) AS Intevenciones,  pc.* 
from historialCP h 
JOIN paciente pc ON h.cedulaP = pc.cedulaP 
group by h.cedulaP;


SELECT 
    -- Convierte la fecha de la cita médica o el procedimiento quirúrgico (si la cita es nula) en formato 'año-mes'
    DATE_FORMAT(IFNULL(CitasMedicas.Fecha, ProcedimientosQuirurjicos.Fecha), '%Y-%m') AS MesAnio, Medicamento.*, SUM(Medicamentos.cantidad) AS CantidadUtilizada
FROM Medicamentos
LEFT JOIN 
    TratamientoPrescrito ON Medicamentos.IdTratamiento = TratamientoPrescrito.IdTratamiento
LEFT JOIN 
    CitasMedicas ON TratamientoPrescrito.IDCita = CitasMedicas.IdCita
LEFT JOIN 
    ProcedimientosQuirurjicos ON TratamientoPrescrito.IdProcedimiento = ProcedimientosQuirurjicos.IdProcedimiento
JOIN 
    Medicamento ON Medicamentos.Nombre = Medicamento.Nombre
GROUP BY 
    MesAnio, Medicamento.Nombre ;


select   DATE_FORMAT(hp.FechaInicio, '%Y-%m-%d') AS fecha, 
    count(hp.CedulaP) as cantidad  
FROM HistorialPadecimientos hp
join Padecimiento pd on pd.NombrePadecimiento=hp.NombrePadecimiento
group by fecha;

