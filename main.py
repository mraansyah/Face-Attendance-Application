from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.lang import Builder

from faceAttendance import face_attendance


Builder.load_file("homepage.kv")
Builder.load_file("absen_masuk.kv")
Builder.load_file("absen_keluar.kv")



class HomePage(MDScreen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	pass

class AbsenMasuk(MDScreen):
	pass

class AbsenKeluar(MDScreen):
    pass

class ScreenManager(ScreenManager):
	pass

class FaceAttendance(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Attendance(MDApp):
    def build(self):
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(HomePage(name='home_page'))
        self.screen_manager.add_widget(AbsenMasuk(name='absen_masuk'))
        self.screen_manager.add_widget(AbsenKeluar(name='absen_keluar'))
        return self.screen_manager
	
    def change_screen(self, screen_name):
        self.screen_manager.transition = SlideTransition(direction='left')
        self.screen_manager.current = screen_name

    def change_screen2(self, screen_name):
        self.screen_manager.transition = SlideTransition(direction='right')
        self.screen_manager.current = screen_name

    def go_to_face_attendance(self):
        face_attendance()

if __name__ == "__main__":
	Attendance().run()