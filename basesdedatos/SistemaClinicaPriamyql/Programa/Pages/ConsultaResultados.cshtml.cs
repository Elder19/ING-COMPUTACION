using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using proyecto1bases.Models;
using Microsoft.Extensions.Configuration;
using System.Collections.Generic;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace Tarea2.Pages
{
    public class ConsultaResultados : PageModel
    {  //LISTAS DE LA CLASE
    /// </summary>
        public List<ConsultaResultado> consultaResultados { get; set; } = new List<ConsultaResultado>();
//STRING DE CONEXION
        private readonly string _connectionString;

        public ConsultaResultados(IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }

        public async Task OnGetAsync(DateTime fechaInicio, DateTime fechaFin)
        {
            consultaResultados = await GetConsultaResultados(fechaInicio, fechaFin);
        }
// LECTURA DE TABLAS DE LA BASE DE DATOS
        private async Task<List<ConsultaResultado>> GetConsultaResultados(DateTime fechaInicio, DateTime fechaFin)
        {
            var resultados = new List<ConsultaResultado>();
            using (var connection = new MySqlConnection(_connectionString))
            {
                await connection.OpenAsync();

                var query = @"
                    CALL ObtenerAtenciones(@FechaInicio, @FechaFin)";
                
                var command = new MySqlCommand(query, connection);
                command.Parameters.AddWithValue("@FechaInicio", fechaInicio);
                command.Parameters.AddWithValue("@FechaFin", fechaFin);

                using (var reader = await command.ExecuteReaderAsync())
                {
                    while (await reader.ReadAsync())
                    {
                        var resultado = new ConsultaResultado
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
                            FechaUltimaCita = reader.IsDBNull(12) ? (DateTime?)null : reader.GetDateTime(12),
                            CantidadAtenciones = reader.IsDBNull(13) ? 0 : reader.GetInt32(13),
                            CantidadProcedimientos = reader.IsDBNull(14) ? 0 : reader.GetInt32(14) // Nueva propiedad
                        };
                        resultados.Add(resultado);
                    }
                }
            }
            return resultados;
        }
    }
}//CLASE DE LA CONSULTA
 public class ConsultaResultado
    {
        public int CedulaP { get; set; }
        public string Nombre { get; set; }
        public string Apellidos { get; set; }
        public DateTime? FechaNacimiento { get; set; }
        public string Genero { get; set; }
        public string Ntelefono { get; set; }
        public string CorreoE { get; set; }
        public string Direccion { get; set; }
       
        public int CantidadPadecimientos { get; set; }
        public int Intervenciones { get; set; }
        public int CantidadMedicamentos { get; set; }
        public DateTime? FechaUltimaCita { get; set; }
        public int CantidadAtenciones { get; set; }
        public int CantidadProcedimientos { get; set; }
         public string GrupoSanguineo { get; set;}}