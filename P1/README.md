To run the whole program from the Data collector part to the ingestion of the different data to MongoDB it is
enough to execute the program main.py, where all the other programs are called in order to execute the whole process.

Some things to keep in mind before running the programs:

- We assume that the Virtual Machine's MongoDB server is already previously initialized.
- The data folder has to be located in the same project/directory where the main program is launched.
- In the Data folder we assume that we already have the different folders idealista, lookup_tables and
    opendatabcn-income (with these same names) with the different data files inside. Regarding the
    data/opendatabcn-rent folder will be created automatically in the data_collector.py program.
- In the main program we have the list of programs ordered according to what we want to execute to implement
    the whole process. In case we only want to execute one of the programs (for example the loader_rent())
    we can comment the other lines of the main and keep only the one we are interested in executing. This way
    it is easy to execute independently each one of the programs of our code.
- We recommend you to install all the versions that appears in our requirements file before executing the main program.
- You may have to change some variables defined in the connection_mongo.py program, setting the MONGO_HOST,
    MONGO_DB, MONGO_USER and MONGO_PASS with which you want to create the connection and ingest the datasets.

The command to execute the programs is:
`python main.py`
