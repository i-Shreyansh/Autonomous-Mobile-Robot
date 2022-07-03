from Libraries import *
import boto3


def AWS_keys(ACCESS_KEY, SECRET_KEY):

    global aws_access_key_id, aws_secret_access_key
    aws_access_key_id = ACCESS_KEY
    aws_secret_access_key = SECRET_KEY

def keys_extract(Name):
    id = read_file(Name)
    keys = dict(subString.split("=") for subString in id.split(","))
    return keys



if __name__ == '__main__':
    
      
    keys = pd.read_csv("credentials.csv")
    k=keys.head()
    access_key,secret_key = k['Access key ID'],k['Secret access key']
    AWS_keys(access_key,secret_key)
    print('done')

    
