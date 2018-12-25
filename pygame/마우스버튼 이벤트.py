import pygame

#게임 엔진 초기화
pygame.init()

#RGB 포맷으로 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#화면의 높이와 폭 설정
size = [400, 300]
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("consolas", 20)

pygame.display.set_caption("Game Title")

#사용자가 클릭할 때까지 반복한다
done = False
flag = None
clock = pygame.time.Clock()

#printText 함수
def printText(msg, color='BLACK', pos=(50,50)):
    textSurface = font.render(msg, True, pygame.Color(color), None)
    textRect = textSurface.get_rect()
    textRect.topleft = pos

    screen.blit(textSurface, textRect)

while not done:

    #1초에 10번의 반복으로 제한
    clock.tick(10)

    #메인 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: #사용자가 눌렀던걸 뗐을 때
            flag = True
        elif event.type == pygame.MOUSEBUTTONUP: #사용자가 눌렀을 때
            flag = False
        elif event.type == pygame.QUIT: #사용자가 닫기를 눌렀을 때
            done = True


    screen.fill(WHITE)

    if flag == True:
        printText('you just mouse down!!', 'RED')
        printText('--> you pressed your', 'RED', (50, 70))
        printText('    left mouse button.', 'RED', (50, 90))

    elif flag == False:
        printText('you just mouse up!!', 'BLUE')
        printText('--> released what you pressed.', 'BLUE', (50, 70))


    else:
        printText('Please press any key.')



    pygame.display.flip()


pygame.quit()
