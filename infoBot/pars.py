from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class VoenmemSchelude:
    path = 'chromedriver.exe'
    url = 'https://www.voenmeh.ru/trainee/timetable-stud#'

    def __init__(self, group_number=''):
        self.group_number = group_number.upper().strip()

    def GetSchelude(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        Select(driver.find_element(By.ID, "cbxGroupNumber")).select_by_visible_text(self.group_number)
        driver.find_element(By.NAME, "bShowTimetable").click()

        schelude = driver.find_element(By.ID, "timetableresult").text
        driver.quit()

        return schelude
