import pygame 

pygame.init()

#Constants 
WIDTH = 640
HEIGHT = 640
SQUARE_SIZE = 80
LIGHT_COLOR = (242, 232, 213)
DARK_COLOR = (181, 136, 99)
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]
pieces_mapping = {
    'r': 'assets/black-rook.png',
    'n': 'assets/black-knight.png',
    'b': 'assets/black-bishop.png',
    'q': 'assets/black-queen.png',
    'k': 'assets/black-king.png',
    'p': 'assets/black-pawn.png',
    'R': 'assets/white-rook.png',
    'N': 'assets/white-knight.png',
    'B': 'assets/white-bishop.png',
    'Q': 'assets/white-queen.png',
    'K': 'assets/white-king.png',
    'P': 'assets/white-pawn.png'
}

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess Game')

def draw_board():
    for row in range(8):
        for col in range(8):
            color = LIGHT_COLOR if (row + col) % 2 == 0 else DARK_COLOR
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    



def draw_pieces(board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != '.': 
                screen.blit(images[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

def load_images(pieces_mapping):
    images = {}
    for piece, path in pieces_mapping.items():
        image = pygame.image.load(path)
        images[piece] = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
    return images

images = load_images(pieces_mapping)

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    draw_board()
    draw_pieces(board)
    pygame.display.flip()

pygame.quit()


