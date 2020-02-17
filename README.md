This repository contains code corresponding to SiegeBreaker, which, consists of these major components:
1. _Client_, who wishes to use Decoy Routing and reach a censored website.
2. _Overt-destination_, a website, which censor thinks client wants to visit.
3. _Covert-destination_, a website, which client **really** wants to visit.
4. _Proxy_, a machine, who proxies client's traffic and fetches covert-destination for it.
5. _SDN Controller_, which installs relevant redirection rules on SDN switches.
                                                             
                                                              
# Building SiegeBreaker
These steps are for Ubuntu 18.04 and derivatives. 
#### The Extremely Easy way
1. `docker pull himanshusagar/ubuntu_siegebreaker`
2. Already built code is inside `/home/user/`
#### The Easy way
Build everything in single go via `build.sh` located inside <repo_path>/build.sh.
#### The Not-so-easy way

Install all dependencies one by one.
###### Install Generic Dependencies
`sudo apt update && sudo apt install gcc make python-minimal libssl-dev git python-pip`
###### Install Seccure
1. `sudo apt install libgmp-dev build-essential python-dev python-pip libmpfr-dev libmpc-dev`
2. `pip install seccure`
###### Install Ryu
1. `pip install ryu`
###### Install libpcap
1. `sudo apt install libpcap-dev`

##### Build Signalling Mechanism
There are two signaling mechanisms in place - "smtplib/imap" and webmail. "smtplib/imap" is written in python for sending emails, when invoked by client code. Any of them can be used with client's c code.

###### Install webmail dependencies
1. Install [Chrome](https://www.google.com/chrome/)
2. Install [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
3. Test whether chromedriver works by typing `$ chromedriver` in terminal.
4. `pip install scapy selenium`

###### Install "smtplib/imap" dependencies
1. `pip install scapy easyimap`

#### Build "C" Code
###### Build Client
1. `cd main`
2. `cd ./client/c`
3. `make`
4. `cd ../../`
###### Build proxy
1. `cd ./proxy/`
2. `make center`
3. `make single_conn_queue`
4. `cd ../`

                                      
# Running SiegeBreaker
`git clone https://github.com/himanshusagar/SiegeBreakerV2`
#### As a Client
1. `cd <repo_path>/main/client/c`
2. `sudo ./client.o PROXY_IP 443 URL TIMEOUT`
3. Example Usage : `sudo ./client.o 192.168.2.5 443 https://censored_site/100M 40`
4. By default, webmail singalling mechanism is used. This can be changed to "smtp/imap" based signaling in [client.c](https://github.com/himanshusagar/SiegeBreakerV2/blob/master/main/client/c/client.c#L155) by changing 'client_send.py' to '[smtp_client_send](https://github.com/himanshusagar/SiegeBreakerV2/blob/master/main/client/smtp/smtp_client_send.py)'


#### As a Proxy
1. `cd <repo_path>/main/proxy/`
2. `sudo ./center.o`

#### As a Controller
1. `cd <repo_path>/main/controller/`
2. `ryu-manager controller_HP3500yl.py`
3. Depending upon which signalling mechanism used in client setup, run corresponding email receiver in controller system.

## Acknowledgements:
1. base64.h used from https://github.com/superwills/NibbleAndAHalf