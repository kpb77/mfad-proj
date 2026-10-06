import pygame
import numpy as np
import sys
from math_engine import mk_cube, axes, rx, ry, rz, project
from ui_engine import Button

def main():
    pygame.init()
    pygame.font.init()
    
    screen_width = 980
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED)
    pygame.display.set_caption("window")
    clock = pygame.time.Clock()
    
    font = pygame.font.SysFont("arial", 16, bold=True)
    
    rotation_matrix = np.eye(3)
    cube_vertices, cube_edges = mk_cube()
    
    def rotate_cube(axis):
        nonlocal rotation_matrix
        angle = np.radians(15)
        rotation_functions = {'x': rx, 'y': ry, 'z': rz}
        rotation_matrix = rotation_functions[axis](angle) @ rotation_matrix

    def reset_cube():
        nonlocal rotation_matrix
        rotation_matrix = np.eye(3)

    padding = 20
    panel_y = padding
    panel_height = screen_height - (padding * 2)
    
    viewport_x = padding
    viewport_width = int(screen_width * 0.62)
    center_x = viewport_x + (viewport_width // 2)
    center_y = panel_y + (panel_height // 2)
    
    control_x = viewport_x + viewport_width + padding
    control_width = screen_width - control_x - padding
    control_center_x = control_x + (control_width // 2)
    
    button_width = 280
    button_height = 40
    button_x = control_center_x - (button_width // 2)
    button_start_y = 100
    button_gap = 10
    
    labels = ["Rotate +X (+15°)", "Rotate +Y (+15°)", "Rotate +Z (+15°)", "Reset"]
    actions = [lambda: rotate_cube('x'), lambda: rotate_cube('y'), lambda: rotate_cube('z'), reset_cube]
    
    buttons = []
    for i in range(len(labels)):
        y_position = button_start_y + i * (button_height + button_gap)
        buttons.append(Button((button_x, y_position, button_width, button_height), labels[i], actions[i]))
    
    is_running = True
    while is_running:
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                is_running = False
            for button in buttons:
                button.handle_event(event)
                
        projected_vertices = project(rotation_matrix @ cube_vertices, (center_x, center_y))
        projected_axes = project(rotation_matrix @ axes, (center_x, center_y))
        
        pygame.draw.rect(screen, (0, 0, 0), (viewport_x, panel_y, viewport_width, panel_height), border_radius=10)
        pygame.draw.rect(screen, (200, 200, 200), (viewport_x, panel_y, viewport_width, panel_height), width=2, border_radius=10)
        
        axis_origin = projected_axes[0]
        axis_colors = [(255, 71, 87), (46, 213, 115), (30, 144, 255)]
        axis_names = ["X", "Y", "Z"]
        for i in range(3):
            axis_end = projected_axes[i + 1]
            pygame.draw.line(screen, axis_colors[i], axis_origin, axis_end, 3)
            screen.blit(font.render(axis_names[i], True, axis_colors[i]), (axis_end[0] + 5, axis_end[1] - 5))
            
        for edge in cube_edges:
            pygame.draw.line(screen, (0, 206, 201), projected_vertices[edge[0]], projected_vertices[edge[1]], 2)
            
        pygame.draw.rect(screen, (0, 0, 0), (control_x, panel_y, control_width, panel_height), border_radius=10)
        pygame.draw.rect(screen, (200, 200, 200), (control_x, panel_y, control_width, panel_height), width=2, border_radius=10)
        
        title_text = font.render("Transformation Controls", True, (255, 255, 255))
        screen.blit(title_text, title_text.get_rect(centerx=control_center_x, top=35))
        
        for button in buttons:
            button.draw(screen, font)
            
        matrix_display_y = 415
        matrix_header = font.render("Active Rotation Matrix (R):", True, (255, 255, 255))
        screen.blit(matrix_header, matrix_header.get_rect(centerx=control_center_x, top=matrix_display_y))
        
        row_spacing = 30
        for i in range(3):
            value_1 = round(rotation_matrix[i, 0], 3)
            value_2 = round(rotation_matrix[i, 1], 3)
            value_3 = round(rotation_matrix[i, 2], 3)
            row_text = f"{value_1}    {value_2}    {value_3}"
            
            matrix_row_label = font.render(row_text, True, (255, 255, 255))
            screen.blit(matrix_row_label, matrix_row_label.get_rect(centerx=control_center_x, top=matrix_display_y + 40 + (i * row_spacing)))
            
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
    sys.exit()

main()
