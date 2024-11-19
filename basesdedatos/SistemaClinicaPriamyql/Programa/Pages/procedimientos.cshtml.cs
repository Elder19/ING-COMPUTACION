using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using proyecto1bases.Models;
using Microsoft.Extensions.Configuration;
using System.Collections.Generic;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace Tarea2.Pages
{
    public class Cirujia : PageModel
    {// ATRIBUTOS DE LA CLASE
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
        [BindProperty]
        public int IdProcedimiento  { get; set; }
   
//LSITAS DE LA CLASE
        public List<Medico> Medicos { get; set; } = new List<Medico>();
        public List<Paciente> Pacientes { get; set; } = new List<Paciente>();
         public List<Medico> Participantes { get; set; } = new List<Medico>();

        private readonly string _connectionString;

        public Cirujia(IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }
// CARGA LA INFORMACION PREVIA
        public async Task<IActionResult> OnGetAsync()
        {                        
            Medicos= await GetPersonaMedico();
            Pacientes=await Getpaciente();
             Participantes = await GetParticipantes(CedulaM); 
            return Page();
        }
//CARGA EN LA BASE DE DATOS LOS DATOS
public async Task<IActionResult> OnPostAsync()
{
    var participantesSeleccionados = Request.Form["Participantes"]; 
    using (var connection = new MySqlConnection(_connectionString))
    {
        await connection.OpenAsync();

        string[] medicoSeleccionado = Request.Form["CedulaM"].ToString().Split(' ');
        CedulaM = int.Parse(medicoSeleccionado[0]); 
        NombreEspecialidad = medicoSeleccionado[1]; 
        
        // Inserción del procedimiento quirúrgico
        var command = new MySqlCommand(
            "INSERT INTO ProcedimientosQuirurjicos (CedulaM, CedulaP, Fecha, Motivo, Hora, Duracion, NombreEspecialidad) " +
            "VALUES (@CedulaM, @CedulaP, @Fecha, @Motivo, @Hora, @Duracion, @NombreEspecialidad)", connection);

        command.Parameters.AddWithValue("@CedulaM", CedulaM);
        command.Parameters.AddWithValue("@CedulaP", CedulaP);
        command.Parameters.AddWithValue("@Fecha", Fecha.ToString("yyyy-MM-dd"));
        command.Parameters.AddWithValue("@Motivo", Motivo);
        command.Parameters.AddWithValue("@Hora", Hora);
        command.Parameters.AddWithValue("@Duracion", Duracion);
        command.Parameters.AddWithValue("@NombreEspecialidad", NombreEspecialidad);

        await command.ExecuteNonQueryAsync();

        // Obtener el último IdProcedimiento
        var selectCommand = new MySqlCommand("SELECT LAST_INSERT_ID()", connection);
        var lastId = await selectCommand.ExecuteScalarAsync();
        IdProcedimiento = Convert.ToInt32(lastId);

        // Insertar en el historial de procedimientos
        var commandS = new MySqlCommand(
            "INSERT INTO historialCP (CedulaP, IdProcedimiento) " +
            "VALUES (@CedulaP, @IdProcedimiento)", connection);

        commandS.Parameters.AddWithValue("@CedulaP", CedulaP);
        commandS.Parameters.AddWithValue("@IdProcedimiento", IdProcedimiento);
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
// LECTURA DE TABLAS DE LA BASE DE DATOS
private async Task<List<Medico>> GetParticipantes(int cedulaMedico)
    {
        var medicos = new List<Medico>();
        using (var connection = new MySqlConnection(_connectionString))
        {
            await connection.OpenAsync();
            var command = new MySqlCommand("SELECT CedulaM, Nombre, Apellidos, NombreEspecialidad FROM PersonalMedico WHERE CedulaM != @CedulaM", connection);
            command.Parameters.AddWithValue("@CedulaM", cedulaMedico);

            using (var reader = await command.ExecuteReaderAsync())
            {
                while (await reader.ReadAsync())
                {
                    var cedula = reader.GetInt32(0);
                    var nombre = reader.GetString(1);
                    var apellidos = reader.GetString(2);
                    var nombreEspecialidad = reader.GetString(3);

                    medicos.Add(new Medico
                    {
                        CedulaM = cedula,
                        Nombre = nombre,
                        Apellidos = apellidos,
                        NombreEspecialidad = nombreEspecialidad
                    });
                }
            }
        }
        return medicos;
    }

    
}}





















