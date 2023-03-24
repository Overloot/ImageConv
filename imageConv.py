import sys
from PIL import Image
import glob


importImageType = ''
if sys.argv[1] == 'png':    
    importImageType = sys.argv[1]
elif sys.argv[1] == 'jpg':
    importImageType = sys.argv[1]
elif sys.argv[1] == 'webp':
    importImageType = sys.argv[1]
else:
     print("Wrong arguments", sys.argv[1])

image_list = []
str_ = '' + sys.argv[2] + "/*." + importImageType
print('patch ' + str_)
for filename in glob.glob(str_):
    im = Image.open(filename) #.convert("RGB")
    image_list.append(im)

exportImageType = ''
if sys.argv[3] == 'png':    
    exportImageType = sys.argv[3]
elif sys.argv[3] == 'jpg':
    exportImageType = sys.argv[3]
elif sys.argv[3] == 'webp':
    exportImageType = sys.argv[3]
else:
     print("Wrong arguments" + sys.argv[2])

print('Images count %d', len(image_list))
index = 0
for exportImage in image_list:
    str_ = '' + str(index) + '.' + exportImageType    
    print('Write to ' + str_ + '\n')
    exportImage.save(str_, exportImageType)
    index = index + 1
    

