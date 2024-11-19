
use Basept1
go 

select year(Fecha_hora) as Año, MONTH(Fecha_hora) as Mes,count (*) as CantidadCitas from Cita
group by year(Fecha_hora), MONTH (Fecha_hora)
order by Año , Mes;


select year(Fecha_hora) as Año, MONTH(Fecha_hora) as Mes,count (*) as cantidadProcedimiento from Procedimiento

 where Duracion>= 10 
group by year(Fecha_hora), MONTH (Fecha_hora)
having count (*) >=1
order by Mes,Año;

