To access properties on the objects, use the `get_property(str)` method, example:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set WebDriver.
driver = webdriver.Chrome()
driver.get('https://www.selenium.dev/selenium/web/web-form.html')

# Get info from website.
color_picker = driver.find_element(by=By.NAME, value='my-colors')
color_picker.send_keys("#ff00ff") # Magenta
print(f"color_picker: [{color_picker.get_property('value')}]")
```