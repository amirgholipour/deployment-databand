import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from dbnd import dbnd_tracking, task, dataset_op_logger

motogp_file = 'sql/motogp.csv'

@task
def read_all_championships():
    
    with dataset_op_logger(motogp_file+'_all',
                            "read",
                            with_schema=True,
                            with_preview=True,
                            with_stats=True,
                            with_histograms=True
                          ) as logger:
        motogp_championships = pd.read_csv(motogp_file, sep=';')
        logger.set(data=motogp_championships)

    return(motogp_championships)

@task
def select_one_year(alldata):
    with dataset_op_logger(motogp_file+'_oneyear',
                            "read",
                            with_schema=True,
                            with_preview=True,
                            with_stats=True,
                            with_histograms=True
                          ) as logger:
        oneyear = alldata[alldata.Season.eq(2022)]
        logger.set(data=oneyear)

    return(oneyear)

@task
def write_to_postgres(oneyear):

    myconntype = "postgresql+psycopg2"
    mydatabase = "postgres"
    myhost = "pg-nodeport-postgres.itzroks-1100005cc8-2lbzmg-6ccd7f378ae819553d37d5f2ee142bd6-0000.us-east.containers.appdomain.cloud"
    myuser = "postgres"
    mypassword = "postgres"
    myport = "30208"

    myconnstring = myconntype+'://'+myuser+':'+mypassword+'@'+myhost+':'+myport+'/'+mydatabase

    myengine = create_engine(myconnstring)
    with dataset_op_logger(motogp_file+'_postgres',
                            "write",
                            with_schema=True,
                            with_preview=True,
                            with_stats=True,
                            with_histograms=True
                          ) as logger:
        oneyear.to_sql('motogp', myengine, if_exists='replace', index="False")
        logger.set(data=oneyear)

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

def motogp_pipeline ():
    with dbnd_tracking (
            conf={
                "core": {
                    "databand_url": "http://databand-web-databand.itzroks-1100005cc8-2lbzmg-6ccd7f378ae819553d37d5f2ee142bd6-0000.us-east.containers.appdomain.cloud",
                    "databand_access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3ODQ2ODc2NCwianRpIjoiMjA0OTAyODAtNTk0YS00NmIzLTllYTQtMDMzYWQwMTc4NzNmIiwidHlwZSI6ImFjY2VzcyIsImlkZW50aXR5IjoiZGF0YWJhbmQiLCJuYmYiOjE2Nzg0Njg3NjQsImV4cCI6MTc0MTU0MDc2NCwidXNlcl9jbGFpbXMiOnsiZW52IjoiIn19.PvBKfoTARg7Dh4lysvzgPeRVHDeHckg9B0yn6U24LpU"
                    }
                },
            job_name="insert champions", 
            run_name="one year",
            project_name="MotoGP Project"
        ) : 
        all_data = read_all_championships()
        one_year = select_one_year(all_data)
        result = write_to_postgres(one_year)
        print('Written: ' + str(result) + ' records')

motogp_pipeline()





    

    



    

    
    


                            



