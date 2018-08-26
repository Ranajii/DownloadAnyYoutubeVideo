from selenium import webdriver
import pafy

url = 'https://www.youtube.com/results?search_query='
x = input('Enter song name: ')
z = x.replace(' ','+')
urlnew = url+z
print(urlnew)
driver = webdriver.Chrome(r"C:\Users\visha\chromedriver")
driver.get(urlnew)

video1st = driver.find_element_by_xpath('//*[@id="dismissable"]/div')
video1st.click()

link = driver.current_url
video = pafy.new(link)
best = video.getbest()
best.resolution, best.extension
download1 = best.download(filepath="E:\Songs")
print(x,'is downloaded successfully')
