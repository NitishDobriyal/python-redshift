import pandas as pd
import time
import math
import numpy as np
from io import StringIO
import time,boto3
import redshift_connector

#Establishing connection
conn = redshift_connector.connect(
             host='endpoint',
                  database='dev',
                       user='awsuser',
                            password='yourpassword'
                              )
#Initializing cursor                              
with conn.cursor() as cursor:
    cursor.execute("select * from test")
    result=pd.DataFrame(cursor.fetch_dataframe())
    result.set_index("id", inplace = True)

#Function to upload dataframe to s3 in parts
def upload_s3(df,i):
    s3 = boto3.client("s3",aws_access_key_id="xyz",aws_secret_access_key="abcd")
    for id, df_i in  enumerate(np.array_split(df, math.ceil( df.shape[0]/1000000 ))):
        csv_buf = StringIO()
        df_i.to_csv(csv_buf, header=True, index=False, sep="|")
        csv_buf.seek(0)
        s3.put_object(Bucket="my_bucket", Body=csv_buf.getvalue(), Key='subfolder/'+str(id)+i)

upload_s3(result,"avis.csv")