import os

import pytest
from playwright.sync_api import Page

from task_2.output import OUTPUT_DIR_PATH
from task_2.locators.eco_impact_locators import EcoImpactLocators
from task_2.pages.eco_impact_page import EcoImpactPage


class TestEcoImpact:
    """ Эковклад пользователя """
    @pytest.mark.user_eco_impact
    def test_user_water_counter(self, page: Page):
        """ Делает скриншот счетчика сохранения воды пользователем"""
        page = EcoImpactPage(page)
        page.open().screenshot_element(
            os.path.join(OUTPUT_DIR_PATH, "ID1_screenshot_water.png"),
            EcoImpactLocators.USER_SAVE_WATER
        )

    @pytest.mark.user_eco_impact
    def test_user_co2_counter(self, page: Page):
        """ Делает скриншот счетчика сохранения атмосферы пользователем"""
        page = EcoImpactPage(page)
        page.open().screenshot_element(
            os.path.join(OUTPUT_DIR_PATH, "ID2_screenshot_co2.png"),
            EcoImpactLocators.USER_SAVE_CO2
        )

    @pytest.mark.user_eco_impact
    def test_user_energy_counter(self, page: Page):
        """ Делает скриншот счетчика сохранения энергии пользователем"""
        page = EcoImpactPage(page)
        page.open().screenshot_element(
            os.path.join(OUTPUT_DIR_PATH, "ID3_screenshot_energy.png"),
            EcoImpactLocators.USER_SAVE_ENERGY
        )
