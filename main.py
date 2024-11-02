from views.splash_screen import Splash
from views.home_screen import HomeScreen, ViewAll
from views.place_screen import PlaceScreen

import flet as ft

def main(page: ft.Page) -> None:
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 380
    page.window.height = 750
    page.window.top = 1
    page.window.right = 2
    page.window.always_on_top = True

    page.fonts = {
        "Lobster": "fonts/Lobster-Regular.ttf",
        "Roboto": "fonts/Roboto-Medium.ttf",
        "Montserrat": "fonts/Montserrat-VariableFont_wght.ttf",
        "Inter": "fonts/Inter-VariableFont_opsz,wght.ttf",
        "NotoSerifOriya": "NotoSerifOriya-VariableFont_wght.ttf"
    }

    def router(_) -> None:
        page.views.clear()
        match page.route:
            case "/":
                page.views.append(Splash())
            case "/home":
                page.views.append(HomeScreen(page))
            case "/place":
                page.views.append(PlaceScreen(page))
            case "/view_all":
                page.views.append(ViewAll())
            case _:
                page.views.append(Splash())
        page.update()

    page.on_route_change = router
    page.go("/")
    page.update()


ft.app(target=main, assets_dir="assets")
