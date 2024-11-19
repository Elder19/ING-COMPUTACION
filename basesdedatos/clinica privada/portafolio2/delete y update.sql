
USE Basept1;
GO
--error en codigo por alguna razon en el insert el formato se supone es correcto, cuando se muestra en la tabla dias y meses salen al revez por lo que falla el codigo--

UPDATE Procedimiento
SET Duracion = Duracion * 1.10
WHERE Fecha_hora >= CAST(DATEADD(DAY, -30, GETDATE()) AS DATE);

SELECT * FROM Procedimiento;


--error en codigo por alguna razon en el insert el formato se supone es correcto, cuando se muestra en la tabla dias y meses salen al revez por lo que falla el codigo--
DELETE FROM Cita
WHERE Fecha_hora >= CAST(DATEADD(DAY, -15, GETDATE()) AS DATE)
  AND Fecha_hora < CAST(DATEADD(DAY, -10, GETDATE()) AS DATE);

SELECT * FROM Cita;