if not "%1" == "max" start /MAX cmd /c %0 max & exit/b
python hip.py --file ./../docs/meadow2.jpg --cols 220 --scale 0.5
pause