from Libraries import *
import boto3
import tensorflow as tf






def AWS_keys(ACCESS_KEY, SECRET_KEY):

    global aws_access_key_id, aws_secret_access_key
    aws_access_key_id = ACCESS_KEY
    aws_secret_access_key = SECRET_KEY

def keys_extract(Name):
    id = read_file(Name)
    keys = dict(subString.split("=") for subString in id.split(","))
    return keys
def aws_detect_labels(photo,MaxLabels):
    with open(photo,'rb') as img:
        img = img.read()

    client = boto3.client('rekognition'
                        ,aws_access_key_id=aws_access_key_id
                        ,aws_secret_access_key=aws_secret_access_key
                        ,region_name='ap-south-1')
    response = client.detect_labels(Image={'Bytes':img},MaxLabels=MaxLabels)
#
   
    print(response)
    print("....done")
    return response


