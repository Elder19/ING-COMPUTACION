using Org.BouncyCastle.Asn1;
using Org.BouncyCastle.Asn1.Cms;

namespace proyecto1bases.Models{

    public class Paciente{
    public int CedulaP { get; set; }
    public string Nombre { get; set; }
     public string Apellidos { get; set; }
    public DateTime FechaNacimiento { get; set; }
    public int Edad { get; set; }
    public char Genero { get; set; }  // 'M' para masculino, 'F' para femenino
    public int Ntelefono { get; set; }
    public string CorreoE { get; set; }
    public string Direccion { get; set; }
    public string GrupoSanguineo { get; set; }


    }
    public class Medico
    {
    public int CedulaM { get; set; }
    public string Nombre { get; set; }
    public string Apellidos { get; set; }
    public char Genero { get; set; }  
    public string Experiencia { get; set; }
    public int Ntelefono { get; set; }
    public string CorreoE { get; set; }
    public string NombreEspecialidad { get; set; } 
}

public class Tratamiento{
public int CedulaM { get; set; }
 public int CedulaP { get; set; }
  public int IdTratamiento { get; set; }
 public string Tipo { get; set; }
 public int IdCita { get; set; }  
 public int IdProcedimiento { get; set; }
 public int Ntelefono { get; set; }
 public int duracion { get; set; }
 public string NombreEspecialidad { get; set; }
  public string estado { get; set; }   

}
 public class Cita
    {
        public int IdCita { get; set; }             
        public int CedulaM { get; set; }             
        public int CedulaP { get; set; }             
        public DateTime Fecha { get; set; }          
        public string Motivo { get; set; }           
        public TimeSpan Hora { get; set; }          
        public TimeSpan Duracion { get; set; }       
        public string NombreEspecialidad { get; set; } // Especialidad del médico
    }
    public class Medicamentos
   {
       public int IdCita { get; set; }             
       public int IdTratamiento { get; set; }             
       public int cantidad { get; set; }             
       public string Nombre { get; set; }          
       public int Dosis { get; set; }   
                
   }
      public class Medicamento
  {
      public string Nombre { get; set; }             
      public String patogeno { get; set; }             
      public string EfectosSecundarios { get; set; }             
      public int cantidad { get; set; }          
      public int Dosis { get; set; }           
  }
 public class ResultadoCitas{
    public int IDCita {get; set;} 
    public string Resultado{get; set;}

 }
  public class ProcedimientosQuirurjicos
    {
      
        public int IdProcedimiento { get; set; }

       
        public int CedulaM { get; set; }

        
        public int CedulaP { get; set; }


 public DateTime Fecha { get; set; }

        
        public TimeSpan Hora { get; set; }

      
        public string Motivo { get; set; }

        
        public TimeSpan Duracion { get; set; }
        
        public string Estado { get; set; }

        public string NombreEspecialidad { get; set; }}
 public class PacienteConsulta5
{
    public int CedulaP { get; set; }             // Identificación del paciente
    public string Nombre { get; set; }            // Nombre del paciente
    public string Apellidos { get; set; }         // Apellidos del paciente
    public DateTime FechaNacimiento { get; set; } // Fecha de nacimiento del pacient            
    public string Genero { get; set; }            // Género del paciente
    public string Ntelefono { get; set; }         // Número de teléfono del paciente
    public string CorreoE { get; set; }           // Correo electrónico del paciente
    public string Direccion { get; set; }         // Dirección del paciente
    public string GrupoSanguineo { get; set; }    // Grupo sanguíneo del paciente
    public int CantidadPadecimientos { get; set; } // Cantidad de padecimientos del paciente
    public int Intervenciones { get; set; }       // Cantidad total de intervenciones (procedimientos + citas)
    public int CantidadMedicamentos { get; set; } // Cantidad total de medicamentos prescritos
    public DateTime? FechaUltimaCita { get; set; } // Fecha de la última cita (puede ser null si no hay citas)
}

}