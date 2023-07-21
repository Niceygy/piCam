# PiCam

## Camera Module

### Installation

1. Clone the repo to your home directory, under "picam" `git clone https://git.niceygylive.xyz/Niceygy/picam.git /home/$USER/picam`
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

1. Clone the repo to your PC. `curl https://packages.niceygylive.xyz/picam/install.sh | pwsh`
2. Get the IP of your PI
3. Replace the IP in openCV/image.py with your IP. Leave the "tcp://" and the ":33" alone
4. Start the app with `python3 openCV/main.py`

<!-- look for image within image
return top left and bottom right coords
crop image
compare against golden sample -->

## Usage

`C. Compare images` <br>
`T. Take a new Template image` <br>
`S. Sync from the camera` <br>
`F. Find a part in an image or` <br>
`A. Add a new part` <br>
Possible options ^ <br>

### 1. Board comparison:

By using the <b>T</b>ake template function, you can take an image of the "golden sample" you want all boards to be like. Then, using the <b>C</b>ompare images function, you can check for diffrences between the "golden sample" and your current board. WARNING! It will work better if it is alligned well, so I suggest using a clamp or vice to keep the boards in the same place from one to the next.

### 2. LED Control

There are three buttons, marked with a "+", a "-" and a backwards "c". The "-" button rotates the lit LEDs clockwise. Only three will be lit up at a time. <br>
The backwards "c" button toggles all lights on/off. <br>
The "-" button is currently broken, although is suppose to take an image. You can use the "Take a template image" function for now.

### 3. Managing parts

You can either <b>F</b>ind parts on a board or <b>A</b>dd a part to the list that it can find.<br>
When adding a part, make sure the camera can see the part and nothing else. If you need to, manually crop the image afterwards.
This part will then be added to `./openCV/parts/parts.txt`, and an image saved under `./images/` <br>
<br>
When <b>F</b>inding a part, make sure the entire board is visible and well lit up. Ideally use the same lighting for taking images of boards and parts.<br>
The Pi will then highlight all the matches to that part that it can find, up to 256 instances.

### 4. Syncing images

This is broken at the moment, so don`t use it.<br>
See https://git.niceygylive.xyz/Niceygy/PiCam/issues/1 for more
