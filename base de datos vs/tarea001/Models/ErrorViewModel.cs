namespace tarea001.Models;

public class ErrorViewModel
{
    public string? RequestId { get; set; }

    public bool ShowRequestId => !string.IsNullOrEmpty(RequestId);
}

public class RegistroPaciente

{
    public string Nombre { get; set; } = string.Empty;
    public string Apellidos { get; set; } = string.Empty;
    public string Cedula { get; set; } = string.Empty;
    public string Edad { get; set; } = string.Empty;
   public DateTime? FechaNacimiento { get; set; } // Cambiado a DateTime?

    public string Direccion { get; set; } = string.Empty;
}
