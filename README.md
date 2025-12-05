# python-daqmx-demo
A demo of the [NI DAQmx Python library](https://nidaqmx-python.readthedocs.io/).

## Getting set up
- [Install python on your system](https://www.python.org/downloads/), if it isn't already installed
  - I prefer to install it from a standalone installer rather than the install manager
  - For this demo, version 3.10 or newer will work just fine 
  - When I install, I pick several nonstandard options from the "Customize Installation" menu
    - I **_do not_** add python.exe to `PATH` (I like to explicitly call the version I want to use)
    - I **_do not_** install the `py` launcher, for the same reason
    - I **_do_** install for all users
    - I put every version in `C:\pythons`, for example, `C:\pythons\python3_10\`, `C:\pythons\python3_12\`, etc.
  - No matter how you choose to install, find the path to the python interpreter (`python.exe`) that got installed
- Next, create a virtual environment
  - The concept is out of scope for this blog, but if you're a beginner, just take my word for it
  - In PowerShell, run `C:\pythons\python3_10\python.exe -m venv venv`
  - Replace the path to `python.exe` with the path you used
- Activate the virtual environment: `.\venv\Scripts\activate`
- Install the required packages from [pypi](https://pypi.org/): `(venv) PS> pip install -r requirements.txt`

## Running the script
Inside your activated virtual environment, simply run `python demo.py`.
