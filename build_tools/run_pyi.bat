@echo off
pyinstaller --windowed ^
            --noconfirm ^
            --icon="build_tools\coffeegrindsize.ico" ^
            --add-data="build_tools\coffeegrindsize.ico;." ^
            --name "coffeegrindsize" ^
            --hidden-import cmath ^
            %GITHUB%\coffeegrindsize\coffeegrindsize.py
