import json
import requests
import speech_recognition
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineIconListItem

Window.size = (360, 590)
r = speech_recognition.Recognizer()

help_str = '''
ScreenManager:
    WelcomeScreen:
    MainScreen:
    LoginScreen:
    SignupScreen:
    MessageScreen:

<WelcomeScreen>:
    name:'welcomescreen'
    Image:
        source: 'logo.jpg'
        size_hint: (None,None)
        pos_hint : {'center_x':0.5,'center_y':0.55}
        width: "480dp"
        height: "480dp"
    MDLabel:
        text:'By The Technocrats'
        font_style:'Caption'
        halign:'center'
        pos_hint: {'center_y':0.2}
    MDFloatingActionButton:
        icon:'account-arrow-right'
        md_bg_color: app.theme_cls.primary_color
        elevation_normal: 8
        pos_hint : {'center_x':0.85,'center_y':0.1}
        size_hint: (None,None)
        on_press: 
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'left'

<LoginScreen>:
    name:'loginscreen'
    Image:
        source: 'pv.jpg'
        size_hint: (None,None)
        pos_hint : {'center_x':0.5,'center_y':0.8}
        width: "300dp"
        height: "100dp"
    MDTextField:
        id:login_email
        pos_hint: {'center_y':0.62,'center_x':0.5}
        size_hint : (None,None)
        width: 300
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'email'
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDTextField:
        id:login_password
        pos_hint: {'center_y':0.5,'center_x':0.5}
        size_hint : (None,None)
        width: 300
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'eye-off'
        icon_right_color: app.theme_cls.primary_color
        required: True
        password: True
    MDRaisedButton:
        text:'                                      Login                                   '
        size_hint: (None,None)
        width: 80
        height: 40
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.login()
            app.username_changer() 
    MDTextButton:
        text: 'New user? Sign Up'
        size_hint: (None,None)
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'up'
<SignupScreen>:
    name:'signupscreen'
    Image:
        source: 'pv.jpg'
        size_hint: (None,None)
        pos_hint : {'center_x':0.5,'center_y':0.85}
        width: "300dp"
        height: "100dp"
    MDTextField:
        id:signup_email
        pos_hint: {'center_y':0.57,'center_x':0.5}
        size_hint : (None,None)
        width: 300
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'email'
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.69,'center_x':0.5}
        size_hint : (None,None)
        width: 300
        hint_text: 'Username'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.45,'center_x':0.5}
        size_hint : (None,None)
        width: 300
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'eye-off'
        icon_right_color: app.theme_cls.primary_color
        required: True
        password: True
    MDRaisedButton:
        text:'                                      Signup                                   '
        size_hint: (None,None)
        width: 60
        height: 40
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: app.signup()
    MDTextButton:
        text: 'Already have an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'


<MainScreen>:
    name: 'mainscreen'
    MDBoxLayout:
        orientation: 'vertical'
        MDBottomNavigation:

            MDBottomNavigationItem:
                name: 'mainscreen'
                icon: 'home'
                MDToolbar:
                    title: '                   Power vocab'
                    right_action_items: [["message", lambda x: app.message()]]
                    elevation:8
                    pos_hint: {"top": 1}
                MDCard:
                    orientation: "vertical"
                    padding: "8dp"
                    size_hint: None, None
                    size: "280dp", "380dp"
                    pos_hint: {"center_x": .5, "center_y": .44}
                    MDLabel:
                        text: "DATE"
                        theme_text_color: "Secondary"
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDSeparator:
                        height: "1dp"
                    MDLabel:
                        text: "WORD"
                        halign: "center"
                    MDIconButton:
                        icon: "volume-high"
                        halign: "center"
                    MDSeparator:
                        height: "1dp"
                    MDLabel:
                        text: "MEANING"
                        halign: "center"

            MDBottomNavigationItem:
                name: 'dictionaryscreen'
                icon: 'book'
                MDIconButton:
                    icon: "magnify"
                    pos_hint: {"center_x": .92, "center_y": .94}
                    on_press: root.manager.current = 'mainscreen'
                MDIconButton:
                    icon: "microphone"
                    pos_hint: {"center_x": .08, "center_y": .94}
                    
                MDTextFieldRound:
                    id: search_here
                    hint_text: "search"
                    size_hint : (None,None)
                    width: 230
                    pos_hint: {'center_y':0.94,'center_x':0.5}
                MDLabel:
                    text: 'all words appear here'
                    halign: "center"


            MDBottomNavigationItem:
                name: 'settingscreen'                
                icon: 'settings'
                MDToolbar:
                    title: '                         Settings'
                    elevation:8
                    pos_hint: {"top": 1}
                MDLabel:
                    text: 'settings screen'
                    halign: "center"

            MDBottomNavigationItem:
                name: 'profilescreen'
                icon: 'account'
                MDToolbar:
                    title: '                          Profile'
                    elevation:8
                    pos_hint: {"top": 1}
                MDLabel:
                    text: 'profile screen'
                    halign: "center"
<MessageScreen>:
    name: 'messagescreen'
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Direct Messages'
            left_action_items: [["keyboard-backspace", lambda x: app.back()]]
            elevation:8
        MDLabel:
            text: 'message screen'
            halign: "center"                   

'''


class WelcomeScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class SignupScreen(Screen):
    pass


class MessageScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='loginscreen'))
sm.add_widget(MainScreen(name='mainscreen'))
sm.add_widget(LoginScreen(name='loginscreen'))
sm.add_widget(SignupScreen(name='signupscreen'))
sm.add_widget(SignupScreen(name='profilescreen'))


class PowerVocabApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(help_str)
        self.url = "https://powervocab-4a606-default-rtdb.firebaseio.com/.json"
        return self.strng

    def signup(self):
        signupEmail = self.strng.get_screen('signupscreen').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupscreen').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupscreen').ids.signup_username.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Input', text='Please Enter a valid Input', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split()) > 1:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Username', text='Please enter username without space',
                                   size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            print(signupEmail, signupPassword)
            signup_info = str(
                {f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            signup_info = signup_info.replace(".", "-")
            signup_info = signup_info.replace("\'", "")
            to_database = json.loads(signup_info)
            print((to_database))
            requests.patch(url=self.url, json=to_database)
            self.strng.get_screen('loginscreen').manager.current = 'loginscreen'

    auth = 'LfNAKTEiDrA9CxibQ1v2nKN8nNaH2GhXe7NFxk0o'

    def login(self):
        loginEmail = self.strng.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.strng.get_screen('loginscreen').ids.login_password.text

        self.login_check = False
        supported_loginEmail = loginEmail.replace('.', '-')
        supported_loginPassword = loginPassword.replace('.', '-')
        request = requests.get(self.url + '?auth=' + self.auth)
        data = request.json()
        emails = set()
        for key, value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.login_check = True
            self.strng.get_screen('mainscreen').manager.current = 'mainscreen'
        else:
            print("user no longer exists")

    def close_username_dialog(self, obj):
        self.dialog.dismiss()

    def back(self):
        self.strng.get_screen('mainscreen').manager.current = 'mainscreen'

    def message(self):
        self.strng.get_screen('messagescreen').manager.current = 'messagescreen'

    def username_changer(self):
        if self.login_check:
            self.strng.get_screen('mainscreen')


PowerVocabApp().run()
