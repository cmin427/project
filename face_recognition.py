import os
import sys
import requests
def facedetection(imagefile_name):
    client_id = "MyPt_Sqvr1IY_HEKA6kT"
    client_secret = "0iufQGxrzt"
    # imagefile_name='C:\\Users\\min\\Desktop\\project\\Afree_market\\unnamed.jpg'
    url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
    # url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식
    files = {'image': open(imagefile_name, 'rb')}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if(rescode==200):
        return (response.text)
    else:
        return ("Error Code:" + rescode)