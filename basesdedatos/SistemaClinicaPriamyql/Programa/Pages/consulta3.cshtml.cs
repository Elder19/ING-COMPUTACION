using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using proyecto1bases.Models;
using Microsoft.Extensions.Configuration;
using System.Collections.Generic;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace Tarea2.Pages
{
    public class consulta3 : PageModel
    {
        public List<Consulta3Resultado> Consulta3Resultados { get; set; } = new List<Consulta3Resultado>();
//STRING DE CONEXION
        private readonly string _connectionString;

        public consulta3(IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }

        public async Task<IActionResult> OnGetAsync()
        {
            Consulta3Resultados = await GetConsulta3Resultados();
            return Page();
        }

        // Método para obtener los resultados de la vista consulta3
        private async Task<List<Consulta3Resultado>> GetConsulta3Resultados()
        {
            var resultados = new List<Consulta3Resultado>();
            using (var connection = new MySqlConnection(_connectionString))
            {
                await connection.OpenAsync();

                var query = @"
                    SELECT 
                        fecha, cantidad, NombrePadecimiento
                    FROM consulta3";
                
                var command = new MySqlCommand(query, connection);

                using (var reader = await command.ExecuteReaderAsync())
                {
                    while (await reader.ReadAsync())
                    {
                        var resultado = new Consulta3Resultado
                        {
                            Fecha = reader.IsDBNull(0) ? string.Empty : reader.GetString(0),
                            Cantidad = reader.IsDBNull(1) ? 0 : reader.GetInt32(1),
                            NombrePadecimiento = reader.IsDBNull(2) ? string.Empty : reader.GetString(2)
                        };
                        resultados.Add(resultado);
                    }
                }
            }
            return resultados;
        }
    }
/// <summary>
/// CLASE DE LA CONSULTA
/// </summary>
    public class Consulta3Resultado
    {
        public string Fecha { get; set; }
        public int Cantidad { get; set; }
        public string NombrePadecimiento { get; set; }
    }
}
