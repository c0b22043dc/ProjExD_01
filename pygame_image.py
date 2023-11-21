import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")#練習１
    bard_img = pg.image.load("ex01/fig/3.png")
    bard_img = pg.transform.flip(bard_img, True, False)#練習２
    bard_imgs = [bard_img,pg.transform.rotozoom(bard_img,10,1.0)]#練習３
    #演習１
    bard_imgs1 =[bard_img,pg.transform.rotozoom(bard_img,7.5,1.0)]
    bard_img1 = [bard_img,pg.transform.rotozoom(bard_img,5,1.0)]
    bard_imgs2 = [bard_img,pg.transform.rotozoom(bard_img,2.5,1.0)]
    bard_img2 = [bard_img,pg.transform.rotozoom(bard_img,0,1.0)]
    bard_imgs3 =[bard_img,pg.transform.rotozoom(bard_img,-2.5,1.0)]
    bard_img3 = [bard_img,pg.transform.rotozoom(bard_img,-5,1.0)]
    bard_imgs4 = [bard_img,pg.transform.rotozoom(bard_img,-7.5,1.0)]
    bard_img4 = [bard_img,pg.transform.rotozoom(bard_img,-10,1.0)]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%1600#練習4

        screen.blit(bg_img, [-x, 0])#練習４
        screen.blit(bg_img,[1600-x,0])
        screen.blit(bg_img, [-x, 0])

       #演習１
        screen.blit(bard_img,[300,200])
        screen.blit(bard_imgs2[tmr%2],[300,200])#2.5度
        screen.blit(bard_img1[tmr%2],[300,200])#5度
        screen.blit(bard_imgs1[tmr%2],[300,200])#7.5度
        screen.blit(bard_imgs[tmr%2],[300,200])#10度
        screen.blit(bard_imgs1[tmr%2],[300,200])#7.5度
        screen.blit(bard_img1[tmr%2],[300,200])#5度
        screen.blit(bard_imgs2[tmr%2],[300,200])#2.5度
        screen.blit(bard_img2[tmr%2],[300,200])#0度
        screen.blit(bard_imgs3[tmr%2],[300,200])#-2.5度
        screen.blit(bard_img3[tmr%2],[300,200])#-5度
        screen.blit(bard_imgs4[tmr%2],[300,200])#-7.5度
        screen.blit(bard_img4[tmr%2],[300,200])#-10度
        screen.blit(bard_imgs4[tmr%2],[300,200])#-7.5度
        screen.blit(bard_img3[tmr%2],[300,200])#-5度
        screen.blit(bard_imgs3[tmr%2],[300,200])#-2.5度
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()