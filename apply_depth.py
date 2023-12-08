from depth_layer import *

path = "./image_To_Edit/"
image = Image.open(path + "imageTest.png")
size = 10


def resizer(img) :
    name = "test.png"
    depthMap = getDepthMap(img)
    img2 = Image.new('RGBA', (img.width*size, img.height*size), (255,255,255,1))
    for i in range(img.height) :
        for j in range(img.width) :
            color = img.getpixel((j,i))[:3]
            for m in range(size) :
                for n in range(size) :
                    if (i == 0 or j == 0 or i == img.height-1 or j == img.width-1) and (i == 0 and n == 0) or (j == 0 and m == 0) or (i == img.height-1 and n == size-1) or (j == img.width-1 and m == size-1) :
                        img2.putpixel((j*size+m,i*size+n), (0, 0, 0))
                    else : img2.putpixel((j*size+m,i*size+n), color)
    img2.show()
    img2.save("./resized_Images/" + name)

resizer(image)

# if (m == 0 and depthMap[i-1][j] > depthMap[i][j]) or (m == size-1 and ) or (n == 0 and) or (n == size-1 and) :
#     img2.putpixel((j*size+m,i*size+n), (0, 0, 0))