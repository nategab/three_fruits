from adafruit_circuitplayground.express import cpx

# A1 blue
# A7 red
# A4 yellow

while True:
    #white (A1 and A7 and A4) fruit
    if cpx.touch_A1 and cpx.touch_A7 and cpx.touch_A4:
        cpx.pixels[0] = ((3, 3, 3))
        cpx.pixels[1] = ((3, 3, 3))
        cpx.pixels[2] = ((3, 3, 3))
        cpx.pixels[3] = ((3, 3, 3))
        cpx.pixels[4] = ((3, 3, 3))
        cpx.pixels[5] = ((3, 3, 3))
        cpx.pixels[6] = ((3, 3, 3))
        cpx.pixels[7] = ((3, 3, 3))
        cpx.pixels[8] = ((3, 3, 3))
        cpx.pixels[9] = ((3, 3, 3))
        cpx.play_file("tada.wav")
        cpx.play_file("fruit_clue.wav")
        time.sleep(0.01)
        
    #purple (A1 and A7) fruit
    elif cpx.touch_A1 and cpx.touch_A7:
        cpx.pixels[0] = ((3, 0, 3))
        cpx.pixels[1] = ((3, 0, 3))
        cpx.pixels[2] = ((3, 0, 3))
        cpx.pixels[7] = ((3, 0, 3))
        cpx.pixels[8] = ((3, 0, 3))
        cpx.pixels[9] = ((3, 0, 3))
        time.sleep(0.01)
        
    #orange (A7 and A4) fruit
    elif cpx.touch_A7 and cpx.touch_A4:
        cpx.pixels[0] = ((3, 0, 3))
        cpx.pixels[1] = ((3, 0, 3))
        cpx.pixels[2] = ((3, 0, 3))
        cpx.pixels[3] = ((3, 0, 3))
        cpx.pixels[4] = ((3, 0, 3))
        cpx.pixels[5] = ((3, 0, 3))
        cpx.pixels[6] = ((3, 0, 3))
        time.sleep(0.01)
        
    #green (A1 and A4) fruit
    elif cpx.touch_A1 and cpx.touch_A4:
        cpx.pixels[3] = ((0, 3, 0))
        cpx.pixels[4] = ((0, 3, 0))
        cpx.pixels[5] = ((0, 3, 0))
        cpx.pixels[6] = ((0, 3, 0))
        cpx.pixels[7] = ((0, 3, 0))
        cpx.pixels[8] = ((0, 3, 0))
        cpx.pixels[9] = ((0, 3, 0))
        time.sleep(0.01)
        
    #blue (A1) fruit
    elif cpx.touch_A1:        
        cpx.pixels[7] = ((0, 0, 3))
        cpx.pixels[8] = ((0, 0, 3))
        cpx.pixels[9] = ((0, 0, 3))
        time.sleep(0.01)
        
    #red (A7) fruit
    elif cpx.touch_A7:        
        cpx.pixels[0] = ((3, 0, 0))
        cpx.pixels[1] = ((3, 0, 0))
        cpx.pixels[2] = ((3, 0, 0))
        time.sleep(0.01)
        
    #yellow (A4) fruit
    elif cpx.touch_A4:        
        cpx.pixels[3] = ((3, 3, 0))
        cpx.pixels[4] = ((3, 3, 0))
        cpx.pixels[5] = ((3, 3, 0))
        cpx.pixels[6] = ((3, 3, 0))
        time.sleep(0.01)
    
    else:
        cpx.pixels[0] = ((0, 0, 0))
        cpx.pixels[1] = ((0, 0, 0))
        cpx.pixels[2] = ((0, 0, 0))
        cpx.pixels[3] = ((0, 0, 0))
        cpx.pixels[4] = ((0, 0, 0))
        cpx.pixels[5] = ((0, 0, 0))
        cpx.pixels[6] = ((0, 0, 0))
        cpx.pixels[7] = ((0, 0, 0))
        cpx.pixels[8] = ((0, 0, 0))
        cpx.pixels[9] = ((0, 0, 0))
        time.sleep(0.01)
    
    time.sleep(0.01)