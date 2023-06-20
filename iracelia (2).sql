create database clinica;

use clinica;

show tables;

create table especialidades(
id int primary key auto_increment,
    nome varchar (45)
);

create table medicos(
	id int primary key auto_increment,
    nome varchar (45),
    crm varchar (255),
    id_especialidade int, 
    foreign key (id_especialidade) references especialidades(id)
);

insert into medicos(nome, crm, especialidades) values ("iracelia", "98765", "psicologa");
insert into especialidas(nome) values ("psicologia");

select * from medicos;
select * from especialidades;
