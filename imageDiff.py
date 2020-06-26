from skimage.metrics import structural_similarity
import imutils
import cv2
from pathlib import Path
import shutil

def ImageDiff(image1_file_name, _file_name, path='./'):
    '''Example: ImageDiff("a.jpg", "b.jpg", './static/')'''
    # actual_Folder = Path().absolute()
    # parent_folder = str(actual_Folder.parent)
    # path = parent_folder + path

    # load the two input images
    imageA = cv2.imread(path + image1_file_name)
    imageB = cv2.imread(path + _file_name)

    # convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (score, diff) = structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("Structural Similarity Index: {}".format(score))

    # threshold the difference image, followed by finding contours to
    # obtain the regions of the two input images that differ
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    #     # loop over the contours
    for c in cnts:
        # compute the bounding box of the contour and then draw the
        # bounding box on both input images to represent where the two
        # images differ
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # resize images 
    new_image_A = cv2.resize(imageA, None, fx=1, fy=1)
    new_image_B = cv2.resize(imageB, None, fx=1, fy=1)

    # Print image
    # cv2.imshow('image',new_image_B)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    res_path1 = path + "result2.png"
    res_path2 = path + "result1.png"

    cv2.imwrite(res_path1, new_image_A)
    cv2.imwrite(res_path2, new_image_B)

    return res_path1, res_path2, "{}".format(score)

if __name__ == "__main__":
    
    ImageDiff("a.jpg", "b.jpg", './static/')
