DROP TABLE IF EXISTS candidatos;
DROP TABLE IF EXISTS partidos;
DROP TABLE IF EXISTS votos;
CREATE TABLE candidatos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  partido INTEGER NOT NULL,
  FOREIGN KEY (partido) REFERENCES partidos (id)
);
CREATE TABLE partidos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL
);
CREATE TABLE votos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  candidato INTEGER NOT NULL,
  partido INTEGER NOT NULL,
  fecha DATE NOT NULL,
  FOREIGN KEY (candidato) REFERENCES candidatos (id),
  FOREIGN KEY (partido) REFERENCES partidos (id)
);
INSERT INTO candidatos (nombre, partido) VALUES ("Juan Pérez", 1);
INSERT INTO candidatos (nombre, partido) VALUES ("María García", 2);
INSERT INTO partidos (nombre) VALUES ("Partido Liberal");
INSERT INTO partidos (nombre) VALUES ("Partido Conservador");
INSERT INTO votos (candidato, partido, fecha) VALUES (1, 1, "2023-07-20");
INSERT INTO votos (candidato, partido, fecha) VALUES (2, 2, "2023-07-21");