import os
import pygame
import time
import random
import time
import psutil
from pygame.locals import *

class in_game():
    class Pause_Menu():
        def __init__():
            pass

    class Player():      
        def __init__(self, game, map) -> None:
            
            if map == "Nova":
                from classes import Ship
                Ship.__init__(self, game)

            self.direction = None
            self.invul_time = 3
            self.hitbox = [self.rect.topleft,self.rect.bottomleft,self.rect.bottomright,self.rect.topright]

        def run(self, game, screen, events) -> None:
            pressed_keys = pygame.key.get_pressed()
            
            self.frame = 'ship_thrust_off'
            self.frameSpeed = 'slow' # default ship speed
            shipSpeed = self.speed # ship movement in pixels per tick
            fuelUsage = self.fuelUsage # fuel used per tick
            self.direction = None # movement direction
            
            if pressed_keys[K_LSHIFT]:
                self.frameSpeed = 'fast'
                shipSpeed = self.speed+self.boostSpeed
                fuelUsage = self.fuelUsage * 5

            if pressed_keys[K_d]:
                    self.direction = "forward"
                    self.frame = f'ship_thrust_{self.frameSpeed}_forward'
                    game.ingame.distanceTravelled += shipSpeed/10
                    self.fuel -= fuelUsage

            if pressed_keys[K_w]:
                    self.direction = None
                    self.rect.move_ip(0, -shipSpeed)
                    self.frame = f'ship_thrust_{self.frameSpeed}_right'
                    self.fuel -= fuelUsage

            if pressed_keys[K_s]:
                    self.direction = None
                    self.rect.move_ip(0, shipSpeed)
                    self.frame = f'ship_thrust_{self.frameSpeed}_left'
                    self.fuel -= fuelUsage

            self.hitbox = [self.rect.topleft,self.rect.bottomleft,self.rect.bottomright,self.rect.topright]
            self.fuel -= self.fuelUsage/10
            game.ingame.distanceTravelled += shipSpeed/100

            

            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > screen.get_size()[0]:
                self.rect.right = screen.get_size()[0]
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= screen.get_size()[1]:
                self.rect.bottom = screen.get_size()[1]

    class Enemy(): # for now only asteroid variants are included


        def __init__(self, game, size, y_position) -> None:
            self.player_hit = False
            self.time_of_hp_loss = time.time() # by setting it to time.time here we are effectively giving the player spawn protection
            if size == "small_ast":
                from classes import Small_Asteroid
                Small_Asteroid.__init__(self, y_position, game)
            elif size == "medium_ast":
                from classes import Medium_Asteroid
                Medium_Asteroid.__init__(self, y_position, game)
            elif size == "large_ast":
                from classes import Large_Asteroid
                Large_Asteroid.__init__(self, y_position, game)

            self.hitbox = [self.rect.topleft,self.rect.bottomleft,self.rect.bottomright,self.rect.topright]
        
        def run(self, player):
            for i in range(5):
                self.rect.move_ip(int((-self.speed/10)),random.randint(-1,1))
                
                # if the time of comparison is 3 seconds in the future from the time of hp loss than the statement passes as true and means the player shall no longer be invulnerable
                # since the player is not in collision with an enemy rect for more than 3 seconds, it is impossible to be hit twice by the same. By introducing the time module into this
                # I give myself the ability to change this in the future if I want to
                if time.time() >= self.time_of_hp_loss+player.invul_time:  
                    
                    if player.rect.colliderect(self.rect):
                        
                        
                        
                        
                        player.health -= self.damage
                        self.time_of_hp_loss = time.time()
            self.hitbox = [self.rect.topleft,self.rect.bottomleft,self.rect.bottomright,self.rect.topright]

    def __init__(self,game, selectedMap: str) -> None:
        self.player = self.Player(game,selectedMap)
        self.screen = game.screen
        self.render_stack = {}
        self.distanceTravelled = 0
        self.fuelUsed = round(self.player.fuel,2)
        self.selectedMap = selectedMap
        self.game = game
        self.running = True
        self.showVars = False
        self.paused = False
        self.game_over = False
        self.game_win = False
        self.t1 = 0
        self.t2 = 0
        self.tt = 0
        self.fpsAVGlist = []
        self.cpuAVGlist = []
        self.fpsAVG = 0
        self.cpuAVG = 0
        self.spawn_size = 0
        self.show_rect_outlines= False
        self.slow_tps = False
        

        self.background=pygame.image.load(f"Game/assets/visual/IngameBackgrounds/Pixelated/Nova_+GLACIO.png")
        self.background.set_alpha(100)
        self.bg_scroll = 0
        
        self.gameoverText = game.largeFont.render("Game Over", True, (255,255,255))
        self.gameoverText_rect = self.gameoverText.get_rect(center=(960,540))

        self.win_text = game.largeFont.render("You Win", True, (255,255,255))
        self.win_text_rect = self.win_text.get_rect(center=(960,540))

        if selectedMap == "nova":
            self.enemy_cap = 10

        self.alive_enemies = []

    def update(self):
        while self.running: # additionally to having a surplus of subclasses in_game() runs its own game loop that allows for better
                            # performance when playing in game, this is because the game does not have to run through additional
                            # irelavent objects and if statements before it reasches the ingame.run() statement
            self.t1 = time.time_ns()
            events = pygame.event.get()
            for event in events: # event handler for in game controls
                if event.type== QUIT:
                    self.running=False
                    exit()

                if event.type == KEYDOWN:

                    if event.key == K_1:
                        if self.showVars:
                            self.showVars = False
                        else: self.showVars = True

                    if event.key == K_ESCAPE or event.key == K_p or event.key== K_2:
                        if self.paused:
                            self.paused = False
                        else: self.paused = True

                    if event.key == K_3:
                        if self.show_rect_outlines:
                            self.show_rect_outlines = False
                        else: self.show_rect_outlines = True

                    if event.key == K_4:
                        if self.slow_tps:
                            self.slow_tps = False
                        else: self.slow_tps = True

                    if event.key == K_7:
                        self.running = False
                        self.game.running = True

                    if event.key == K_8:
                        breakpoint()

                    if event.key == K_9:
                        self.running = False
                        exit()

                
            self.screen.fill((0,0,0)) # refresh the screen
            self.render_stack[self.background] = (self.bg_scroll,0)

            if not self.paused and not self.game_over and not self.game_win: # game updates running while game unpaused






                if self.player.fuel > 0 and self.bg_scroll >= -2416:
                    if self.player.direction == None:
                        self.bg_scroll-=0.25
                    elif self.player.direction == "forward" and self.player.frameSpeed == "fast": # test for boost first as it will never get tested for if player is already moving forward
                        self.bg_scroll -= 1
                    elif self.player.direction == "forward" :
                        self.bg_scroll -= 0.5     
            
                self.player.run(self.game,self.screen,events)




                
                for i in range(1,2): # spawn chance, the higher the number in the for loop the lower the tps but the more likely a spawn occurs
                    if i == random.randint(1,50): # thus we raise this number to decrease spawn rate
                        if len(self.alive_enemies) < 10:
                            self.spawn_size = random.randint(1,10)
                            y_spawn = random.randint(0,self.game.screen.get_size()[1])
                            if self.spawn_size >= 1 and self.spawn_size <= 6:
                                self.alive_enemies.append(self.Enemy(self.game, "small_ast", y_spawn))
                            elif self.spawn_size >=7 and self.spawn_size <= 9:
                                self.alive_enemies.append(self.Enemy(self.game, "medium_ast", y_spawn))
                            elif self.spawn_size == 10:
                                self.alive_enemies.append(self.Enemy(self.game, "large_ast", y_spawn))

                for i in self.alive_enemies:

                    i.run(self.player)
                    if i.rect.right<0:
                        self.alive_enemies.remove(i)





                self.distanceTravelled=round(self.distanceTravelled,1)
                self.fuelUsed = round(self.player.fuel,2)



                

                dTSurf = self.game.mediumFont.render(f"Distance: {self.distanceTravelled} Km", False, (255,255,255))
                dTSurf_rect = dTSurf.get_rect()
                dTSurf_rect.topright = (1900,20)

                fuelSurf = self.game.mediumFont.render(f"Fuel: {self.fuelUsed} %", False, (255,255,255))
                fuelSurf_rect = fuelSurf.get_rect()
                fuelSurf_rect.topleft = (20,80)

                player_hp = self.game.mediumFont.render(f"Health: {self.player.health}", False, (255,255,255))
                player_hp_rect = player_hp.get_rect()
                player_hp_rect.topleft = (20,20)






            self.render_stack[self.player.images[f'{self.player.frame}']] = self.player.rect

            for i in self.alive_enemies:      
                self.render_stack[i.surf] = i.rect

            self.render_stack[dTSurf] = dTSurf_rect
            self.render_stack[player_hp] = player_hp_rect
            self.render_stack[fuelSurf] = fuelSurf_rect




            
            if self.player.fuel <= 0 and self.game_win == False:                                # game bounds
                    self.render_stack[self.gameoverText] = self.gameoverText_rect
                    self.game_over = True

            if self.player.health <= 0 and self.game_win == False:
                    self.render_stack[self.gameoverText] = self.gameoverText_rect
                    self.game_over = True

            elif self.bg_scroll <= -2416:
                self.game_win = True
                self.render_stack[self.win_text] = self.win_text_rect






            
            if self.showVars: # So I can view variables in runtime rather than relying on pdb breakpoints
                developer_overlay = [[],[],[]] # list stores text renders in different categories
                self.cpu = psutil.cpu_percent()

                if len(self.fpsAVGlist) < 61: # average fps calculations and logic. Has a sample size of 60, this means an ideal sample would take exactly one second
                    self.fpsAVGlist.append(round(1/(self.tt/1000)))
                else: 
                    for i in self.fpsAVGlist:
                        self.fpsAVG += i
                    self.fpsAVG /= len(self.fpsAVGlist)
                    self.fpsAVG =round(self.fpsAVG)
                    self.fpsAVGlist = []
                if len(self.cpuAVGlist) < 31: # average cpu calculations and logic. Has a sample size of 60, this means an ideal sample would take exactly one second
                    self.cpuAVGlist.append(round(self.cpu))
                else: 
                    for i in self.cpuAVGlist:
                        self.cpuAVG += i
                    self.cpuAVG /= len(self.cpuAVGlist)
                    self.cpuAVG =round(self.cpuAVG)
                    self.cpuAVGlist = []






                y=1060
                x=0
                variables = [ # variables that are displayed when F1 is pressed
                        {
                            "running":f"{self.running} (should not say False!)",
                            "paused":self.paused,
                            "show_variables":self.showVars,
                            "show_hitboxes":self.show_rect_outlines,
                            "slow_tps":self.slow_tps,
                            "game_over":self.game_over,
                            "game_win":self.game_win,
                            "Flags":""
                        },
                        {
                            "selected_map":self.selectedMap,
                            "player_pos":self.player.rect.center,
                            "background_scroll":self.bg_scroll,
                            "fuel_used":self.fuelUsed,
                            "distance_travelled":self.distanceTravelled,
                            "enemies_alive":len(self.alive_enemies),
                            "spawn_size":self.spawn_size,
                            "tick_speed_ms":self.tt,
                            "ticks_per_second": round(1/(self.tt/1000)),
                            "Avg_ticks_per_second":self.fpsAVG,
                            "CPU":self.cpu,
                            "Average_CPU": self.cpuAVG,
                            "Memory":round(psutil.Process().memory_info().vms)/1000000,
                            "Variables":""
                        },
                        {
                            
                            "screen": self.screen.__repr__(),
                            "player": self.player.__repr__(),
                            "background": self.background.__repr__(),
                            "fuelSurf": fuelSurf.__repr__(),
                            "dTSurf":dTSurf.__repr__(),
                            "enemies_alive":self.alive_enemies,
                            "Objects":""
                        }
                ]

                # some very BASIC dictionary algebra or smth (took me like 20 minutes to do)
                # iterates through the varaibles dictionary defined above, and blits rendered texts

                for n,i in enumerate(variables): # i is the nested dictionary, n is the number of iterations through the base dictionary

                    for i_ in i: # i_ are the key | value pairs inside the dictionaries. NOTE: it is important to get the value from the i_ key 

                        if type(i.get(i_)) != type(list()): # looks for any lists
                            developer_overlay[n].append(self.game.smallFont.render(f"{i_}: {i.get(i_)}",False,(255,255,255)))
                        else:
                            for n2,i__ in enumerate(i.get(i_)): # i__ is the values inside the list inside the nested dictionaries, n2 is the number of iterations inside said list
                                developer_overlay[n].append(self.game.smallFont.render(f"{n2}: {i__.__repr__()}",False,(255,255,255)))

                            developer_overlay[n].append(self.game.smallFont.render(f"{i_}: ",False,(255,255,255)))

                for a in developer_overlay:
                    for a_ in a:
                        self.render_stack[a_] = (x,y)
                        y-=20
                    x+= 500                 
                    y=1060




            if self.slow_tps:
                global FPS
                FPS = 2
            else:
                FPS = 60


            
            for i in self.render_stack:
                self.game.screen.blit(i,self.render_stack.get(i))
            if self.show_rect_outlines:
                pygame.draw.lines(surface=self.screen,color=(255,255,255),closed=True,points=self.player.hitbox)
                for i in self.alive_enemies:
                    pygame.draw.lines(surface=self.screen,color=(255,255,255),closed=True,points=i.hitbox)
            self.render_stack= {}





            pygame.display.flip()

            self.game.clock.tick(FPS)
            self.t2 = time.time_ns()
            self.tt = (self.t2-self.t1)/1000000

    def detectcollisions(self):
        for i in self.alive_enemies:
            if self.player.rect.colliderect(i.rect):
                self.collision