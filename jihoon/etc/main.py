import flet as ft
from basic_calc import CalculatorApp as BasicCalculator
from engineering_calc import CalculatorApp as EngineeringCalculator


def main(page: ft.Page):

    def show_basic(e=None):
        page.controls.clear()
        page.add(BasicCalculator(show_engineering))
        page.update()

    def show_engineering(e=None):
        page.controls.clear()
        page.add(EngineeringCalculator(show_basic))
        page.update()

    show_basic()


ft.run(main)