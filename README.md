# timecamp-scripts
Automatize the working hours in Timecamp

## Instructions for `default.js`

1. Add your API KEY from Timecamp.
2. Add the TASK ID in which you want to apply.
3. Add the js code in a bookmark ([Bookmarklet](https://en.wikipedia.org/wiki/Bookmarklet)), and then open it in a new tab.
4. Timecamp website should load, click again the bookmark and follow instrucctions.

If you want to set a normal workday from 9 to 13 and 14 to 18, just press "OK.
If not, type NO and fill the required information.


## Instructions for `default.py`

1. Create a .env file in the top directory containing:
```
API_TOKEN = "here your api token"
TASK_JORNADA_LABORAL = "here the task id"
```
2. Install the requirements
```
pip install -r requirements.txt
```
3. Execute the script for the initial and end dates to submit (both included). This will create a 4h task in the 
   morining plus 4h in the afternoon. Example:
```
python default.py 2021-02-08 2021-02-12
```
