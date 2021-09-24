import pygame, random, math
from pygame import mixer 

pg=pygame

# --------- MUSIC ---------
mixer.init() # initializes the mixer module
mixer.music.load('images&music\playsound.mp3') # lofi beats
mixer.music.play()

pg.init()

# --------- DISPLAY WINDOW ---------
a=pg.display.set_mode((1000,650)) # setting the size of display window
pg.display.set_caption('Hangman') # sets a name to the pygame window pop up


# --------- HANGMAN TITLE ---------
hang=pg.image.load('images&music\hangmantitle.png')


# --------- CHOOSE A CATEGORY ---------
categ=pg.image.load('images&music\chooseacategory.png')
cs=[] # cs is a list containing the categories - 4 categories
for i in range(1,5):
    c=pg.image.load('images&music\category'+str(i)+'.png')
    cs.append(c)
Font1=pg.font.SysFont('comicsans',28)   # font of the 'click on the category to play'

# --------- BLANK SPACES/ ANSWERS FONT ---------
Font2=pg.font.SysFont('calibri',37,'bold')

# --------- LIVES: ---------
Font3=pg.font.SysFont('calibri',40,'bold')

# --------- YOU LOST/WON WITH SAD AND FACES ---------
youwon=pg.image.load('images&music\youwon.png')
youlost=pg.image.load('images&music\youlost.png')
happyface=pg.image.load('images&music\happyface.png')
happyface=pg.transform.scale(happyface,(96,84))
sadface=pg.image.load('images&music\sadface.png')
sadface=pg.transform.scale(sadface,(84,84))

# --------- PLAY AGAIN ---------
playagain=pg.image.load('images&music\playagain.png')

# --------- LETTERS ---------
letters=[] #nested list of coordinates and the letter it contants - [x,y,letter]
achar=65 # ascii value of 'A'
chrcount=0
for j in [425,505,585]: # where j represents the y coordinates of each row
    horizontal=350 # starting coordinate of 'A'
    for i in range(9):
        if i==8 and j==585: # there are only supposed to be 8 buttons in the last row
            pass
        else:
            horizontal+=65 # spacing between the centers of 2 letters 
            letters.append([horizontal,j,chr(achar+chrcount),True]) # if chrcount=1, it'll give 66 which is B
            # the last value i.e. True will remain as True if the user hasn't clicked it
            # it will become False if the user has clicked it
            chrcount+=1
Font=pg.font.SysFont('comicsans',38)                 


# --------- CLOUDS ---------
clouds=pg.image.load('images&music\cloudforbg.png')
cloudsmall=pg.transform.scale(clouds,(75,35)) # resizes the clouds
# you can use pg.transform.rotate to rotate the images of the clouds


# --------- HANGMAN IMAGES ---------
hms=[] # creating a list of the hangman images
for i in range(1,8):
    hm=pg.image.load('images&music\hangman'+str(i)+'.png')
    aftertransform=pg.transform.scale(hm,(400,450))
    hms.append(aftertransform)
position=0 # 0-starting, 1- one error, 2- two errors and so on
# index of the hms list



def draw(f,word): # deals with the hangman figures, colours, bg colour etc
    global cl1,cl2,cl3,cl4,cl5,cl6,letters, guessed, position

    # --------- BACKGROUND ---------
    a.fill((0,190,255)) # light blue colour for the bg (R,G,B)


    # --------- CLOUDS ---------
    a.blit(cloudsmall,(cl1.x,cl1.y))
    a.blit(cloudsmall,(cl2.x,cl2.y))
    a.blit(cloudsmall,(cl3.x,cl3.y))
    a.blit(cloudsmall,(cl4.x,cl4.y))
    a.blit(cloudsmall,(cl5.x,cl5.y))
    a.blit(cloudsmall,(cl6.x,cl6.y))


    # --------- HANGMAN TITLE ---------
    a.blit(hang,(272,50))

    if f==0: # The starting page (one with choosing the category)
        
        a.blit(categ,(250,225)) # choose the category picture
        wc,hc=420,300 # coordinates of movies
        for i in range(4):
            if i>=2: # as the have more letters
                wc=410
            a.blit(cs[i],(wc,hc)) #cs is a list containing the categories
            hc+=62
        notice=Font1.render('*click on the category to play*',1,(0,0,0))
        a.blit(notice, (350,600))


    if f==1: # the main game page
        
        # --------- MAKING THE BLANK SPACES ---------
        onthescreen=''
        for p in word:
            if p in guessed: # if the letter that the user guessed is part of the word
                onthescreen+=p+' '
            else:
                if p==' ':
                    onthescreen+=p+'  '
                else:
                    onthescreen+='_ ' # blank
        
        do=Font2.render(onthescreen,1,(0,0,0))
        a.blit(do,(380,250))

        # --------- HANGMAN ---------
        if position<=6:
            a.blit(hms[position],(65,225)) # displaying the hangman images based on the index
        else:
            a.blit(hms[6],(65,225))
        


        # --------- ALPHABETS ---------
        for letter in letters:
            x,y,l,visible=letter # x coordinate & y coordinate & letter & true if it's visible
            if visible:
                pg.draw.circle(a,(128,0,0),(x,y),23.5,3) # (display, colour code for maroon, coordinates, radius, thickness)
                alpha=Font.render(l,1,(0,0,0))  # renders the alphabets
                # font.render( text, antialias, colour) -- antialias- a boolean, if true, the letters will have smooth edges
                h,v=(alpha.get_width()/2),(alpha.get_height()/2)
                a.blit(alpha,(x-h,y-v))

        # --------- LIVES: ---------
        live=Font3.render('LIVES :  '+str(6-position),1,(0,0,0))
        a.blit(live,(90,550))
        




    if f==2 or f==3: # the "you lost/won" the game and do you wanna try again

        if f==2:
            a.blit(youwon,(300,225))
            a.blit(happyface,(75,200))
            a.blit(happyface,(841,200))
            happy=Font2.render('Well Done, you aced it!',1,(0,0,0))
            a.blit(happy,(290,350))
        if f==3:
            a.blit(youlost,(275,225))
            a.blit(sadface,(841,200))
            a.blit(sadface,(75,200))
            sad=Font2.render('Word: '+word,1,(0,0,0))
            a.blit(sad,(310,350))
            sad2=Font2.render('Better Luck Next Time!',1,(0,0,0))
            a.blit(sad2,(310,400))
        pg.draw.rect(a,(128,0,0),[378,500,250,75],4) # drawing the rectangle for play again
        # (display,colour,[starting corner x coordinate, y coordinate, length, breadth of the rectangle],thickness)
        h,v=(playagain.get_width()/2),(playagain.get_height()/2)
        a.blit(playagain,(505-h,537-v))


    pg.display.update() # updates the changes made to the display window
    # the colour of the window does not change without this statement    




def main(): # main game function that has the main game loop
    global cl1,cl2,cl3,cl4,cl5,cl6, guessed, position
    word=0

    # --------- THE WORDS ---------
    SPORTS=['BASKETBALL','FOOTBALL','GOLF','HORSE RACING','FIGURE SKATING','FENCING','RUGBY','TABLE TENNIS']
    MOVIES=['THE GODFATHER','THE WIZARD OF OZ','THE SOUND OF MUSIC','MISSION IMPOSSIBLE','FAST AND FURIOUS','INCEPTION','THE DARK KNIGHT','THE CONJURING']
    SINGERS=['TAYLOR SWIFT','SELENA GOMEZ','ED SHEERAN','JUSTIN BIEBER','ADELE','BILLIE EILISH','ARIANA GRANDE','DUA LIPA']
    ANIMALS=['DONKEY','MONKEY','ELEPHANT','GIRAFFE','POLAR BEAR','JAGUAR','ALLIGATOR','HIPPOPOTAMUS']
    position=0
    f=0
    
    # --------- CLOUDS ---------
    cl1=pg.Rect(0,25,75,35) # for the mobile clouds - (x coordinate, y coordinate, width of the cloud, height)
    cl2=pg.Rect(333.3,25,75,35)
    cl3=pg.Rect(666.6,25,75,35)
    cl4=pg.Rect(166.65,100,75,35)
    cl5=pg.Rect(499.95,100,75,35)
    cl6=pg.Rect(833.25,100,75,35) # distance between each cloud is 258.3
    # therefore the distance between the start of each cloud is 333.3

    clock=pg.time.Clock() # creates an object that helps keep track of time
    run=True
    
    
    # --------- MAIN PROGRAM ---------
    while run:
        clock.tick(60)
        # frames per second = 60
        # why we're using this- the game continuously refreshes and draws as long as the py game window is open
        # by doing this, the program will never run at more than 60 frames per second
        
        for event in pg.event.get():
            if event.type==pg.QUIT: # if the user quit the window
                run=False # ends the while loop and quits the game
                
            # ------ DETERMINING WHAT THE USER CLICKED -----
            # ------ BUTTON COLLISION ----------------------
            if event.type==pg.MOUSEBUTTONDOWN: # if a user clicks anywhere
                px,py=pg.mouse.get_pos() # stores the x and y coordinates where the user clicked
                
                        
                    
                if f==0:
                    a=random.randint(0,7)
                    tt=0
                    guessed=[' ',]
                    # DECIPHER WHICH CATEGORY THE USER SELECTED
                    if (px>=420 and px<=548) and (py>=298 and py<=319):
                        word=MOVIES[a]
                        tt+=1
                    if (px>=420 and px<=548) and (py>=362 and py<=379):
                        word=SPORTS[a]
                        tt+=1
                    if (px>=409 and px<=561) and (py>=423 and py<=441):
                        word=SINGERS[a]
                        tt+=1
                    if (px>=409 and px<=561) and (py>=486 and py<=504):
                        word=ANIMALS[a]
                        tt+=1
                    if tt!=0:
                        f=1
                    break


                if f==2 or f==3:
                    if (px>=380 and px<=630) and (py>=500 and py<=575):
                        f=0 # going back to the home screen
                        position=0 # making hangman position to the beginning
                        for i in letters:
                            i[3]=True # making the letters visible again
                        
                if f==1:
                    for i in letters:
                        x,y,l,visible=i # as letters is a nested list of [x coordinate, y coordinate, alphabet, whether it's visible of not]
                        if visible:
                            d=math.sqrt(((x-px)**2) + ((y-py)**2)) # distance formula between 2 coordinates
                            if d<23.5:
                                i[3]=False # The user has clicked the button so it should no longer be visible (visible=False)
                                guessed.append(l) # add the letter to the guessed list
                                if l not in word: # if the guessed letter is incorrect, update the hangman figure
                                    position+=1

                    game=True
                    for i in word:
                        if i not in guessed: # if one of the correct letters are not part of the list, you have not won yet
                            game=False
                            break
                    if game:
                        f=2 # you won the game
                        
                    if position==6:
                        f=3 # all 6 lives are over, you lost the game


        # --------- CLOUD POSITIONS ---------
        if cl1.x==925: # when the cloud reaches toward the end of the screen,
            cl1.x=-75  # it gets shifted to (-75) which is the position of the start of the cloud i.e. when the
                       # end of the cloud enters the screen
        if cl2.x==925:
            cl2.x=-75
        if cl3.x==925:
            cl3.x=-75
        if cl4.x==925:
            cl4.x=-75
        if cl5.x==925:
            cl5.x=-75
        if cl6.x==925:
            cl6.x=-75
            

        # --------- MOVING CLOUDS ---------
        cl1.x+=1 # changes the position of cloud to the right by 1 coordinate every fps i.e. 60 coordinates in a sec
        cl2.x+=1
        cl3.x+=1
        cl4.x+=1
        cl5.x+=1
        cl6.x+=1

        
        draw(f,word)
    pg.quit() # quits pygame and closes the window
    # without the above lines, the pygame window wont close unless you close the python shell window

main()
