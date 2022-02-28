#Authored by Drake Farmer

#Set up secondary game loop
                        #Do once:
                            #Get minigames, save to array
                            #Draw background rectangle
                            #initial draw of first 3 minigames on rectangle
                            #Create array of len 2 to hold 3 minigames on "wheel"
                        #For loop
                            #grow array[0] slightly and move down
                            #move array[1] down slightly
                            #shrink array[0] slightly
                            #if array[2] size is small enough...
                                #move array[1] to array[2]
                                #move array[0] to array[1]
                                #Create a new text display with next minigame on it, set height to start height and put in array[0]
                        #Not in for loop
                            #Once we exit for loop...
                            #Select minigame in array[1]
                            #result = minigame folder -> minigame -> gameMain.py.launch()
                            #print("Minigame ended")
                            #isDuel = result[4]
                            #if(!isDuel):
                                #print("Standard - rewarding players")
                                #player1.addmoney(result[0])
                                #player2.addmoney(result[1])
                                #player3.addmoney(result[2])
                                #player4.addmoney(result[3])
                            #else:
                                #print("Duel - rewarding victor")
                                #figure out duel logic here
                        #print("Minigame state completed")
                        #quit minigame