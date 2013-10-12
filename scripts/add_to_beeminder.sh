export PYTHONPATH=/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages
python_arg="/Applications/Pomodoro.app/Contents/Resources/pomodoro-beeminder/scripts/add_to_beeminder.py "$1
python $python_arg
# echo $command