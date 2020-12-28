```bash
#download python3.6.8 and install
#unzip the 0.1 release
#create the python environement 
python -m venv alpr
alpr/Scripts/activate
# make sure pip 20.2.3
pip install -r requirements.txt
# open port on firewall
netsh advfirewall firewall add rule name="Open Port ALPR" dir=in action=allow protocol=TCP localport=8889 remoteip=0.0.0.0





```
