import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleDDYearSelection(self, e):
        pass

    def handleCreaGrafo(self,e):
        anno = self._view._ddAnno.value
        if anno is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f'Selezionare un anno!', color = "red"))
            self._view.update_page()
            return
        anno = int(anno)
        self._model.buildGraph(anno)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f'Grafo creato correttamente'))
        self._view.txt_result.controls.append(ft.Text(f'Numero di nodi: {self._model.getNumNodes()}'))
        self._view.txt_result.controls.append(ft.Text(f'Numero di archi: {self._model.getNumEdges()}'))
        bestDriver, best = self._model.getBestDriver()
        self._view.txt_result.controls.append(ft.Text(f'Best driver: {bestDriver.surname} with score {best}'))

        self._view.update_page()


    def handleCerca(self, e):
        pass

    def fillDDYear(self):
        anni = self._model.getAllAnni()
        for anno in anni:
            self._view._ddAnno. options.append(ft.DropdownOption(text=anno))
        self._view.update_page()