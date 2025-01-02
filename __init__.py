import shutil

userName = "user"
wpilibVersion = 2025
materialIconVersion = "5.16.0"
meterialIconsPath = "/extensions/pkief.material-icon-theme-" + materialIconVersion + "/icons"
fullIconPath = ""

icons = [
  "folder-2025wpilib", "folder-2025wpilib-open",
  "folder-angleChanger", "folder-angleChanger-open",
  "folder-arm", "folder-arm-open",
  "folder-chassis", "folder-chassis-open",
  "folder-ctre", "folder-ctre-open",
  "folder-elevator", "folder-elevator-open",
  "folder-gripper", "folder-gripper-open",
  "folder-led", "folder-led-open",
  "folder-paths", "folder-paths-open",
  "folder-subsystem", "folder-subsystem-open",
  "folder-sysid", "folder-sysid-open",
  "folder-vision", "folder-vision-open"
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
