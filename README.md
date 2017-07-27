Files Included:

DataCollection_YelpAPI.py


DataLoading.py


Steps to execute the files:
-> Requirements:
    MySQL Server/MySQL Workbench
    Python 2.7/PyCharm with python 2.7
    
-> Include the credentials, mainly cleint_id and client_secret in the code. 
   You can find them on https://www.yelp.com/developers/v3/manage_app

-> Change the database name and credentials of the MySQL server.

-> Run the DataCOllection_YelpAPI.py file 
    i. In command prompt, you can run the file as: python DataCollection_YelpAPI.py (default values for term and location are "lunch" and        "Dallas, TX")
    ii. In command prompt, you can run the file by passing command line arguments as:
        python DataCollection_YelpAPI.py --term="dinner" --location="chicago,IL"
    iii. Creating a project in PyCharm and copying the files and run the DataCollection_YelpAPI.py
