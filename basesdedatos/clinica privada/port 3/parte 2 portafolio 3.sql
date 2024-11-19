


use Clinica_Privada;
go 
SELECT 
    pm.N_cedula, 
    (pm.Nombre + ' ' + pm.apellido_1 + ' ' + pm.apellido_2) AS nombre_completo,
    COUNT(pd.N_cedula) AS cantidad_procedimientos
FROM 
    Personal_Medico pm
JOIN 
    Procedimiento pd ON pm.N_cedula = pd.N_cedula
GROUP BY 
    pm.N_cedula, pm.Nombre, pm.apellido_1, pm.apellido_2
HAVING 
    COUNT(pd.N_cedula) > 2;



(select apellido_1 from Pacientes) union all (select apellido_1 from PacienteFrecuente)
(select apellido_1 from Pacientes) union  (select apellido_1 from PacienteFrecuente)

(select apellido_1 from Pacientes) intersect  (select apellido_1 from PacienteFrecuente)
(select apellido_1 from Pacientes) intersect all (select apellido_1 from PacienteFrecuente)--Msg 324, Level 15, State 1, Line 25
--No se admite la versión 'ALL' del operador INTERSECT.

(select apellido_1 from Pacientes) except  (select apellido_1 from PacienteFrecuente)

(select apellido_1 from PacienteFrecuente)except (select apellido_1 from Pacientes)