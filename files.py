from pathlib import Path
from imageDiff import ImageDiff

class File:

    def __init__(self, path, name, date):
        self.path = path
        self.name = name
        self.date = date

    def getPath(self):
        return self.path

    def getName(self):
        return self.name

    def getDate(self):
        return self.date

class ImageFiles:

    def generateResultImages(self, assert_image_name='model'):
        to_evaluate = self.getLastsUniqueValues()
        print(to_evaluate.values())
        for path, most_recent_file in to_evaluate.items():
            try:
                image1 = most_recent_file + '.png'
                image2 = assert_image_name + '.png'

                ImageDiff(path)
                ImageDiff(path + '/', most_recent_file + '.png')
            except:
                print('******************* Problema na comparacao de ' + path)

    def getLastsUniqueValues(self):

        files_obj, unique_values = self.recursivelySearch('*.png')
        lasts_unique_values = {}

        # for obj in files_obj:
        for path in unique_values:
            dates = []
            for obj in files_obj:
                if unique_values[path] == obj.name:
                    dates.append(int(obj.date.replace('_', '').replace('-', '')))
            most_recent = self.intToStringDate(max(dates))
            # common_path = path + "/" + unique_values[path] + " "
            # most_recent_path = common_path + most_recent + ".png" 
            most_recent_file = unique_values[path] + " " + most_recent

            lasts_unique_values.update({path: most_recent_file})

        return lasts_unique_values

    def recursivelySearch(self, strToSearch):
        files_obj = []
        unique_values = {}

        target_folder = Path('static/')

        for file in target_folder.rglob(strToSearch):
            file = str(file)

            file_splited = file.rsplit('/', 1)
            path = file_splited[0]
            try:
                date = file_splited[1].rsplit(' ', 1)[1].rstrip('.png')

                name = path.rsplit('/', 1)[1]

                newfile = File(path, name, date)
                files_obj.append(newfile)
                unique_values.update({path: name})
            except:
                pass

        return files_obj, unique_values

    def intToStringDate(self, value):
        k = str(value)
        if len(k) < 14: return None
        k = k[0:8] + "_" + k[8:10] + "-" + k[10:12] + "-" + k[12:]
        return k

# def imageBaseExist(target_path):

#     #actual_Folder = Path().absolute()
#     target_file = Path(target_path + 'base.png')
#     exist = target_file.is_file()

#     return exist

    # verify if folder have imageBase, copy if exists
    # hasImgBase = imageBaseExist(path)
    # if not hasImgBase: shutil.copy(path + image2, path + 'base.png') 


if __name__ == "__main__":
    # resultPaths = ImageFiles()
    resultPaths = ImageFiles()
    resultPaths.generateResultImages()
