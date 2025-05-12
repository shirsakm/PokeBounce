import pygame
from src.constants import WINDOW_HEIGHT, WINDOW_WIDTH, battler_sprites, move_sprites


class Sprites:
    base_dir = "assets/img"
    battler_dir = f"{base_dir}/battlers"
    move_dir = f"{base_dir}/moves"

    def __init__(self):
        # Caches for different parameters
        self._battler_cache: dict[tuple, pygame.Surface] = {}
        self._move_cache: dict[tuple, pygame.Surface] = {}
        # Legacy dicts for direct access (factor=1, no offset)
        self.battlers: dict[str, pygame.Surface] = {}
        self.moves: dict[str, pygame.Surface] = {}
        self.arena = None

        # Preload assets
        print(f"Loading images from '{self.base_dir}/*'...")
        print("Arena...")
        self.get_arena()
        print("Battlers...")
        for bid in battler_sprites:
            # default factor=1, offsets=0 -> populates both cache and self.battlers
            self.get_battler(bid)
        print("Moves...")
        for mid in move_sprites:
            # default factor=1, offsets=0 -> populates both cache and self.moves
            self.get_move(mid)

    def get_arena(self) -> pygame.Surface:
        if self.arena is None:
            self.arena = self._load_img(
                f"{Sprites.base_dir}/arena.png",
                WINDOW_WIDTH, WINDOW_HEIGHT
            )
        return self.arena

    def get_battler(
        self,
        battler_id: str,
        factor: float = 1.0,
        offset_x: int = 0,
        offset_y: int = 0
    ) -> pygame.Surface:
        key = (battler_id, factor, offset_x, offset_y)
        if key not in self._battler_cache:
            surf = self._load_img(
                f"{self.battler_dir}/{battler_id}.png",
                204, 168,
                factor, offset_x, offset_y
            )
            self._battler_cache[key] = surf

            # legacy dict for no-transform calls
            if factor == 1.0 and offset_x == 0 and offset_y == 0:
                self.battlers[battler_id] = surf
        return self._battler_cache[key]

    def get_move(
        self,
        move_id: str,
        factor: float = 1.0,
        offset_x: int = 0,
        offset_y: int = 0
    ) -> pygame.Surface:
        key = (move_id, factor, offset_x, offset_y)
        if key not in self._move_cache:
            # determine base icon size
            scale = 100 if move_id != "poison" else 10
            surf = self._load_img(
                f"{self.move_dir}/{move_id}.png",
                scale, scale,
                factor, offset_x, offset_y
            )
            self._move_cache[key] = surf
            # legacy direct mapping
            if factor == 1.0 and offset_x == 0 and offset_y == 0:
                self.moves[move_id] = surf
        return self._move_cache[key]

    def _load_img(
        self,
        file_path: str,
        x_scale: int | None,
        y_scale: int | None,
        factor: float = 1.0,
        offset_x: int = 0,
        offset_y: int = 0
    ) -> pygame.Surface:
        # load source
        src = pygame.image.load(file_path).convert_alpha()
        orig_w, orig_h = src.get_size()

        # canvas dims
        tgt_w = x_scale or orig_w
        tgt_h = y_scale or orig_h

        # crop to content
        bbox = src.get_bounding_rect()
        if bbox.width == 0 or bbox.height == 0:
            return pygame.Surface((tgt_w, tgt_h), pygame.SRCALPHA)
        content = src.subsurface(bbox).copy()

        # compute scales
        sx = tgt_w / orig_w
        sy = tgt_h / orig_h
        csx = sx * factor
        csy = sy * factor

        # scale content
        scaled_w = max(1, int(bbox.width * csx))
        scaled_h = max(1, int(bbox.height * csy))
        content = pygame.transform.scale(content, (scaled_w, scaled_h))

        # blit into canvas
        canvas = pygame.Surface((tgt_w, tgt_h), pygame.SRCALPHA)
        # original region in canvas
        reg_w = int(bbox.width * sx)
        reg_h = int(bbox.height * sy)
        reg_x = int(bbox.x * sx)
        reg_y = int(bbox.y * sy)
        # center and apply offsets
        pos_x = reg_x + (reg_w - scaled_w) // 2 + offset_x
        pos_y = reg_y + (reg_h - scaled_h) // 2 + offset_y
        canvas.blit(content, (pos_x, pos_y))

        return canvas


INSTANCE = Sprites()
