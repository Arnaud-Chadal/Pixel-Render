from PIL import Image


def getDepthLevels(nom_fichier, chemin=None) :
    img = Image.open(nom_fichier)
    depthLevels = []
    depthMap = []
    for i in range(img.height) :
        for j in range(img.width) :
            depth = img.getpixel((j,i))[:3]
            if not depth in depthLevels :
                depthLevels.append(depth)
    depthLevels.sort(key=lambda x: (x[0]+x[1]+x[2]), reverse=True)
    return depthLevels, depthMap

print(getDepthLevels("depthImage.png"))
