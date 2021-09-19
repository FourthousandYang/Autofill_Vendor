from selenium import webdriver                                  
from selenium.webdriver.chrome.options import Options                                                              
from selenium.webdriver.common.by import By                     
from selenium.webdriver.support.ui import WebDriverWait                                                            
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random, os, configparser, time, datetime


retryCount = 0
i = 1

def autoFill(id):
    global i
    options = Options()
    
    options.add_argument("--no-sandbox")                                                                               
    options.add_argument("--headless") 
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--log-level=3") #close logging message
    try:
        local_time = time.localtime() # 取得時間元組
        timeString = time.strftime("%Y%m%d", local_time) # 轉成想要的字串形式
        print("Today is "+timeString)

        if os.path.isdir("pic") == False:
            os.mkdir("pic")
            if os.path.isdir("pic/"+str(id)) == False:
                os.mkdir("pic/"+str(id))
                
        else:
            if os.path.isdir("pic/"+str(id)) == False:
                os.mkdir("pic/"+str(id))
                
        if os.path.isdir("pic/"+str(id)+"/"+timeString) == False:
                    
                    os.mkdir("pic/"+str(id)+"/"+timeString)
        chrome = webdriver.Chrome(options=options)
        chrome.get("https://zh.surveymonkey.com/r/VendorHealthCheck")
        
        
        #agreeCheck
        agreeCheck = chrome.find_element_by_xpath("//label[@id='683680575_4495738438_label']/span").click()
        picture_url=chrome.get_screenshot_as_file("pic/"+str(id)+"/"+timeString+"/check_"+str(i)+".png")
        i+=1

                                                                                                                        
        #employId
        chrome.find_element_by_id("683680584").click()
        chrome.find_element_by_id("683680584").clear()
        chrome.find_element_by_id("683680584").send_keys(id)
        picture_url=chrome.get_screenshot_as_file("pic/"+str(id)+"/"+timeString+"/check_"+str(i)+".png")
        i+=1

        #foreheadTemp check
        foreheadTemp = chrome.find_element_by_xpath("//label[@id='683680577_4495738440_label']/span").click()
        picture_url=chrome.get_screenshot_as_file("pic/"+str(id)+"/"+timeString+"/check_"+str(i)+".png")
        i+=1

        #foreheadTemp
        foreheadDegree=str(round(random.uniform(35.9, 36.7), 1))
        chrome.find_element_by_id("683680573").click()
        chrome.find_element_by_id("683680573").clear()
        chrome.find_element_by_id("683680573").send_keys(foreheadDegree)
        picture_url=chrome.get_screenshot_as_file("pic/"+str(id)+"/"+timeString+"/check_"+str(i)+".png")
        i+=1
        
        #Symptoms
        chrome.find_element_by_xpath("//div[@id='question-field-683680590']/fieldset/div/div/div/div/label/span").click()
        picture_url=chrome.get_screenshot_as_file("pic/"+str(id)+"/"+timeString+"/check_"+str(i)+".png")
        i+=1

        
        #contacted people who returned from aboard in the last 14 days
        chrome.find_element_by_xpath("//label[@id='683680582_4495738465_label']/span").click()
        picture_url=chrome.get_screenshot_as_file("pic/"+str(id)+"/"+timeString+"/check_"+str(i)+".png")
        i+=1

        #health declaration form
        print("health declaration form")
        if vaccinated == 1:
            ##Yes
            chrome.find_element_by_xpath("//label[@id='683680812_4495740025_label']/span").click()
            picture_url=chrome.get_screenshot_as_file("pic/"+str(id)+"/"+timeString+"/check_"+str(i)+".png")
            i+=1
            print("Yes")
        else:
            ##No
            chrome.find_element_by_xpath("//label[@id='683680812_4495740026_label']/span").click()
            picture_url=chrome.get_screenshot_as_file("pic/"+str(id)+"/"+timeString+"/check_"+str(i)+".png")
            i+=1
            print("No")


        #in the past 7 days
        chrome.find_element_by_xpath("//label[@id='683680583_4496057527_label']/span").click()
        picture_url=chrome.get_screenshot_as_file("pic/"+str(id)+"/"+timeString+"/check_"+str(i)+".png")
        i+=1
        chrome.find_element_by_xpath("//label[@id='683680588_4496057876_label']/span").click()
        picture_url=chrome.get_screenshot_as_file("pic/"+str(id)+"/"+timeString+"/check_"+str(i)+".png")
        i+=1
        chrome.find_element_by_xpath("//label[@id='683680586_4495738508_label']/span").click()
        picture_url=chrome.get_screenshot_as_file("pic/"+str(id)+"/"+timeString+"/check_"+str(i)+".png")
        i+=1
        chrome.find_element_by_xpath("//label[@id='683680587_4495738514_label']/span").click()
        picture_url=chrome.get_screenshot_as_file("pic/"+str(id)+"/"+timeString+"/check_"+str(i)+".png")
        i+=1
        
        #declaration radio button
        chrome.find_element_by_xpath("//label[@id='683680574_4495738430_label']/span").click()
        picture_url=chrome.get_screenshot_as_file("pic/"+str(id)+"/"+timeString+"/check_"+str(i)+".png")
        i+=1
        
        if test_mode == 1:
            print("Not Send!!")
            pass
        else: 
            #submit btn to next page
            chrome.find_element_by_xpath("//button[contains(text(), '下一頁')]").click()                                        
            # picture_url=chrome.get_screenshot_as_file("pic/"+str(id)+"/"+timeString+"/check_"+str(i)+".png")
            # i+=1   

            #successful landing page                                                                                     
            compleredTxtPath = "(//span[@class='title-text'])"                                                                 
            compleredTxt = WebDriverWait(chrome, 10, 1).until(EC.visibility_of_element_located((By.XPATH, compleredTxtPath))).text
            picture_url=chrome.get_screenshot_as_file("pic/"+str(id)+"/"+timeString+"/check_"+str(i)+".png")
            i+=1

            print(compleredTxt)
            print(id+" degree :"+foreheadDegree)
            print("Send!!")

        print ("Done!!")

        chrome.quit() 

    except TimeoutException:
        chrome.quit()
        global retryCount
        retryCount+=1
        if(retryCount == 2):
            print(id+" Write to error log")
            retryCount = 0
            pass
        else:
            print(id+" Try again")
            autoFill(id)

def readFile(): 
    fileHandler = open("Id.txt", "r")
    IdList = fileHandler.read().splitlines()
    fileHandler.close()
    return IdList

if __name__ == "__main__":
    
    date_of_today = datetime.date.today()
    print ("Open program date: " + str(date_of_today))
    config = configparser.ConfigParser()
    config.read('config.ini')

    loop_mode = int(config['mode']['loop_mode'])
    single_multiple_mode = int(config['mode']['single_multiple'])
    test_mode = int(config['mode']['test'])
    employeeId = config['employeeId']['id']
    vaccinated = int(config['selection']['vaccinated'])
    try:
        while loop_mode:
            date_of_today = datetime.date.today()
            current_day = None
            if (current_day == date_of_today) and (current_day is not None):
                print("Still today")
                pass
            else:
                print("Next day")
                if single_multiple_mode == 0:
                    autoFill(employeeId)
                else:
                    IdList = readFile()
                    print(IdList)
                    for data in IdList:
                        i = 1
                        id = data.split(",")[0]
                        vaccinated = int(data.split(",")[1])
                        print("Fill in ID: "+id+" vaccinated: "+ str(vaccinated))
                        autoFill(id)
                
            current_day = date_of_today

            time.sleep(86400)
        else:
            if single_multiple_mode == 0:
                autoFill(employeeId)
            else:
                IdList = readFile()
                print(IdList)
                for data in IdList:
                    i = 1
                    id = data.split(",")[0]
                    vaccinated = int(data.split(",")[1])
                    print("Fill in ID: "+id+" vaccinated: "+ str(vaccinated))
                    autoFill(id)
    except Exception as e:
        print(e)
    print("Progress Finish!")
    os.system('pause')
