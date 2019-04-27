centerX = 0
centerY = 0
road1Ybeg = centerY + 30
road1Yend = centerY + 10

road2Xbeg = centerX - 30
road2Xend = centerX - 10

road3Xbeg = centerX + 30
road3Xend = centerX + 10

output = open("output.txt", "w+")

output.write("(")
output.write(str(centerX))
output.write(", ")
output.write(str(road1Ybeg))
output.write(")")

output.write(",")

output.write("(")
output.write(str(centerX))
output.write(", ")
output.write(str(road1Yend))
output.write(")")
output.write(",[] \n")

output.write("(")
output.write(str(centerX))
output.write(", ")
output.write(str(road1Yend))
output.write(")")

output.write(",")

output.write("(")
output.write(str(road2Xend))
output.write(", ")
output.write(str(centerY))
output.write(")")
output.write(",[] \n")

output.write("(")
output.write(str(road3Xbeg))
output.write(", ")
output.write(str(centerY))
output.write(")")

output.write(",")

output.write("(")
output.write(str(road3Xend))
output.write(", ")
output.write(str(centerY))
output.write(")")
output.write(",[] \n")

output.close()



