import pygame
from game_client import sio, send_position

WIDTH, HEIGHT = 640, 480
GRID_SIZE = 10

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DeepTrust Prototype")
font = pygame.font.SysFont(None, 24)

# Static agent info for now
agents = {
    "John": [2, 2],
    "Anna": [5, 5],
    "Arun": [8, 2]
}

def draw_agents():
    win.fill((30, 30, 30))
    for name, (x, y) in agents.items():
        pygame.draw.rect(win, (255, 255, 0), (x * GRID_SIZE, y * GRID_SIZE, 20, 20))
        text = font.render(name, True, (255, 255, 255))
        win.blit(text, (x * GRID_SIZE, y * GRID_SIZE - 20))
    pygame.display.update()

sio.connect("http://localhost:8001")

@sio.event
async def connect(sid, environ):
    print(f"✅ WebSocket connected: {sid}")
    
run = True
while run:
    draw_agents()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Dummy update
    agents["John"][0] += 1
    send_position("John", agents["John"][0], agents["John"][1])
    pygame.time.delay(1000)

sio.disconnect()
pygame.quit()