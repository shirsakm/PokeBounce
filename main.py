"""Synchronous launcher.

For desktop we keep the original immediate loop for simplicity, but for
pygbag (web) we delegate to the async main defined in main_async.py so the
event loop can yield to the browser.
"""

import os
import sys
import pygame

from src.constants import WINDOW_HEIGHT, WINDOW_WIDTH
from src.globals import g

RUN_ASYNC = os.environ.get("PYGBAG") == "1" or "emscripten" in sys.modules

if RUN_ASYNC:
    # Defer everything to async implementation
    from main_async import main as async_main  # type: ignore
    import asyncio

    asyncio.run(async_main())
else:
    pygame.init()
    FPS = 60
    fpsClock = pygame.time.Clock()
    g.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.Surface.convert_alpha(g.window)
    pygame.display.set_caption("Auto Arena")

    from src.game import Game

    game = Game()
    last_ticks = pygame.time.get_ticks()
    while True:
        now = pygame.time.get_ticks()
        dt_ms = now - last_ticks
        last_ticks = now
        dt = dt_ms / 1000.0
        game.update(dt)
        pygame.display.flip()
        fpsClock.tick(FPS)
