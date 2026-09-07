import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillddAnno(self):
        self._view.anno.options.append(ft.DropdownOption(text="Nessun filtro"))
        anni = self._model.getAnni()
        for anno in anni:
            self._view.anno.options.append(ft.DropdownOption(text=anno))

    def fillddBrand(self):
        self._view.brand.options.append(ft.DropdownOption(text="Nessun filtro"))
        brands = self._model.getBrand()
        for brand in brands:
            self._view.brand.options.append(ft.DropdownOption(text=brand))

    def fillddRetailer(self):
        self._view.retailer.options.append(ft.DropdownOption(text="Nessun filtro"))
        retailers = self._model.getAllRetailer()
        for retailer in retailers:
            self._view.retailer.options.append(ft.DropdownOption(key = retailer.Retailer_code,
                                                                 text=retailer,
                                                                 data=retailer,
                                                                 on_click=self.read_retailer))

    def read_retailer(self, e):
        self.retailer = e.control.data


    def handleTopVendite(self, e):
        self._view.txt_result.controls.clear()
        anno = self._view.anno.value
        if anno == "Nessun filtro":
            anno = anno
        else:
            anno = int(anno)
        brand = self._view.brand.value
        retailer = self._view.retailer.value
        if retailer == "Nessun filtro":
            retailer = retailer
        else:
            retailer = int(retailer)
        print(retailer, anno, brand)
        sales = self._model.getAllSales()
        topSales = []

        if (anno == "Nessun filtro" and brand == "Nessun filtro" and retailer == "Nessun filtro"):
            topSales = sales[:5]
        elif (anno != "Nessun filtro" and brand != "Nessun filtro" and retailer != "Nessun filtro"):
            for sale in sales:
                if(sale.Date.year == anno and sale.Product_brand == brand and sale.Retailer_code == retailer):
                    topSales.append(sale)
        elif (anno == "Nessun filtro" and brand != "Nessun filtro" and retailer != "Nessun filtro"):
            for sale in sales:
                if (sale.Product_brand == brand and sale.Retailer_code == retailer):
                    topSales.append(sale)
        elif (anno == "Nessun filtro" and brand == "Nessun filtro" and retailer != "Nessun filtro"):
            for sale in sales:
                if (sale.Retailer_code == retailer):
                    topSales.append(sale)
        elif (anno == "Nessun filtro" and brand != "Nessun filtro" and retailer == "Nessun filtro"):
            for sale in sales:
                if (sale.Product_brand == brand):
                    topSales.append(sale)
        elif (anno != "Nessun filtro" and brand == "Nessun filtro" and retailer == "Nessun filtro"):
            for sale in sales:
                if (sale.Date.year == anno):
                    topSales.append(sale)
        elif (anno != "Nessun filtro" and brand == "Nessun filtro" and retailer != "Nessun filtro"):
            for sale in sales:
                if (sale.Date.year == anno and sale.Retailer_code == retailer):
                    topSales.append(sale)
        elif (anno != "Nessun filtro" and brand != "Nessun filtro" and retailer == "Nessun filtro"):
            for sale in sales:
                if (sale.Date.year == anno and sale.Product_brand == brand):
                    topSales.append(sale)

        topSales = topSales[:5]
        for sale in topSales:
            self._view.txt_result.controls.append(ft.Text(sale))
        self._view.update_page()


    def handleAnalizzaVendite(self, e):
        self._view.txt_result.controls.clear()
        anno = self._view.anno.value
        if anno == "Nessun filtro":
            anno = anno
        else:
            anno = int(anno)
        brand = self._view.brand.value
        retailer = self._view.retailer.value
        if retailer == "Nessun filtro":
            retailer = retailer
        else:
            retailer = int(retailer)
        print(retailer, anno, brand)
        sales = self._model.getAllSales()
        allSales = []

        if (anno == "Nessun filtro" and brand == "Nessun filtro" and retailer == "Nessun filtro"):
            allSales = sales
        elif (anno != "Nessun filtro" and brand != "Nessun filtro" and retailer != "Nessun filtro"):
            for sale in sales:
                if (sale.Date.year == anno and sale.Product_brand == brand and sale.Retailer_code == retailer):
                    allSales.append(sale)
        elif (anno == "Nessun filtro" and brand != "Nessun filtro" and retailer != "Nessun filtro"):
            for sale in sales:
                if (sale.Product_brand == brand and sale.Retailer_code == retailer):
                    allSales.append(sale)
        elif (anno == "Nessun filtro" and brand == "Nessun filtro" and retailer != "Nessun filtro"):
            for sale in sales:
                if (sale.Retailer_code == retailer):
                    allSales.append(sale)
        elif (anno == "Nessun filtro" and brand != "Nessun filtro" and retailer == "Nessun filtro"):
            for sale in sales:
                if (sale.Product_brand == brand):
                    allSales.append(sale)
        elif (anno != "Nessun filtro" and brand == "Nessun filtro" and retailer == "Nessun filtro"):
            for sale in sales:
                if (sale.Date.year == anno):
                    allSales.append(sale)
        elif (anno != "Nessun filtro" and brand == "Nessun filtro" and retailer != "Nessun filtro"):
            for sale in sales:
                if (sale.Date.year == anno and sale.Retailer_code == retailer):
                    allSales.append(sale)
        elif (anno != "Nessun filtro" and brand != "Nessun filtro" and retailer == "Nessun filtro"):
            for sale in sales:
                if (sale.Date.year == anno and sale.Product_brand == brand):
                    allSales.append(sale)

        giroAffari = 0
        numVendite = 0
        totRetailer = []
        totProduct = []

        for sale in allSales:
            giroAffari += sale.Revenue
            numVendite += 1
            totRetailer.append(sale.Retailer_code)
            totProduct.append(sale.Product_number)

        totRetailer = list(set(totRetailer))
        totProduct = list(set(totProduct))
        numRetailer = len(totRetailer)
        numProduct = len(totProduct)

        self._view.txt_result.controls.append(ft.Text(f'Statistiche vendite:'))
        self._view.txt_result.controls.append(ft.Text(f'Giro di affari: {giroAffari}'))
        self._view.txt_result.controls.append(ft.Text(f'Numero vendite: {numVendite}'))
        self._view.txt_result.controls.append(ft.Text(f'Numero retailer coinvolti: {numRetailer}'))
        self._view.txt_result.controls.append(ft.Text(f'Numero profdotti coinvolti: {numProduct}'))

        self._view.update_page()
