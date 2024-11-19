
CREATE PROCEDURE InsertarCita
    @Paciente NVARCHAR(100),
    @Profesional NVARCHAR(100),
    @Fecha DATE,
    @Motivo NVARCHAR(100),
    @Duracion TIME,
    @Resultados NVARCHAR(200),
    @MensajeError NVARCHAR(200) OUTPUT
AS
BEGIN
    BEGIN TRY

        INSERT INTO dbo.Cita (Paciente, Profesional, Fecha, Motivo, Duracion, Resultados)
        VALUES (@Paciente, @Profesional, @Fecha, @Motivo, @Duracion, @Resultados);

        SET @MensajeError = 'Cita insertada.';
    END TRY
    BEGIN CATCH
        
        SET @MensajeError = ERROR_MESSAGE();
    END CATCH
END;


--inseert
DECLARE @Resultado NVARCHAR(200);
EXEC InsertarCita
    @Paciente = 'C001', 
    @Profesional = 'P001', 
    @Fecha = '2024-10-15',
    @Motivo = 'Consulta general',
    @Duracion = '01:00:00',
    @Resultados = 'Diagnóstico preliminar',
    @MensajeError = @Resultado OUTPUT;
PRINT @Resultado;
go 


    declare PacientesCursor cursor for
    select N_carnet, Nombre, apellido_1, apellido_2, telefono, correo, Sexo, grupo_Sanguineo, FechaNacimiento, Direccion
    from Pacientes;

  
    declare @N_carnet nvarchar(100),
            @Nombre nvarchar(100),
            @apellido_1 nvarchar(100),
            @apellido_2 nvarchar(100),
            @telefono nvarchar(100),
            @correo nvarchar(100),
            @Sexo nvarchar(50),
            @grupo_Sanguineo nvarchar(50),
            @FechaNacimiento date,
            @Direccion nvarchar(200);

    open PacientesCursor;
    fetch next from PacientesCursor into @N_carnet, @Nombre, @apellido_1, @apellido_2, @telefono, @correo, @Sexo, @grupo_Sanguineo, @FechaNacimiento, @Direccion
    
    while @@FETCH_STATUS = 0
    begin
        insert into PacientesVIP (N_carnet, Nombre, apellido_1, apellido_2, telefono, correo, Sexo, grupo_Sanguineo, FechaNacimiento, Direccion)
        values (@N_carnet, @Nombre, @apellido_1, @apellido_2, @telefono, @correo, @Sexo, @grupo_Sanguineo, @FechaNacimiento, @Direccion);


        fetch next from PacientesCursor into @N_carnet, @Nombre, @apellido_1, @apellido_2, @telefono, @correo, @Sexo, @grupo_Sanguineo, @FechaNacimiento, @Direccion;
    end;
    close PacientesCursor;
    deallocate PacientesCursor;





