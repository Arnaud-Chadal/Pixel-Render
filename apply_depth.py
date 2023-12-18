from depth_layer import *

path = "./image_To_Edit/"
pathLayer = "./depth_Layer/"
image = Image.open(path + "lemon.png")
layer = Image.open(pathLayer + "lemon_depth.png")
depth_levels = getDepthLevels(layer)
size = 100

strenght = 100
lenght = 4


def resizer(img) :
    name = "test.png"
    depthMap = getDepthMap(layer, depth_levels)
    print(depthMap)
    img8 = Image.new('RGBA', (img.height*size, img.width*size), "white")
    for i in range(img.height) :
        for j in range(img.width) :
            color = img.getpixel((i, j))[:3]
            if depthMap[j+1][i+1] != -1 :
                north = depthMap[j+1][i] > depthMap[j+1][i+1]
                south = depthMap[j+1][i+2] > depthMap[j+1][i+1]
                west = depthMap[j][i+1] > depthMap[j+1][i+1]
                east = depthMap[j+2][i+1] > depthMap[j+1][i+1]
                northwest = depthMap[j][i] > depthMap[j+1][i+1]
                northeast = depthMap[j+2][i] > depthMap[j+1][i+1]
                southwest = depthMap[j][i+2] > depthMap[j+1][i+1]
                southeast = depthMap[j+2][i+2] > depthMap[j+1][i+1]
                for m in range(size) :
                    for n in range(size) :
                        if north :
                            if img8.getpixel((i*size+m,j*size+n))[0] > color[0]-(strenght-m*lenght) and strenght-m*lenght >= 0 :
                                img8.putpixel((i*size+m,j*size+n), (color[0]-(strenght-m*lenght), color[1]-(strenght-m*lenght), color[2]-(strenght-m*lenght)))
                        if south :
                            if img8.getpixel((i*size+m,j*size+n))[0] > color[0]-(strenght-(size-m)*lenght) and strenght-(size-m)*lenght >= 0 :
                                img8.putpixel((i*size+m,j*size+n), (color[0]-(strenght-(size-m)*lenght), color[1]-(strenght-(size-m)*lenght), color[2]-(strenght-(size-m)*lenght)))
                        if west :
                            if img8.getpixel((i*size+m,j*size+n))[0] > color[0]-(strenght-n*lenght) and strenght-n*lenght >= 0 :
                                img8.putpixel((i*size+m,j*size+n), (color[0]-(strenght-n*lenght), color[1]-(strenght-n*lenght), color[2]-(strenght-n*lenght)))
                        if east :
                            if img8.getpixel((i*size+m,j*size+n))[0] > color[0]-(strenght-(size-n)*lenght) and strenght-(size-n)*lenght >= 0 :
                                img8.putpixel((i*size+m,j*size+n), (color[0]-(strenght-(size-n)*lenght), color[1]-(strenght-(size-n)*lenght), color[2]-(strenght-(size-n)*lenght)))
                        if northwest :
                            if img8.getpixel((i*size+m,j*size+n))[0] > color[0]-(strenght-max(m, n)*lenght) and strenght-max(m, n)*lenght >= 0 :
                                img8.putpixel((i*size+m,j*size+n), (color[0]-(strenght-max(m, n)*lenght), color[1]-(strenght-max(m, n)*lenght), color[2]-(strenght-max(m, n)*lenght)))
                        if northeast :
                            if img8.getpixel((i*size+m,j*size+n))[0] > color[0]-(strenght-max(m, (size-n))*lenght) and strenght-max(m, (size-n))*lenght >= 0 :
                                img8.putpixel((i*size+m,j*size+n), (color[0]-(strenght-max(m, (size-n))*lenght), color[1]-(strenght-max(m, (size-n))*lenght), color[2]-(strenght-max(m, (size-n))*lenght)))
                        if southwest :
                            if img8.getpixel((i*size+m,j*size+n))[0] > color[0]-(strenght-max((size-m), n)*lenght) and strenght-max((size-m), n)*lenght >= 0 :
                                img8.putpixel((i*size+m,j*size+n), (color[0]-(strenght-max((size-m), n)*lenght), color[1]-(strenght-max((size-m), n)*lenght), color[2]-(strenght-max((size-m), n)*lenght)))
                        if southeast :
                            if img8.getpixel((i*size+m,j*size+n))[0] > color[0]-(strenght-max((size-m), (size-n))*lenght) and strenght-max((size-m), (size-n))*lenght >= 0 :
                                img8.putpixel((i*size+m,j*size+n), (color[0]-(strenght-max((size-m), (size-n))*lenght), color[1]-(strenght-max((size-m), (size-n))*lenght), color[2]-(strenght-max((size-m), (size-n))*lenght)))
                        if not(north or south or west or east or northwest or northeast or southwest or southeast) or img8.getpixel((i*size+m,j*size+n))[0] == 255 :
                            img8.putpixel((i*size+m,j*size+n), color)
            else :
                for m in range(size) :
                    for n in range(size) :
                        img8.putpixel((i*size+m,j*size+n), color)
    img8.show()
    img8.save("./resized_Images/" + name)

resizer(image)