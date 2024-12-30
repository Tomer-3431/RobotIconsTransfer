# Robot Icons Transfer

this code transfer icons from the icons folder to the icons folder of material icons based on where the extension is

## How The Code Works

the code works by using shutils library </br>
the code ask the user where to put the icons: (either wpilib or default vscode) </br>
after couple of questions to determined where to put the icons the code will put all of the icons there

## How To Excecute

this is a simple python code </br>
using `python __init__.py` command in a cmd in the workspace folder will run the code </br>
after running the code you will need to copy the content in [settings](settings.json) and add it to either the workspace settings or the user settings

## Important Note

if material icons update their version of extension the code will not works as the vscode folder name change by the version </br>
if this is happening all you need to do is to put the extension version name in [\_\_init\_\_](__init__.py#L5) in the materialIconVersion variable

## Questions

for any question feel free to ask me [@Tomer-3431](https://github.com/Tomer-3431) </br>
and thank you for using my custom icons
