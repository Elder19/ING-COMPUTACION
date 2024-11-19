
create database if not exists sistema_clinica_privada;

use sistema_clinica_privada; 
#tabla para la informacion del paciente
create table if not exists paciente (
	CedulaP int, 
    Nombre varchar (255)not null,
    Apellidos varchar (255) not null,
    fechaNacimiento date not null, 
    Edad int not null, 
	genero ENUM('M', 'F') NOT NULL,
    Ntelefono int not null, 
    CorreoE varchar (255) not null, 
    Direccion varchar (255) not null,
    GrupoSanguineo ENUM('O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-') NOT NULL,
    primary key(cedulaP)
    );
# Tabla secundaria para los detalles del personal
create table if not exists Especialidad(
	NombreEspecialidad varchar (255) not null, 
	primary key (NombreEspecialidad)
  
    
    );
    
# Tabla con la informacion del personalmedico
create table if not exists PersonalMedico (
	CedulaM int, 
    Nombre varchar (255)not null,
    Apellidos varchar (255) not null,
	genero ENUM('M', 'F') NOT NULL,
	Experiencia varchar (255) not null, 
    Ntelefono int not null, 
    CorreoE varchar (255) not null,
    NombreEspecialidad varchar (255) not null, 
    primary key(CedulaM,NombreEspecialidad),
    foreign key(NombreEspecialidad) references Especialidad(NombreEspecialidad)
    );
    
create table if not exists CitasMedicas( 
	IdCita int not null auto_increment,
    CedulaM int not null, 
    CedulaP int not null, 
    Fecha date not null, 
    motivo varchar(255), 
    hora time not null,
    duracion time not null, 
    NombreEspecialidad varchar(255),
    primary key (IdCita),
	foreign key (CedulaM,NombreEspecialidad) references PersonalMedico(CedulaM,NombreEspecialidad), 
    foreign key (CedulaP) references paciente(CedulaP)
    );
    
create table if not exists Padecimiento(
	NombrePadecimiento varchar(255) not null, 
    Sintomas varchar(255) not null,
    primary key (NombrePadecimiento)
);

create table if not exists HistorialPadecimientos(
	NombrePadecimiento varchar(255) not null, 
    CedulaP int not null, 
    FechaInicio date not null,
    Sintomas varchar(255) not null,
    foreign key (NombrePadecimiento) references Padecimiento(NombrePadecimiento) ,
    foreign key (CedulaP) references paciente(CedulaP)
    );
create table if not exists Medicamento(
	Nombre varchar (255) not null, 
    patogeno varchar(255) not null,
    EfectosSecundarios varchar(255) not null, 
    cantidad int not null,
    primary key (Nombre)
);

create table if not exists ProcedimientosQuirurjicos(
	IdProcedimiento int not null auto_increment,
    CedulaM int not null, 
    CedulaP int not null, 
    Fecha date, 
    Hora time, 
    Motivo varchar (255),
    Duracion time ,
	NombreEspecialidad varchar(255),
	primary key (IdProcedimiento),
	foreign key (CedulaP) references paciente(CedulaP),
	foreign key (CedulaM,NombreEspecialidad) references PersonalMedico(CedulaM,NombreEspecialidad)
    
);




create table if not exists ResultadosCita(
	IdCita int not null, 
    Resultado varchar(255) not null,
    foreign key (IdCita) references CitasMedicas(idCita)
    );
    
    
    
    
Create table if not exists TratamientoPrescrito(
	IdTratamiento int not null auto_increment, 
    IDCita int null, 
    IdProcedimiento int null, 
    CedulaM int not null,
    CedulaP int not null,
    tipo varchar (255) not null,
    duracion time not null,
    NombreEspecialidad varchar(255)not null,
    primary key (IdTratamiento),
    foreign key (IDCita) references CitasMedicas(IDCita),
    foreign key (CedulaM,NombreEspecialidad) references PersonalMedico(CedulaM,NombreEspecialidad),
     foreign key (CedulaP) references paciente(CedulaP),
    foreign key (IdProcedimiento) references ProcedimientosQuirurjicos(IdProcedimiento)
);

create table if not exists Medicamentos(
	IdTratamiento int not null, 
    cantidad int not null,
    Nombre varchar(255) not null,
    Dosis int not null,
    foreign key (IdTratamiento) references TratamientoPrescrito(IdTratamiento),
    foreign key (Nombre) references Medicamento(Nombre)

);
create table if not exists PersonalParticipante(
	IdProcedimiento int not null,
    CedulaM int not null, 
    NombreEspecialidad varchar(255),
	foreign key (CedulaM,NombreEspecialidad) references PersonalMedico(CedulaM,NombreEspecialidad),
    foreign key (IdProcedimiento) references ProcedimientosQuirurjicos(IdProcedimiento)
);
create table if not exists ResultadoProcedimiento(
	IdProcedimiento int not null,
    Epicrisis varchar(255) not null, 
   foreign key (IdProcedimiento) references ProcedimientosQuirurjicos(IdProcedimiento)
);
create table if not exists historialCP (
	CedulaP int not null, 
    IdCita int null, 
    IdProcedimiento int null,
	foreign key (IdCita) references CitasMedicas(idCita),
	foreign key (CedulaP) references paciente(CedulaP),
	foreign key (IdProcedimiento) references ProcedimientosQuirurjicos(IdProcedimiento)
);
    

#drop database sistema_clinica_privada;
#drop table HistorialPadecimientos;