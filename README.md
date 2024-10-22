# NetAdmin-Automation-Scripts
Scripts to automate some typical network administration tasks. 

### NOTE ###
* Any information (code, articles, Proof of Concept, etc) contained wihtin this repo are Strictly for educational purposes or AUTHORIZED professional use cases. I do not condone or authorize any and all information contained here to be used for illiict activity
  
* Please be careful if you hardcode credentials in a script. It is wise (If not best practice) to use an external secret management tool - espeically in a production environment.

* For these scripts to work, SSH must be enabled on the switch and that the IP address the request is coming from has the permission to connect via SSH. 

18OCT24: 
My first addition here was a basic Cisco Switch configuration written in Python. I used my own knowledge along with additional internet research to develop the script. Configure_Cisco_Switch.py was created on 18OCT24 but has not been run in a production environment. Updates will be provided as the script is updated and/or tested. 

21OCT24:
Second addition here is a python script for determining interface status (Up or Down) on a Cisco switch. The script is just a foundation I plan to add logic to to automatically close unused open ports to enhance port security on my switches. 
