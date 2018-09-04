
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';
--
-- Base de datos: `sddb`
--
CREATE DATABASE sddb;
use sddb;
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autor`
--


CREATE TABLE IF NOT EXISTS `autor` (
  `idautor` int(11) NOT NULL,
  `nombreautor` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idautor`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `autor`
--

INSERT INTO `autor` (`idautor`, `nombreautor`) VALUES
(1, 'José Madero'),
(2, 'Blackpink');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cancion`
--

CREATE TABLE IF NOT EXISTS `cancion` (
  `idcancion` int(11) NOT NULL,
  `nombrecancion` varchar(45) DEFAULT NULL,
  `albumcancion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idcancion`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `cancion`
--

INSERT INTO `cancion` (`idcancion`, `nombrecancion`, `albumcancion`) VALUES
(1, 'Fantasmas', 'Noche'),
(2, 'El ser supremo', 'Noche'),
(3, 'Stay', 'Square two'),
(4, 'Whistle', 'Squere One');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cancion_autor`
--

CREATE TABLE IF NOT EXISTS `cancion_autor` (
  `idcancion_autor` int(11) NOT NULL,
  `cancion_idcancion` int(11) NOT NULL,
  `autor_idautor` int(11) NOT NULL,
  PRIMARY KEY (`idcancion_autor`,`cancion_idcancion`,`autor_idautor`),
  KEY `fk_cancion_autor_cancion_idx` (`cancion_idcancion`),
  KEY `fk_cancion_autor_autor1_idx` (`autor_idautor`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `cancion_autor`
--

INSERT INTO `cancion_autor` (`idcancion_autor`, `cancion_idcancion`, `autor_idautor`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 2),
(4, 4, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cancion_genero`
--

CREATE TABLE IF NOT EXISTS `cancion_genero` (
  `idcancion_genero` int(11) NOT NULL,
  `cancion_idcancion` int(11) NOT NULL,
  `genero_idgenero` int(11) NOT NULL,
  PRIMARY KEY (`idcancion_genero`,`cancion_idcancion`,`genero_idgenero`),
  KEY `fk_cancion_genero_cancion1_idx` (`cancion_idcancion`),
  KEY `fk_cancion_genero_genero1_idx` (`genero_idgenero`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `cancion_genero`
--

INSERT INTO `cancion_genero` (`idcancion_genero`, `cancion_idcancion`, `genero_idgenero`) VALUES
(1, 1, 1),
(2, 3, 3),
(3, 4, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero`
--

CREATE TABLE IF NOT EXISTS `genero` (
  `idgenero` int(11) NOT NULL,
  `nombregenero` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idgenero`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `genero`
--

INSERT INTO `genero` (`idgenero`, `nombregenero`) VALUES
(1, 'pop'),
(2, 'rock'),
(3, 'k-pop');

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cancion_autor`
--
ALTER TABLE `cancion_autor`
  ADD CONSTRAINT `fk_cancion_autor_autor1` FOREIGN KEY (`autor_idautor`) REFERENCES `autor` (`idautor`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_cancion_autor_cancion` FOREIGN KEY (`cancion_idcancion`) REFERENCES `cancion` (`idcancion`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `cancion_genero`
--
ALTER TABLE `cancion_genero`
  ADD CONSTRAINT `fk_cancion_genero_cancion1` FOREIGN KEY (`cancion_idcancion`) REFERENCES `cancion` (`idcancion`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_cancion_genero_genero1` FOREIGN KEY (`genero_idgenero`) REFERENCES `genero` (`idgenero`) ON DELETE NO ACTION ON UPDATE NO ACTION;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
