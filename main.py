from datetime import timedelta
from minio import Minio
from minio.error import S3Error
from config.minio_config import ACCESS_KEY, SECRET_KEY

import io
import pandas as pd
import numpy as np
import random

def main():
      client = Minio(
         endpoint='localhost:9000',
         access_key=ACCESS_KEY,
         secret_key=SECRET_KEY,
         secure=False, # for development only
      )

      bucket_name = 'bronze'      
      objs = client.list_objects(bucket_name, recursive=True)
      
      for obj in objs:
         if 'bank' in obj.object_name:
            url = client.get_presigned_url(
               'GET',
               bucket_name,
               obj.object_name,
               expires=timedelta(hours=1)
            )
            
            df = pd.read_csv(url, sep=";")
            
            # Replace 'unknown' with NaN in all columns
            df.replace('unknown', np.nan, inplace=True)
            
            # Map yes/no to True/False
            df['default'] = df['default'].map({'no': False, 'yes': True})
            df['housing'] = df['housing'].map({'no': False, 'yes': True})
            df['loan'] = df['loan'].map({'no': False, 'yes': True})
            df['y'] = df['y'].map({'no': False, 'yes': True})
            
            ### You can use various methods and techniques depending on the type of data and the desired format
            
            for idx, row in df.iterrows():
               rd = random.randint(1000, 99999)
               # education = str(row['education'])
               # contact = str(row['contact'])
               # day = str(row['day'])
               # duration = int(row['duration'])
               # housing = str(row['housing'])
               # y = str(row['y'])
               # month = str(row['month'])
               # campaign = str(row['campaign'])
               # loan = str(row['loan'])
               # marital = str(row['marital'])
               # age = int(row['age'])
               # job = str(row['job'])
               # pdays = str(row['pdays'])
               # default = str(row['default'])
               # poutcome = str(row['poutcome'])
               # balance = str(row['balance'])
               # previous = str(row['previous'])
               file_name = f'bank_loan_{rd}.json' # You can change this to another format
               
               record = row.to_json()
               record_bytes = record.encode('utf8')
               record_stream = io.BytesIO(record_bytes)
               record_stream_len = len(record_bytes)
               
               client.put_object(
                  'bank-records', # bucket name
                  f'records/{file_name}', # path
                  data=record_stream,
                  length=record_stream_len,
                  content_type='application/json'
               )
               
               print(f'Uploaded {file_name} to Minio')
            

if __name__ == '__main__':
   try:
      main()
   except S3Error as e:
      print('Error occured.', e)