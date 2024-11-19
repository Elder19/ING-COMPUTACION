
use Clinica_Privada;
go 

CREATE view PorCIta  as 
select ct.duracion as duracion, ct.motivo, pc.Nombre+' '+pc.apellido_1+' '+pc.apellido_2 as nombre
,pm.Nombre+' '+PM.apellido_1+' '+PM.apellido_2 AS MEDICO
from dbo.Cita ct

join Pacientes pc on pc.N_carnet= ct.Paciente

join Personal_Medico PM on pm.N_cedula=ct.profesional;
go


select pc.* , count(pd.Paciente) as Padecimientos from Pacientes pc
left join Padecimiento pd on pc.N_carnet = pd.Paciente
group by  pc.N_carnet, 
    pc.Nombre, 
    pc.apellido_1, 
    pc.apellido_2, 
    pc.telefono, 
    pc.correo, 
    pc.Sexo, 
    pc.grupo_Sanguineo,
    pc.FechaNacimiento, 
    pc.Direccion; ;

go

SELECT 
    pm.*, 
   
    (COUNT(DISTINCT mc.medicamentos) + COUNT(DISTINCT mp.medicamentos)) AS Total_Distintos_Medicamentos
FROM 
    Personal_Medico pm
JOIN 
    Cita ct ON ct.profesional = pm.N_cedula
LEFT JOIN 
    Medicamento_Cita mc ON mc.IdCita = ct.IdCita
LEFT JOIN 
    Procedimiento pc ON pc.N_cedula = pm.N_cedula
LEFT JOIN 
    Medicamento_Procedimiento mp ON mp.IdProcedimiento = pc.IdProcedimiento 
GROUP BY 
    pm.N_cedula, 
    pm.Nombre, 
    pm.apellido_1, 
    pm.apellido_2, 
    pm.telefono, 
    pm.correo, 
    pm.profesion,
	pm.especialidad;
	go

	
create view citasA as 
select pc.Nombre,count(mc.medicamentos) as Medicamentos, count(ct.IdCita) as citas  from Pacientes pc

join Cita ct on ct.Paciente=pc.N_carnet
join Medicamento_Cita mc on mc.IdCita= ct.IdCita
group by pc.Nombre;



