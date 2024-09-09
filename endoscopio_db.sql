CREATE DATABASE IF NOT EXISTS endoscopio_db;

CREATE TABLE Exploraciones (
	id INT AUTO_INCREMENT PRIMARY KEY,
	fecha DATE NOT NULL,
	doctor VARCHAR(100) NOT NULL,
	paciente VARCHAR(100) NOT NULL,
	duracion INT NOT NULL
);

CREATE TABLE Imagenes (
	id INT AUTO_INCREMENT PRIMARY KEY,
    exploracion_id INT,
    url_imagen VARCHAR(255) NOT NULL, 
    FOREIGN KEY (exploracion_id) REFERENCES Exploraciones(id)
);

CREATE TABLE Videos (
	id INT AUTO_INCREMENT PRIMARY KEY,
    exploracion_id INT,
    url_video VARCHAR(255) NOT NULL,
    FOREIGN KEY (exploracion_id) REFERENCES Exploraciones(id)
    );
    
INSERT INTO Exploraciones (fecha, doctor, paciente, duracion) VALUES 
('2024-09-01', 'Dr. Garcia', 'Juan Perez', 30),
('2024-09-02', 'Dr. Lopez', 'Maria Gomez', 25),
('2024-09-03', 'Dr. Martinez', 'Carlos Rivera', 40),
('2024-09-04', 'Dr. Sanchez', 'Lucia Fernandez', 20),
('2024-09-05', 'Dr. Ortiz', 'Luis Mendez', 35),
('2024-09-06', 'Dr. Diaz', 'Ana Suarez', 50),
('2024-09-07', 'Dr. Castro', 'Pedro Morales', 30),
('2024-09-08', 'Dr. Delgado', 'Rosa Ramirez', 15),
('2024-09-09', 'Dr. Perez', 'Sofia Nunez', 60),
('2024-09-10', 'Dr. Ruiz', 'Jorge Sosa', 45);

INSERT INTO Imagenes (exploracion_id, url_imagen) VALUES 
(1, 'https://example.com/imagen1.jpg'),
(2, 'https://example.com/imagen2.jpg'),
(3, 'https://example.com/imagen3.jpg'),
(4, 'https://example.com/imagen4.jpg'),
(5, 'https://example.com/imagen5.jpg');

INSERT INTO Videos (exploracion_id, url_video) VALUES 
(1, 'https://example.com/video1.mp4'),
(2, 'https://example.com/video2.mp4'),
(3, 'https://example.com/video3.mp4'),
(4, 'https://example.com/video4.mp4'),
(5, 'https://example.com/video5.mp4');

select * from exploraciones where doctor = 'Dr. Garcia';

select * from imagenes where exploracion_id = 1;

select count(*) from videos;

select sum(duracion) as total_duracion from exploraciones;

SELECT paciente, url_video 
FROM Exploraciones e
JOIN Videos v ON e.id = v.exploracion_id
ORDER BY duracion DESC LIMIT 1;

