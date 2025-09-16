# main_async_debug.py
import asyncio
import pygame
import sys
import traceback

# Set up error handling
print("Starting pygame initialization...")

try:
    pygame.init()
    print("Pygame initialized successfully")
except Exception as e:
    print(f"Pygame init failed: {e}")
    sys.exit(1)

try:
    from src.constants import WINDOW_WIDTH, WINDOW_HEIGHT

    print(f"Constants loaded: {WINDOW_WIDTH}x{WINDOW_HEIGHT}")
except Exception as e:
    print(f"Failed to load constants: {e}")
    WINDOW_WIDTH, WINDOW_HEIGHT = 1450, 800

try:
    from src.globals import g

    print("Globals loaded successfully")
except Exception as e:
    print(f"Failed to load globals: {e}")
    sys.exit(1)

try:
    g.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.Surface.convert_alpha(g.window)
    pygame.display.set_caption("Auto Arena")
    print("Display setup successful")
except Exception as e:
    print(f"Display setup failed: {e}")
    sys.exit(1)

FPS = 60
clock = pygame.time.Clock()

try:
    from src.game import Game

    print("Game class imported successfully")
except Exception as e:
    print(f"Failed to import Game class: {e}")
    traceback.print_exc()
    sys.exit(1)


# async main loop for pygbag
async def main():
    print("Starting main game loop...")

    try:
        game = Game()
        print("Game instance created successfully")
    except Exception as e:
        print(f"Failed to create Game instance: {e}")
        traceback.print_exc()
        # Create a fallback simple game loop
        print("Creating fallback game loop...")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Simple red background with text
            g.window.fill((255, 0, 0))
            font = pygame.font.Font(None, 74)
            text = font.render("GAME LOAD ERROR", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            g.window.blit(text, text_rect)

            pygame.display.flip()
            await asyncio.sleep(0)
            clock.tick(FPS)

        pygame.quit()
        return

    running = True
    frame_count = 0

    while running:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            game.update()
            pygame.display.flip()

            # yield to wasm handler - this is crucial for pygbag
            await asyncio.sleep(0)

            clock.tick(FPS)

            frame_count += 1
            if frame_count % 60 == 0:  # Every second
                print(f"Game running, frame {frame_count}")

        except Exception as e:
            print(f"Error in game loop: {e}")
            traceback.print_exc()
            # Show error on screen
            g.window.fill((255, 0, 0))
            font = pygame.font.Font(None, 48)
            text = font.render("RUNTIME ERROR", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            g.window.blit(text, text_rect)

            error_text = font.render(str(e)[:50], True, (255, 255, 255))
            error_rect = error_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60))
            g.window.blit(error_text, error_rect)

            pygame.display.flip()
            await asyncio.sleep(0)

    pygame.quit()
    print("Game ended successfully")


if __name__ == "__main__":
    print("Running async main...")
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Fatal error: {e}")
        traceback.print_exc()
