


/*Realice un procedimiento almacenado que reciba los parámetros para incluir un paciente y una cita
Agrupe los insert en una transacción, maneje bloque try catch para manejo de error, commit en caso exitoso y catch en caso de error*/
create procedure pacientecita
    @n_carnet nvarchar(100),
    @nombre nvarchar(100),
    @apellido_1 nvarchar(100),
    @apellido_2 nvarchar(100),
    @telefono nvarchar(100),
    @correo nvarchar(100),
    @sexo nvarchar(50),
    @grupo_sanguineo nvarchar(50),
    @fecha_nacimiento date,
    @direccion nvarchar(200),
    @paciente_cita nvarchar(100),
    @profesional_cita nvarchar(100),
    @fecha_cita date,
    @motivo_cita nvarchar(100),
    @duracion_cita time,
    @resultados_cita nvarchar(200)
as
begin
    begin try
        begin transaction
        
        insert into dbo.pacientes (n_carnet, nombre, apellido_1, apellido_2, telefono, correo, sexo, grupo_sanguineo, FechaNacimiento, direccion)
        values (@n_carnet, @nombre, @apellido_1, @apellido_2, @telefono, @correo, @sexo, @grupo_sanguineo, @fecha_nacimiento, @direccion)
        
        insert into dbo.cita (paciente, profesional, fecha, motivo, duracion, resultados)
        values (@paciente_cita, @profesional_cita, @fecha_cita, @motivo_cita, @duracion_cita, @resultados_cita)
        
        commit transaction
    end try
    begin catch
        rollback transaction
    end catch
end



exec pacientecita
    @n_carnet = 'C001000',
    @nombre = 'Juan',
    @apellido_1 = 'Pérez',
    @apellido_2 = 'González',
    @telefono = '123456789',
    @correo = 'juan.perez@email.com',
    @sexo = 'Masculino',
    @grupo_sanguineo = 'O+',
    @fecha_nacimiento = '1990-01-15',
    @direccion = 'Calle 123, Ciudad',
    @paciente_cita = 'C001000',  
    @profesional_cita = 'P001', 
    @fecha_cita = '2024-11-08',
    @motivo_cita = 'Consulta general',
    @duracion_cita = '01:00:00',
    @resultados_cita = 'En espera';
