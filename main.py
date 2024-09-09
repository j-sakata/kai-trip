from selenium import webdriver
import chromedriver_binary

def main():
    driver = webdriver.Chrome()
    driver.get('https://hoshinoresorts.com/jp/sp/kaitabi20s/')
    
if __name__ == "__main__":
    main()