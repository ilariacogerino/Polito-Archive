import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillddStore(self):
        for s in self._model.getAllStores():
            self._view._ddStore.options.append(ft.DropdownOption(s))
        self._view.update_page()

    def handleCreaGrafo(self, e):
        store_id = self._view._ddStore.value
        if store_id is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f'Selezionare uno store!', color = "red"))
            self._view.update_page()
            return

        k = self._view._txtIntK.value
        if k is None or k == "" or k.isdigit() == False:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f'Inserire un valore!', color="red"))
            self._view.update_page()
            return

        store_id = int(store_id)
        k = int(k)
        self._model.buildGraph(store_id, k)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f'Grafo correttamente creato'))
        self._view.txt_result.controls.append(ft.Text(f'Numero di nodi: {self._model.getNumNodes()}'))
        self._view.txt_result.controls.append(ft.Text(f'Numero di nodi: {self._model.getNumEdges()}'))
        self._view.update_page()

    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass
