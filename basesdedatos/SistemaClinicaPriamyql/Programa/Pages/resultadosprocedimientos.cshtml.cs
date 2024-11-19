using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using proyecto1bases.Models;
using Microsoft.Extensions.Configuration;
using System.Collections.Generic;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace Tarea2.Pages
{
    public class TratamientoCi : PageModel
    {
        [BindProperty]
        public int IDCita { get; set; }

        [BindProperty]
        public string Resultado { get; set; }

    
   
//LSITAS DE LA CLASE
        public List<ProcedimientosQuirurjicos> citas { get; set; } = new List<ProcedimientosQuirurjicos>();
        public List<Paciente> Pacientes { get; set; } = new List<Paciente>();
        public List<ResultadoCitas> resultados { get; set; } = new List<ResultadoCitas>();
        

        private readonly string _connectionString;

        public TratamientoCi (IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }
//CARGA INFORMACION PREVIA
        public async Task<IActionResult> OnGetAsync()
        { 
                           
            citas= await GetProcedimientos();
            Pacientes= await Getpaciente();
            resultados= await GetResultados();
           
            return Page();
        }

        
        public async Task<IActionResult> OnPostAsync()

{      
       citas = await GetProcedimientos();
       resultados= await GetResultados();
   
          

    // Realizar la inserción en la base de datos
    using (var connection = new MySqlConnection(_connectionString))
    {
        var command = new MySqlCommand(
            "INSERT INTO ResultadoProcedimiento (IdProcedimiento,Epicrisis) " +
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
     
    
     var command = new MySqlCommand("SELECT IdProcedimiento,Epicrisis from ResultadoProcedimiento", connection);
     
     using (var reader = await command.ExecuteReaderAsync())
     {
         while (await reader.ReadAsync())
         {   var IdProcedimiento = reader.GetInt32(0);
             var Epicrisis= reader.GetString(1);
             
             resutaldos.Add(new ResultadoCitas
             {
                 IDCita = IdProcedimiento,
                 Resultado= Epicrisis
                 
             });
         }
     }
 }
 return resutaldos;

  }
// LECTURA DE TABLAS DE LA BASE DE DATOS
         private async Task<List<ProcedimientosQuirurjicos>> GetProcedimientos()
        {
            var citas = new List<ProcedimientosQuirurjicos>();
               resultados= await GetResultados();
            using (var connection = new MySqlConnection(_connectionString))
            {
                await connection.OpenAsync();
                var command = new MySqlCommand("SELECT IdProcedimiento, CedulaM, CedulaP, NombreEspecialidad FROM ProcedimientosQuirurjicos", connection);
                using (var reader = await command.ExecuteReaderAsync())
                {
                    while (await reader.ReadAsync())
                    {
                        var IdProcedimiento = reader.GetInt32(0);
                        var CedulaM = reader.GetInt32(1);
                        var CedulaP = reader.GetInt32(2);
                        var NombreEspecialidad = reader.GetString(3);   

                        if (!resultados.Any(t => t.IDCita == IdProcedimiento)){
                        citas.Add(new ProcedimientosQuirurjicos
                        {
                            IdProcedimiento = IdProcedimiento,
                            CedulaM = CedulaM,
                            CedulaP = CedulaP,
                            NombreEspecialidad = NombreEspecialidad
                        });
                    }
                }
            }
            return citas;
        }}
    

   
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






















