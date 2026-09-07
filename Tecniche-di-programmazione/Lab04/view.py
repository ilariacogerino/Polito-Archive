import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT

        # Controller
        self.__controller = None

        # UI elements
        self.__title = None
        self.__theme_switch = None
        self.ddLanguage = None
        self.ddModality = None
        self.txtIn = None
        self.btnSpellCheck = None
        self.txtOut = None


    def add_content(self):
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        row1 = ft.Row(controls=[self.__theme_switch, self.__title], spacing=30, alignment=ft.MainAxisAlignment.CENTER)
        self.page.add(row1)

        # select language
        self.ddLanguage = ft.Dropdown(label="Select Language",
                                        options=[ft.DropdownOption("english"), ft.DropdownOption("italian"), ft.DropdownOption("spanish")],
                                        on_change=self.__controller.handleLanguage)
        self.page.add(self.ddLanguage)

        # modality + txtIn + Spell check button
        self.ddModality = ft.Dropdown(label="Search Modality",
                                        options=[ft.DropdownOption("Default"), ft.DropdownOption("Linear"), ft.DropdownOption("Dichotomic")],
                                        on_change=self.__controller.handleModality)
        self.txtIn = ft.TextField(label="Add your sentence here")
        self.btnSpellCheck = ft.ElevatedButton(text="Spell Check",
                                                 on_click=self.__controller.handleSpellCheck)
        row2 = ft.Row(controls=[self.ddModality, self.txtIn, self.btnSpellCheck], alignment=ft.MainAxisAlignment.CENTER)
        self.page.add(row2)

        # listview to write from controller
        self.txtOut = ft.ListView(expand=1, spacing=10)
        self.page.add(self.txtOut)


        self.page.update()


    def update(self):
        self.page.update()


    def setController(self, controller):
        self.__controller = controller


    def theme_changed(self, e):
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        self.page.update()