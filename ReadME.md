To run the app:

"flask run" (This only runs on local host, bind to gunicorn to make it run on public IP)

To run the tests:

"python3 -m pytest"

To bind it to gunicorn:

"gunicorn app:app -c gunicorn.py"