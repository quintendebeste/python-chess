import sys, pygame as pg,time

pg.init()
screen_size = 750,750
screen = pg.display.set_mode(screen_size)
pg.font.init()
playing = True
green = (0,255,0)
red = (255,0,0)


# draws nodes on the same spot as the chesspieces using the "chess_pieces" list for the location of the pieces
def draw_nodes():
    offset = 55
    for row in range(8):
        for col in range(8):
            output = chess_grid[row][col]
            if output != 'Null':
                if output in chess_pieces:
                    output = chess_pieces[output]
                pg.draw.circle(screen, red, (col * 90 + offset + 5, row * 90 + offset - 2), 10)

# checks the position of the mouse and if the position is equal to the position of a node and if its clicked
def mouse_detection():
    mouse_pos = pg.mouse.get_pos()
    for row in range(8):
        for col in range(8):
            output = chess_grid[row][col]
            if output != 'Null':
                node_x = col * 90 + 55 + 5
                node_y = row * 90 + 55 - 2
                node_rect = pg.Rect(node_x - 25, node_y - 25, 50, 50)
                pg.draw.rect(screen, red, node_rect)
                if node_rect.collidepoint(mouse_pos):
                    if pg.mouse.get_pressed()[0]:
                        if output in chess_pieces:
                            output = chess_pieces[output]
                            return output,row,col

# a function wich shows the possible moves according to the clicked piece in the "mouse_detection" function
def moves_show(piece,row,col):
    offset = 55
    piece = piece
    row = row
    col = col
    print(piece,f"location: (row:{row},column:{col})")
    if(piece == chess_pieces['w_pawn']):
        for i in range(2):
            row -= 1
            pg.draw.circle(screen, green, (col * 90 + offset + 5, row * 90 + offset - 2), 10)
            print("move")



# font for chesspieces
set_font = pg.font.match_font("Segoe UI Symbol")
font = pg.font.Font(set_font, 42)

# a list of the unicode for each chesspiece put in a variable for ease of use
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

# this list represents a chess board with the pieces on their locations
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

# a function for going trough the chess_grid list and placing the pices on the board according to their location in the list
def draw_pieces():
    offset = 35
    for row in range(8):
        for col in range(8):
            output = chess_grid[row][col]
            if output != 'Null':
                if output in chess_pieces:
                    output = chess_pieces[output]
                piece_surface = font.render(output, True, pg.Color('black'))
                screen.blit(piece_surface, (col * 90 + offset + 5, row * 90 + offset - 2))

# a function for drawing a chess board in the pygame window for the chesspices to stand on
def draw_background():
    screen.fill(pg.Color("burlywood2"))
    pg.draw.rect(screen, pg.Color("burlywood4"), pg.Rect(15, 15, 720, 720), 7)
    i = 1
    for i in range(1, 8):
        #vertical lines
        Vstrt_pos = pg.Vector2((i * 90) + 15, 15)
        Vend_pos = pg.Vector2((i * 90) + 15, 730)
        line_length = 715
        pg.draw.line(screen, pg.Color("burlywood4"), Vstrt_pos, Vend_pos, 2)

        #horizontal lines
        Hstrt_pos = pg.Vector2(15, (i * 90) + 15)
        Hend_pos = pg.Vector2(730, (i * 90) + 15)
        pg.draw.line(screen, pg.Color("burlywood4"), Hstrt_pos, Hend_pos, 2)

# a function wich represents a basic gameloop that's running all the previous functions one after another
def game_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT:
             sys.exit()

    draw_background()
    draw_pieces()
    #draw_nodes()
    mouse_detection()
    piece,row,col = mouse_detection()
    if(piece):
        moves_show(piece,row,col)
    pg.display.flip()

# a while loop that keeps looping the game_loop function until the window is closed
while playing:
    mouse = pg.mouse.get_pos()
    game_loop() 