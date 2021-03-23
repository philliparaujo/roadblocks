from pygame import Surface


class UiError(Surface):
    def __init__(self, message):
        Surface.__init__(self, (600, 200))
        self.display_count = 0
        self.fill((255, 255, 255))
        self.message = message

    def draw(self, screen):
        if self.display_count > 1000:
            return False

        (screen_width, screen_height) = screen.get_size()

        self.display_count = self.display_count + 1
        screen.blit(self,
                    ((screen_width - self.get_width()) / 2,
                     (screen_height - self.get_height()) / 2))
        return True
