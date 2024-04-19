# Thesis Scripting Utils
This repository contains scripts used in preprocessing images for thesis and a user guide for people not comfortable with the terminal. 
Note: most of the scripts are hardcoded. 


## Remote Access Guide for Thesis PC
I'm running this on Ubuntu 22 LTS. For windows peeps, they could download WSL instead and download the necessary packages.

Moreover, you'll need a public IP. In my case, I just used zero tier to allow access.

Also, use vim to edit stuff via terminal.


#### Code for Setting Up an SSH Tunnel
``` bash
# This will forward all local connections from localhost:8899 to <REDACTED_IP>:8899 with user eugene
# You can use the -f flag to allow this code to run in background
ssh -p 2222 -N -L localhost:8899:localhost:8899 eugene@<REDACTED_IP>
```
After making the tunnel, you can access jupyter notebook  by typing `http://localhost:8899` on your browser.

Also you could symlink missing dirs in HOME instead of copy pasting. For example:
``` bash
ln -sfn /mnt/f/Downloads/temp_codes /home/eugene/temp_codes
```


#### Sample Code to SSH Into WSL
``` bash
# This will connect to Thesis PC via SSH on Port 2222.  
ssh -p 2222 eugene@<REDACTED_IP>
```

#### WSL SSH Config
- I set the wsl ssh port to 2222. You can edit it back via `/etc/ssh/sshd_config`
- Note: WSL IP changes everytime you reboot the computer. Hence it is recommended that you run the start-up script at init via windows.

**Source**: https://superuser.com/questions/1582234/make-ip-address-of-wsl2-static

```powershell
# route_ssh_to_wsl.ps1
# Below code allows wsl to be port forwarded
wsl.exe sudo /etc/init.d/ssh start #might ask for password. you could configure wsl to not ask password at boot by editing the /etc/sudoers: %sudo ALL=(ALL) NOPASSWD: /etc/init.d/ssh
$wsl_ip = (wsl hostname -I).trim()
Write-Host "WSL Machine IP: ""$wsl_ip"""
netsh interface portproxy add v4tov4 listenport=2222 connectport=2222 connectaddress=$wsl_ip
```

```powershell
$trigger = New-JobTrigger -AtStartup -RandomDelay 00:00:15
Register-ScheduledJob -Trigger $trigger -FilePath C:\route_ssh_to_wsl.ps1 -Name RouteSSHtoWSL
```

#### Launching Jupyter Notebook
- In WSL, run
``` bash
jupyter notebook --no-browser --port=8899 --ip 0.0.0.0
```

#### Logging into Jupyter Notebook 
- In your browser, type localhost:8899. it will prompt for a password token generated when you ran jupyter notebook.
- Type `jupyter notebook list` on the terminal to get a list of running jupyter notebooks with their tokens


## File Transfer Guide
#### Rsync Via Port 2222
```bash
# Upload temp_test to eugene@<REDACTED_IP>:/home/eugene 
rsync -rvz -e 'ssh -p 2222' temp_test  eugene@<REDACTED_IP>:/home/eugene


# Downloads the contents of eugene@<REDACTED_IP>:/home/eugene to temp_test
rsync -rvz -e 'ssh -p 2222' temp_test  eugene@<REDACTED_IP>:/home/eugene
```


## Running Commands in the background
``` bash
# Squashes std output and allows a cli command to run in the background. Instead, it pipes both std out and std err to foo.log and foo.err respectively
nohup myprogram > foo.log 2> foo.err < /dev/null &
```

For example:
``` bash
# crop face.sh
export VID_DIR="/home/eugene/Document/train_dir_raw"
export CROPPED_DIR="/home/eugene/Document/train_dir"
python3 extract_frames.py --source $SOURCE_DIR --dest $DEST_DIR > foo.log 2> foo.err < /dev/null &

export SOURCE_DIR="/home/eugene/Document/train_dir "
export DEST_DIR="/home/eugene/Document/train_dir"
python3 crop_faces.py --source $SOURCE_DIR --dest $DEST_DIR > foo.log 2> foo.err < /dev/null &

```

```
nohup ./crop_face.sh > job01_crop_face.log 2> job01_crop_face.err < /dev/null &
```


