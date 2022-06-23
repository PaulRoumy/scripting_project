Listing all metrics available on MACOS and Linux (Debian). 

Creation of a script logging all the metrics available (CPU, Memory, Disks, Network, Sensors, Other system info, Process Management)

and log them in a temporal database (INFLUXDB).

The script must be launchable from a command line using an argument of the type int.

Displaying the results on a Grafana dashboard.

Creation of a Debian service (Systemd) to automatically launch the script.
