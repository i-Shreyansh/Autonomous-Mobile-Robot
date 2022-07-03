from Libraries import *
import boto3
import json



def AWS_keys(ACCESS_KEY, SECRET_KEY):

    global aws_access_key_id, aws_secret_access_key
    aws_access_key_id = ACCESS_KEY
    aws_secret_access_key = SECRET_KEY

def keys_extract(Name):
    id = read_file(Name)
    keys = dict(subString.split("=") for subString in id.split(","))
    return keys
def aws_detect_labels(photo):
    with open(photo,'rb') as img:
        img = img.read()

    client = boto3.client('rekognition'
                        ,aws_access_key_id=access_key
                        ,aws_secret_access_key=secret_key
                        ,region_name='ap-south-1')
    response = client.detect_labels(Image={'Bytes':img},MaxLabels=1)
#
   
    print(response)
    print("....done")
    return response


if __name__ == '__main__':
    
    cmd('cls') 
    keys = pd.read_csv("credentials.csv")
    access_key,secret_key = keys['Access key ID'].values[0],keys['Secret access key'].values[0]
    AWS_keys(access_key,secret_key)

    #photo location
    photo = r"img.jpg"
    response = aws_detect_labels(photo)
    
    write_file('res.txt',response)
    response = read_file('res.txt')
    print(response)



    