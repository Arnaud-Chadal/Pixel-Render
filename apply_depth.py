from depth_layer import *

path = "./depth_Layer/"
image = Image.open(path + "depthImage2.png")
size = 10


def applyDepthOnImage(x, y, depthMap) :
    if x in [0] or y in [0] :
        return (0,0,0)
    else : return (255, 255, 255)


def resizer(img) :
    name = "test.png"
    depthMap = getDepthMap(img)
    img2 = Image.new('RGBA', (img.width*size, img.height*size), (255,255,255,1))
    for i in range(img.height) :
        for j in range(img.width) :
            for m in range(size) :
                for n in range(size) :
                    img2.putpixel((j*size+m,i*size+n), applyDepthOnImage(m,n,depthMap))
    img2.show()
    img2.save("./resized_Images/" + name)

resizer(image)