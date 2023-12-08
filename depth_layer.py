from PIL import Image
path = "./depth_Layer/"
image = Image.open(path + "depthImage2.png")

def getDepthLevels(img) :
    depthLevels = []
    for i in range(img.height) :
        for j in range(img.width) :
            depth = img.getpixel((j,i))[:3]
            if not depth in depthLevels :
                depthLevels.append(depth)
    depthLevels.sort(key=lambda x: (x[0]+x[1]+x[2]), reverse=True)
    return depthLevels

#print(getDepthLevels(image))


def getDepthMap(img) :
    depthMap = [[] for i in range(img.height)]
    depthLevels = getDepthLevels(img)
    for i in range(img.height) :
        for j in range(img.width) :
            color = img.getpixel((j,i))[:3]
            depth = depthLevels.index(color)
            depthMap[i].append(depth)
    return depthMap


#print(getDepthMap(image))