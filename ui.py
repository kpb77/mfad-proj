import pygame

class Button:
    def __init__(self, rect, text, cb, col=(0, 0, 0), hov=(30, 30, 30)):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.cb = cb
        self.col = col
        self.hov = hov

    def draw(self, surf, font):
        bg = self.hov if self.rect.collidepoint(pygame.mouse.get_pos()) else self.col
        pygame.draw.rect(surf, bg, self.rect, border_radius=8)
        pygame.draw.rect(surf, (200, 200, 200), self.rect, width=2, border_radius=8)
        t = font.render(self.text, True, (255, 255, 255))
        surf.blit(t, t.get_rect(center=self.rect.center))

    def handle_event(self, ev):
        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1 and self.rect.collidepoint(ev.pos):
            self.cb()
