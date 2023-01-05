#-------------------------------------------------------------------------------
# Name:         download_images.py
# Purpose:      This Python script downloads random images from the website 
#               and saves in the images folder.
# Author:       Kiran Chandrashekhar
# Created:      26-Dec-2022
#-------------------------------------------------------------------------------
import os
from random import randint
import requests
from urllib.parse import urlencode
import conf

class DownloadRandomImages:
    """
    Download Random Images from https://picsum.photos/
    """
    def __init__(self):
        self.base_url = r'https://picsum.photos'
    
    def generate_image_url(self):
        """
        Generate URL based on the Image configuration
        """
        url = f"{self.base_url}/{conf.IMAGE_WIDTH}/{conf.IMAGE_HEIGHT}.{conf.EXTENSION_TYPE}"
       
        data = {}
        if conf.GRAY_SCALE:
            data['grayscale'] = None
        if conf.BLUR_IMAGE:
            data['blur'] = None #Add the blur level from 1 to 10

        url = f"{url}?{urlencode(data)}"
        return url

     
    def download_single_image(self, num_count:int):
        """
        num_count is the number of images to be downloaded
        """
        url = self.generate_image_url()

        for i in range(0, num_count, 1):
            print("Downloading Image: ", i+1)

            image_path = f"{os.getcwd()}/images/{randint(100_000,999_999)}.{conf.EXTENSION_TYPE}"

            response = requests.get(url)
            with open(image_path, mode='wb') as fp:
                fp.write(response.content)
    

    def download_image(self, num_count:int):
        """
        num_count is the number of images to be downloaded
        """
        for i in range(0, num_count, 1):
            print("Downloading Image: ", i+1)
            self.download_single_image()


def main():
    obj = DownloadRandomImages()
    obj.download_image(10)
    
    
if __name__ == '__main__':
    main()
    print("Done")