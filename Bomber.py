from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from sys import exit

class WhatsApp:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://web.whatsapp.com/")
        sleep(2)
        print("\n\n----Please Login into your Whatsapp account to continue---\n")
        

    def Bomber(self, MESSAGE, TIMES):
        for times in range(TIMES):
            text_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')\
                .send_keys(MESSAGE)
            text_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')\
                .send_keys(Keys.ENTER)
        sleep(2)
        print("\n----Bombed Succesfully !!! <3\n")
        sleep(4)       

if __name__ == "__main__":
    whatsapp = WhatsApp()
    sleep(2)
    
    while(True):
        print("\n----Select an option to continue----\n")
        print("----1. Bomb inbox\n----2. Exit\n")
        option = int(input())

        if option == 1:
            message = input("\nEnter the message to be sent ...\n")
            times = int(input("\nEnter the number of times the message to be sent ...\n"))
            sleep(2)
            whatsapp.Bomber(message, times)

        elif option == 2:
            print("\n\n----Thank You----\n\n")
            sleep(2)
            exit()
        
        else :
            print("\n----Enter proper choice----\n")
            sleep(2)