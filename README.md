SCRIPTING PROJECT


DESCRIPTION : SYSTEM SUPERVISION SCRIPT

Listing all metrics available on MACOS and Linux (Debian). 

Creation of a script logging all the metrics available (CPU, Memory, Disks, Network, Sensors, Other system info, Process Management)

and log them in a temporal database (INFLUXDB).

The script must be launchable from a command line using an argument of the type int.

Displaying the results on a Grafana dashboard.

Creation of a Debian service (Systemd) to automatically launch the script.

HOW TO USE THE PROJECT :
Example of the command line to launch the script : python3 launcher.py -i 3

CREDITS :
Project led by Anais HAMMOUCHE, Claire MATHIRON, Baptiste CHOQUET and Paul ROUMY.

Their github accounts are :

https://github.com/AnaisHammouche
https://github.com/ClaireMath
https://github.com/BaptisteChoquet
https://github.com/PaulRoumy