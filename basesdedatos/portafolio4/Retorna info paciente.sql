

use Clinica_Privada ;
go 

create function DatosPAC ()
returns table 
as 
return(
 select (pc.Nombre + ' ' + pc.apellido_1 + ' '+pc.apellido_2) as NombreCompleto, pc.N_carnet as Cartnet,pc.FechaNacimiento as fecha, 
 DATEDIFF(YEAR, pc.FechaNacimiento, GETDATE()) AS Edad
 from Pacientes pc
)
end; 


SELECT * FROM DatosPAC();



---Cree una consulta que retorne por cada
--procedimiento el nombre del paciente,
--nombre del profesional, fecha, duracion.
--Utilice función definida por el usuario para retornar los totales


create function dbo.duracon()
returns table
as
    return (
        select 
            p.nombre as nombrepaciente,
            pf.nombre as nombreprofesional,
            pr.fecha,
            pr.duracion
        from 
            procedimiento pr
        join 
            Pacientes p on pr.N_carnet = p.N_carnet
        join 
            Personal_Medico pf on pr.N_cedula = pf.N_cedula
    );


select * from dbo.duracon()

/*Cree una función que reciba como
parámetro un número de carnet y por
cada paciente retorne el nombre de los
profesionales que lo han atendido.*/

create function dbo.atenciones (
    @n_carnet varchar(100)
)
returns table
as
    return (
        select 
            pf.nombre as nombreprofesional
        from 
            procedimiento pr
        join 
            Personal_Medico pf on pr.N_cedula = pf.N_cedula
        where 
            pr.N_carnet = @n_carnet
        group by 
            pf.nombre
    );

select * from dbo.atenciones('C003'); 
