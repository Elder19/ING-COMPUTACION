using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using System;

namespace Tarea2.Pages
{
    public class Consulta : PageModel
    {
        [BindProperty]
        public DateTime FechaInicio { get; set; }

        [BindProperty]
        public DateTime FechaFin { get; set; }

        private readonly string _connectionString;

        public Consulta(IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }

        public void OnGet()
        {
            // Este método se ejecuta cuando se accede a la página a través de una solicitud GET
        }

        public IActionResult OnPost()
        {
            // Verificar que la fecha de inicio sea menor o igual a la fecha de fin
            if (FechaInicio > FechaFin)
            {
                ModelState.AddModelError(string.Empty, "La fecha de inicio debe ser menor o igual a la fecha de fin.");
                return Page();
            }

            // Redirigir a la página de resultados con las fechas como parámetros
            return RedirectToPage("ConsultaResultados", new { fechaInicio = FechaInicio, fechaFin = FechaFin });
        }
    }
}
