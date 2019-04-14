# TransDataCollectionBackend
## Instructions for running the server
* Locate setting.py in the path projectBackEnd/projectBackEnd/settings.py.
* Locate the line number 28 mentioning the list of Allowed hosts.
* Add a ip address of the local network that will act as the server, you can add the ip address of the computer itself.
* Then on terminal inside the directory **TransDataCollectionBackend/projectBackEnd/** run the manage.py as follows:
  `python manage.py runserver <ipAddress:portnumber>`
* Type `https://ipAddress:portnumber/` on the browser. You should see the success message for now.
