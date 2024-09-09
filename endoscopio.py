
class Endoscopio:
    def __init__(self):
        self._esta_encendido = False
        self._imagenes = []
        self._videos = []
        self._max_video_duration = 60  # en segundos, por ejemplo
    
    def encender(self):
        self._esta_encendido = True
        print("Endoscopio encendido.")
    
    def apagar(self):
        self._esta_encendido = False
        print("Endoscopio apagado.")
    
    def capturar_imagen(self):
        if self._esta_encendido:
            imagen = f"imagen_{len(self._imagenes) + 1}.jpg"
            self._imagenes.append(imagen)
            print(f"{imagen} capturada.")
            return imagen
        else:
            raise Exception("El endoscopio está apagado, no puede capturar imágenes.")
    
    def capturar_video(self, duracion):
        if self._esta_encendido:
            if duracion > self._max_video_duration:
                raise ValueError(f"La duración del video no puede exceder {self._max_video_duration} segundos.")
            video = f"video_{len(self._videos) + 1}.mp4"
            self._videos.append(video)
            print(f"{video} grabado durante {duracion} segundos.")
            return video
        else:
            raise Exception("El endoscopio está apagado, no puede grabar videos.")
    
    def transmitir_video(self):
        if self._esta_encendido:
            print("Transmitiendo video en tiempo real.")
            return True
        else:
            raise Exception("El endoscopio está apagado, no puede transmitir video.")
    
    def __str__(self):
        estado = "encendido" if self._esta_encendido else "apagado"
        return f"Endoscopio está actualmente {estado}."
