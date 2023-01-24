import sys, pygame as pg

pg.init()
screen_size = 750,750
screen = pg.display.set_mode(screen_size)
pg.font.init()
playing = True

#tile fill list
set_font = pg.font.match_font("Segoe UI Symbol")
font = pg.font.Font(set_font, 45)
chess_pieces = {
    'b_checker': u'\u25FB',
    'b_pawn': u'\u265F',
    'b_rook': u'\u265C',
    'b_knight': u'\u265E',
    'b_bishop': u'\u265D',
    'b_king': u'\u265A',
    'b_queen': u'\u265B',
    'w_checker': u'\u25FC',
    'w_pawn': u'\u2659',
    'w_rook': u'\u2656',
    'w_knight': u'\u2658',
    'w_bishop': u'\u2657',
    'w_king': u'\u2654',
    'w_queen': u'\u2655'
}

chess_grid = [
    ['b_rook', 'b_knight', 'b_bishop', 'b_queen', 'b_king', 'b_bishop', 'b_knight', 'b_rook'],
    ['b_pawn', 'b_pawn', 'b_pawn', 'b_pawn', 'b_pawn', 'b_pawn', 'b_pawn', 'b_pawn'],
    ['Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null'],
    ['Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null'],
    ['Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null'],
    ['Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null'],
    ['w_pawn', 'w_pawn', 'w_pawn', 'w_pawn', 'w_pawn', 'w_pawn', 'w_pawn', 'w_pawn'],
    ['w_rook', 'w_knight', 'w_bishop', 'w_queen', 'w_king', 'w_bishop', 'w_knight', 'w_rook']
]

def draw_pieces():
    offset = 35
    for row in range(8):
        for col in range(8):
            output = chess_grid[row][col]
            if output != 'Null':
                if output in chess_pieces:
                    output = chess_pieces[output]
                    print(output)
                piece_surface = font.render(output, True, pg.Color('black'))
                screen.blit(piece_surface, (col * 90 + offset + 5, row * 90 + offset - 2))

def draw_background():
    screen.fill(pg.Color("burlywood2"))
    pg.draw.rect(screen, pg.Color("burlywood4"), pg.Rect(15, 15, 720, 720), 7)
    i = 1
    for i in range(1, 8):
        pg.draw.line(screen, pg.Color("burlywood4"), pg.Vector2((i * 90) + 15, 15), pg.Vector2((i * 90) + 15, 730), 2)
        pg.draw.line(screen, pg.Color("burlywood4"), pg.Vector2(15, (i * 90) + 15), pg.Vector2(730, (i * 90) + 15), 2)

def game_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT:
             sys.exit()

    draw_background()
    draw_pieces()
    pg.display.flip()

while playing:
    game_loop() 