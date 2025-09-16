# debug_async.py - Simple test to see if pygame works with pygbag
import asyncio
import pygame

pygame.init()

# Simple constants for testing
WINDOW_WIDTH = 1450
WINDOW_HEIGHT = 800
FPS = 60

# Create window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Debug Test")
clock = pygame.time.Clock()


async def main():
    running = True
    color = (255, 0, 0)  # Red

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill screen with red to test if rendering works
        window.fill(color)

        # Draw a simple white rectangle
        pygame.draw.rect(window, (255, 255, 255), (100, 100, 200, 100))

        # Draw some text (without external fonts)
        font = pygame.font.Font(None, 36)
        text = font.render("PYGAME WORKS!", True, (0, 0, 0))
        window.blit(text, (150, 130))

        pygame.display.flip()

        # Yield to wasm handler
        await asyncio.sleep(0)

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())
