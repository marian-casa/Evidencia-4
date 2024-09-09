
class Endoscopio:

    def __init__(self):
        self.esta_encendido = False
        self._imagenes = []
        self._videos = []
        self._max_video_duration = 60  #segundos
    
    def encender(self):
        self.esta_encendido= True
        print('Endoscopio encendido.')

    
    def apagar(self):
        self.esta_encendido= False
        print('Endoscopio apagado.')

    def capturar_imagen(self):
        if self.esta_encendido:
            imagen = f"imagen_{len(self._imagenes) +1}.jpg"
            self._imagenes.append(imagen)
            print(f"{imagen} capturada.")
            return imagen
        else:
            raise Exception('El endoscopio esta apagado, no puede capturar imagenes')
    
    def capturar_video(self, duracion):
        if self.esta_encendido:
            if duracion > self._max_video_duration:
                raise ValueError(f'La duracion del video no puede exeder {self._max_video_duration} segundos.')
            video = f'video_{len(self._videos) + 1}.mp4'
            self._videos.append(video)
            print(f'{video} grabando durante {duracion} segundos.')
            return video
        else:
            raise Exception('El endoscopio esta apagado, no puede trasmitir video.')

    
    def __str__(self):
        estado = "encendido" if self.esta_encendido else "apagado"
        return f"El endoscopio esta actualmente {estado}"
