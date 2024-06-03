from playwright.sync_api import Page


class EcoImpactPage:
    """ Базовый класс работы со страницами. """
    ECO_IMPACT_PATH = "/avito-care/eco-impact"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        """ Открытие страницы. """
        self.page.goto(self.ECO_IMPACT_PATH)
        return self

    def screenshot_element(self, screen_path: str, locator: str):
        """ Создание скриншота элемента. """
        element = self.page.locator(locator)
        element.scroll_into_view_if_needed()
        element.screenshot(path=screen_path)
