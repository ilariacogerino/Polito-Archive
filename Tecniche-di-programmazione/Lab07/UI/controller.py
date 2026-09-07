from functools import lru_cache

import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):
        self._view.lst_result.controls.clear()
        mese = int(self._view.dd_mese.value)
        if mese == None or mese == 0:
            self._view.create_alert("Selezionare un mese!!")
            self._view._page.update()
        umiditaTO = 0
        umiditaMi = 0
        umiditaGe = 0
        countTo = 0
        countMi = 0
        countGe = 0
        situazioniTo = self._model.getSituazioni("Torino", mese)
        for situazione in situazioniTo:
            umiditaTO += situazione.umidita
            countTo += 1

        situazioniMi = self._model.getSituazioni("Milano", mese)
        for situazione in situazioniMi:
            umiditaMi += situazione.umidita
            countMi += 1

        situazioniGe = self._model.getSituazioni("Genova", mese)
        for situazione in situazioniGe:
            umiditaGe += situazione.umidita
            countGe += 1
        print(countTo, countMi, countGe)

        self._view.lst_result.controls.append(ft.Text("L'umidità media nel mese selezionato è:"))
        self._view.lst_result.controls.append(ft.Text(f'Genova: {round(umiditaGe/countGe, 4)}'))
        self._view.lst_result.controls.append(ft.Text(f'Milano: {round(umiditaMi/countMi, 4)}'))
        self._view.lst_result.controls.append(ft.Text(f'Genova: {round(umiditaTO/countTo, 4)}'))
        self._view._page.update()

    @lru_cache(maxsize=None)
    def handle_sequenza(self, e):
        self._view.lst_result.controls.clear()
        mese = int(self._view.dd_mese.value)
        if mese == None or mese == 0:
            self._view.create_alert("Selezionare un mese!!")
            self._view._page.update()
        soluzione, costo = self._model.calcola_sequenza(mese)
        self._view.lst_result.controls.append(ft.Text(f'La sequenza ottima ha costo {costo} ed è:'))
        for situazione in soluzione:
            self._view.lst_result.controls.append(ft.Text(situazione))
        self._view._page.update()

    def read_mese(self, e):
        self._mese = int(e.control.value)



