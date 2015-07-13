# kimonolabs
This python script will attempt to retrieve data from both current and previous versions of an API built using [kimonolabs](https://www.kimonolabs.com/) API generator and save files in JSON format.  To use the script, simply edit the *api_id* and *api_key* values with your own in the **kimonoconfig.py.sample** file and save as **kimonoconfig.py**.  After editing the config file, run script to fetch and save your data.

The script will determine the current version of the API.  If the file doesn't already exist, the script will create it.  From there, the script simply goes back one version at a time, making sure it doesn't overwrite an existing file, until all available versions have been saved.  **NOTE:** [kimonolabs](https://www.kimonolabs.com/) currently limits previous data access to the past 30 days.

## Requirements
* Built-in modules: *os.path* and *json*
* 3rd party modules: [requests](http://docs.python-requests.org/en/latest/user/install/) - `$ pip install requests`
* Config file: **kimonoconfig.py** - **kimonoconfig.py.sample** provided for convenience

## Usage
`$ python kimonolabs.py`