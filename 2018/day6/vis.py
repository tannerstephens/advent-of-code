from PIL import Image
import os, math, hashlib

def colorHash(d):
  m = hashlib.sha256()
  m.update(d.encode())
  o = m.digest()
  r,g,b = o[0],o[1],o[2]

  return (r,g,b)

directory = os.path.dirname(os.path.realpath(__file__))

extra = 15
base = 65

with open(directory + "/input") as f:
  data = f.readlines()

coords = []

for line in data:
  work = line.split(", ")
  coords.append((int(work[0]) + extra, int(work[1][:-1]) + extra))


w = max(coords, key=lambda k: k[0])[0] + extra
h = max(coords, key=lambda k: k[1])[1] + extra

im = Image.new("RGB", (w*2, h*2), "black")

for x in range(w):
  for y in range(h):
    m = math.inf
    k = None
    for i,coord in enumerate(coords):
      distance = abs(coord[0] - x) + abs(coord[1] - y)

      if distance == m:
        k = "."
      elif distance < m:
        m = distance
        k = chr(base + i)
    color = colorHash(k)
    im.putpixel((x*2,y*2), color)
    im.putpixel((x*2+1,y*2), color)
    im.putpixel((x*2,y*2+1), color)
    im.putpixel((x*2+1,y*2+1), color)

im.save("vis.png")
