using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using proyecto1bases.Models;
using Microsoft.Extensions.Configuration;
using System.Collections.Generic;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace Tarea2.Pages
{
    public class consulta2 : PageModel
    {
        public List<Consulta2Resultado> Consulta2Resultados { get; set; } = new List<Consulta2Resultado>();
        private readonly string _connectionString;

        public consulta2(IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }

        public async Task<IActionResult> OnGetAsync()
        {
            Consulta2Resultados = await GetConsulta2Resultados();
            return Page();
        }

        private async Task<List<Consulta2Resultado>> GetConsulta2Resultados()
        {
            var resultados = new List<Consulta2Resultado>();
            using (var connection = new MySqlConnection(_connectionString))
            {
                await connection.OpenAsync();

                // Seleccionar datos de la vista consulta
         var query = @"
    SELECT 
        MesAnio, 
        Nombre, 
        patogeno, 
        EfectosSecundarios, 
        CantidadUtilizada
    FROM consulta20;";

                var command = new MySqlCommand(query, connection);

                using (var reader = await command.ExecuteReaderAsync())
                {
                    while (await reader.ReadAsync())
                    {
                        var resultado = new Consulta2Resultado
                        {
                            MesAnio = reader.IsDBNull(0) ? string.Empty : reader.GetString(0),
                            NombreMedicamento = reader.IsDBNull(1) ? string.Empty : reader.GetString(1),
                            Patogeno = reader.IsDBNull(2) ? string.Empty : reader.GetString(2),
                            EfectosSecundarios = reader.IsDBNull(3) ? string.Empty : reader.GetString(3),
                            CantidadUtilizada = reader.IsDBNull(4) ? 0 : reader.GetInt32(4)
                        };
                        resultados.Add(resultado);
                    }
                }
            }
            return resultados;
        }
    }
//CLASE DE LA CONSULTA
    public class Consulta2Resultado
    {
        public string MesAnio { get; set; }
        public string NombreMedicamento { get; set; }
        public string Patogeno { get; set; } // Campo para Patogeno
        public string EfectosSecundarios { get; set; } // Campo para Efectos Secundarios
        public int CantidadUtilizada { get; set; } // Campo para Cantidad Utilizada
    }
}
