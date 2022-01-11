# robot_hand
The labview code was programmed using labview 2016 32-bit from the roboRIO DVDs. It is unclear if it can run on other versions of labview.

The arm was modelled using Solidworks 2021-2022.

*Quick Start Guide*
1.	Install LabVIEW 2016 32-bit with roboRIO toolkit and drivers from the DVDs included with the roboRIO
2.	Install Python 3.x
3.	Plugin the roboRIO: USB, external power and servos. Thumb is PWM0, index finger is PWM1… Be careful and make sure that the servos are not plugged in the wrong way, there is no reverse polarity protection. Black is ground. Plug in the servos before connecting the roboRIO to the computer or external power.
4.	Download LabVIEW and Python files from https://github.com/Emanuel-Bjurhager/robot_hand/
5.	Edit the file called ”UDP relay.py”. Make sure the roboRIO IP variable “IP” is correct
6.	In the file “UDP relay.py” change the variable “UDP_IP” to your computer IP address (you can find your IP using the command “ipconfig” in CMD) and save the file 
7.	Run the Python code using the CMD “ python ‘.\UDP relay.py’ ”
8.	Open the LabVIEW project by double clicking the file called “Neuroteknik projekt.lvproj”.
9.	In the LabVIEW project, open and run the filed called Main.vi
10.	The hand should now move when commands are sent to your computers IP and port 1337. If it does not work, try disabling Windows Firewall.
