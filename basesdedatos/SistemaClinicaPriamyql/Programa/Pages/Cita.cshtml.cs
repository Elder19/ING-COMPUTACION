using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using proyecto1bases.Models;
using Microsoft.Extensions.Configuration;
using System.Collections.Generic;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace Tarea2.Pages
{ //ATRIBUTOS DE LA CLASE
    public class Citas : PageModel
    {
        [BindProperty]
        public int CedulaM { get; set; }

        [BindProperty]
        public int CedulaP { get; set; }

        [BindProperty]
        public DateOnly Fecha { get; set; }

        [BindProperty]
        public string Motivo { get; set; }

        [BindProperty]
        public TimeOnly Hora { get; set; }

        [BindProperty]
        public TimeOnly Duracion { get; set; }
        [BindProperty]
        public string NombreEspecialidad { get; set; }
   
//LISTAS DE LA CLASE
        public List<Medico> Medicos { get; set; } = new List<Medico>();
        public List<Paciente> Pacientes { get; set; } = new List<Paciente>();

        private readonly string _connectionString;
// STRING DE CONEXION 
        public Citas(IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }

        public async Task<IActionResult> OnGetAsync()
        {                        
            Medicos= await GetPersonaMedico();
            Pacientes=await Getpaciente();
            return Page();
        }
// INSERTA LOS DATOS EN LA BASE
        public async Task<IActionResult> OnPostAsync()
        {
            
            using (var connection = new MySqlConnection(_connectionString))
            {  string[] medicoSeleccionado = Request.Form["CedulaM"].ToString().Split(' ');
                        CedulaM = int.Parse(medicoSeleccionado[0]); 
                        NombreEspecialidad = medicoSeleccionado[1]; 
            
                var command = new MySqlCommand(
                    "INSERT INTO CitasMedicas (CedulaM, CedulaP, Fecha, Motivo, Hora, Duracion,NombreEspecialidad) " +
                    "VALUES (@CedulaM, @CedulaP, @Fecha, @Motivo, @Hora, @Duracion,@NombreEspecialidad)", connection);

                command.Parameters.AddWithValue("@CedulaM", CedulaM);
                command.Parameters.AddWithValue("@CedulaP", CedulaP);
                command.Parameters.AddWithValue("@Fecha", Fecha.ToString("yyyy-MM-dd"));
                command.Parameters.AddWithValue("@Motivo", Motivo);
                command.Parameters.AddWithValue("@Hora", Hora);
                command.Parameters.AddWithValue("@Duracion", Duracion);
                command.Parameters.AddWithValue("@NombreEspecialidad", NombreEspecialidad);



                connection.Open();
                await command.ExecuteNonQueryAsync();
                // Obtén el ID de la cita recién insertada
                var selectCommand = new MySqlCommand("SELECT LAST_INSERT_ID()", connection);
                var lastId = await selectCommand.ExecuteScalarAsync();

                // Convierte el resultado a int (o long si es necesario)
                int idCita = Convert.ToInt32(lastId);

                var commandS = new MySqlCommand(
                "INSERT INTO historialCP (CedulaP, idCita) " +
                "VALUES (@CedulaP, @IdCita)", connection);

                 commandS.Parameters.AddWithValue("@CedulaP", CedulaP);
                commandS.Parameters.AddWithValue("@IdCita", idCita);
                 await commandS.ExecuteNonQueryAsync();
   
  
 
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
        
       
        var command = new MySqlCommand("SELECT CedulaM, Nombre, Apellidos,NombreEspecialidad FROM PersonalMedico", connection);
        
        using (var reader = await command.ExecuteReaderAsync())
        {
            while (await reader.ReadAsync())
            {
                var cedula = reader.GetInt32(0);    
                var nombre = reader.GetString(1);   
                var apellidos = reader.GetString(2);
                var NombreEspecialidad = reader.GetString(3);

                
                medicos.Add(new Medico
                {
                    CedulaM = cedula,
                    Nombre = nombre,
                    Apellidos = apellidos,
                    NombreEspecialidad=NombreEspecialidad
                });
            }
        }
    }
    return medicos;
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
    
    
    
    
}}





















