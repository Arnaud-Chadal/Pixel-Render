from depth_layer import *

path = "./image_To_Edit/"
pathLayer = "./depth_Layer/"
image = Image.open(path + "imageTest.png")
layer = Image.open(pathLayer + "depthImage2.png")
size = 10


def resizer(img) :
    name = "test.png"
    depthMap = getDepthMap(layer)
    img2 = Image.new('RGBA', (img.width*size, img.height*size), (255,255,255,1))
    for i in range(img.height) :
        for j in range(img.width) :
            color = img.getpixel((i, j))[:3]
            north = False
            south = False
            west = False
            east = False
            if depthMap[i-1][j] > depthMap[i][j] :
                north = True
            if depthMap[i+1][j] > depthMap[i][j] :
                south = True
            if depthMap[i][j-1] > depthMap[i][j] :
                west = True
            if depthMap[i][j+1] > depthMap[i][j] :
                east = True
            for m in range(size) :
                for n in range(size) : 
                    if north :
                        img2.putpixel((j*size+m,i*size+n), (color[0]-(200-m*40), color[1]-(200-m*40), color[2]-(200-m*40)))
                    if south :
                        img2.putpixel((j*size+m,i*size+n), (color[0]-(200-(size-m)*40), color[1]-(200-(size-m)*40), color[2]-(200-(size-m)*40)))
                    if west :
                        img2.putpixel((j*size+m,i*size+n), (color[0]-(50-n*10), color[1]-(50-n*10), color[2]-(50-n*10)))
                    if east :
                        img2.putpixel((j*size+m,i*size+n), (color[0]-(200-(size-n)*40), color[1]-(200-(size-n)*40), color[2]-(200-(size-n)*40)))
                    if not(north or south or west or east) :
                        img2.putpixel((j*size+m,i*size+n), color)
    img2.show()
    img2.save("./resized_Images/" + name)

resizer(image)