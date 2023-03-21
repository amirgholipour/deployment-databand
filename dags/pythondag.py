# File: pythondag.py
# Simple DAG for the Databand hands-on workshop

# This python program can be run standalone, on any server or client that can
# connect to the system running databand (and Postgres)

# Create a test table, load data from csv, select data, delete data or drop the table
# Featuring:
#   - logging information with the Databand SDK function (dataset_op_logger)
#   - combine logging and non-logging parts in the code
#   - integrated with Postgres

# Mandatory imports
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from dbnd import dbnd_tracking, task, dataset_op_logger

# The name of the csv file to load into Postgres
# The path must be found and accesible by the python program when it runs
# This name will be displayed by Databand as a dataset (substituyng the slash by dot)
motogp_file = 'sql/motogp.csv'

# Task #1: load a table
@task
def read_all_championships():
    
    # begin logging
    with dataset_op_logger(motogp_file,
                            "read",
                            with_schema=True,
                            with_preview=True,
                            with_stats=True,
                            with_histograms=True
                          ) as logger:
        
        # operation to be logged - read the file into pandas
        motogp_championships = pd.read_csv(motogp_file, sep=';')

        # end logging
        logger.set(data=motogp_championships)

    return(motogp_championships)

# Task #2: Filter the data and select only the records of 2022
@task
def select_one_year(alldata):

    # begin logging
    with dataset_op_logger(motogp_file,
                            "read",
                            with_schema=True,
                            with_preview=True,
                            with_stats=True,
                            with_histograms=True
                          ) as logger:
        
        # operation to be logged - select the Season 2022 in pandas
        oneyear = alldata[alldata.Season.eq(2022)]

        # end logging
        logger.set(data=oneyear)

    return(oneyear)

# Task #3: Write data to Postgres and simulate other operation that 
#   we don't want to log
@task
def write_to_postgres(oneyear):

    # Build the connection
    myconntype = "postgresql+psycopg2"
    mydatabase = "postgres"
    myhost = "pg-nodeport-postgres.itzroks-1100005cc8-2lbzmg-6ccd7f378ae819553d37d5f2ee142bd6-0000.us-east.containers.appdomain.cloud"
    myuser = "postgres"
    mypassword = "postgres"
    myport = "30208"
    myconnstring = myconntype+'://'+myuser+':'+mypassword+'@'+myhost+':'+myport+'/'+mydatabase
    myengine = create_engine(myconnstring)

    # begin logging
    with dataset_op_logger(motogp_file,
                            "write",
                            with_schema=True,
                            with_preview=True,
                            with_stats=True,
                            with_histograms=True
                          ) as logger:
        
        # operation to be logged - write the pandas dataframe to postgres
        oneyear.to_sql('motogp', myengine, if_exists='replace', index=False)

        # end logging
        logger.set(data=oneyear)

    
    # simulate an operation that we don't want to log
    # (just open a connection and select some data)
    conn = psycopg2.connect(database=mydatabase,
                            host=myhost,
                            user=myuser,
                            password=mypassword,
                            port=myport)
    mysqlcount = "select count(*) from motogp"
    cur = conn.cursor()
    cur.execute(mysqlcount)
    result = cur.fetchone()

    return(result[0])

# Function to define the connection to Databand and run the pipeline
def motogp_pipeline ():
    with dbnd_tracking (
            conf={
                "core": {
                    "databand_url": "http://databand-web-databand.itzroks-1100005cc8-2lbzmg-6ccd7f378ae819553d37d5f2ee142bd6-0000.us-east.containers.appdomain.cloud",
                    "databand_access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3OTA3MDcxMSwianRpIjoiYzNiYTgxOGYtMzA0ZS00MGQzLTgwNTQtZmZlMGRlMmY4MDc0IiwidHlwZSI6ImFjY2VzcyIsImlkZW50aXR5IjoiZGF0YWJhbmQiLCJuYmYiOjE2NzkwNzA3MTEsImV4cCI6MTc0MjE0MjcxMSwidXNlcl9jbGFpbXMiOnsiZW52IjoiIn19.LuR2DrQH3ve1NrztTeW_1h1ZNWF-TAHpXy1lpSQw5h4"
                    }
                },
            job_name="Python_DAG", 
            run_name="Python_DAG",
            project_name="Python pipelines"
        ) : 

        # Execution sequence: read csv - select year 2022 - write data to postgres
        all_data = read_all_championships()
        one_year = select_one_year(all_data)
        result = write_to_postgres(one_year)

        # just to be sure...
        print('Written: ' + str(result) + ' records')

# The program starts here
motogp_pipeline()