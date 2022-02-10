import pygame
import esper
import components
import src.engine.physics as phys

class Processors:

#   ------------------------------------------------------------------------------
    #   Movement processor from
    #   https://github.com/benmoran56/esper/blob/master/examples/pygame_example.py
    class MovementProcessor(esper.Processor):
        def __init__(self, minx, maxx, miny, maxy):
            super().__init__()
            self.minx = minx
            self.maxx = maxx
            self.miny = miny
            self.maxy = maxy

        def process(self):
            # This will iterate over every Entity that has BOTH of these components:
            for ent, (vel, rend) in self.world.get_components(components.Velocity, components.Renderable):
                # Update the Renderable Component's position by it's Velocity:
                rend.x += vel.x
                rend.y += vel.y
                # An example of keeping the sprite inside screen boundaries. Basically,
                # adjust the position back inside screen boundaries if it tries to go outside:
                rend.x = max(self.minx, rend.x)
                rend.y = max(self.miny, rend.y)
                rend.x = min(self.maxx - rend.w, rend.x)
                rend.y = min(self.maxy - rend.h, rend.y)

#   ------------------------------------------------------------------------------
    #   Render processor from
    #   https://github.com/benmoran56/esper/blob/master/examples/pygame_example.py
    class RenderProcessor(esper.Processor):
        def __init__(self, window, clear_color=(0, 0, 0)):
            super().__init__()
            self.window = window
            self.clear_color = clear_color

        def process(self):
            # Clear the window:
            self.window.fill(self.clear_color)
            # This will iterate over every Entity that has this Component, and blit it:
            # So it renders every entity that contains renderable
            for ent, rend in self.world.get_component(components.Renderable):
                self.window.blit(rend.image, (rend.x, rend.y))
            # Flip the framebuffers
            pygame.display.flip()

#   ------------------------------------------------------------------------------
    #   My processors
    #   Detects when the player and enemy collide with each other
    class CollisionProcessor(esper.Processor):
        def __init__(self, player, enemy):
            super().__init__()
            self.player = player
            self.enemy = enemy

        def process(self):
            playerPos = self.world.component_for_entity(self.player, components.Components.Renderable)
            enemyPos = self.world.component_for_entity(self.enemy, components.Components.Renderable)

            # Left and right edges of the enemy cube
            # Top and bottom edges of the enemy cube
            enemyLeft = enemyPos.x - (enemyPos.w / 2)
            enemyRight = enemyPos.x + (enemyPos.w / 2)
            enemyBottom = enemyPos.y - (enemyPos.h / 2)
            enemyTop = enemyPos.y + (enemyPos.h / 2)

            # Left and right edges of the player cube
            # Top and bottom edges of the player cube
            playerLeft = playerPos.x - (playerPos.w / 2)
            playerRight = playerPos.x + (playerPos.w / 2)
            playerBottom = playerPos.y - (playerPos.h / 2)
            playerTop = playerPos.y + (playerPos.h / 2)

            if ((playerRight >= enemyLeft) and (enemyRight >= playerLeft)):
                if ((playerBottom <= enemyTop) and (enemyBottom <= playerTop)):
                    print("-- Bonk --")
            else:
                print("No collision yet")

#   ------------------------------------------------------------------------------