for j in range(0,12,1):
    for i in range(0,12,1):
        time=str(9+j)+":"+str(5*i).zfill(2)
        angle=((90-j*30)+i*30)-i*2.5
        print(time+" - "+str(angle%360))
    print()
