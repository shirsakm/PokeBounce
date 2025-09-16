# main_async.py
import asyncio
import pygame
from src.constants import WINDOW_WIDTH, WINDOW_HEIGHT
from src.globals import g
from src.game import Game

pygame.init()
g.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.Surface.convert_alpha(g.window)
pygame.display.set_caption("Auto Arena")
FPS = 60
clock = pygame.time.Clock()


# async main loop for pygbag
async def main():
    game = Game()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.update()
        pygame.display.flip()

        # yield to wasm handler - this is crucial for pygbag
        await asyncio.sleep(0)

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())
