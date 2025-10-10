
###PART 1 Code

for i in range(10):
  xspeeds.append(random.randint(-10, 10))
  yspeeds.append(random.randint(-10, 10))
  bxs.append(random.randint(0, 200))
  bys.append(random.randint(0, 200))


#### Part 2 code

for i in range(10):

  bxs[i] +=xspeeds[i]
  bys[i] +=yspeeds[i]

  if bxs[i] < 10 or bxs[i] > width - 10:
    xspeeds[i] *=-1
  if bys[i] < 10 or bys[i] > height - 10:
    yspeeds[i] *= -1
  pygame.draw.circle(surface,(255, 0, 0), (bxs[i], bys[i]),bsize)

