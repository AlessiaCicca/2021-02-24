import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_migliore(self, e):
        migliore=self._model.migliore()
        self._view.txt_result.controls.append(ft.Text(f"GIOCATORE MIGLIORE:"))
        self._view.txt_result.controls.append(ft.Text(f"{migliore[0]}, delta efficienza= {migliore[1]}"))
        self._view.update_page()
    def handle_grafo(self, e):
        match=self._view.dd_match.value
        if match is None:
            self._view.create_alert("Selezionare un match")
            return
        grafo = self._model.creaGrafo(match)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        self._view.update_page()

    def fillDD(self):
        match=self._model.getMatch
        for m in match.keys():
            self._view.dd_match.options.append(ft.dropdown.Option(
                text=m))