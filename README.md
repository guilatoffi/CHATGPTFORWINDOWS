
# CHATGPTFORWINDOWS
**ChatGPT for Windows bypass** to allow regular (non-premium) users to access new voice features and create custom GPTs.

## Installation Steps

### 1. Download ChatGPT (early version)

- [Link to ChatGPT app on the Microsoft Store](https://apps.microsoft.com/detail/9nt1r1c2hh7j?hl)

### 2. Install mitmproxy

- Download mitmproxy from the official website: [mitmproxy.org](https://www.mitmproxy.org/)
- Install the certificate:
  - [Download the certificate](https://github.com/guilatoffi/CHATGPTFORWINDOWS/blob/main/mitmproxy-ca-cert.p12)
  - Run the file, click "Next," and leave all options as default.

### 3. Configure the proxy with kill2.py

#### Option 1: Automatic setup (batch file)

1. Download all necessary files to your desktop.
2. Run `LaunchProxy.bat` to set up and start the proxy automatically.

#### Option 2: Manual setup

1. In an admin terminal, go to the directory where the `kill2.py` file is located.
2. Run the following command:
   ```bash
   mitmproxy -s kill2.py
   ```
3. In Windows settings, set the proxy to `127.0.0.1:8080`.
4. Run ChatGPT as usual.

### 4. Disable the proxy

- When done, run `DISABLE PROXY.bat` to restore your proxy settings to default.
![voice ui](https://github.com/user-attachments/assets/8f1ec23c-af75-4984-97a0-3bd6086d75dc)
![ui](https://github.com/user-attachments/assets/05793bbc-6c06-414f-9528-f2f9010ffbcc)
![voice choices](https://github.com/user-attachments/assets/ea48ce51-5f9f-4c8e-a4a0-a6a6a12a1cec)
