@echo off
powershell mkdir ~/uninstallerformsedge
cd %USERPROFILE%\uninstallerformsedge
powershell wget https://github.com/Yasir65/ultimate-edge-uninstaller/raw/main/python.zip -o py3.zip
powershell wget https://raw.githubusercontent.com/Yasir65/ultimate-edge-uninstaller/main/main.py -o main.py
powershell Expand-Archive py3.zip
cd py3
cd python
cls
python %USERPROFILE%\uninstallerformsedge\main.py
cd ..
cd ..
cd ..
powershell rm -r %USERPROFILE%\uninstallerformsedge