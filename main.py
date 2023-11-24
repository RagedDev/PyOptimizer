# Todo
# Make the tweaks
# Make the apply button work




# Imports
import configparser
import customtkinter as ctk
import webbrowser
import requests
from tkinter import messagebox
import getpass

version = "0.1"

if __name__ == '__main__':
    newver = requests.get("https://pastebin.com/raw/dtakqTbP")

    # Gui Setup
    app = ctk.CTk()
    ctk.set_default_color_theme("dark-blue")
    app.geometry("1080x650")
    app.title("PyOptimizer")

    #All Tabs
    def apply():
        print("Tweaks Applyed")
        if xres.get() != "" and yres.get() != "":
            GUS = configparser.ConfigParser()
            GUS.read("C:/users/"+getpass.getuser()+"/appdata/local/FortniteGame/Saved/Config/WindowsClient/GameUserSettings.ini")
            GUS.set("/Script/FortniteGame.FortGameUserSettings", "ResolutionSizeX", xres.get())
            GUS.set("/Script/FortniteGame.FortGameUserSettings", "ResolutionSizeY", yres.get())
            GUS.set("/Script/FortniteGame.FortGameUserSettings", "LastUserConfirmedResolutionSizeX", xres.get())
            GUS.set("/Script/FortniteGame.FortGameUserSettings", "LastUserConfirmedResolutionSizeY", yres.get())
            GUS.set("/Script/FortniteGame.FortGameUserSettings", "DesiredScreenWidth", xres.get())
            GUS.set("/Script/FortniteGame.FortGameUserSettings", "DesiredScreenHeight", yres.get())
            GUS.set("/Script/FortniteGame.FortGameUserSettings", "LastUserConfirmedDesiredScreenWidth", xres.get())
            GUS.set("/Script/FortniteGame.FortGameUserSettings", "LastUserConfirmedDesiredScreenHeight", yres.get())
            with open("C:/users/"+getpass.getuser()+"/appdata/local/FortniteGame/Saved/Config/WindowsClient/GameUserSettings.ini", 'w') as configfile:
                GUS.write(configfile)

        if fpslimit.get() != "":
            GUS = configparser.ConfigParser()
            GUS.read("C:/users/"+getpass.getuser()+"/appdata/local/FortniteGame/Saved/Config/WindowsClient/GameUserSettings.ini")
            GUS.set("/Script/FortniteGame.FortGameUserSettings", "frameratelimit", fpslimit.get())
            with open("C:/users/"+getpass.getuser()+"/appdata/local/FortniteGame/Saved/Config/WindowsClient/GameUserSettings.ini", 'w') as configfile:
                GUS.write(configfile)

    if version != newver.text:
        print(newver.text)
        updatebutton = ctk.CTkButton(app, text="Update", command=update)
        updatebutton.pack()
    def gitlink():
        webbrowser.open_new("https://www.google.com/")

    # Apply Button
    button = ctk.CTkButton(app, text="Apply", command=apply, width=10, height=10)
    button.pack(padx=500, pady=1)

    #Tabs
    tabview = ctk.CTkTabview(master=app, width=1080, height=1000)
    tabview.pack(padx=20, pady=20)

    tabview.add("About")
    tabview.add("FPS Optimization")
    tabview.add("Network Optimization")
    tabview.add("Streched Resolution")
    tabview.set("About")

    #About Tab
    aboutlabel = ctk.CTkLabel(tabview.tab("About"), text="""Hello i am Raged a new developer to this project i am building this so other people can optimize their pc and learn python
    and this project will be opensource on my github""", )
    GHLink = ctk.CTkButton(tabview.tab("About"), text="Github Link", fg_color="blue", cursor="hand2", command=gitlink)
    GHLink.pack()

    aboutlabel.pack(padx=20, pady=20)

    # Streched Resoulution Tab
    xres = ctk.CTkEntry(tabview.tab("Streched Resolution"), placeholder_text="X Resolution")
    yres = ctk.CTkEntry(tabview.tab("Streched Resolution"), placeholder_text="Y Resolution")
    xres.pack()
    yres.pack()
    fpslimit = ctk.CTkEntry(tabview.tab("Streched Resolution"), placeholder_text="FPS Limit")
    fpslimit.pack()


    reslabel = ctk.CTkLabel(tabview.tab("Streched Resolution"), text="Recommended Resolutions: 1680x1080, 1080x1080, 1440x1080, 1576x1080")
    reslabel.pack()

    #Network Optimization Tab


    #FPS Optimization Tab

    #Mainloop
    app.mainloop()

