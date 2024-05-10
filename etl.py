import requests
import sqlalchemy 
import pandas 

url = "http://api.coincap.io/v2/assets"


headers = { "Content-Type":"application/json",
           
           "Accept-Encoding" :"deflate"
  
}


response = requests.request("GET", url, headers=headers)

#print(response)
responseData  = response.json()

#print(responseData)

df = pandas.json_normalize(responseData,'data')

#print(df)

engine = sqlalchemy.create_enginer('postgresql://username:password@localhost/mydatabase')


df.to_sql(name="Tiktokexercise",con=engine,index=False,if_exists='fail')
