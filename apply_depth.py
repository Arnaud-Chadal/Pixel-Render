from depth_layer import *

path = "./image_To_Edit/"
pathLayer = "./depth_Layer/"
image = Image.open(path + "apple.png")
layer = Image.open(pathLayer + "apple_depth.png")
size = 100


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
                        if img2.getpixel((i*size+m,j*size+n))[0] > color[0]-(80-m*2) and 80-m*2 >= 0 :
                            img2.putpixel((i*size+m,j*size+n), (color[0]-(80-m*2), color[1]-(80-m*2), color[2]-(80-m*2)))
                    if south :
                        if img2.getpixel((i*size+m,j*size+n))[0] > color[0]-(80-(size-m)*2) and 80-(size-m)*2 >= 0 :
                            img2.putpixel((i*size+m,j*size+n), (color[0]-(80-(size-m)*2), color[1]-(80-(size-m)*2), color[2]-(80-(size-m)*2)))
                    if west :
                        if img2.getpixel((i*size+m,j*size+n))[0] > color[0]-(80-n*2) and 80-n*2 >= 0 :
                            img2.putpixel((i*size+m,j*size+n), (color[0]-(80-n*2), color[1]-(80-n*2), color[2]-(80-n*2)))
                    if east :
                        if img2.getpixel((i*size+m,j*size+n))[0] > color[0]-(80-(size-n)*2) and 80-(size-n)*2 >= 0 :
                            img2.putpixel((i*size+m,j*size+n), (color[0]-(80-(size-n)*2), color[1]-(80-(size-n)*2), color[2]-(80-(size-n)*2)))
                    if not(north or south or west or east) or img2.getpixel((i*size+m,j*size+n))[0] == 255 :
                            img2.putpixel((i*size+m,j*size+n), color)
    img2.show()
    img2.save("./resized_Images/" + name)

resizer(image)