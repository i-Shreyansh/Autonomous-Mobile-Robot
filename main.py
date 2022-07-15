from Libraries import *
from Train import *
from Vision import *
import json



def run():
    loader()

if __name__ == '__main__':
  
    run()
    keys = pd.read_csv("credentials.csv")
    access_key,secret_key = keys['Access key ID'].values[0],keys['Secret access key'].values[0]
    AWS_keys(access_key,secret_key)

    #photo location
    photo = r"img.jpg"


    #response = aws_detect_labels(photo)

    re = str(response)
    re = re.replace("\'", "\"")
    print(re)
    re = json.loads(re)
    print(re['Labels'])

