from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivymd.uix.floatlayout import MDFloatLayout
import sqlite3
import os
import sys
import webbrowser

Window.size = (300, 500)

KV = '''
<SplashScreen>:
    name: 'splash'
    Image:
        source: 'image/bg.png'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint: (1, 1)
        allow_stretch: True
        keep_ratio: False  # Ensure the image stretches to fill the screen

    Image:
        source: 'image/logo.png'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        size_hint: (0.6, 0.3)
        allow_stretch: False
        keep_ratio: False

    Image:
        source: 'image/pizza.png'
        pos_hint: {'center_x': 1, 'center_y': 0.1}
        size_hint: (0.8, 0.6)
        allow_stretch: False
        keep_ratio: False

    Label:
        text: 'El Pizza'
        font_name: 'Roboto'
        font_size: '55sp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        outline_width: 2
        outline_color: (1, 0, 0, 1)

    Button:
        text: 'Next'
        background_color: (1, 0, 0, 1)
        size_hint: (.4, .1)
        pos_hint: {'center_x': .5, 'y': 0.1}
        on_release: root.go_to_login()


<LoginScreen>:
    MDFloatLayout:

        MDLabel:
            text: "Log in"
            font_style: "H4"
            pos_hint: {"center_x": 0.5, "center_y": 0.9}
            halign: "center"

        MDTextField:
            id: email
            hint_text: "Email Address"
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
            size_hint_x: 0.8

        MDTextField:
            id: password
            hint_text: "Password"
            pos_hint: {"center_x": 0.5, "center_y": 0.65}
            size_hint_x: 0.8
            password: True
            icon_right: "eye-off"
            icon_right_color: app.theme_cls.primary_color
            on_text_validate: app.login()

        MDIconButton:
            id: eye_icon
            icon: "eye-off"
            pos_hint: {"center_x": 0.9, "center_y": 0.65}
            on_release: app.show_password()

        MDTextButton:
            text: "Forgot Password?"
            pos_hint: {"center_x": 0.5, "center_y": 0.57}
            theme_text_color: "Custom"
            text_color: 1, 0, 0, 1

        MDRaisedButton:
            text: "Log in"
            pos_hint: {"center_x": 0.5, "center_y": 0.45}
            size_hint_x: 0.6
            md_bg_color: 1, 0, 0, 1
            on_release: app.login()

        MDTextButton:
            text: "Don't have an account? Sign up"
            pos_hint: {"center_x": 0.5, "center_y": 0.35}
            theme_text_color: "Custom"
            text_color: 0, 0, 1, 1
            on_release: app.go_to_signup()

        MDLabel:
            text: "OR"
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            halign: "center"

        MDFlatButton:
            text: "Sign in with Google"
            pos_hint: {"center_x": 0.5, "center_y": 0.25}
            size_hint_x: 0.8
            on_release: app.open_google_login()

        MDFlatButton:
            text: "Sign in with Facebook"
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            size_hint_x: 0.8
            on_release: app.open_facebook_login()

<SignupScreen>:
    MDFloatLayout:

        MDLabel:
            text: "Sign Up"
            font_style: "H4"
            pos_hint: {"center_x": 0.5, "center_y": 0.9}
            halign: "center"

        MDTextField:
            id: email
            hint_text: "Email Address"
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
            size_hint_x: 0.8

        MDTextField:
            id: password
            hint_text: "Password"
            pos_hint: {"center_x": 0.5, "center_y": 0.65}
            size_hint_x: 0.8
            password: True
            icon_right: "eye-off"
            icon_right_color: app.theme_cls.primary_color
            on_text_validate: app.signup()

        MDTextField:
            id: confirm_password
            hint_text: "Confirm Password"
            pos_hint: {"center_x": 0.5, "center_y": 0.55}
            size_hint_x: 0.8
            password: True
            icon_right: "eye-off"
            icon_right_color: app.theme_cls.primary_color
            on_text_validate: app.signup()

        MDIconButton:
            id: eye_icon_signup
            icon: "eye-off"
            pos_hint: {"center_x": 0.9, "center_y": 0.55}
            on_release: app.show_password_signup()

        MDRaisedButton:
            text: "Sign Up"
            pos_hint: {"center_x": 0.5, "center_y": 0.45}
            size_hint_x: 0.6
            md_bg_color: 1, 0, 0, 1
            on_release: app.signup()
'''


class SplashScreen(Screen):
    def go_to_login(self):
        self.manager.current = 'login'


class LoginScreen(Screen):
    pass


class SignupScreen(Screen):
    pass


class LoginApp(MDApp):
    def build(self):
        self.create_database()
        Builder.load_string(KV)  # Load the KV string
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignupScreen(name='signup'))
        return sm

    def create_database(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def login(self):
        email = self.root.get_screen('login').ids.email.text
        password = self.root.get_screen('login').ids.password.text
        self.cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (email, password))
        user = self.cursor.fetchone()
        if user:
            print(f"Welcome {user[1]}!")
            self.launch_builder_script()
        else:
            print("Invalid username or password")

    def signup(self):
        email = self.root.get_screen('signup').ids.email.text
        password = self.root.get_screen('signup').ids.password.text
        confirm_password = self.root.get_screen('signup').ids.confirm_password.text
        if password == confirm_password:
            try:
                self.cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)',
                                    (email, password, 'user'))
                self.conn.commit()
                print("User registered successfully!")
                self.launch_builder_script()
            except sqlite3.IntegrityError:
                print("Email already exists")
        else:
            print("Passwords do not match")

    def go_to_signup(self):
        self.root.current = 'signup'

    def open_google_login(self):
        webbrowser.open('https://accounts.google.com/signin')

    def open_facebook_login(self):
        webbrowser.open('https://www.facebook.com/login/')

    def launch_builder_script(self):
        self.stop()
        os.system(f'{sys.executable} main.py')

    def on_stop(self):
        self.conn.close()

    def show_password(self):
        password_field = self.root.get_screen('login').ids.password
        eye_icon = self.root.get_screen('login').ids.eye_icon
        if password_field.password:
            password_field.password = False
            eye_icon.icon = "eye"
        else:
            password_field.password = True
            eye_icon.icon = "eye-off"

    def show_password_signup(self):
        password_field = self.root.get_screen('signup').ids.password
        confirm_password_field = self.root.get_screen('signup').ids.confirm_password
        eye_icon = self.root.get_screen('signup').ids.eye_icon_signup
        if password_field.password:
            password_field.password = False
            confirm_password_field.password = False
            eye_icon.icon = "eye"
        else:
            password_field.password = True
            confirm_password_field.password = True
            eye_icon.icon = "eye-off"


if __name__ == '__main__':
    LoginApp().run()
