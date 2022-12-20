from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import numpy as np


driver = webdriver.Firefox()

driver.get("https://howkteam.vn/learn")

imgList = []
author = []
Title1 = []
viewList = []
text_box = driver.find_element(
    by=By.XPATH, value=".//div[@class='d-inline-block']/strong")
imgElement = driver.find_elements(
    By.CSS_SELECTOR, value="img[class='img-fluid options-item w-100']")
elementsTitle = driver.find_elements(
    By.CSS_SELECTOR, value="h4[class='font-size-default font-w600 mb-10 text-overflow-dot']")
authorElement = driver.find_elements(By.XPATH, value=".//div[@class='block-content block-content-full useravatar-edit-container']")
totalView = driver.find_elements(
    By.XPATH, value=".//div[@class='d-inline-block']/strong")


for span in imgElement:
    imgList.append(span.get_attribute("src"))


for span1 in elementsTitle:
    Title1.append(span1.get_attribute("innerHTML"))

for span2 in authorElement:
    val1 = span2.find_elements(By.XPATH, value=".//span[@class='ml-5']")
    AuthorList = []
    for span3 in val1:
        AuthorList.append(span3.get_attribute("innerHTML"))
    author.append(AuthorList)
    AuthorList=[]
    
for span3 in totalView:
    viewList.append(span3.get_attribute("innerHTML"))
finalData= []
finalData.append([imgList, Title1, author, viewList])
print(len(imgList))
print(len(Title1))
print(len(author))
print(len(viewList))
d ={'ImgSrc':imgList, "Title":Title1, "Author": author, "View": viewList}
df1 = pd.DataFrame(data=d)
df1.to_excel("output.xlsx")
driver.quit()
