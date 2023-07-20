### PiCam

## Camera Module

# Installation

1. Clone the repo to your home directory, under "picam"
2. Install python3, git and wget with `apt update -y && apt install python3 git wget`
3. Install requirements with `python3 -m pip install -r requirements.txt`
4. Add the following to CRON (WARNING! This will make your PI only usable over SSH. Check that it is working beforehand!). Replace USER with your username
   `@reboot /home/USER/picam/app/paralell.bat "python3 /home/USER/picam/app/main.py 1" "python3 /home/USER/picam/app/cam.py" "python3 -m http.server"`
   `@weekly cd /home/USER/picam && git pull --force`
5. Reboot your PI

# Updating

This is handled automatically! You`re welcome

## PC App

# Installation

1. Clone the repo to your PC.
2. Get the IP of your PI
3. Replace the IP in openCV/image.py with your IP. Leave the "tcp://" and the ":33" alone
4. Start the app with `python3 openCV/main.py`

<!-- look for image within image
return top left and bottom right coords
crop image
compare against golden sample -->
