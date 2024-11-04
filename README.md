# CHATGPTFORWINDOWS
chatgpt for windows bypass for regular user (non premium) to acess new voice features and make custom gpts

1. Download chatgpt early version form the app store:
https://apps.microsoft.com/detail/9nt1r1c2hh7j?hl

2. Download mitmproxy
https://www.mitmproxy.org/
RUN mitmproxy-ca-cert.p12 (click next and leave everything by default)

4. Download my kill2.py
   
- 4.1 AUTOMATIC(batch file)
download all the files to your desktop
Click on LaunchProxy.bat to setup and start the proxy automaticly

- 4.2 MANUAL: 
In an admin terminal at the root of where the .py file is located run : mitmproxy -s kill2.py
Set your windows setting proxy to 127.0.0.1:8080 and run Chatgpt as normal


Once done you can click on the DISABLE PROXY.bat to put back your proxy setting to default
