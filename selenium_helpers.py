def check_if_exists_by_name(name):
    try:
        driver.find_element_by_name(name)
    except:
        return False
    return True

def click_if_exists_by_name(name):
    if check_if_exists_by_name(name):
        driver.find_element_by_name(name).click()
        return
def click_when_exists_by_name(self, name):
    try:
        element = WebDriverWait(driver, 1000).until(
                EC.presence_of_element_located((By.NAME, name))
                )
    finally:



