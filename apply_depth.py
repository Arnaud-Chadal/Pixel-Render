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
                    if m in [0, size-1] or n in [0, size-1] :
                        img2.putpixel((j*size+m,i*size+n), (0, 0, 0))
                    else : img2.putpixel((j*size+m,i*size+n), color)
    img2.show()
    img2.save("./resized_Images/" + name)

resizer(image)