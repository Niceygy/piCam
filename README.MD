# PiCam

## Camera Module

### Installation

1. Clone the repo to your home directory, under "picam"
2. Install python3, git and wget with `apt update -y && apt install python3 git wget`
3. Install requirements with `python3 -m pip install -r requirements.txt`
4. Add the following to CRON (WARNING! This will make your PI only usable over SSH. Check that it is working beforehand!). Replace USER with your username
   `@reboot /home/USER/picam/app/paralell.bat "python3 /home/USER/picam/app/main.py 1" "python3 /home/USER/picam/app/cam.py" "python3 -m http.server"`
   `@weekly cd /home/USER/picam && git pull --force`
5. Reboot your PI

### Updating

This is handled automatically! You`re welcome

## PC App

### Installation

1. Clone the repo to your PC.
2. Get the IP of your PI
3. Replace the IP in openCV/image.py with your IP. Leave the "tcp://" and the ":33" alone
4. Start the app with `python3 openCV/main.py`

<!-- look for image within image
return top left and bottom right coords
crop image
compare against golden sample -->

## Usage

### 1. Board comparison:

By using the <b>T</b>ake template function, you can take an image of the "golden sample" you want all boards to be like. Then, using the <b>C</b>ompare images function, you can check for diffrences between the "golden sample" and your current board. WARNING! It will work better if it is alligned well, so I suggest using a clamp or vice to keep the boards in the same place from one to the next.

### 2. LED Control

There are three buttons, marked with a "+", a "-" and a backwards "c". The "-" button rotates the lit LEDs clockwise. Only three will be lit up at a time. <br>
The backwards "c" button toggles all lights on/off. <br>
The "-" button is currently broken, although is suppose to take an image. You can use the "Take a template image" function for now.
