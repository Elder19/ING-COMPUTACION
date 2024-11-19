using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using proyecto1bases.Models;
using Microsoft.Extensions.Configuration;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace Tarea2.Pages
{
    public class TratamientoC : PageModel
    {// ARTRIBUTOS DE LA CLASE 
        [BindProperty]
        public int IDCita { get; set; }

        [BindProperty]
        public int IdProcedimiento { get; set; }

        [BindProperty]
        public int CedulaM { get; set; }

        [BindProperty]
        public int CedulaP { get; set; }

        [BindProperty]
        public string NombreEspecialidad { get; set; }

        [BindProperty]
        public int Duracion { get; set; }

        [BindProperty]
        public string Tipo { get; set; } 
//LISTAS DE LA CLASE
        public List<ProcedimientosQuirurjicos> citas { get; set; } = new List<ProcedimientosQuirurjicos>();
        public List<Tratamiento> tratamientos { get; set; } = new List<Tratamiento>();
        public List<Paciente> Pacientes { get; set; } = new List<Paciente>();

        private readonly string _connectionString;

        public TratamientoC(IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }
//CARGA LAS LISTAS PREVIAMENTE
        public async Task<IActionResult> OnGetAsync()
        {    
            tratamientos = await GetTratamientosAsync();                    
            citas = await GetProcedimientos();
            Pacientes = await Getpaciente();
            return Page();
        }
// LECTURA DE TABLAS DE LA BASE DE DATOS
        public async Task<IActionResult> OnPostAsync()
        {      
            citas = await GetProcedimientos();
            var cita = citas.FirstOrDefault(c => c.IdProcedimiento == IdProcedimiento);
            CedulaM = cita.CedulaM;
            CedulaP = cita.CedulaP;
            NombreEspecialidad = cita.NombreEspecialidad;

            using (var connection = new MySqlConnection(_connectionString))
            {
                var command = new MySqlCommand(
                    "INSERT INTO TratamientoPrescrito (IdProcedimiento, CedulaM, CedulaP, tipo, Duracion, NombreEspecialidad) " +
                    "VALUES (@IdProcedimiento, @CedulaM, @CedulaP, @tipo, @Duracion, @NombreEspecialidad)", connection);

                command.Parameters.AddWithValue("@IdProcedimiento", IdProcedimiento);
                command.Parameters.AddWithValue("@CedulaM", CedulaM);
                command.Parameters.AddWithValue("@CedulaP", CedulaP);
                command.Parameters.AddWithValue("@tipo", Tipo);
                command.Parameters.AddWithValue("@Duracion", Duracion);
                command.Parameters.AddWithValue("@NombreEspecialidad", NombreEspecialidad);

                connection.Open();
                await command.ExecuteNonQueryAsync();
            }

            return RedirectToPage();
        }

// LECTURA DE TABLAS DE LA BASE DE DATOS
private async Task<List<Tratamiento>> GetTratamientosAsync()
{
    var tratamientos = new List<Tratamiento>();

    using (var connection = new MySqlConnection(_connectionString))
    {
        await connection.OpenAsync();

        var command = new MySqlCommand("SELECT IDCita, CedulaP, IdTratamiento, estado,IdProcedimiento FROM TratamientoPrescrito", connection);
        using (var reader = await command.ExecuteReaderAsync())
        {
            while (await reader.ReadAsync())
            {
                var IDCita = reader.IsDBNull(0) ? 0 : reader.GetInt32(0); 
                var CedulaP = reader.IsDBNull(1) ? 0 : reader.GetInt32(1); 
                var IdTratamiento = reader.IsDBNull(2) ? 0 : reader.GetInt32(2); 
                var estado = reader.IsDBNull(3) ? "No asignado" : reader.GetString(3);
                var IdProcedimiento = reader.IsDBNull(4) ? 0 : reader.GetInt32(4); 

                if (estado == "No asignado")
                {
                    tratamientos.Add(new Tratamiento
                    {    IdProcedimiento = IdProcedimiento,
                        IdCita = IDCita,
                        CedulaP = CedulaP,
                        IdTratamiento = IdTratamiento,
                        estado = estado
                    });
                }
            }
        }
    }
    return tratamientos;
}


// LECTURA DE TABLAS DE LA BASE DE DATOS
        private async Task<List<Paciente>> Getpaciente()
        {
            var Pacientes = new List<Paciente>();
            using (var connection = new MySqlConnection(_connectionString))
            {
                await connection.OpenAsync();
                var command = new MySqlCommand("SELECT CedulaP, Nombre, Apellidos FROM paciente", connection);
                using (var reader = await command.ExecuteReaderAsync())
                {
                    while (await reader.ReadAsync())
                    {
                        var cedula = reader.GetInt32(0);    
                        var nombre = reader.GetString(1);   
                        var apellidos = reader.GetString(2); 
                        
                        Pacientes.Add(new Paciente
                        {
                            CedulaP = cedula,
                            Nombre = nombre,
                            Apellidos = apellidos
                        });
                    }
                }
            }
            return Pacientes;
        }
// LECTURA DE TABLAS DE LA BASE DE DATOS

        private async Task<List<ProcedimientosQuirurjicos>> GetProcedimientos()
        {
            var procedimientos = new List<ProcedimientosQuirurjicos>();
            using (var connection = new MySqlConnection(_connectionString))
            {
                await connection.OpenAsync();
                var command = new MySqlCommand("SELECT IdProcedimiento, CedulaM, CedulaP, NombreEspecialidad FROM ProcedimientosQuirurjicos", connection);
                using (var reader = await command.ExecuteReaderAsync())
                {
                    while (await reader.ReadAsync())
                    {
                        var IdProcedimiento = reader.GetInt32(0);
                        var CedulaM = reader.GetInt32(1);
                        var CedulaP = reader.GetInt32(2);
                        var NombreEspecialidad = reader.GetString(3);   
                         if (!tratamientos.Any(t => t.IdProcedimiento == IdProcedimiento)){
                        procedimientos.Add(new ProcedimientosQuirurjicos
                        {
                            IdProcedimiento = IdProcedimiento,
                            CedulaM = CedulaM,
                            CedulaP = CedulaP,
                            NombreEspecialidad = NombreEspecialidad
                        });
                    }
                }
            }
            return procedimientos;
        }
    }
}}
