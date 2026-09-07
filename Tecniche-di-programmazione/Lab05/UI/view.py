import flet as ft


class View():
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddCorsi = None
        self.btnCercaIscritti = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("App gestione studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        # corso + btn cerca iscritti
        self.ddCorsi = ft.Dropdown(
            label="corso",
            width=200,
            hint_text="Selezionare un corso"
        )
        self._controller.fillDDCorsi()

        self.btnCercaIscritti = ft.ElevatedButton(text="Cerca Iscritti",
                                                  on_click=self._controller.handleCercaIscritti)

        row1 = ft.Row(controls=[self.ddCorsi, self.btnCercaIscritti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.matricola = ft.TextField(label="matricola")
        self.nome = ft.TextField(label="nome")
        self.cognome = ft.TextField(label="cognome")

        row2 = ft.Row(controls=[self.matricola, self.nome, self.cognome],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.btnCercaStudente = ft.ElevatedButton(text="Cerca Studente",
                                                  on_click=self._controller.handleCercaStudente)
        self.btnCercaCorsi = ft.ElevatedButton(text="Cerca Corsi",
                                               on_click=self._controller.handleCercaCorsi)
        self.btnIscrivi = ft.ElevatedButton(text="Iscrivi",
                                            on_click=self._controller.handleIscrivi)

        row3 = ft.Row(controls=[self.btnCercaStudente, self.btnCercaCorsi, self.btnIscrivi],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

