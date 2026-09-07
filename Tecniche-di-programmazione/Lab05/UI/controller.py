import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDCorsi(self):
        corsi = self._model.getAllCorsi()
        for corso in corsi:
            self._view.ddCorsi.options.append(ft.DropdownOption(key=corso.codins,
                                                               text=corso.__str__()))
        self._view._page.update()

    def handleCercaIscritti(self, e):
        corso = self._view.ddCorsi.value
        if corso == "" or corso is None:
            self._view.create_alert("Selezionare un corso!")
            return

        self._view.txt_result.controls.clear()
        self._view._page.update()

        iscritti = self._model.getIscritti(corso)

        self._view.txt_result.controls.append(ft.Text(f'Ci sono {len(iscritti)} iscritti al corso'))
        for iscritto in iscritti:
            self._view.txt_result.controls.append(ft.Text(iscritto))
        self._view.update_page()

    def handleCercaStudente(self, e):
        matricola = self._view.matricola.value

        if matricola == "" or matricola is None:
            self._view.create_alert("Selezionare un matricola!")
            return
        self._view.txt_result.controls.clear()
        self._view._page.update()

        studente = self._model.getMatricola(matricola)
        print(studente)
        self._view.cognome.value = studente.cognome
        self._view.nome.value = studente.nome
        self._view.update_page()

    def handleCercaCorsi(self, e):
        matricola = self._view.matricola.value

        if matricola == "" or matricola is None:
            self._view.create_alert("Selezionare un matricola!")
            return
        self._view.txt_result.controls.clear()
        self._view._page.update()

        corsi = self._model.getCorsi(matricola)
        self._view.txt_result.controls.append(ft.Text(f'Risultano {len(corsi)} corsi'))
        for corso in corsi:
            self._view.txt_result.controls.append(ft.Text(corso))
        self._view.update_page()

    def handleIscrivi(self,e):
        matricola = self._view.matricola.value
        corso = self._view.ddCorsi.value

        if corso == "" or corso is None:
            self._view.create_alert("Selezionare un corso!")
            return

        if matricola == "" or matricola is None:
            self._view.create_alert("Selezionare un matricola!")
            return

        self._view.txt_result.controls.clear()
        self._view._page.update()

        esito = self._model.iscrivi(matricola, corso)
        if esito == True:
            self._view.txt_result.controls.append(ft.Text(f'Studente iscritto!'))
        else:
            self._view.txt_result.controls.append(ft.Text(f'Studente non scritto'))

        self._view.update_page()




