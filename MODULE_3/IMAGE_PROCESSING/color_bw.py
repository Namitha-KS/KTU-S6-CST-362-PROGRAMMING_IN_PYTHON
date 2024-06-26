from images import Image
def blackAndWhite(image):
    blackPixel = (0,0,0)
    whitePixel = (255,255,255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r,g,b) = image.getPixel(x,y)
            average = (r+g+b)
            if average < 128:
                image.setPixel(x,y,blackPixel)
            else:
                image.setPixel(x,y,whitePixel)

def main(filename = "cat.png"):
    image = Image(filename)
    print("Close the image window to continue.")
    image.draw()
    blackAndWhite(image)
    print("Close the image window to quit")
    image.draw()
    image.save("cat.png")
if __name__ == "__main__":
    main()