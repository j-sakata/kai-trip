from selenium import webdriver
import chromedriver_binary

def main():
    driver = webdriver.Chrome()
    driver.get('https://www.google.co.jp')
    
if __name__ == "__main__":
    main()