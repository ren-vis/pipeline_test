import pandas as pd
import boto3
import urllib.request

urllib.request.urlretrieve("https://dabtest2.s3.eu-west-1.amazonaws.com/custom_1988_2020.csv?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCWV1LXdlc3QtMiJIMEYCIQD6LqzfdrjXlQHhKeKl73BS0oE438Td8Ev5Kl5We2ijjQIhAPBUdzrPYXnbWRW2B0ab%2FNuoXm1dVp7VcnyEkYNB68s7KugCCHsQABoMNzYyNTA1MTE1NjM1IgyvHYYnsrIJ%2BvjyxX8qxQJPr1ftY8xpb3pFKg3j0x1bFUGpE2gSnJ8pd2vgcwk6vMrhzc%2FhYgHCQjRzRQx3zs%2BLO%2FySt1EbY8BzwJPsbhp%2BbqyCJ950QD36LQ89JZLgwMLsMUyhbOfeIGzrhMVze8UYNhmozYLuxmsBsddPkmXzUfnbXF1iV%2BqW3vMaCsP7R3E3e%2Fi%2FGeFeClL%2BJ2q6gmhr%2FG%2FFCse4gPh3IjG24CvEPj%2F7LNtmEj3CCBdkEtA4RoWGZRcgZDa3dEuE3UZ3V1UeiX039TI%2BDafw3SOg21JkRoLlyvRvFfKKesAyjA1VFryO9h8IBZpCnsN3YiM5BiUPtkBVXDZLUyerEdoo%2BIXH26qp5Q%2BR4hqJRYYKxHRHhFp9haDbMnWUTIBHjVUz0%2B7XHKKQQxnHrtCRoQbqBRyAyphXVD%2FcwmQfsk5gvvyY0zdhqmluMJOp8Z0GOrICEBFW19eiLd7z0tcAGsiqdjSWLSO4aT6ub6Rdh9yqsjzDfpqR8mAGJ95M8vvFjQl4cMpm2qX9Zr0SmZiQ2Rke0ed1Rpls3VZr4gsoUISIwOVHvsB3%2Fu5gJsa0VzMFO58IfDuAdwU5rW6pKTScPMhnYUx3L5PjxSol6WxbG2mij8Xjs6jteEByxy%2F5gIWpk4u9YdTUG%2FLU2UJdEkdFW8Vl6lofir1SsW%2BS4JDQXSHribGexoTjUJotaHt3Nj%2Bb4wVntewT2FNBzF4dRa%2BI7ScwDtSRzqo%2FClr4FyV5RXOM3QX6eF5rE1OB2MMUCPxnjth7dSN%2B0V1Nsc%2FwqeSh7D66z9Cp1G%2BqgUbj2imygMilxNkI5Gt01yBXOwxRO4M3KPVkmKQL98l4tRTy3m7N%2Bi5QJ66z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230109T181555Z&X-Amz-SignedHeaders=host&X-Amz-Expires=36000&X-Amz-Credential=ASIA3DCGYW7Z6LWUX2DN%2F20230109%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Signature=53cad03c01b318bb18747e66d5b8832d3a78900cd6fd79d8a6550f6dac9cff55", "test.csv")

df1 = pd.read_csv('test.csv', delimiter=',')
nRow, nCol = df1.shape
print(f'There are {nRow} rows and {nCol} columns')
print(df1)