**Moving the data from Redshift to S3**

Requirements:<br>
We have a test table in redshift public schema, we need to move all the data from the table 
to s3 partitioned in the way that one file can contain only 1 million records.

Steps:
1. Download a dependancy redshift_connector using pip/conda
   pip install redshift_connector
2. Establish a connection using redshift_connector class giving hostname, dbname, user, password
3. Initialise the cursor
4. Read from the table using cursor execute (SQL Statement)
5. Typecast the resultset into dataframe
6. Create a function and invoke s3 object using boto3 client
7. Loop through dataframe chunk and put the files in respective s3 path

