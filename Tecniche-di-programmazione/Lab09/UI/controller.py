import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaAeroporti(self, e):
        self._view.txt_result.controls.clear()
        distance = self._view.txt_distance.value

        if distance == "" or distance is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f'Inserire una distanza minima!',
                                                          color = "red"))
            self._view.update_page()
            return

        self._model.buildGraph(distance)

        self._view.txt_result.controls.append(ft.Text(f'Numero di vertici del grafo: {self._model.getNumNodes()}'))
        self._view.txt_result.controls.append(ft.Text(f'Numero di archi del grafo: {self._model.getNumEdges()}'))

        self._view.update_page()
