
-- Funcion retornasrt nombres en mayuscucula,
create function nombreIUper(@nombre varchar(100), @apellido varchar(100))
returns varchar (200)
as 
begin 
 declare @Resultado varchar(200)
 set @Resultado = UPPER(@nombre + ' '+@apellido)
 return @Resultado
end; 
GO 

SELECT dbo.nombreIUper('Juan', 'Pérez') AS NombreCompletoEnMayusculas;
select  dbo.nombreIUper ('Elder', 'leon') AS NombreCompletoEnMayusculas;
