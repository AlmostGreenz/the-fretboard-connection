#Welcome to the Code for The Fretboard Connection by Ryan Green!

add_library('sound') # Imports Sound Library

#Defining Variables

notpaused = True
x = -30
score = 0
muscount = 218.51
introlist = [0]*535
difficulty = True #True = Beginner, False = Normal
diff = "Beginner"
notmainmenu = False
whammycount = 0
whamperc = 0
whammyready = False
shift = False
wham = False
whammul = 1
endscreen = False
menudown = 0
menurdm = int(random(0,4))
endcount = 0
highest = 0
quit = False

def setup():
    size(800, 600) #Set Up Size
    global sound1, sound2, sound3, sound4, sound5, sound6, sound7, sound8, sound9, sound10, sound11, logo, menumusic, menufont, notefont, diffsound, rocksound, lightsound, rlightsound, guitar, clrbars #Global Variables
    #Import from data folder
    sound1 = SoundFile(this, "Sound1.wav")
    sound2 = SoundFile(this, "Sound2.wav")
    sound3 = SoundFile(this, "Sound3.wav")
    sound4 = SoundFile(this, "Sound4.wav")
    sound5 = SoundFile(this, "Sound5.wav")
    sound6 = SoundFile(this, "Sound6.wav")
    sound7 = SoundFile(this, "Sound7.wav")
    sound8 = SoundFile(this, "Sound8.wav")
    sound9 = SoundFile(this, "Sound9.wav")
    sound10 = SoundFile(this, "Sound10.wav")
    sound11 = SoundFile(this, "Sound11.wav")
    menumusic = SoundFile(this, "Ubiquitous Unanimity - Ryan Green.wav")
    logo = loadImage("Game_Logo.png")
    menufont = loadFont("Skinny-48.vlw")
    notefont = loadFont("LucidaSans-50.vlw")
    diffsound = SoundFile(this, "Blip_Select25.wav")
    rocksound = SoundFile(this, "Guitar2.wav")
    lightsound = SoundFile(this, "Lightning.wav")
    rlightsound = SoundFile(this, "gninthgiL.wav")
    guitar = loadImage("Guitar.png")
    clrbars = loadImage("SMPTE_Color_Bars.svg.png")

def draw():
    background(255) #White Background in draw loop to replace old objects
    global x, score, muscount, difficulty, whammycount, whamperc, whammyready, wham, whammul, endscreen, menudown, menurdm, highest #Global Variables
    
    textFont(notefont) #Score Display in Bottom Right
    textSize(14)
    text("Score: %s" %score, 2, 598)
    textSize(12)

    if notmainmenu and not endscreen: #Ensures no objects drawn on other screens (besides game screen)
        if notpaused: # If paused, allows movement of notes with x
            x+=2
            menumusic.amp(0) # Stops music from playing during gameplay
            
        if whammycount == 55: #Tests for Full Whammy-Charge
            whammyready = True
        elif whammycount > 55: #Stops overpowering Whammy
            whammycount -= 1

        fill(101,210,238) #Whammy-Meter
        stroke(101,210,238)
        rect(1,550,(whammycount/55.0)*100, 10)
        stroke(0)
        line(0,550, 101, 550)
        line(0,550,0,560)
        line(0,560,101,560)
        line(101, 550, 101, 560)
        whamperc = (whammycount/55.0)*100
        whamperc = round(whamperc,1)
        text("Whammy at %s %s" %(whamperc, "%"), 1 , 572) #Whammy Percentage
        if whammyready:
            fill(random(255), random(255), random(255)) #Random Colours when Fully Charged
            text("Whammy Ready!", 2 , 560)
        
        if wham: #Activation of Whammy
            whammycount -= 0.1
            whammyready = False
            whammul = 2
            if whammycount <= 0:
                wham = False
                whammul = 1
                whammycount = 0
                rlightsound.amp(0.45)
                rlightsound.play()

            
        textAlign(LEFT)
        
        #RED Note
        if x < 1800:
            for nred in range(20):
                if wham:
                    stroke(101,210,238)
                fill(227, 78, 78)
                ellipse(670, -15 +(nred*-55) + x, 75, 50)
                fill(232, 117, 117)
                if introlist[(nred * 2) + 1] == 1:
                    fill(255)
                ellipse(670, -15 +(nred*-55) + x, 47.5, 35)
                stroke(0)
                if difficulty:
                    fill(255)
                    textSize(25)
                    text("<=", 650, -30 + (nred*-55) + x, 75, 50)
    
        #GREEN Note
        if x < 1800:
            for ngreen in range(20):
                if wham:
                    stroke(101,210,238)
                fill(53, 211, 11)
                ellipse(750, (ngreen*-55) + x, 75, 50)
                fill(41, 134, 16)
                if introlist[(ngreen * 2)] == 1:
                    fill(255)
                ellipse(750, (ngreen*-55) + x, 47.5, 35) #1-8
                stroke(0)
                if difficulty:
                    fill(255)
                    textSize(25)
                    text("=>", 730, -15 + (ngreen*-55) + x, 75, 50)
         
        #GREEN Note Post-Intro      
        for ngreen in range(22,24) + range(29,31) + range(36,38) + range(43,45) + range(135,138) + range(195,197) + range(202,204) + range(277,280) + range(337,339) + range(344,346) + range(395,396) + range(399,400) + range(406,409) + range(419,420) + range(427,428) + range(457,458):
            #^Range + 20 = Position in introlist
            if wham:
                    stroke(101,210,238) #Changes Outline Colour for WHAMMY!
            fill(53, 211, 11) #Fill Outside
            ellipse(750, (ngreen*-55) + x, 75, 50) #Draw Outside
            fill(41, 134, 16) #Fill Inside
            if introlist[(ngreen + 20)] == 1: #If already hit, fill white
                    fill(255)
            ellipse(750, (ngreen*-55) + x, 47.5, 35) #Draw Inside
            stroke(0) #Ouline to Black
            if difficulty: #Draw label for beginner mode
                fill(255)
                textSize(25)
                text("=>", 730, -15 + (ngreen*-55) + x, 75, 50)
            
        #BLUE Note    
        for nblue in range(20,22) + range(24, 25) + range(27,29) + range(31,32) + range(34,36) + range(38,39) + range(41,43) + range(45,46) + range(193,195) + range(197,198) + range(200,202) + range(204,205) + range(335,337) + range(339,340) + range(342,344) + range(346,347):
            if wham:
                    stroke(101,210,238)
            fill(84, 82, 203)
            ellipse(590,(nblue*-55) + x, 75, 50)
            fill(112, 111, 193)
            if introlist[(nblue + 20)] == 1:
                    fill(255)
            ellipse(590, (nblue*-55) + x, 47.5, 35)
            stroke(0)
            if difficulty:
                    fill(255)
                    textSize(25)
                    text(" ^", 575, -15 + (nblue*-55) + x, 75, 50)
                    
        #YELLOW Note
        for nyell in range(25,27) + range(32,34) + range(39,41) + range(46,49) + range(55,57) + range(63,65) + range(71,73) + range(85,87) + range(92,94) + range(99,101) + range(104,107) + range(112,114) + range(119,121) + range(126,128) + range(131,135) + range(138,141) + range(198,200) + range(205,207)  + range(213,215) + range(227,229) + range(234,236)  + range(241,243) + range(246,249) + range(254,256) + range(261,263) + range(268,270) + range(273,277) + range(280,283) + range(340,342) + range(347,349) + range(354,356) + range(359,362) + range(367,369) + range(373,375) + range(377,379) + range(382,385) + range(434,436) + range(442,444) + range(449,451) + range(454,457) + range(458,461) + range(463,466) + range(473,475) + range(478,481) + range(486,488) + range(491,494) + range(499,501) + range(504,508):
            if wham:
                    stroke(101,210,238)
            fill(191, 193, 82)
            ellipse(530,(nyell*-55) + x, 75, 50)
            fill(231, 234, 71)
            if introlist[(nyell + 20)] == 1:
                    fill(255)
            ellipse(530, (nyell*-55) + x, 47.5, 35)
            stroke(0)
            if difficulty:
                fill(255)
                textSize(25)
                text(" v", 515, -15 + (nyell*-55) + x, 75, 50)
                
        #PURPLE/FUSCHIA Note    
        for npurp in range(49,51) + range(54,55) + range(57, 61) + range(62,63) + range(65,67) + range(70,71) + range(73,77) + range(78,80) + range(153,154) + range(166,167) + range(179,180) + range(192,193) + range(207,209) + range(212,213) + range(215,219) + range(220,222) + range(295,296) + range(308,309) + range(321,322) + range(334,335) + range(388,389) + range(412,413)+ range(421,422) + range(426,427) + range(428,430) + range(433,434) + range(436,440) + range(441,442):
            if wham:
                    stroke(101,210,238)
            fill(193, 76, 188)
            ellipse(470,(npurp*-55) + x, 75, 50)
            fill(203, 132, 200)
            if introlist[(npurp + 20)] == 1:
                    fill(255)
            ellipse(470, (npurp*-55) + x, 47.5, 35)
            stroke(0)
            if difficulty:
                fill(255)
                textSize(25)
                text(" a", 455, -15 + (npurp*-55) + x, 75, 50)
         
        #SILVER Note       
        for nsilv in range(51,52) + range(67,68) + range(151,153) + range(164,166) + range(177,179) + range(190,192) + range(209,210) + range(293,295) + range(306,308) + range(319,321) + range(332,334)  + range(387,388) + range(392,393) + range(405,406) + range(411,412) + range(416,417) + range(420,423, 2) + range(423,426) + range(430,431):
            if wham:
                    stroke(101,210,238)
            fill(165, 165, 165)
            ellipse(410,(nsilv*-55) + x, 75, 50)
            fill(211, 211, 211)
            if introlist[(nsilv + 20)] == 1:
                    fill(255)
            ellipse(410, (nsilv*-55) + x, 47.5, 35)
            stroke(0)
            if difficulty:
                fill(255)
                textSize(25)
                text(" s", 395, -15 + (nsilv*-55) + x, 75, 50)
        
        #BROWN Note    
        for nbrown in range(52,53) + range(68,69) + range(142,143) + range(144,145) + range(146,147) + range(148,149) + range(150,151) + range(155,156) + range(157,158) + range(159,160) + range(161,162) + range(163,164) + range(168,169) + range(170,171) + range(172,173) + range(174,175) + range(176,177) + range(181,182) + range(183,184) + range(185,186) + range(187,188) + range(189,190) + range(210,211) + range(284, 294, 2) + range(297,307,2) + range(310,320,2) + range(323,333,2) + range(386,387) + range(390,391) + range(397,398) + range(403,404) + range(410,411) + range(414,415) + range(431,432):
            if wham:
                    stroke(101,210,238)
            fill(103, 66, 60)
            ellipse(350,(nbrown*-55) + x, 75, 50)
            fill(113, 87, 82)
            if introlist[(nbrown + 20)] == 1:
                    fill(255)
            ellipse(350, (nbrown*-55) + x, 47.5, 35)
            stroke(0)
            if difficulty:
                fill(255)
                textSize(25)
                text(" d", 335, -15 + (nbrown*-55) + x, 75, 50)
        
        #WHITE Note
        for nwhite in range(53,54) + range(61,62) + range(69,70) + range(77,78) + range(141,142) + range(143,144) + range(145,146) + range(147,148) + range(149,150) + range(154,155) + range(156,157) + range(158,159) + range(160,161) + range(162,163) + range(167,168) + range(169,170) + range(171,172) + range(173,174) + range(175,176) + range(180,181) + range(182,183) + range(184,185) + range(186,187) + range(188,189) + range(211,212) + range(219,220)  + range(283, 293, 2) + range(296,306,2) + range(309,319,2) + range(322,332,2) + range(385,386) + range(389,392,2) + range(393,395) + range(396,399, 2) + range(400,403) + range(404,405) + range(409,410) + range(413,418,2) + range(418,419) + range(432,433) + range(440,441):
            if wham:
                    stroke(101,210,238)
            fill(224, 224, 215)
            ellipse(290,(nwhite*-55) + x, 75, 50)
            fill(232, 229, 215)
            if introlist[(nwhite + 20)] == 1:
                    fill(255)
            ellipse(290, (nwhite*-55) + x, 47.5, 35)
            stroke(0)
            if difficulty:
                fill(255)
                textSize(25)
                text(" f", 275, -15 + (nwhite*-55) + x, 75, 50)
        
        #PINK Note       
        for npink in range(80,83) + range(84,85) + range(87,90) + range(94,96) + range(98,99) + range(101,102) + range(103,104) + range(107,110) + range(111,112) + range(114,117) + range(121,123) + range(125,126) + range(128,129) + range(130,131) + range(222,225) + range(226,227) + range(229,232) + range(236,238) + range(240,241)  + range(243,244) + range(245,246) + range(249,252) + range(253,254) + range(256,259) + range(263,265) + range(267,268) + range(270,271) + range(272,273) + range(349,351) + range(353,354) + range(356,359,2) + range(362,365) + range(366,367) + range(369,371) + range(375,376) + range(379,382,2) + range(444,446) + range(448,449) + range(451,454,2) + range(461,462) + range(466,467) + range(468,470) + range(472,473) + range(475,478,2) + range(481,483) + range(485,486) + range(488,491,2) + range(494,496) + range(498,499) + range(501,504,2):
            if wham:
                    stroke(101,210,238)
            fill(255, 206, 250)
            ellipse(230,(npink*-55) + x, 75, 50)
            fill(214, 145, 207)
            if introlist[(npink + 20)] == 1:
                    fill(255)
            ellipse(230, (npink*-55) + x, 47.5, 35)
            stroke(0)
            if difficulty:
                fill(255)
                textSize(25)
                text(" g", 215, -15 + (npink*-55) + x, 75, 50)
        
        #LIGHT BLUE Note
        for nlblue in range(83,84) + range(90,91) + range(96,98) + range(102,103) + range(110,111) + range(117,118) + range(123,125) + range(129,130) + range(225,226) + range(232,233) + range(238,240) + range(244,245) + range(252,253) + range(259,260) + range(265,267) + range(271,272) + range(351,353) + range(357,358) + range(365,366) + range(371,372) + range(376,377) + range(380,381) + range(446,448) + range(452,453) + range(462,463) + range(467,468) + range(470,472) + range(476,477) + range(483,485) + range(489,490) + range(496,498) + range(502,503):
            if wham:
                    stroke(101,210,238)
            fill(96, 232, 213)
            ellipse(170,(nlblue*-55) + x, 75, 50)
            fill(73, 206, 187)
            if introlist[(nlblue + 20)] == 1:
                    fill(255)
            ellipse(170, (nlblue*-55) + x, 47.5, 35)
            stroke(0)
            if difficulty:
                fill(255)
                textSize(25)
                text(" v", 155, -15 + (nlblue*-55) + x, 75, 50)
        
        #ORANGE Note    
        for norange in range(91,92) + range(118,119) + range(233,234) + range(260,261) + range(372,373):
            if wham:
                    stroke(101,210,238)
            fill(245, 170, 89)
            ellipse(110,(norange*-55) + x, 75, 50)
            fill(185, 122, 54)
            if introlist[(norange + 20)] == 1:
                    fill(255)
            ellipse(110, (norange*-55) + x, 47.5, 35)
            stroke(0)
            if difficulty:
                fill(255)
                textSize(25)
                text(" b", 95, -15 + (norange*-55) + x, 75, 50)
            
        fill(0, 255, 0)
        rect(0, 500, 800, 5) #Indicator Line
        
        if not notpaused: #Pause Menu
            image(clrbars, 400.5, 300, logo.width/1.22, logo.height/1.22) 
            fill(0)
            textFont(menufont)
            textAlign(CENTER)
            textSize(65)
            fill(101,210,238)
            text("Paused", 400, 550)
            textSize(55)
            if (mouseX >= 187 and mouseX <= 613) and (mouseY >= 310 and mouseY <= 350):
                fill(47,120,137)
                text("Quit to Main Menu", 398, 348)
                fill(101,210,238)
            text("Quit to Main Menu", 400, 350)
            textAlign(LEFT)
    
            textFont(notefont)
            textSize(14)
            text("Score: %s" %score, 2, 598)
        
        if x >= 28555: #End Screen Activation
            endscreen = True
            muscount = 219
            if score > highest:
                highest = score

        
    elif not notmainmenu: #Main Menu
        textAlign(CENTER)
        background(31,52,108)
        imageMode(CENTER)
        image(logo, 400, 135, logo.width/2, logo.height/2)        
        textFont(menufont)
        if (mouseX >= 308 and mouseX <= 488.5) and (mouseY >= 295 and mouseY <= 390): #Difficulty Highlight
            fill(47,120,137)
            text("Difficulty:", 398, 328)
            text(diff, 398, 378)
        fill(101,210,238)
        text("Difficulty:", 400, 330)
        text(diff, 400, 380)
        textSize(58)
        if (mouseX >= 336 and mouseX <= 460) and (mouseY >= 430 and mouseY <= 475): #Rock! Highlight
            fill(47,120,137)
            text("Rock!", 398, 473)
        fill(101,210,238)
        text("Rock!", 400, 475)
        textSize(20)
        textAlign(RIGHT)
        text("Created By: Ryan Green", 795, 20) 
        textSize(28)
        text("Highest This Session: %s" %highest, 798, 592.5) #High Score
        textAlign(LEFT)
        if (mouseX >= 4 and mouseX <= 70) and (mouseY >= 5 and mouseY <= 25):
            fill(47,120,137)
            text("Retire", 4, 24)
        fill(101,210,238)
        text("Retire", 5, 25)
        if (mouseX >= 5 and mouseX <= 137) and (mouseY >= 575 and mouseY <= 595): #Instructions
            fill(47,120,137)
            text("Instructions!", 4, 594)
            fill(101,210,238)
        text("Instructions!", 5, 595)
        textSize(19)
        if (mouseX >= 415 and mouseX <= 748) and (mouseY >= 180 and mouseY <= 198): #Song (based on)
            fill(47,120,137)
            text('Featuring: "Ghostbusters" By: Ray Parker Jr.', 414, 194)
            fill(101,210,238)
        text('Featuring: "Ghostbusters" By: Ray Parker Jr.', 415, 195)
        
        if (mouseX >= 415 and mouseX <= 748) and (mouseY >= 200 and mouseY <= 218): #Song (inspired by)
            fill(47,120,137)
            text("Inspired by 8 Bit Universe's 8-Bit Remix", 414, 214)
            fill(101,210,238)
        text("Inspired by 8 Bit Universe's 8-Bit Remix", 415, 215)
    
        if muscount <= 218.5: #Original Music Loop
            muscount += 0.641625

        elif muscount > 218.5:
            menumusic.amp(0.35)
            menumusic.play()
            muscount = 0
        else:
            muscount += 0.5
        
        menudown += 2 #Moves Random Notes Down


        if menudown != 880 and menurdm == 0: #Green
            fill(53, 211, 11)   
            ellipse(750, (-55 + menudown), 75, 50)
            fill(41, 134, 16)
            ellipse(750, (-55 + menudown), 47.5, 35)
            
        elif menudown != 880 and menurdm == 1: #Red
            fill(227, 78, 78)
            ellipse(670, (-55 + menudown), 75, 50)
            fill(232, 117, 117)
            ellipse(670, (-55 + menudown), 47.5, 35)
        elif menudown != 880 and menurdm == 2: #Orange
            fill(245, 170, 89)
            ellipse(50,(-55 + menudown), 75, 50)
            fill(185, 122, 54)
            ellipse(50, (-55 + menudown), 47.5, 35)
        elif menudown != 880 and menurdm == 3: #Light Blue
            fill(96, 232, 213)
            ellipse(170,(-55 + menudown), 75, 50)
            fill(73, 206, 187)
            ellipse(170, (-55 + menudown), 47.5, 35)
        else:
            menurdm = int(random(0,4)) #Random Selection
            menudown = 0 #Scroll Reset

    
    elif endscreen: #End Screen
        global endcount
        textAlign(CENTER)
        background(31,52,108)
        imageMode(CENTER)
        endcount += 2
        for n in range(0,2000, 100): #Spinning Guitars
            pushMatrix()
            translate(400,300)
            rotate(radians(5 + endcount + n))
            image(guitar, 0, 200, 88, 165)
            translate(0,200 + n)
            popMatrix()
        fill(101,210,238)
        textFont(menufont)
        textSize(58)
        if quit:
            text("Good Try!", 400, 300) #Displays if Quit to Menu
        else:
            text("You Rock!", 400, 300) #Displays if Finished
        textSize(42)
        text("Score: %s" %score, 400, 350) #Final Score
        textAlign(LEFT)
        textSize(28)
        if (mouseX >= 665 and mouseX <= 796) and (mouseY >= 575 and mouseY <= 597): #Main Menu Highlight
            fill(47,120,137)
            text("Main Menu", 664, 596.25)
            fill(101,210,238)
        text("Main Menu", 665, 597.25)
        if muscount <= 218.5: #Original Music Loop
            muscount += 0.741625

        elif muscount > 218.5:
            menumusic.amp(0.35)
            menumusic.play()
            muscount = 0
        else:
            muscount += 0.5
        
def mousePressed(): 
    global x, score, muscount, introlist, difficulty, diff, notmainmenu, whammycount, whamperc, whammyready, shift, wham, whammul, endscreen, menudown, menurdm, endcount, quit, notpaused #Global Variables

    if ((mouseX >= 308 and mouseX <= 488.5) and (mouseY >= 295 and mouseY <= 390)) and not notmainmenu: #Difficulty Button (Main Menu)
        if difficulty:
            difficulty = False
            diff = " Normal"
            diffsound.amp(0.325)
            diffsound.play()
        else:
            difficulty = True
            diff = "Beginner"
            diffsound.amp(0.45)
            diffsound.play()
    
    if ((mouseX >= 336 and mouseX <= 460) and (mouseY >= 430 and mouseY <= 475)) and not notmainmenu: #Rock! Button (Main Menu)
        notmainmenu = True
        rocksound.amp(0.45)
        rocksound.play()
        
    if ((mouseX >= 5 and mouseX <= 137) and (mouseY >= 575 and mouseY <= 595)) and not notmainmenu: #Instructions Button (Main Menu)
        launch(sketchPath("\data\Fretboard Instructions.txt"))
        diffsound.amp(0.45)
        diffsound.play()
        
    if (mouseX >= 665 and mouseX <= 796) and (mouseY >= 575 and mouseY <= 597) and endscreen: #Back to Main Menu Button (End Screen) - Resets Everything (not high score or music count though)
        diffsound.amp(0.45)
        diffsound.play()
        notpaused = True
        x = -30
        score = 0
        introlist = [0]*535
        difficulty = True #True = Beginner, False = Normal
        diff = "Beginner"
        notmainmenu = False
        whammycount = 0
        whamperc = 0
        whammyready = False
        shift = False
        wham = False
        whammul = 1
        endscreen = False
        menudown = 0
        menurdm = int(random(0,4))
        endcount = 0
        quit = False
        notpaused = True

    if ((mouseX >= 4 and mouseX <= 70) and (mouseY >= 5 and mouseY <= 25)) and not notmainmenu: #Retire Button
        exit()

    if ((mouseX >= 415 and mouseX <= 748) and (mouseY >= 180 and mouseY <= 198)) and not notmainmenu: #Ray Parker Jr. Link
        link("https://www.youtube.com/watch?v=TgNWyBXBC0E")
        
    if ((mouseX >= 415 and mouseX <= 748) and (mouseY >= 200 and mouseY <= 218)) and not notmainmenu: #8 Bit Universe Link
        link("https://www.youtube.com/watch?v=e5lcETwAItA")

    if ((mouseX >= 187 and mouseX <= 613) and (mouseY >= 310 and mouseY <= 350)) and notmainmenu and not endscreen and not notpaused: #Quitter Button
        x = 28556
        quit = True

def keyReleased():
    
    if notmainmenu and not endscreen and notpaused: #Prevents Button on Menu & End Screens
            
        if keyCode == 'SHIFT': #For Arrow Whammy
                shift = False
    
def keyPressed():
    global notpaused, x, score, whammycount, shift, wham, whammul #Global Variables
    if notmainmenu and not endscreen: #Prevents Button on Menu & End Screens
        if key == '`' or key == '~': #Pause Button
            if notpaused: 
                notpaused = False
            else:
                notpaused = True
        if notpaused: #Prevents Buttons when Paused
            if key == CODED:
                #RED Note
                if keyCode == LEFT:
                    for n in range(20):
                        if (x >= (490 + 55*n)) and x <= (540 + 55*n) and (introlist[(n * 2) + 1] == 0):
                            introlist[(n * 2) + 1] = 1
                            if shift and wham != True:
                                whammycount += 1
                            score += 10 * whammul
                            sound1.rate(1.175)
                            sound1.amp(0.45)
                            sound1.play()
                    
                        
                #GREEN Note
                elif keyCode == RIGHT: 
                    if x < 1575:
                        for n in range(20):
                            if (x >= (475 + 55*n)) and x <= (525 + 55*n) and (introlist[int(n * 2)] == 0):
                                introlist[(n * 2)] = 1
                                if shift and wham != True:
                                    whammycount += 1
                                score += 10 * whammul
                                sound2.rate(1.175)
                                sound2.amp(0.45)
                                sound2.play()
                                
                    #GREEN Note (Post-Intro)   
                    else:
                        for n in range(22, 24) + range(29, 31) + range(36,38) + range(43,45) + range(135,138) + range(195,197) + range(202,204) + range(277,280) + range(337,339) + range(344,346) + range(395,396) + range(399,400)  + range(406,409)  + range(419,420) + range(427,428) + range(457,458):
                            #Range + 20 = Position in introlist
                            if (x >= (475 + 55*n)) and x <= (525 + 55*n) and (introlist[int(n + 20)] == 0): #If statement to see if press is correct
                                introlist[(n + 20)] = 1 #If correct, says completed in list
                                if shift and wham != True: #Add 1 Wham-Charge
                                    whammycount += 1
                                score += 10 * whammul #+ 10 Score (+ 20 if WHAM)
                                sound2.rate(1.175) #Sound Rate
                                sound2.amp(0.45) #Sound Volume
                                sound2.play() #Play Sound
                        
                #BLUE Arrow
                elif keyCode == UP:
                    for n in range(20, 22) + range(24,25) + range(27,29) + range(31,32) + range(34,36) + range(38,39) + range(41,43) + range(45,46) + range(193,195) + range(197,198) + range(200,202) + range(204,205)  + range(335,337) + range(339,340) + range(342,344) + range(346,347):
                        if (x >= (475+ 55*n) and x <= (525+ 55*n)) and (introlist[(20 + n)] == 0):
                            introlist[(20 + n)] = 1
                            if shift and wham != True:
                                whammycount += 1
                            score += 10 * whammul
                            sound3.rate(1)
                            sound3.play()
                    
                #YELLOW Arrow           
                elif keyCode == DOWN:
                    for n in range(25,27) + range(32,34) + range(39,41) + range(46,49) + range(55,57) + range(63,65) + range(71,73) + range(85,87) + range(92,94) + range(99,101) + range(104,107) + range(112,114) + range(119,121) + range(126,128) + range(131,135)  + range(138,141) + range(198,200) + range(205,207) + range(213,215) + range(227,229) + range(234,236) + range(241,243) + range(246,249) + range(254,256) + range(261,263) + range(268,270) + range(273,277) + range(280,283) + range(340,342) + range(347,349) + range(354,356) + range(359,362) + range(367,369) + range(373,375) + range(377,379) +range(382,385) + range(434,436) + range(442,444) + range(449,451)  + range(454,457) + range(458,461)  + range(463,466) + range(473,475) + range(478,481) + range(486,488) + range(491,494) + range(499,501) + range(504,508):
                        if (x >= (475 + 55*n) and x <= (525+ 55*n)) and (introlist[(20 + n)] == 0):
                            introlist[(20 + n)] = 1
                            if shift and wham != True:
                                whammycount += 1
                            score += 10 * whammul
                            sound4.amp(0.95)
                            sound4.play()
                  #Arrow Whammy  
                if keyCode == SHIFT:
                    shift = True
                else:
                    shift = False
            #Whammy Activate    
            if key == TAB:
                if whammyready:
                    wham = True
                    lightsound.amp(0.35)
                    lightsound.play()
            
            #FUSHCIA/PURPLE Note
            if key == 'a' or key == 'A':
                for n in range(49,51) + range(54,55) + range(57, 61) + range(62,63) + range(65,67) + range(70,71) + range(73,77) + range(78,80) + range(153,154) + range(166,167) + range(179,180) + range(192,193) + range(207,209) + range(212,213) + range(215,219) + range(220,222) + range(295,296) + range(308,309) + range(321,322)  + range(334,335) + range(388,389) + range(412,413) + range(421,422) + range(426,427) + range(428,430) + range(433,434) + range(436,440) + range(441,442):
                    if (x >= (475+ 55*n) and x <= (525 + 55*n)) and (introlist[(20 + n)] == 0):
                        introlist[(20 + n)] = 1
                        if key == 'A' and wham != True:
                            whammycount += 1
                        score += 10 * whammul
                        sound5.amp(0.95)
                        sound5.play()
               
            #SILVER Note
            if key == 's' or key == 'S': 
                for n in range(51,52) + range(67,68) + range(151,153) + range(164,166) + range(177,179) + range(190,192) + range(209,210) + range(293,295) + range(306,308) + range(319,321) + range(332,334) + range(387,388) + range(392,393) + range(405,406) + range(411,412) + range(416,417) + range(420,423, 2) + range(423,426) + range(430,431):
                    if (x >= (475+ 55*n) and x <= (525+ 55*n)) and (introlist[(20 + n)] == 0):
                        introlist[(20 + n)] = 1
                        if key == 'S' and wham != True:
                            whammycount += 1
                        score += 10 * whammul
                        sound6.amp(0.95)
                        sound6.play()
                
            #BROWN Note
            if key == 'd' or key == 'D':
                for n in range(52,53) + range(68,69) + range(142,143) + range(144,145) + range(146,147) + range(148,149) + range(150,151) + range(155,156) + range(157,158) + range(159,160) + range(161,162) + range(163,164)  + range(168,169) + range(170,171) + range(172,173) + range(174,175) + range(176,177) + range(181,182) + range(183,184) + range(185,186) + range(187,188) + range(189,190) + range(210,211)  + range(284, 294, 2) + range(297,307,2) + range(310,320,2) + range(323,333,2) + range(386,387) + range(390,391) + range(397,398)  + range(403,404) + range(410,411)  + range(414,415) + range(431,432):
                    if (x >= (475+ 55*n) and x <= (525+ 55*n)) and (introlist[(20 + n)] == 0):
                        introlist[(20 + n)] = 1
                        if key == 'D' and wham != True:
                            whammycount += 1
                        score += 10 * whammul
                        sound7.amp(0.95)
                        sound7.play()
                
            #White Note           
            if key == 'f' or key == 'F': 
                for n in range(53,54)  + range(61,62) + range(69,70) + range(77,78) + range(141,142) + range(143,144) + range(145,146) + range(147,148) + range(149,150)  + range(154,155) + range(156,157) + range(158,159) + range(160,161) + range(162,163)  + range(167,168) + range(169,170) + range(171,172) + range(173,174) + range(175,176) + range(180,181) + range(182,183) + range(184,185) + range(186,187) + range(188,189) + range(211,212) + range(219,220) + range(283, 293, 2) + range(296,306,2) + range(309,319,2) + range(322,332,2) + range(385,386) + range(389,392,2) + range(393,395)  + range(396,399, 2) + range(400,403) + range(404,405) + range(409,410) + range(413,418,2) + range(418,419) + range(432,433) + range(440,441):
                    if (x >= (475+ 55*n) and x <= (525+ 55*n)) and (introlist[(20 + n)] == 0):
                        introlist[(20 + n)] = 1
                        if key == 'F' and wham != True:
                            whammycount += 1
                        score += 10 * whammul
                        sound8.amp(0.95)
                        sound8.play()
                
            # PINK Note            
            if key == 'g' or key == 'G': 
                for n in range(80,83) + range(84,85) + range(87,90) + range(94,96) + range(98,99) + range(101,102) + range(103,104) + range(107,110) + range(111,112) + range(114,117) + range(121,123) + range(125,126) + range(128,129) + range(130,131) + range(222,225) + range(226,227) + range(229,232) + range(236,238) + range(240,241) + range(243,244) + range(245,246) + range(249,252) + range(253,254) + range(256,259) + range(263,265) + range(267,268) + range(270,271) + range(272,273)  + range(349,351) + range(353,354)  + range(356,359,2) + range(362,365) + range(366,367)  + range(369,371) + range(375,376)  + range(379,382,2) + range(444,446)  + range(448,449) + range(451,454,2) + range(461,462) + range(466,467) + range(468,470)  + range(472,473)  + range(475,478,2) + range(481,483)  + range(485,486) + range(488,491,2)  + range(494,496) + range(498,499)  + range(501,504,2):
                    if (x >= (475+ 55*n) and x <= (525+ 55*n)) and (introlist[(20 + n)] == 0):
                        introlist[(20 + n)] = 1
                        if key == 'G' and wham != True:
                            whammycount += 1
                        score += 10 * whammul
                        sound9.amp(0.95)
                        sound9.play()
               
            # LIGHT BLUE Note        
            if key == 'v' or key == 'V': 
                for n in range(83,84) + range(90,91) + range(96,98) + range(102,103) + range(110,111) + range(117,118) + range(123,125) + range(129,130) + range(225,226) + range(232,233) + range(238,240) + range(244,245) + range(252,253) + range(259,260) + range(265,267) + range(271,272) + range(351,353) + range(357,358) + range(365,366)  + range(371,372) + range(376,377) + range(380,381) + range(446,448) + range(452,453) + range(462,463) + range(467,468) + range(470,472)  + range(476,477)  + range(483,485) + range(489,490) + range(496,498)  + range(502,503):
                    if (x >= (475+ 55*n) and x <= (525+ 55*n)) and (introlist[(20 + n)] == 0):
                        introlist[(20 + n)] = 1
                        if key == 'V' and wham != True:
                            whammycount += 1
                        score += 10 * whammul
                        sound10.amp(0.95)
                        sound10.play()
               
            # ORANGE Note
            if key == 'b' or key == 'B': 
                for n in range(91,92) + range(118,119) + range(233,234) + range(260,261) + range(372,373):
                    if (x >= (475+ 55*n) and x <= (525+ 55*n)) and (introlist[(20 + n)] == 0):
                        introlist[(20 + n)] = 1
                        if key == 'B' and wham != True:
                            whammycount += 1
                        score += 10 * whammul
                        sound11.amp(0.95)
                        sound11.play()