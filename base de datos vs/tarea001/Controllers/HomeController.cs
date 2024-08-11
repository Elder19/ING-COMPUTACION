using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using tarea001.Models;
using Newtonsoft.Json;
using System.Collections.Generic;
using System.IO;

namespace tarea001.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            // Ruta para el directorio donde se guarda el archivo JSON
            string directoryPath =  @"C:\Users\coleg\OneDrive\Escritorio\base de datos vs\tarea001\wwwroot\JSON" ;
            string filePath = Path.Combine(directoryPath, "datos.json");

            List<RegistroPaciente> registros = new List<RegistroPaciente>();

            // Leer el contenido del archivo JSON si existe
            if (System.IO.File.Exists(filePath))
            {
                var jsonData = System.IO.File.ReadAllText(filePath);
                try
                {
                    registros = JsonConvert.DeserializeObject<List<RegistroPaciente>>(jsonData) ?? new List<RegistroPaciente>();
                }
                catch (JsonSerializationException ex)
                {
                    // Manejar la excepción de deserialización
                    _logger.LogError(ex, "Error al deserializar el archivo JSON.");
                }
            }

            // Pasar los datos a la vista
            return View(registros);
        }

        public IActionResult Privacy()
        {
            return Index();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }

        [HttpPost]
        public JsonResult DatosRegistro([FromBody] RegistroPaciente datos)
        {
            if (datos == null)
            {
                return Json(new { Success = false, Message = "Datos no recibidos. El objeto es nulo." });
            }

            try
            {
                // Ruta para el directorio donde se guardará el archivo JSON
                string directoryPath = @"C:\Users\coleg\OneDrive\Escritorio\base de datos vs\tarea001\wwwroot\JSON";
                string filePath = Path.Combine(directoryPath, "datos.json");

                // Verifica si el directorio existe; si no, créalo
                if (!Directory.Exists(directoryPath))
                {
                    Directory.CreateDirectory(directoryPath);
                }

                // Leer el contenido existente del archivo JSON
                List<RegistroPaciente> registros;
                if (System.IO.File.Exists(filePath))
                {
                    var jsonData = System.IO.File.ReadAllText(filePath);
                    registros = JsonConvert.DeserializeObject<List<RegistroPaciente>>(jsonData) ?? new List<RegistroPaciente>();
                }
                else
                {
                    registros = new List<RegistroPaciente>();
                }

                // Agregar el nuevo registro a la lista
                registros.Add(datos);

                // Convertir la lista a una cadena JSON
                string jsonString = JsonConvert.SerializeObject(registros, Formatting.Indented);

                /// Escribir la cadena JSON en el archivo (sin usar FileShare.None)
        using (var fileStream = new FileStream(filePath, FileMode.Create, FileAccess.Write, FileShare.ReadWrite))
        using (var streamWriter = new StreamWriter(fileStream))
        {
            streamWriter.Write(jsonString);
        }
            
            return Json(new { message = "Datos recibidos correctamente" });
            }
            catch (Exception ex)
            {
                // Loguear el error y devolver un mensaje de error
                _logger.LogError(ex, "Error al escribir en el archivo JSON.");
                return Json(new { Success = false, Message = "Error al escribir en el archivo JSON." });
            }
        }
    }
}
