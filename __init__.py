import shutil

userName = "user"
wpilibVersion = 2025
materialIconVersion = "5.16.0"
meterialIconsPath = "/extensions/pkief.material-icon-theme-" + materialIconVersion + "/icons"
fullIconPath = ""

icons = [
]

while True:
  print("what are you using vscode or wpilib vscode:\n1. vscode\n2. wpilib")
  response = input().lower()

  if response == "1" or response == "vscode":
    print("what is your user name in windows:")
    userName = input()
    fullIconPath = "C:/Users/" + userName + "/.vscode" + meterialIconsPath
    break

  elif response == "2" or response == "wpilib":
    print("what is your wpilib year version:")
    wpilibVersion = input()
    fullIconPath = "C:/Users/Public/wpilib/" + wpilibVersion + "/vscode/data" + meterialIconsPath
    break
  else:
    print("illegel choice please try again")

for i in icons:
  shutil.copy("./icons/" + i + ".svg", fullIconPath)

print("Fully moved all the icons into meterial icons")
