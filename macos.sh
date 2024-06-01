sudo dpkg --configure -a
sudo brew install android-tools-adb

python3 -m venv ./scrd
chmod -R 777 scrd
source scrd/bin/activate

sudo brew install -r requirementsLinux.txt
python3 main.py

deactivate