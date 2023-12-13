from PIL import Image

def getDepthLevels(img) :
    depthLevels = []
    for i in range(img.height) :
        for j in range(img.width) :
            depth = img.getpixel((i,j))[:3]
            if not depth in depthLevels :
                depthLevels.append(depth)
    depthLevels.sort(key=lambda x: (x[0]+x[1]+x[2]))
    return depthLevels

#print(getDepthLevels(image))


def getDepthMap(img) :
    depthMap = [[] for i in range(img.height+2)]
    depthLevels = getDepthLevels(img)
    for i in range(img.height+2) :
        for j in range(img.width+2) :
            if j == 0 or j == img.width+1 or i == 0 or i == img.height+1 :
                depthMap[i].append(-1)
            else :
                color = img.getpixel((j-1,i-1))[:3]
                depth = depthLevels.index(color)
                depthMap[i].append(depth)
    return depthMap


print(getDepthMap(Image.open("./depth_Layer/depthImage2.png")))