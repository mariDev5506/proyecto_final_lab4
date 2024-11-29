
-- Script de la base de datos gimnasio_db para el gestor MySQL Workbench


-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema gimnasio_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema gimnasio_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS gimnasio_db DEFAULT CHARACTER SET utf8 ;
USE gimnasio_db ;

-- -----------------------------------------------------
-- Table gimnasio_db.Alumno
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS gimnasio_db.Alumno (
  idAlumno INT NOT NULL AUTO_INCREMENT,
  nombreAlumno VARCHAR(30) NOT NULL,
  apellidoAlumno VARCHAR(30) NOT NULL,
  membresia VARCHAR(20) NOT NULL,
  dniAlumno VARCHAR(8) NOT NULL,
  PRIMARY KEY (idAlumno))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table gimnasio_db.Entrenador
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS gimnasio_db.Entrenador (
  idEntrenador INT NOT NULL AUTO_INCREMENT,
  nombreEntrenador VARCHAR(30) NOT NULL,
  apellidoEntrenador VARCHAR(30) NOT NULL,
  dniEntrenador VARCHAR(8) NOT NULL,
  PRIMARY KEY (idEntrenador))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table gimnasio_db.Presentismo
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS gimnasio_db.Presentismo (
  Entrenador_idEntrenador INT NOT NULL,
  Alumno_idAlumno INT NOT NULL,
  fecha DATE NOT NULL,
  hora TIME NOT NULL,
  PRIMARY KEY (Entrenador_idEntrenador, Alumno_idAlumno),
  INDEX fk_Entrenador_has_Alumno_Alumno1_idx (Alumno_idAlumno ASC),
  INDEX fk_Entrenador_has_Alumno_Entrenador_idx (Entrenador_idEntrenador ASC),
  CONSTRAINT fk_Entrenador_has_Alumno_Entrenador
    FOREIGN KEY (Entrenador_idEntrenador)
    REFERENCES gimnasio_db.Entrenador (idEntrenador)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Entrenador_has_Alumno_Alumno1
    FOREIGN KEY (Alumno_idAlumno)
    REFERENCES gimnasio_db.Alumno (idAlumno)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;