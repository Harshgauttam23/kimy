from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def append_row_to_spreadsheet(spreadsheet_title, worksheet_index, data):
    t1 = datetime.now()
    
    # Set up credentials and access the Google Sheets API
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
    print(creds)
    client = gspread.authorize(creds)
    # Open the desired spreadsheet using its title
    spreadsheet = client.open(spreadsheet_title)
    # Select the specific worksheet within the spreadsheet
    worksheet = spreadsheet.get_worksheet(worksheet_index)

    # Append data as a new row to the worksheet
    worksheet.append_row(data)

    t2 = datetime.now()
    print("Data has been appended to the spreadsheet.")
    print("Time taken:", t2 - t1)

# Define data to append


# Call the function to append the data to the spreadsheet


















screen_helper = """

ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name: 'login'
    MDTextField:
        id: username_field
        hint_text: "Enter username"
        helper_text: "Forgot username no problem "
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        size_hint_x:None
        width:300
        
    MDTextField:
        id: password_field
        hint_text: "Password"
        helper_text: "Forgot password? No problem, just click on Login"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:300
        
    MDRectangleFlatButton:
        text: 'Login'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: app.login()
        
<UploadScreen>:
    name: 'upload'
    MDTextField:
        id: Part_field
        hint_text: "Enter Part no."
        helper_text: "Forgot Part no. no problem "
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id: Sr_field
        hint_text: "Serial No."
        helper_text: "Forgot Serial No.? koi baat nhi"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:300

    MDTextField:
        id: Problem_field
        hint_text: "Problem Reported"
        helper_text: "Forgot this ? rehne do phir"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        size_hint_x:None
        width:300   
    MDRectangleFlatButton:
        text: 'Submit'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: app.b()
        
"""


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


# Create the screen manager


class DemoApp(MDApp):



    def b(self):
        username = self.root.get_screen('login').ids.username_field.text
        password = self.root.get_screen('login').ids.password_field.text
        
        part = self.root.get_screen('upload').ids.Part_field.text
        serial = self.root.get_screen('upload').ids.Sr_field.text
        problem = self.root.get_screen('upload').ids.Problem_field.text

        print(username,password,part,serial,problem)
        new_data = [username,password,part,serial,problem]
        append_row_to_spreadsheet('NEPO', 0, new_data)



    


    def login(self):
        # Get input values from the text fields
        username = self.root.get_screen('login').ids.username_field.text
        password = self.root.get_screen('login').ids.password_field.text
       
        # Perform login logic here (e.g., validate credentials)
        # For this example, let's assume valid credentials always
        self.root.current = 'upload'  # Switch to the menu screen after successful login
        print(username,password)

    def build(self):
        screen = Builder.load_string(screen_helper)
        self.root = ScreenManager()
        self.root.add_widget(MenuScreen(name='login'))
        self.root.add_widget(ProfileScreen(name='profile'))
        self.root.add_widget(UploadScreen(name='upload'))

        
        
        return screen


DemoApp().run()