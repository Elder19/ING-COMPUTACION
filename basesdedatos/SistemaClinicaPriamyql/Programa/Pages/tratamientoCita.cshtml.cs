using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using proyecto1bases.Models;
using Microsoft.Extensions.Configuration;
using System.Collections.Generic;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace Tarea2.Pages
{
    public class TratamientoCita : PageModel
    {
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
        public string tipo { get; set; }
   

        public List<Cita> citas { get; set; } = new List<Cita>();
         public List<Tratamiento> tratamientos { get; set; } = new List<Tratamiento>();
        public List<Paciente> Pacientes { get; set; } = new List<Paciente>();

        private readonly string _connectionString;

        public TratamientoCita(IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }

        public async Task<IActionResult> OnGetAsync()
        {    
            tratamientos=await GetTratamientosAsyncq();                    
            citas= await GetCitas();
            Pacientes=await Getpaciente();
            return Page();
        }

        
        public async Task<IActionResult> OnPostAsync()

{      
       citas = await GetCitas();
     var cita = citas.FirstOrDefault(c => c.IdCita == IDCita);
        CedulaM= cita.CedulaM;
        CedulaP=cita.CedulaP;
        NombreEspecialidad=cita.NombreEspecialidad;

        



    // Realizar la inserción en la base de datos
    using (var connection = new MySqlConnection(_connectionString))
    {
        var command = new MySqlCommand(
            "INSERT INTO TratamientoPrescrito (IDCita, CedulaM, CedulaP, tipo, Duracion, NombreEspecialidad) " +
            "VALUES (@IDCita, @CedulaM, @CedulaP, @tipo, @Duracion, @NombreEspecialidad)", connection);

        command.Parameters.AddWithValue("@IDCita", IDCita);
        command.Parameters.AddWithValue("@CedulaM", CedulaM);
        command.Parameters.AddWithValue("@CedulaP", CedulaP);
        command.Parameters.AddWithValue("@tipo", tipo);
        command.Parameters.AddWithValue("@Duracion", Duracion);
        command.Parameters.AddWithValue("@NombreEspecialidad", NombreEspecialidad);

        connection.Open();
        await command.ExecuteNonQueryAsync();
    }

    return RedirectToPage();
}

  // LECTURA DE TABLAS DE LA BASE DE DATOS                                                                                                     
 private async Task<List<Tratamiento>> GetTratamientosAsyncq()
{
    var tratamientos = new List<Tratamiento>();

    using (var connection = new MySqlConnection(_connectionString))
    {
        await connection.OpenAsync();

        var command = new MySqlCommand("SELECT IDCita, CedulaP, IdTratamiento, estado FROM TratamientoPrescrito", connection);
        using (var reader = await command.ExecuteReaderAsync())
        {
            while (await reader.ReadAsync())
            {
                var IDCita = reader.IsDBNull(0) ? 0 : reader.GetInt32(0); 
                var CedulaP = reader.IsDBNull(1) ? 0 : reader.GetInt32(1); 
                var IdTratamiento = reader.IsDBNull(2) ? 0 : reader.GetInt32(2); 
                var estado = reader.IsDBNull(3) ? "No asignado" : reader.GetString(3);

                if (estado == "No asignado")
                {
                    tratamientos.Add(new Tratamiento
                    {
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
    private async Task<List<Cita>> GetCitas()
{
    var citas = new List<Cita>();
    using (var connection = new MySqlConnection(_connectionString))
    {
        await connection.OpenAsync();
        
       
        var command = new MySqlCommand("SELECT IdCita,CedulaM,CedulaP,NombreEspecialidad FROM CitasMedicas", connection);
        
        using (var reader = await command.ExecuteReaderAsync())
        {
            while (await reader.ReadAsync())
            {   var IdCita = reader.GetInt32(0);
                var cedulaM= reader.GetInt32(1);
                var cedula = reader.GetInt32(2);
                var NombreEspecialidad=reader.GetString(3);    
                if (!tratamientos.Any(t => t.IdCita == IdCita)){
                citas.Add(new Cita
                {
                    CedulaP = cedula,
                    CedulaM= cedulaM,
                    IdCita = IdCita,
                    NombreEspecialidad = NombreEspecialidad
                  
                });}
            }
        }
    }
    return citas;
}
    
}}





















