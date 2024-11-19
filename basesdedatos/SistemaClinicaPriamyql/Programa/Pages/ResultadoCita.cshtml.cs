using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using proyecto1bases.Models;
using Microsoft.Extensions.Configuration;
using System.Collections.Generic;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace Tarea2.Pages
{
    public class ResultadoCita : PageModel
    {
        [BindProperty]
        public int IDCita { get; set; }

        [BindProperty]
        public string Resultado { get; set; }

    
   //LISTAS DE LA CLASE

        public List<Cita> citas { get; set; } = new List<Cita>();
        public List<Paciente> Pacientes { get; set; } = new List<Paciente>();
        public List<ResultadoCitas> resultados { get; set; } = new List<ResultadoCitas>();
        
// STRING DE CONEXION 
        private readonly string _connectionString;

        public ResultadoCita (IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }

        public async Task<IActionResult> OnGetAsync()
        { 
                           
            citas= await GetCitas();
            Pacientes= await Getpaciente();
            resultados= await GetResultados();
           
            return Page();
        }

        
        public async Task<IActionResult> OnPostAsync()

{      
       citas = await GetCitas();
       resultados= await GetResultados();
   
          

    // Realizar la inserción en la base de datos
    using (var connection = new MySqlConnection(_connectionString))
    {
        var command = new MySqlCommand(
            "INSERT INTO ResultadosCita (IDCita,Resultado) " +
            "VALUES (@IDCita,@Resultado)", connection);

        command.Parameters.AddWithValue("@IDCita", IDCita);
        command.Parameters.AddWithValue("@Resultado", Resultado);
    

        connection.Open();
        await command.ExecuteNonQueryAsync();
    }

    return RedirectToPage();
}
  private async Task<List<ResultadoCitas>> GetResultados(){
    var resutaldos= new List<ResultadoCitas>();
     using (var connection = new MySqlConnection(_connectionString))
 {
     await connection.OpenAsync();
     
    
     var command = new MySqlCommand("SELECT IdCita,Resultado from resultadoscita", connection);
     
     using (var reader = await command.ExecuteReaderAsync())
     {
         while (await reader.ReadAsync())
         {   var IdCita = reader.GetInt32(0);
             var Resultado= reader.GetString(1);
             
             
            
             resutaldos.Add(new ResultadoCitas
             {
                 IDCita = IdCita,
                 Resultado= Resultado
                 
                
               
             });
         }
     }
 }
 return resutaldos;

  }
// LECTURA DE TABLAS DE LA BASE DE DATOS
   private async Task<List<Cita>> GetCitas(){
    var citas = new List<Cita>();
    resultados=await GetResultados();
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

                 if (!resultados.Any(t => t.IDCita == IdCita)){
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
}}}






















