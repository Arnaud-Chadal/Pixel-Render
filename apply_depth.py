from depth_layer import *

path = "./depth_Layer/"
image = Image.open(path + "depthImage2.png")

def resizer(img, size) :
    name = "test.png"
    img2 = Image.new('RGBA', (img.width*size, img.height*size), (255,255,255,1))
    for i in range(img.height) :
        for j in range(img.width) :
            for m in range(size) :
                for n in range(size) :
                    img2.putpixel((j*size+m,i*size+n), img.getpixel((j,i)))
    img2.show()
    img2.save("./resized_Images/" + name)

resizer(image, 1000)