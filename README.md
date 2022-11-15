# pdfTextExtract
Running this application on a local environment
Prerequisites:
In order to run the app the following prerequisites are needed to be installed.
Python 2.7.x or Python 3.6.x

1. Clone the repository

```
git clone https://github.com/somya-15/pdfTextExtract.git
```

2. Change to the project directory

3. Create a python virtual environment

```
python -m venv <virtual-env-name>
```

This command creates a python virtual environment under the flask-app folder.

4. Activate the virtual environment

```
source <virtual-env-name>/bin/activate
```
This step is mandatory if you wish to keep your root installation of Python from being overwritten. The packages that will be
installed as part of the next step will only exist within the virtual environment and not in Python installation's root
folder

5. Install the requirements

```
pip install -r requirements.txt
```

6. Running the app
```
export FLASK_APP=app.py 
python -m flask run
```

This starts the application and can be viewed from the following URL: http://localhost:5000 in your laptop. Port can
be configured as needed.
