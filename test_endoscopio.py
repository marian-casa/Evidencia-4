import unittest
from endoscopio import Endoscopio


class TestEndoscopio(unittest.TestCase):
    
    def setUp(self):
        self.endoscopio = Endoscopio()
    
    def test_encender_apagar(self):
        self.endoscopio.encender()
        self.assertTrue(self.endoscopio._esta_encendido)
        self.endoscopio.apagar()
        self.assertFalse(self.endoscopio._esta_encendido)
    
    def test_captura_imagen_con_endoscopio_apagado(self):
        with self.assertRaises(Exception):
            self.endoscopio.capturar_imagen()
    
    def test_captura_imagen_con_endoscopio_encendido(self):
        self.endoscopio.encender()
        imagen = self.endoscopio.capturar_imagen()
        self.assertEqual(imagen, "imagen_1.jpg")
    
    def test_transmision_video_con_endoscopio_apagado(self):
        with self.assertRaises(Exception):
            self.endoscopio.transmitir_video()
    
    def test_transmision_video(self):
        self.endoscopio.encender()
        self.assertTrue(self.endoscopio.transmitir_video())
    
    def test_capturar_video(self):
        self.endoscopio.encender()
        video = self.endoscopio.capturar_video(30)
        self.assertEqual(video, "video_1.mp4")
    
    def test_capturar_video_con_duracion_excesiva(self):
        self.endoscopio.encender()
        with self.assertRaises(ValueError):
            self.endoscopio.capturar_video(70)

if __name__ == '__main__':
    unittest.main()


