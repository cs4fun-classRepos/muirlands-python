complete the code in main.py with the following detection codes

```python
#########################################
#detecting collisions
#########################################
for missile in missileList:
    killed = pygame.sprite.spritecollide(missile, alienList, True)
    if len(killed) > 0:
    missileList.remove(missile)
    allSpriteList.remove(missile)
########################################
#reset levels for winning
########################################
if len(alienList) == 0:
    level+=1
    for i in range(50):
    alien = Alien()
    alien.yspeed -= level * 5
    allSpriteList.add(alien)
    alienList.add(alien)
#######################################
#reset levels for losing
#######################################
hit1 = pygame.sprite.spritecollide(player, alienList, False)
if len(hit1) > 0:
    pygame.event.pump()
    scoretext = myfont.render("Sorry. You lost! Good luck next time!", 1, (255,0,0))
    screen.blit(scoretext, (100, 200))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()



```