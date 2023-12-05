# importing PIL.Image library and os library
from PIL import Image #from PIL import Image 
import os

# Deletes old created images if they exist
images = ["combinedFilters.jpg","filter1.jpg","filter2.jpg","filter3.jpg","grey.jpg"]
for i in images:
  if os.path.exists(i):
    os.remove(i)

# Adds two blank lines before any output
print("\n\n")

# Opens image - upload a Local File into repl.it
img = Image.open('flower.jpg')

# Rescale image size down, if original is too large
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
  scale = mwidth
else:
  scale = mheight
if scale != 0:
  img = img.resize( (width // scale, height // scale) )


#####################
#    Your Filter    #
#####################

#decreases the green value by 50% to make a purple color
def purplescale():
  newpix = list(img.getdata())
  
  #apply filter
  for i in range(len(newpix)):
    p = newpix[i]
    r, g, b = p
    #Get 50% of the green value, and half it. Then subtract it to make the image look purple. 
    if g != 0:
        per = int((g * 50) / 100)
        newg = g - per
        newpix[i] = (r, newg, b)


  newImage = Image.new("RGB", img.size) 
  newImage.putdata(newpix)
  return newImage

#####################################
#    Your Filters with User Input   #
#####################################

#increases RGB values by a factor inputed by a user to make the image brighter
def brightdark():
  newpix = list(img.getdata())
  fxtr = float(input("What factor would you like the image to be brightened/darkened by?\n"))
    
  for i in range(len(newpix)):
      r, g, b = newpix[i]

      # Apply the brightness/darkness
      newr = int(r * fxtr)
      newg = int(g * fxtr)
      newb = int(b * fxtr)

       # Ensure values do not go over or under 255 or 0
      newr = max(0, min(newr, 255))
      newg = max(0, min(newg, 255))
      newb = max(0, min(newb, 255))

      # Update the pixel in the list
      newpix[i] = (newr, newg, newb)

  # Create a new image with the modified pixelz
  modified_img = Image.new(img.mode, img.size)
  modified_img.putdata(newpix)

  return modified_img

    


#itarates through the image based on a factor, then makes a smaller white image, wich the gathered pixels will be appended to. 
def compress():
  newpix = list(img.getdata())
  fxtr = float(input("Factor to compress?\n"))
  width, height = img.size
  compr = []

  # Iterate through pixels
  for y in range(0, height, int(fxtr)):
      row = []
      for x in range(0, width, int(fxtr)):
          # Get the pixel at (x, y)
          pixel = img.getpixel((x, y))
          row.append(pixel)

      compr.append(row)

  #create the blank white image with proper dimensions
  compr_img = Image.new("RGB", (len(compr[0]), len(compr)), "white")
  for y, row in enumerate(compr):
      for x, pixel in enumerate(row):
          compr_img.putpixel((x, y), pixel)

  return compr_img

# Creates the four filter images and saves them to our files


b = purplescale()
b.save("purplescale.jpg")
c = brightdark()
c.save("brightdark.jpg")
d = compress()
d.save("compressed.jpg")

# Image filter names for use below
f1 = "purplescale"
f2 = "brightness"
f3 = "compress"

# Apply multiple filters through prompts with the user
answer = input("\nWhich filter do you want me to apply?\n" +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
while answer != f1 and answer != f2 and answer != f3 and answer != "none":
  answer = input("\nIncorrect filter, please enter:\n  " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")

while answer == f1 or answer == f2 or answer == f3:
  if answer == f1:
   img = purplescale()
  elif answer == f2:
   img = brightdark()
  elif answer == f3:
   img = compress()
  else:
    break
  print("Filter \"" + answer + "\" applied...")
  answer = input("\nWhich filter do you want me to apply next?\n" + "\n"+  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
  while answer != "grey" and answer != f1 and answer != f2 and answer != f3 and answer != "none":
    answer = input("\nIncorrect filter, please enter:\n" +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
print("Image being created...Done")

# Create the combined filter image and saves it to our files
img.save("combinedFilters.jpg")