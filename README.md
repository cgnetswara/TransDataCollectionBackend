# TransDataCollectionBackend

## About
This project provides a backend for [TransDataCollection Android App](https://github.com/cgnetswara/TransDataCollection). This android app is an effort to collect data from the lay people with the most minimal efforts. 

## Installation Instructions
Please follow the instructions carefully for a successful installation process.

* The complete Django project is in the `projectBackEnd` folder. cd into the folder.

    ```sh
    cd projectBackEnd
    ```

* Install the required packages

    ```sh
    pip install -r ../requirements.txt
    ```

Note: Make sure you are using correct python and pip versions all along installation

* Set the ALLOWED_HOSTS
    We have already included all the possible hosts which are neccessary to run the django app along with android app on localhost. If you want to add any other address (like a network address), please add that in the ALLOWED_HOSTS variable in `projectBackEnd/projectBackEnd/settings.py`.

    Note: Host `10.0.2.2` is necessary to let the android emulator to access the django app on localhost

* Create your local database (db.sqlite3)
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

* Create an admin superuser to access question and answers
    ```sh
    python manage.py createsuperuser
    ```

* Run the server
    ```sh
    python manage.py runserver
    ```

* To observe the input output, visit `Answers` and `Questions` tab in `localhost:8000/admin`.

## Team and Contributors
Anurag Shukla (Android App) (IIIT Naya Raipur)
Ankush Jain (Backend) (IIIT Naya Raipur)
Devansh Mehta (Testing and Brain Storming) (CGNet Swara)
Vipin Kirar (Field Testing) (CGNet Swara)
Sebastin Santy (App Testing) (Microsoft Research)

