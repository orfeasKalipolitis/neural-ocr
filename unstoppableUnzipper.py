import os
import zipfile

font_folder = 'fonts'
extension = '.zip'
zip_folder = 'downloadedFonts'
fontExtension = '.ttf'

print('Gonna try unzipping all download zipped fonts.\n')

# Create font folder in case it doesn't exist
try:
    os.mkdir(font_folder)
    print('Font folder created')
except FileExistsError:
    print('Font folder already exists')

for dirItem in os.listdir(zip_folder):
    if dirItem.endswith(extension):
        try:
            file_name = os.path.abspath(zip_folder + '\\' + dirItem)
            print('Unzipping file: ' + file_name + '\n')
            zip_ref = zipfile.ZipFile(file_name)
            zip_ref.extractall(font_folder)
            zip_ref.close()
        except:
            print('Failed with zip: ' + file_name + '\n')
            continue

for dirItem in os.listdir(font_folder):
    if not dirItem.endswith(fontExtension):
        file_name = os.path.abspath(font_folder + '\\' + dirItem)
        os.remove(file_name)

print('Done unzipping all downloaded fonts :D\n')