# main_minimal.py - Minimal version avoiding problematic imports
import asyncio
import pygame

pygame.init()

# Simple constants
WINDOW_WIDTH = 1450
WINDOW_HEIGHT = 800
FPS = 60

# Create window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Auto Arena - Minimal")
clock = pygame.time.Clock()

# Simple game state
game_time = 0
color_cycle = 0


async def main():
    global game_time, color_cycle
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Cycle through colors to show it's working
        game_time += 1
        if game_time % 120 == 0:  # Every 2 seconds
            color_cycle = (color_cycle + 1) % 3

        if color_cycle == 0:
            bg_color = (50, 50, 150)  # Dark blue
        elif color_cycle == 1:
            bg_color = (50, 150, 50)  # Dark green
        else:
            bg_color = (150, 50, 50)  # Dark red

        window.fill(bg_color)

        # Draw some basic shapes to show rendering works
        pygame.draw.circle(window, (255, 255, 255), (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 50)
        pygame.draw.rect(window, (255, 255, 0), (100, 100, 200, 100))

        # Basic text without custom fonts
        font = pygame.font.Font(None, 74)
        text = font.render("POKEBOUNCE LOADING...", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 150))
        window.blit(text, text_rect)

        # Show frame counter
        font_small = pygame.font.Font(None, 36)
        frame_text = font_small.render(f"Frame: {game_time}", True, (255, 255, 255))
        window.blit(frame_text, (50, 50))

        pygame.display.flip()

        # Yield to wasm handler
        await asyncio.sleep(0)

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())
