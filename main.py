from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd


def create_browser():
    options = Options()
    options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=options)

def activate_containing(browser, tag, property, value):
    element = browser.find_element(by=By.XPATH, value=f"//{tag}[contains({property}, '{value}')]")
    element.click()

def login(browser, username, password):
    username_login_textbox = browser.find_element(by=By.ID, value='username')
    password_login_textbox = browser.find_element(by=By.ID, value='password')
    login_button = browser.find_element(by=By.CLASS_NAME, value='btn-primary')

    username_login_textbox.send_keys(username)
    password_login_textbox.send_keys(password)
    login_button.click()

def main():
    grupo_id = '67593'
    evaluacion = '2'
    criterio_id = '9198'
    nombre_col_csv = 'Actividades'

    calificaciones = pd.read_csv('calif_electro.csv')

    browser = create_browser()
    browser.get('https://gaatx.itsx.edu.mx/auth/login')

    login(browser, '', '')

    activate_containing(browser, 'a', '@href', f'/lista/id/{grupo_id}')
    activate_containing(browser, 'a', '@href', f'/calificar/id/{grupo_id}')
    activate_containing(browser, 'a', '@href', f'/u/{evaluacion}')
    activate_containing(browser, 'a', '@href', f'/c/{criterio_id}/u/{evaluacion}')

    for control in calificaciones['Control']:
        try:
            control_cell = browser.find_element(by=By.XPATH, value=f'//td[contains(text(), "{control}")]')
            row = control_cell.find_element(by=By.XPATH, value='..')

            input_calificacion = row.find_element(by=By.TAG_NAME, value='input')
            calificacion = calificaciones[calificaciones['Control'] == control][nombre_col_csv].values[0]
            input_calificacion.clear()
            input_calificacion.send_keys(f"{calificacion}")

        except NoSuchElementException as ex:
            print(f"Error al asignar calificacion a: {control}.")
            print(ex.msg)

if __name__ == '__main__':
    main()
