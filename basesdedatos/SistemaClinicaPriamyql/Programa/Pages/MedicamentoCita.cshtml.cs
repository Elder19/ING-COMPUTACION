using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using proyecto1bases.Models;
using Microsoft.Extensions.Configuration;
using System.Collections.Generic;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace Tarea2.Pages
{
    public class MedicamentoCita : PageModel
    {
        // Propiedades que se utilizarán en el formulario
        [BindProperty]
        public int IdTratamiento { get; set; }

        [BindProperty]
        public int cantidad { get; set; }

        [BindProperty]
        public string Nombre { get; set; }

        [BindProperty]
        public string Dosis { get; set; }

        [BindProperty]
        public string estado { get; set; }

        [BindProperty]
        public int IdProcedimiento { get; set; }

        // Listas para almacenar datos
        public List<Cita> citas { get; set; } = new List<Cita>();
        public List<Tratamiento> tratamientos { get; set; } = new List<Tratamiento>();
        public List<Paciente> Pacientes { get; set; } = new List<Paciente>();
        public List<Medicamento> medicamentos { get; set; } = new List<Medicamento>();
        public List<Medicamentos> medicamentoss { get; set; } = new List<Medicamentos>();

        private readonly string _connectionString;

        // Constructor para obtener la cadena de conexión
        public MedicamentoCita(IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }

        // Método que se ejecuta en la carga de la página
        public async Task<IActionResult> OnGetAsync()
        {
            citas = await GetCitas();
            Pacientes = await Getpaciente();
            tratamientos = await GetTratamientosAsyncq();
            medicamentos = await GetMedicamento();
            medicamentoss = await GetMedicamentos();
            return Page();
        }

        // Método que se ejecuta al enviar el formulario
        public async Task<IActionResult> OnPostAsync()
        {
            using (var connection = new MySqlConnection(_connectionString))
            {
                await connection.OpenAsync(); // Conexión abierta

                // Inserción de un nuevo medicamento
                var command = new MySqlCommand(
                    "INSERT INTO Medicamentos (IdTratamiento, Nombre, Dosis, cantidad) " +
                    "VALUES (@IdTratamiento, @Nombre, @Dosis, @cantidad)", connection);

                // Agregar parámetros
                command.Parameters.AddWithValue("@IdTratamiento", IdTratamiento);
                command.Parameters.AddWithValue("@Nombre", Nombre);
                command.Parameters.AddWithValue("@Dosis", Dosis);
                command.Parameters.AddWithValue("@cantidad", cantidad); // Asegúrate de que este campo existe en la base de datos
            
                await command.ExecuteNonQueryAsync(); 

                // Actualizar el estado del tratamiento
                var update = new MySqlCommand("UPDATE TratamientoPrescrito SET estado = @estado WHERE IdTratamiento = @IdTratamiento", connection);
                update.Parameters.AddWithValue("@estado", estado); 
                update.Parameters.AddWithValue("@IdTratamiento", IdTratamiento);
                await update.ExecuteNonQueryAsync(); 
            }
            
            return RedirectToPage();
        }

        // Método para obtener tratamientos
        private async Task<List<Tratamiento>> GetTratamientosAsyncq()
        {
            var tratamientos = new List<Tratamiento>();

            using (var connection = new MySqlConnection(_connectionString))
            {
                await connection.OpenAsync();

                var command = new MySqlCommand("SELECT IDCita, CedulaP, IdTratamiento, estado, IdProcedimiento FROM TratamientoPrescrito", connection);
                using (var reader = await command.ExecuteReaderAsync())
                {
                    while (await reader.ReadAsync())
                    {
                        var IDCita = reader.IsDBNull(0) ? 0 : reader.GetInt32(0); 
                        var CedulaP = reader.IsDBNull(1) ? 0 : reader.GetInt32(1); 
                        var IdTratamiento = reader.IsDBNull(2) ? 0 : reader.GetInt32(2); 
                        var estado = reader.IsDBNull(3) ? "No asignado" : reader.GetString(3);
                        var IdProcedimiento = reader.IsDBNull(4) ? 0 : reader.GetInt32(4); 

                        if (estado == "No asignado")
                        {
                            tratamientos.Add(new Tratamiento
                            {   
                                IdProcedimiento = IdProcedimiento,
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

        // Método para obtener pacientes
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

        // Método para obtener citas
        private async Task<List<Cita>> GetCitas()
        {
            var citas = new List<Cita>();
            using (var connection = new MySqlConnection(_connectionString))
            {
                await connection.OpenAsync(); 

                var command = new MySqlCommand("SELECT IdCita, CedulaM, CedulaP, NombreEspecialidad FROM CitasMedicas", connection);
                using (var reader = await command.ExecuteReaderAsync())
                {
                    while (await reader.ReadAsync())
                    {
                        var IdCita = reader.GetInt32(0);
                        var cedulaM = reader.GetInt32(1);
                        var cedula = reader.GetInt32(2);
                        var NombreEspecialidad = reader.GetString(3);

                        citas.Add(new Cita
                        {
                            CedulaP = cedula,
                            CedulaM = cedulaM,
                            IdCita = IdCita,
                            NombreEspecialidad = NombreEspecialidad
                        });
                    }
                }
            }
            return citas;
        }

        // Método para obtener medicamentos
        private async Task<List<Medicamento>> GetMedicamento()
        {
            var medicamentos = new List<Medicamento>();
            using (var connection = new MySqlConnection(_connectionString))
            {
                await connection.OpenAsync(); 

                var command = new MySqlCommand("SELECT Nombre, patogeno, EfectosSecundarios FROM Medicamento", connection);
                using (var reader = await command.ExecuteReaderAsync())
                {
                    while (await reader.ReadAsync())
                    {
                        var Nombre = reader.GetString(0);
                        var patogeno = reader.GetString(1);
                        var EfectosSecundarios = reader.GetString(2);
                    

                        medicamentos.Add(new Medicamento
                        {
                            Nombre = Nombre,
                            patogeno = patogeno,
                            EfectosSecundarios = EfectosSecundarios,
                           
                        });
                    }
                }
            }
            return medicamentos;
        }
    
        // Método para obtener tratamientos prescritos
        private async Task<List<Medicamentos>> GetMedicamentos()
        {
            var medicamentos = new List<Medicamentos>();
            using (var connection = new MySqlConnection(_connectionString))
            {
                await connection.OpenAsync(); 
                var command = new MySqlCommand("SELECT IdTratamiento FROM Medicamentos", connection);
                using (var reader = await command.ExecuteReaderAsync())
                {
                    while (await reader.ReadAsync())
                    {
                        var IdTratamiento = reader.GetInt32(0);
                        
                        medicamentoss.Add(new Medicamentos
                        {
                            IdTratamiento = IdTratamiento
                        });
                    }
                }
            }
            return medicamentos;
        }
    }
}
