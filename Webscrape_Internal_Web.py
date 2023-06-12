from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import json

driver = webdriver.Firefox()
driver.get("https://gis.wilmarapps.com/wilmargis/default.aspx")

username = driver.find_element(By.ID, "texbox1")
password = driver.find_element(By.ID, "texbox2")

username.send_keys("###")
password.send_keys("###")

# Sumbit Enter
driver.find_element(By.ID, "ImageButton1").click()

# membuat dataframe dulu pake pandas
awal = [["awal", "awal", "awal", "awal", "awal", "awal", "awal", "awal", "awal", "awal", "awal", "awal", "awal",
         "awal", "awal", "awal", "awal", "awal", "awal", "awal", "awal"]]


df = pd.DataFrame(awal, columns=["Block", "SurveyStatus","Month(Planted)", 
                                 "Age(Month)", "TM/TBM", "GrossArea", "Planted", "LC",
                                 "UnPlanted", "Nursery", "Garapan", "NotPlantable", "POM",
                                 "RH", "HCV", "PalmCount", "SPH", "Type", "ESTNR", "Owner", "Bulan"])

f = open("F:\\10. Project\\Dashboard\\Parameter\\MasterData.json")

jsondata = json.load(f)

regrange = range(1, 6)
listreg = []
for r in regrange:
    regitem = jsondata["REGION " + str(r)]
    listreg.append(regitem)

s1 = []
for estates in listreg:
    
    for estate in estates:
        url = "https://gis.wilmarapps.com/wilmargis/content/inv/inv.aspx?estate="
        exturl = "&invmn=mbldt"
        urlmerge = url + str(estate) + exturl
        driver.get(urlmerge)

        pathbulan = "/html/body/form/div[4]/table/tbody/tr/td/table/tbody/tr[1]/td[2]/table[3]/tbody/tr/td/div/div/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/div[2]/div[1]/div/div/div/span[2]/table/tbody/tr/td/b"
        bulan_detail = driver.find_element(By.XPATH, pathbulan).text
        print(bulan_detail[41:])

        #Keruwetan scraping dimulai, dari inti dulu

        path_inti = "//span[@id='ctl12_tabcont1_tabsummaryinti_lblblockdetails']//table//tbody//tr//td//div[2]//table//tbody//tr"
        tabel_inti = driver.find_elements(By.XPATH, path_inti)
        rowinti = len(tabel_inti)

        def scrape(path_tab, row_tab, est, bulan):

            if path_tab == path_inti:
                owner = "Inti"
            elif path_tab == path_plasma:
                owner = "Plasma"


            x = range(1, row_tab)
            for i in x:
                relative1 = "[" + str(i) + "]"
                merge1 = path_tab + relative1
                mergecondition = merge1 + "//td[1]"
                element1 = driver.find_element(By.XPATH, mergecondition).text

                s2 = []
                x2 = range(1, 22)
                for i2 in x2:
                    if element1 == "SUB TOTAL":
                        continue
                    elif element1 == "":
                        continue
                    elif "Div" in element1:
                        continue

                    if i2 == 19:
                        s2.append(est)
                    elif i2 == 20:
                        s2.append(owner)
                    elif i2 == 21:
                        s2.append(bulan)

                    else:
                        realtive2 = "//td[" + str(i2) + "]"
                        merge2 = merge1 + realtive2
                        element2 = driver.find_element(By.XPATH, merge2).text
                        s2.append(element2)


                s1.append(s2)



        scrape(path_inti, rowinti, estate, bulan_detail[41:])

        pathtab = driver.find_elements(By.XPATH, "//div[@id='ctl12_tabcont1_header']//span")
        t = len(pathtab)


        if t > 6:
            driver.find_element(By.ID, "ctl12_tabcont1_tabsummaryplasma_lblownerplasma").click()
            path_plasma = "//span[@id='ctl12_tabcont1_tabsummaryplasma_lblblockdetailsplasma']//table//tbody//tr//td//div[2]//table//tbody//tr"
            tabel_plasma = driver.find_elements(By.XPATH, path_plasma)
            rowplasma = len(tabel_plasma)

            scrape(path_plasma, rowplasma, estate, bulan_detail[41:])

    

# Cleaning data frame
res_s1 = list(filter(None, s1))

for i in res_s1:
    df.loc[len(df.index)] = i

r = range(5, 15)
for i in r:
    df.iloc[:,i] = df.iloc[:,i].str.replace(".",",")

df.iloc[:,15] = df.iloc[:,15].str.replace(",","")
df.iloc[:,0] = df.iloc[:,0].str.replace("000","0")

c1 = df["Month(Planted)"].tolist()

lp = []
for c2 in c1:
    c3 = str(c2)
    c4 = c3[0:4]
    lp.append(c4)

df["Year"] = lp
df2 = df.loc[df["Block"] != "awal"]

print(df2)

df2.to_csv("F:\\10. Project\\Dashboard\\Parameter\\ScrapeInv.csv", sep=';', decimal=',',index= False)

df2.to_csv("F:\\10. Project\\Dashboard\\HistoryDetailBlock\\ScrapeInv_"+str(bulan_detail[41:])+".csv", sep=';', decimal=',',index= False)

# nambah komen test git



driver.close()

