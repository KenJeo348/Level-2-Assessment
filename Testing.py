import easygui


something = easygui.enterbox("Say something")

if something == "Hi":
    print("User said hi")
if something is None:
    print("Yeah")
