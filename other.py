# quelle touche a ete utiliser
if event.key == pygame.K_RIGHT:
    game.player.move_right()

if event.key == pygame.K_LEFT:
    game.player.move_left()

if event.key == pygame.K_UP:
    game.player.move_up()

if event.key == pygame.K_DOWN:
    game.player.move_down()