from dataclasses import dataclass


@dataclass
class EcoImpactLocators:
    """ Локаторы страницы экологического вклада. """
    USER_SAVE_WATER = "//a[@id='personal-impact-view']/..//div[text()='было сохранено']/parent::div/parent::div"
    USER_SAVE_CO2 = "//a[@id='personal-impact-view']/..//div[text()='не попало в атмосферу']/parent::div/parent::div"
    USER_SAVE_ENERGY = "//a[@id='personal-impact-view']/..//div[text()='было сэкономлено']/parent::div/parent::div"
