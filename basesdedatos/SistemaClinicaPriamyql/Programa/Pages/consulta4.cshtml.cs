using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using proyecto1bases.Models;
using Microsoft.Extensions.Configuration;
using System.Collections.Generic;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace Tarea2.Pages
{
    public class consulta4 : PageModel
    {
        // Propiedades para enlazar datos
        [BindProperty]
        public string Resultado { get; set; }

        // Lista para almacenar resultados de la consulta
        public List<Consulta54Resultado> Consulta4Resultados { get; set; } = new List<Consulta54Resultado>();

        private readonly string _connectionString;

        // Constructor que recibe la configuración para la conexión a la base de datos
        public consulta4(IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }

        // Método para manejar la solicitud GET
        public async Task<IActionResult> OnGetAsync()
        {
            Consulta4Resultados = await GetConsulta4Resultados();
            return Page();
        }

        // Método para obtener los resultados de la vista consulta4
        private async Task<List<Consulta54Resultado>> GetConsulta4Resultados()
{
    var resultados = new List<Consulta54Resultado>();
    using (var connection = new MySqlConnection(_connectionString))
    {
        await connection.OpenAsync();

        var query = @"
            SELECT 
                medico,
                Intevenciones,
                CantidadMedicamento
            FROM consulta4";
        
        var command = new MySqlCommand(query, connection);

        using (var reader = await command.ExecuteReaderAsync())
        {
            while (await reader.ReadAsync())
            {
                var resultado = new Consulta54Resultado
                {
                    Medico = reader.IsDBNull(0) ? string.Empty : reader.GetString(0),
                    Intervenciones = reader.IsDBNull(1) ? 0 : reader.GetInt32(1),
                    CantidadMedicamentos = reader.IsDBNull(2) ? 0 : reader.GetInt32(2)
                };
                resultados.Add(resultado);
            }
        }
    }
    return resultados;
}



    }

    // Definición de la clase para almacenar los resultados
    public class Consulta54Resultado
    {
        public string Medico { get; set; }
        public int Intervenciones { get; set; }
        public int CantidadMedicamentos { get; set; }
    }
}
