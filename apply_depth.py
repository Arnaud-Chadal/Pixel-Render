from depth_layer import *

path = "./image_To_Edit/"
pathLayer = "./depth_Layer/"
image = Image.open(path + "apple.png")
layer = Image.open(pathLayer + "apple_depth.png")
size = 10


def resizer(img) :
    name = "test.png"
    depthMap = getDepthMap(layer)
    img2 = Image.new('RGBA', (img.height*size, img.width*size), "white")
    for i in range(img.height) :
        for j in range(img.width) :
            color = img.getpixel((i, j))[:3]
            north = depthMap[j+1][i] > depthMap[j+1][i+1]
            south = depthMap[j+1][i+2] > depthMap[j+1][i+1]
            west = depthMap[j][i+1] > depthMap[j+1][i+1]
            east = depthMap[j+2][i+1] > depthMap[j+1][i+1]
            for m in range(size) :
                for n in range(size) :
                    if north :
                        if img2.getpixel((i*size+m,j*size+n))[0] > color[0]-(180-m*45) and 180-m*45 >= 0 :
                            img2.putpixel((i*size+m,j*size+n), (color[0]-(180-m*45), color[1]-(180-m*45), color[2]-(180-m*45)))
                    if south :
                        if img2.getpixel((i*size+m,j*size+n))[0] > color[0]-(180-(size-m)*45) and 180-(size-m)*45 >= 0 :
                            img2.putpixel((i*size+m,j*size+n), (color[0]-(180-(size-m)*45), color[1]-(180-(size-m)*45), color[2]-(180-(size-m)*45)))
                    if west :
                        if img2.getpixel((i*size+m,j*size+n))[0] > color[0]-(180-n*45) and 180-n*45 >= 0 :
                            img2.putpixel((i*size+m,j*size+n), (color[0]-(180-n*45), color[1]-(180-n*45), color[2]-(180-n*45)))
                    if east :
                        if img2.getpixel((i*size+m,j*size+n))[0] > color[0]-(180-(size-n)*45) and 180-(size-n)*45 >= 0 :
                            img2.putpixel((i*size+m,j*size+n), (color[0]-(180-(size-n)*45), color[1]-(180-(size-n)*45), color[2]-(180-(size-n)*45)))
                    if not(north or south or west or east) or img2.getpixel((i*size+m,j*size+n))[0] == 255 :
                            img2.putpixel((i*size+m,j*size+n), color)
    img2.show()
    img2.save("./resized_Images/" + name)

resizer(image)