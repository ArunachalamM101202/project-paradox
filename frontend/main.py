import pygame
import socketio
import requests
from common.config import TILE_SIZE, SCREEN_SIZE
from frontend.renderer import draw_agent

sio = socketio.Client()
sio.connect('http://localhost:5000')

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()
agents = requests.get("http://localhost:5000/agents").json()

@sio.on('agent_update')
def update_agent(data):
    agents.update(data)

def main_loop():
    running = True
    while running:
        screen.fill((30, 30, 30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for name, info in agents.items():
            draw_agent(screen, name, info['pos'], info['status'])

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main_loop()