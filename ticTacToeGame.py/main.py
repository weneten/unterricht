import pygame

pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('TicTacToe - Cross')
font = pygame.font.SysFont("arial", 70)

rect1 = pygame.Rect(0, 0, 240, 240)
rect2 = pygame.Rect(240, 0, 240, 240)
rect3 = pygame.Rect(480, 0, 240, 240)

rect4 = pygame.Rect(0, 240, 240, 240)
rect5 = pygame.Rect(240, 240, 240, 240)
rect6 = pygame.Rect(480, 240, 240, 240)

rect7 = pygame.Rect(0, 480, 240, 240)
rect8 = pygame.Rect(240, 480, 240, 240)
rect9 = pygame.Rect(480, 480, 240, 240)

rectangles = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9]

circleStates = [False] * 9
crossStates = [False] * 9
playerTurn = "Cross"

board = [None] * 9

winConditions = [
                [0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]
                ]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            for i, rect in enumerate(rectangles):
                if rect.collidepoint(event.pos) and board[i] is None:
                    board[i] = playerTurn 
                    if playerTurn == "Cross":
                        crossStates[i] = "Cross"
                        playerTurn = "Circle"
                    elif playerTurn == "Circle":
                        circleStates[i] = "Circle"
                        playerTurn = "Cross"
                    pygame.display.set_caption(f'TicTacToe - {playerTurn}')

    screen.fill("white")
    
    mouseX, mouseY = pygame.mouse.get_pos()

    for i, rect in enumerate(rectangles):
        pygame.draw.rect(screen, color=(0, 0, 0), rect=rect, width=10)
        if circleStates[i]:
            pygame.draw.circle(screen, (0, 0, 0), center=(rect.centerx, rect.centery), radius=69, width=12)
        if crossStates[i]:
            pygame.draw.line(screen, (0, 0, 0), (rect.centerx - 40, rect.centery - 40), (rect.centerx + 40, rect.centery + 40), 16)
            pygame.draw.line(screen, (0, 0, 0), (rect.centerx - 40, rect.centery + 40), (rect.centerx + 40, rect.centery - 40), 16)
            

    for condition in winConditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] is not None:
            winner = board[condition[0]].capitalize()
            text = font.render(f"{winner} Won!", True, "black")
            text_rect = text.get_rect(center=(360, 360))
            screen.fill("white")
            screen.blit(text, text_rect)
            break
        elif all(x is not None for x in board):
            text = font.render("Draw", True, "black")
            text_rect = text.get_rect(center=(360, 360))
            screen.fill("white")
            screen.blit(text, text_rect)
            break


    pygame.display.flip()

pygame.quit()