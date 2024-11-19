
/*Cree un trigger en la tabla cita que en
lugar de eliminar un registro le cambie el
estado a inactivo.*/
create trigger actualizar
on dbo.cita
instead of delete
as
begin
    update dbo.cita
    set activo = 'inactivo'
    where idcita in (select idcita from deleted);
end;

delete from dbo.cita where idcita = 1;
select * from dbo.cita;


/*Cree un trigger en la tabla paciente
que al modificar un registro imprima los
valores anteriores y los nuevos valores.*/
create trigger modif
on dbo.pacientes
after update
as
begin
    
    select 
       *
    from 
        deleted d;  

    select 
       *
    from 
        inserted i; 

end;

update dbo.Pacientes
set Nombre = '68', apellido_1 = 'Lopez', telefono = '987654321'
where N_carnet = 'C001';



















