using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using proyecto1bases.Models;
using Microsoft.Extensions.Configuration;
using System.Collections.Generic;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace Tarea2.Pages
{
    public class Participantes : PageModel
    {
        [BindProperty]
        public int CedulaM { get; set; }

        [BindProperty]
        public int IdProcedimiento { get; set; }

        public List<Medico> Medicos { get; set; } = new List<Medico>();
        public List<Paciente> Pacientes { get; set; } = new List<Paciente>();
        public List<Medico> ParticipantesMedicos { get; set; } = new List<Medico>();
        public List<ProcedimientosQuirurjicos> Procedimientos { get; set; } = new List<ProcedimientosQuirurjicos>();
      //STRING DE CONEXION
        private readonly string _connectionString;

        public Participantes(IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }

        public async Task<IActionResult> OnGetAsync()
        {
            Medicos = await GetPersonaMedico();
            Procedimientos = await GetProcedimientos();
            return Page();
        }
//iNSERTA EN LA BASE DE DATOS LA INFORMACION
        public async Task<IActionResult> OnPostAsync()
        {
            var participantesSeleccionados = Request.Form["Participantes"];

            using (var connection = new MySqlConnection(_connectionString))
            {
                await connection.OpenAsync();

                // Inserta participantes seleccionados
                foreach (var cedula in participantesSeleccionados)
                {
                    if (!string.IsNullOrWhiteSpace(cedula))
                    {
                        var commandParticipante = new MySqlCommand(
                            "INSERT INTO PersonalParticipante (IdProcedimiento, CedulaM) " +
                            "VALUES (@IdProcedimiento, @CedulaM)", connection);

                        commandParticipante.Parameters.AddWithValue("@IdProcedimiento", IdProcedimiento);
                        commandParticipante.Parameters.AddWithValue("@CedulaM", cedula);
                        await commandParticipante.ExecuteNonQueryAsync();
                    }
                }

                // Actualiza el estado del procedimiento
                var commandEstado = new MySqlCommand(
                    "UPDATE ProcedimientosQuirurjicos SET Estado = 'Asignado' WHERE IdProcedimiento = @IdProcedimiento", connection);
                commandEstado.Parameters.AddWithValue("@IdProcedimiento", IdProcedimiento);
                await commandEstado.ExecuteNonQueryAsync();
            }

            return RedirectToPage();
        }
// LECTURA DE TABLAS DE LA BASE DE DATOS
        private async Task<List<Medico>> GetPersonaMedico()
        {
            var medicos = new List<Medico>();
            using (var connection = new MySqlConnection(_connectionString))
            {
                await connection.OpenAsync();
                var command = new MySqlCommand("SELECT CedulaM, Nombre, Apellidos, NombreEspecialidad FROM PersonalMedico", connection);
                using (var reader = await command.ExecuteReaderAsync())
                {
                    while (await reader.ReadAsync())
                    {
                        medicos.Add(new Medico
                        {
                            CedulaM = reader.GetInt32(0),
                            Nombre = reader.GetString(1),
                            Apellidos = reader.GetString(2),
                            NombreEspecialidad = reader.GetString(3)
                        });
                    }
                }
            }
            return medicos;
        }
// LECTURA DE TABLAS DE LA BASE DE DATOS
        private async Task<List<ProcedimientosQuirurjicos>> GetProcedimientos()
        {
            var procedimientos = new List<ProcedimientosQuirurjicos>();
            using (var connection = new MySqlConnection(_connectionString))
            {
                await connection.OpenAsync();
                var command = new MySqlCommand("SELECT IdProcedimiento, CedulaM, Estado FROM ProcedimientosQuirurjicos", connection);
               
                using (var reader = await command.ExecuteReaderAsync())
                {
                    while (await reader.ReadAsync())
                    {
                        var estado = reader.GetString(2);
                        
                        if (estado == "No asignado")
                        {
                            procedimientos.Add(new ProcedimientosQuirurjicos
                            {
                                IdProcedimiento = reader.GetInt32(0),
                                CedulaM = reader.GetInt32(1),
                                Estado = estado
                            });
                        }
                    }
                }
            }
            return procedimientos;
        }
    }
}
