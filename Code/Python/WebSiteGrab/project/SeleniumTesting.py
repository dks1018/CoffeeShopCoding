from selenium import webdriver
import time 


chromedriver = "C:\\Users\\dks10\\OneDrive\\Desktop\\Projects\\Code\\Python\\WebSiteGrab\\Final\\chromedriver_win32\chromedriver.exe"
#chromedriver = "C:\\Users\\chris\\Documents\\chromedriver\\chromedriver.exe"

browser = webdriver.Chrome(chromedriver)

addr_list = ['900 COBBLESTONE CT', '1475 SHADE TREE WAY', '1485 SHADE TREE WAY', '1495 SHADE TREE WAY', '1530 SHADE TREE WAY', '1520 SHADE TREE WAY', '1510 SHADE TREE WAY', '1500 SHADE TREE WAY', '1470 SHADE TREE WAY', '1460 SHADE TREE WAY', '1450 SHADE TREE WAY', '2260 FAIRFAX DR', '2250 FAIRFAX DR', '1420 SHADE TREE WAY', '1490 SHADE TREE WAY', '925 COBBLESTONE CT', '935 COBBLESTONE CT', '930 COBBLESTONE CT', '920 COBBLESTONE CT', '1515 SHADE TREE WAY', '1525 SHADE TREE WAY', '1535 SHADE TREE WAY', '1560 SHADE TREE WAY', '1550 SHADE TREE WAY', '1540 SHADE TREE WAY', '2105 FAIRFAX DR', '2115 FAIRFAX DR', '2125 FAIRFAX DR', '2135 FAIRFAX DR', '2145 FAIRFAX DR', '725 PADDOCK CT', '735 PADDOCK CT', '745 PADDOCK CT', '730 PADDOCK CT', '720 PADDOCK CT', '710 CROWN COVE', '811 SMOKE HOUSE CT', '821 SMOKE HOUSE CT', '831 SMOKE HOUSE CT', '830 SMOKE HOUSE CT', '820 SMOKE HOUSE CT', '810 SMOKE HOUSE CT', '2165 FAIRFAX DR', '705 PADDOCK CT', '2195 FAIRFAX DR', '801 SMOKEHOUSE CT', '800 SMOKE HOUSE CT', '1440 SHADE TREE WAY', '1430 SHADE TREE WAY', '1420 SHADE TREE WAY']
city_list = [' ALPHARETTA GA 30009', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30201', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30022', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30009', ' ALPHARETTA GA 30004', ' ALPHARETTA GA 30009']





     #front    middle         Backend
front = "https://www.truepeoplesearch.com/details?streetaddress" #&citystatezip=  &rid=0x0 iterate 1-10
Page_Num = 0
Addr = 0 #string?
City_Zip = 0 #string?
inc = 0
for addr in addr_list:
    Page_Num = 0
    customer_informtion = {}
    custoemr_phone = []
    while(Page_Num <= 9): #code is stopping because the page num equals 9/ need to reset page num every time through the loop 
        print("Please wait 5 seconds!")
        time.sleep(3)

        new_Addr = str(Addr)
        new_City = str(City_Zip)
        new_Page_Num = str(Page_Num)
        new_Addr = addr_list[inc]
        new_City = city_list[inc]
        Address = "=" + new_Addr
        middle = "&citystatezip"
        City = "=" + new_City
        backend = "&rid="
        Page = "0x" + new_Page_Num
        URL = front + Address + middle + City + backend + Page
        Page_Num += 1
        browser.get(URL)
        
        name = browser.find_element_by_css_selector('#personDetails > div:nth-child(1) > div > span.h2').text
        try: 
            pn1 = browser.find_element_by_css_selector('#personDetails > div:nth-child(6) > div.col-12.col-sm-11 > div:nth-child(2) > div > div > a').text
        except:
            pn1 = "NA"
        try:
            pn2 = browser.find_element_by_css_selector('#personDetails > div:nth-child(6) > div.col-12.col-sm-11 > div:nth-child(3) > div > div > a').text
        except:
            pn2 = "NA"  
        try:
            pn3 = browser.find_element_by_css_selector('#personDetails > div:nth-child(6) > div.col-12.col-sm-11 > div:nth-child(4) > div > div > a').text
        except:
            pn3 = "NA"

        # customer_informtion[name] = [pn1]
        value = "\n"
        print(value)
        customer_informtion[name] = "1: " + pn1 + ", 2: " + pn2 + ", 3: " + pn3
        print(customer_informtion)
    inc += 1
    #need to close browser and then open new browser
