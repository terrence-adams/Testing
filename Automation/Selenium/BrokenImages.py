import selenium
from selenium import webdriver
import requests

# Returns a Boolean as the active status of the image
def validate_image(url):
    try:
        response = requests.get(url)
        if response is not None:
            if response.status_code is 200:  # Verify image by server response of 200
                return True
            else:
                return False
    except Exception as ex:
        return ex

#Returns a list as well prints to console the broken images
def find_bad_images():
    driver = webdriver.Ie()  #Set up
    driver.maximize_window()
    my_url = 'http://www.naturehills.com/trees'

    driver.get(my_url)
    images = list()
    bad_images = list()

    images = driver.find_elements_by_tag_name('img')  # Locate by tage type

    for img in images:  # Find url from tag elements
        my_src = img.get_attribute('src')
        valid_image = validate_image(my_src)  # Validated by helper function

        if valid_image is not True:
            if my_src is not None:
                bad_images.append(my_src)
        else:
            if bad_images is None:
                print("No bad images found.")

    for bad in bad_images:
        print("Here are your bad images:")
        print(bad)

    driver.close()  #Clean up

    return bad_images



if __name__ == '__main__':
   bad_images =  find_bad_images()
