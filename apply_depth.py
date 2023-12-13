from depth_layer import *

path = "./image_To_Edit/"
pathLayer = "./depth_Layer/"
image = Image.open(path + "imageTest.png")
layer = Image.open(pathLayer + "depthImage2.png")
size = 10


def resizer(img) :
    name = "test.png"
    depthMap = getDepthMap(layer)
    img2 = Image.new('RGBA', (img.width*size, img.height*size), "white")
    for i in range(img.height) :
        for j in range(img.width) :
            color = img.getpixel((i, j))[:3]
            north = False
            south = False
            west = False
            east = False
            if depthMap[i][j+1] > depthMap[i+1][j+1] :
                north = True
            if depthMap[i+2][j+1] > depthMap[i+1][j+1] :
                south = True
            if depthMap[i+1][j] > depthMap[i+1][j+1] :
                west = True
            if depthMap[i+1][j+2] > depthMap[i+1][j+1] :
                east = True
            for m in range(size) :
                for n in range(size) :
                    if north :
                        if img2.getpixel((j*size+m,i*size+n))[0] > color[0]-(120-m*60) :
                            img2.putpixel((j*size+m,i*size+n), (color[0]-(120-m*60), color[1]-(120-m*60), color[2]-(120-m*60)))
                    if south :
                        if img2.getpixel((j*size+m,i*size+n))[0] > color[0]-(120-(size-m)*60) :
                            img2.putpixel((j*size+m,i*size+n), (color[0]-(120-(size-m)*60), color[1]-(120-(size-m)*60), color[2]-(120-(size-m)*60)))
                    if west :
                        if img2.getpixel((j*size+m,i*size+n))[0] > color[0]-(120-n*60) :
                            img2.putpixel((j*size+m,i*size+n), (color[0]-(120-n*60), color[1]-(120-n*60), color[2]-(120-n*60)))
                    if east :
                        if img2.getpixel((j*size+m,i*size+n))[0] > color[0]-(120-(size-n)*60):
                            img2.putpixel((j*size+m,i*size+n), (color[0]-(120-(size-n)*60), color[1]-(120-(size-n)*60), color[2]-(120-(size-n)*60)))
                    if not(north or south or west or east) or img2.getpixel((j*size+m,i*size+n))[0] == 255 :
                            img2.putpixel((j*size+m,i*size+n), color)
    img2.show()
    img2.save("./resized_Images/" + name)

resizer(image)