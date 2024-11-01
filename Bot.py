import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

window=tk.Tk()
window.geometry("500x400")

def Instagram():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url="https://www.instagram.com/accounts/login/?source=auth_switcher"
    driver.get(url)
    time.sleep(1)

    email=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
    if(email_entry.get()==""):
        msg="Please enter email.."
        error_label.config(text=f"{msg}")
    else:
        email.send_keys(email_entry.get())
        time.sleep(1)

    password=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
    if(password_entry.get()==""):
        msg2="Please enter password"
        error_label.config(text=f"{msg2}")
    else:
        password.send_keys(password_entry.get())
        time.sleep(1)
        enter=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
        enter.click()
        time.sleep(10)

def Facebook():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url="https://www.facebook.com/?locale=tr_TR"
    driver.get(url)
    time.sleep(1)

    email=driver.find_element(By.NAME,"email")
    if(email_entry.get()==""):
        msg="Please enter email.."
        error_label.config(text=f"{msg}")
    else:
        email.send_keys(email_entry.get())
        time.sleep(1)

    password=driver.find_element(By.NAME,"pass")
    if(password_entry.get()==""):
        msg2="Please enter password.."
        error_label.config(text=f"{msg2}")
    else:
        password.send_keys(password_entry.get())
        time.sleep(1)
        enter = driver.find_element(By.NAME,"login")
        enter.click()
        time.sleep(10)

def Twitter():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url="https://x.com/i/flow/login"
    driver.get(url)
    time.sleep(2)

    login=driver.find_elements(By.NAME,"text")
    time.sleep(2)
    if(email_entry.get()==""):
        msg="Please enter email.."
        error_label.config(text=f"{msg}")
    else:
        login[0].send_keys(email_entry.get(),Keys.ENTER)
        time.sleep(3)
    
    password = driver.find_element(By.NAME,"password")
    if(password_entry.get()==""):
        msg2="Please enter password"
        error_label.config(text=f"{msg2}")
    else:
        password.send_keys(password_entry.get())
        time.sleep(1)
        password.send_keys(Keys.ENTER)
        time.sleep(10)
    
#Email Edıtor
email_label=tk.Label(text="Email",font=("Calibri",20,"bold"))
email_label.place(x=110,y=20)

email_entry=tk.Entry(width=30)
email_entry.place(x=190,y=33)

#Password Edıtor
password_label=tk.Label(text="Password",font=("Calibri",20,"bold"))
password_label.place(x=70,y=60)

password_entry=tk.Entry(width=30)
password_entry.place(x=190,y=71)

#İnstagram Button
instagram_button=tk.Button(text="INSTAGRAM",width=12,height=3,command=Instagram,bg="#bc45a2",fg="white")
instagram_button.place(x=30,y=150)

#Facebook Button
facebook_button=tk.Button(text="FACEBOOK",width=12,height=3,command=Facebook,bg="#2839bf",fg="white")
facebook_button.place(x=200,y=150)

#Twitter Button
twitter_button=tk.Button(text="TWITTER",width=12,height=3,command=Twitter,bg="black",fg="white")
twitter_button.place(x=370,y=150)

#Error Label
error_label=tk.Label(text="",font=("Calibri",20,"bold"))
error_label.place(x=140,y=280)

window.mainloop()