using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using proyecto1bases.Models;
using Microsoft.Extensions.Configuration;
using System.Collections.Generic;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace Tarea2.Pages
{
    public class consulta5 : PageModel
    {
        [BindProperty]
        public int IDCita { get; set; }

        [BindProperty]
        public string Resultado { get; set; }

        public List<Consulta5Resultado> Consulta5Resultados { get; set; } = new List<Consulta5Resultado>();

        private readonly string _connectionString;

        public consulta5(IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }

        public async Task<IActionResult> OnGetAsync()
        {
            // Obtener los resultados de la vista consulta5
            Consulta5Resultados = await GetConsulta5Resultados();
            return Page();
        }

        // Método para obtener los resultados de la vista consulta5
        private async Task<List<Consulta5Resultado>> GetConsulta5Resultados()
        {
            var resultados = new List<Consulta5Resultado>();
            using (var connection = new MySqlConnection(_connectionString))
            {
                await connection.OpenAsync();

                var query = @"
                    SELECT 
                        CedulaP, Nombre, Apellidos, fechaNacimiento, genero, Ntelefono, 
                        CorreoE, Direccion, GrupoSanguineo, CantidadPadecimientos, Intervenciones, 
                        CantidadMedicamentos, FechaUltimaCita
                    FROM consulta5";

                var command = new MySqlCommand(query, connection);

                using (var reader = await command.ExecuteReaderAsync())
                {
                    while (await reader.ReadAsync())
                    {
                        // Crear una nueva instancia de Consulta5Resultado y asignar valores
                        var resultado = new Consulta5Resultado
                        {
                            CedulaP = reader.IsDBNull(0) ? 0 : reader.GetInt32(0),
                            Nombre = reader.IsDBNull(1) ? string.Empty : reader.GetString(1),
                            Apellidos = reader.IsDBNull(2) ? string.Empty : reader.GetString(2),
                            FechaNacimiento = reader.IsDBNull(3) ? (DateTime?)null : reader.GetDateTime(3),
                            Genero = reader.IsDBNull(4) ? string.Empty : reader.GetString(4),
                            Ntelefono = reader.IsDBNull(5) ? string.Empty : reader.GetString(5),
                            CorreoE = reader.IsDBNull(6) ? string.Empty : reader.GetString(6),
                            Direccion = reader.IsDBNull(7) ? string.Empty : reader.GetString(7),
                            GrupoSanguineo = reader.IsDBNull(8) ? string.Empty : reader.GetString(8),
                            CantidadPadecimientos = reader.IsDBNull(9) ? 0 : reader.GetInt32(9),
                            Intervenciones = reader.IsDBNull(10) ? 0 : reader.GetInt32(10),
                            CantidadMedicamentos = reader.IsDBNull(11) ? 0 : reader.GetInt32(11),
                            FechaUltimaCita = reader.IsDBNull(12) ? (DateTime?)null : reader.GetDateTime(12) // Asignar FechaUltimaCita
                        };

                        // Agregar el resultado a la lista
                        resultados.Add(resultado);
                    }
                }
            }
            return resultados; // Retornar la lista con los resultados
        }
    }

    public class Consulta5Resultado
    {
        public int CedulaP { get; set; }
        public string Nombre { get; set; }
        public string Apellidos { get; set; }
        public DateTime? FechaNacimiento { get; set; } 
        public string Genero { get; set; }
        public string Ntelefono { get; set; }
        public string CorreoE { get; set; }
        public string Direccion { get; set; }
        public string GrupoSanguineo { get; set; }
        public int CantidadPadecimientos { get; set; }
        public int Intervenciones { get; set; }
        public int CantidadMedicamentos { get; set; }
        public DateTime? FechaUltimaCita { get; set; }  
    }
}
