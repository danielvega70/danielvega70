import pygame

# initialize pygame
pygame.init()

# set up game window
win_width = 600
win_height = 800
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Geometry Dash Clone")

# set up game variables
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsans', 30)
score = 0

# set up player variables
player_width = 50
player_height = 50
player_x = 50
player_y = 350
player_vel = 10
player_jump_vel = 20
player_jump = False
player_jump_count = 0

# set up obstacle variables
obstacle_width = 50
obstacle_height = 50
obstacle_gap = 200
obstacle_vel = 5
obstacle_x = win_width
obstacle_y = 0

# set up game loop
run = True
while run:
    # set up event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_jump = True

    # move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= player_vel
    if keys[pygame.K_DOWN]:
        player_y += player_vel

    # handle player jumping
    if player_jump:
        if player_jump_count == 0:
            player_jump_count = 1
            player_y -= player_jump_vel
        elif player_jump_count < 10:
            player_jump_count += 1
            player_y -= player_jump_vel
        else:
            player_jump = False
            player_jump_count = 0

    # move obstacle
    obstacle_x -= obstacle_vel
    if obstacle_x < -obstacle_width:
        obstacle_x = win_width
        score += 1

    # check for collision
    if (player_x + player_width > obstacle_x and player_x < obstacle_x + obstacle_width and
            (player_y < obstacle_y + obstacle_gap or player_y + player_height > obstacle_y + obstacle_gap + obstacle_height)):
        run = False

    # draw game objects
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (0, 0, 0), (player_x, player_y, player_width, player_height))
    pygame.draw.rect(win, (255, 0, 0), (obstacle_x, obstacle_y, obstacle_width, obstacle_gap))
    pygame.draw.rect(win, (255, 0, 0), (obstacle_x, obstacle_y + obstacle_gap + obstacle_height, obstacle_width, win_height - obstacle_y - obstacle_gap - obstacle_height))
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    win.blit(score_text, (10, 10))

    # update game window
    pygame.display.update()
    clock.tick(60)

# end game
pygame.quit()
