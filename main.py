from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager() .install()), options=options)

driver.get('https://www.amazon.com/')

# Amazon Shopping list

search1 = driver.find_element(By.ID,'twotabsearchtextbox')
search1.send_keys('dymatize')

try:
    # Product 1
    click_search1 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.ID, 'nav-search-submit-button'))
    )
    click_search1.click()

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    click_product1 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Dymatize ISO 100 Whey Protein Powder with 25g of Hydrolyzed'
                                                      ' 100% Whey Isolate, Chocolate Peanut Butter, 5 Pound'))
    )
    click_product1.click()

    click_add_to_cart1 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.ID, 'add-to-cart-button'))
    )
    click_add_to_cart1.click()

    # Product 2
    search2 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
    )
    search2.send_keys('peanut butter powder')

    click_search2 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.ID, 'nav-search-submit-button'))
    )
    click_search2.click()

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    click_product2 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'PBfit All-Natural Organic Peanut Butter Powder, '
                                                      'Powdered Peanut Spread from Real Roasted Pressed Peanuts, '
                                                      '8g of Protein, 30 Ounce (Pack of 1)'))
    )
    click_product2.click()

    click_add_to_cart2 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.ID, 'add-to-cart-button'))
    )
    click_add_to_cart2.click()

    # Product 3
    search3 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
    )
    search3.send_keys('thorne multivitamin')

    click_search3 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.ID, 'nav-search-submit-button'))
    )
    click_search3.click()

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    click_product3 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Thorne Basic Nutrients 2/Day - '
                                                      'Comprehensive Daily Multivitamin '
                                                      'with Optimal Bioavailability - '
                                                      'Vitamin and Mineral Formula - '
                                                      'Gluten-Free, Dairy-Free, Soy-Free - 60 Capsules - 30 Servings'))
    )
    click_product3.click()

    click_add_to_cart3 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.ID, 'add-to-cart-button'))
    )
    click_add_to_cart3.click()

    # Product 4
    search4 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
    )
    search4.send_keys('thorne omega 3')

    click_search4 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.ID, 'nav-search-submit-button'))
    )
    click_search4.click()

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    click_product4 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Thorne Super EPA - Omega-3 Fatty Acids EPA '
                                                      '425mg and DHA 270mg Supplement - Support Healthy Heart, '
                                                      'Brain, Cardiovascular, Joints, and Skin - '
                                                      'Gluten-Free, Dairy-Free, Soy-Free - 90 Gelcaps'))
    )
    click_product4.click()

    click_add_to_cart4 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.ID, 'add-to-cart-button'))
    )
    click_add_to_cart4.click()

    # Product 5
    search5 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
    )
    search5.send_keys('shaker bottle star wars')

    click_search5 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.ID, 'nav-search-submit-button'))
    )
    click_search5.click()

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    click_product5 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'BlenderBottle Star Wars Classic V2 '
                                                      'Shaker Bottle Perfect for Protein Shakes '
                                                      'and Pre Workout, 28-Ounce, Boba Fett Helmet'))
    )
    click_product5.click()

    click_add_to_cart5 = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.ID, 'add-to-cart-button'))
    )
    click_add_to_cart5.click()

    # Review Cart
    click_review_cart = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.ID, 'nav-cart'))
    )
    click_review_cart.click()
except:
    driver.quit()
