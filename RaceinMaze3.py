from cmu_112_graphics import *
import random


def appStarted(app):
    app.rows = 25
    app.cols = 25
    app.margin = 50
    app.r = 20
    app.highscore = 0    
    initRaceinMaze(app)
    
    

def initRaceinMaze(app):
    app.wall = {(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(0,12),(0,13),(0,14),(0,15),(0,16),(0,17),(0,18),(0,19),(0,20),(0,21),(0,22),(0,23),(0,24),
                (1,0),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,20),(1,21),(1,22),(1,23),(1,24),
                (2,0),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(2,12),(2,13),(2,14),(2,15),(2,16),(2,17),(2,20),(2,21),(2,22),(2,23),(2,24),
                (3,0),(3,8),(3,9),(3,12),(3,13),(3,14),(3,15),(3,16),(3,17),(3,20),(3,21),(3,22),(3,23),(3,24),
                (4,0),(4,8),(4,9),(4,12),(4,13),(4,14),(4,23),(4,24),
                (5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,8),(5,9),(5,12),(5,13),(5,14),(5,23),(5,24),
                (6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,8),(6,9),(6,12),(6,13),(6,14),(6,15),(6,16),(6,17),(6,20),(6,21),(6,22),(6,23),(6,24),
                (7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,8),(7,9),(7,14),(7,15),(7,16),(7,17),(7,20),(7,21),(7,22),(7,23),(7,24),
                (8,0),(8,3),(8,4),(8,5),(8,14),(8,15),(8,16),(8,17),(8,20),(8,21),(8,22),(8,23),(8,24),
                (9,0),(9,3),(9,4),(9,5),(9,8),(9,9),(9,10),(9,11),(9,12),(9,13),(9,14),(9,15),(9,16),(9,17),(9,18),(9,19),(9,20),(9,21),(9,22),(9,23),(9,24),
                (10,0),(10,10),(10,11),(10,12),(10,13),(10,14),(10,15),(10,16),(10,17),(10,18),(10,19),(10,20),(10,21),(10,22),(10,23),(10,24),
                (11,0),(11,17),(11,18),(11,19),(11,20),(11,21),(11,22),(11,23),(11,24),
                (12,0),(12,1),(12,2),(12,3),(12,4),(12,5),(12,6),(12,7),(12,8),(12,9),(12,10),(12,11),(12,17),(12,18),(12,19),(12,20),(12,21),(12,24),
                (13,0),(13,1),(13,2),(13,3),(13,4),(13,5),(13,6),(13,7),(13,8),(13,9),(13,10),(13,11),(13,12),(13,13),(13,14),(13,17),(13,18),(13,19),(13,20),(13,21),(13,24),
                (14,0),(14,1),(14,2),(14,5),(14,6),(14,7),(14,8),(14,9),(14,10),(14,11),(14,12),(14,13),(14,14),(14,24),
                (15,0),(15,1),(15,2),(15,24),
                (16,0),(16,1),(16,2),(16,12),(16,13),(16,14),(16,15),(16,16),(16,17),(16,18),(16,19),(16,20),(16,21),(16,22),(16,23),(16,24),
                (17,0),(17,1),(17,2),(17,3),(17,4),(17,5),(17,6),(17,7),(17,8),(17,9),(17,12),(17,13),(17,14),(17,15),(17,16),(17,17),(17,18),(17,19),(17,20),(17,21),(17,22),(17,23),(17,24),
                (18,0),(18,1),(18,2),(18,3),(18,4),(18,5),(18,6),(18,7),(18,8),(18,9),(18,24),
                (19,0),(19,1),(19,5),(19,6),(19,7),(19,8),(19,9),(19,24),
                (20,0),(20,1),(20,5),(20,6),(20,7),(20,8),(20,9),(20,10),(20,11),(20,12),(20,13),(20,14),(20,15),(20,16),(20,17),(20,20),(20,21),(20,22),(20,23),(20,24),
                (21,0),(21,1),(21,7),(21,8),(21,9),(21,10),(21,11),(21,12),(21,13),(21,14),(21,15),(21,16),(21,17),(21,20),(21,21),(21,22),(21,23),(21,24),
                (22,0),(22,1),(22,12),(22,13),(22,14),(22,15),(22,24),
                (23,0),(23,1),(23,2),(23,3),(23,24),
                (24,0),(24,1),(24,2),(24,3),(24,4),(24,5),(24,6),(24,7),(24,8),(24,9),(24,10),(24,11),(24,12),(24,13),(24,14),(24,15),(24,16),(24,17),(24,18),(24,19),(24,20),(24,21),(24,22),(24,23),(24,24)}
    app.start = [(1,1)]
    app.direction = (0,0)
    app.score = 0
    app.steps = 300
    app.timer = 60
    placescoredot(app)
    # gametime(app)
    app.gameOver = False


def getCell(app, x, y):
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth  = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    row = int((y - app.margin) / cellHeight)
    col = int((x - app.margin) / cellWidth)

    return (row, col)

def getCellBounds(app, row, col):
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = app.margin + col * cellWidth
    x1 = app.margin + (col+1) * cellWidth
    y0 = app.margin + row * cellHeight
    y1 = app.margin + (row+1) * cellHeight
    return (x0, y0, x1, y1)

def keyPressed(app, event):
    (trow,tcol) = app.start[0]
    if (event.key == 'Up'):
        if((trow-1,tcol) not in app.wall):
            app.direction = (-1, 0)
            takeStep(app)
    elif (event.key == 'Down'):
        if((trow+1,tcol) not in app.wall):
            app.direction = (+1, 0)
            takeStep(app)
    elif (event.key == 'Left'):
        if((trow,tcol-1) not in app.wall):
            app.direction = (0, -1)
            takeStep(app)
    elif (event.key == 'Right'):
        if((trow,tcol+1) not in app.wall):
            app.direction = (0, +1)
            takeStep(app)
    elif (event.key == 'r'):
        initRaceinMaze(app)


def takeStep(app):
    (drow, dcol) = app.direction
    (headRow, headCol) = app.start[0]
    (newRow, newCol) = (headRow+drow, headCol+dcol)
    if(app.timer == 0):
        app.gameOver = True
    else:
        app.start[0] = (newRow,newCol)
        # app.steps -= 1
        if(app.scoredotPosition == (newRow,newCol)):
            placescoredot(app)
            app.score += 1
            if(app.score>app.highscore):
                app.highscore = app.score
        

def placescoredot(app):
    while True:
        row = random.randint(0, app.rows-1)
        col = random.randint(0, app.cols-1)
        if (row,col) not in app.start:
            if((row,col) not in app.wall):
                app.scoredotPosition = (row, col)
                return

        

def drawboard(app,canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            fill = "black"
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)
    

def drawscoredot(app, canvas):
    if (app.scoredotPosition != None):
        (row, col) = app.scoredotPosition
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_oval(x0, y0, x1, y1, fill='green')

def drawwall(app,canvas):
    for(row,col) in app.wall:
        (x0,y0,x1,y1) = getCellBounds(app, row, col)
        canvas.create_rectangle(x0,y0,x1,y1, fill= "#560C0C")

def drawplayerdot(app,canvas):
    
    for(row,col) in app.start:
        (x0,y0,x1,y1) = getCellBounds(app,row,col)
        canvas.create_oval(x0,y0,x1,y1,fill="white")

def drawAppInfo(app, canvas):
    font = 'Arial 18 bold'
    title ='Race In Maze'
    canvas.create_text(app.width/5, 20, text=title, font=font,fill="white")
    canvas.create_text(app.width-100, 20,
                       text=f'Score: {app.score}',
                       font=font,fill="white")
    canvas.create_text(app.width-150, app.height - 20,
                       text=f'HighestScore: {app.highscore}',
                       font=font,fill="white")
    canvas.create_text(app.width-300,20,
                       text=f'Steps Left: {app.timer}',
                       font=font, fill="white")   

def drawGameOver(app, canvas):
    if (app.gameOver):
        canvas.create_rectangle(app.width/7,app.height*2/7,app.width*6/7,app.height*4/5,fill="Bisque")
        canvas.create_text(app.width/2, app.height/2-70, text='Game over',
                           font='Arial 50 bold', fill="black")
        canvas.create_text(app.width/2, (app.height/2),
                       text=f'Score: {app.score}',
                       font='Arial 50 bold', fill="black")
        canvas.create_text(app.width/2, (app.height/2)+70,
                       text=f'HighestScore: {app.highscore}',
                       font='Arial 50 bold', fill="black")
        canvas.create_text(app.width/2, (app.height/2)+140,
                           text='Press r to restart',
                           font='Arial 50 bold', fill="black")
        

def drawscreen(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height, fill="black")

def redrawAll(app, canvas):
    drawscreen(app,canvas)
    drawboard(app, canvas)
    drawwall(app,canvas)
    drawplayerdot(app, canvas)
    drawscoredot(app, canvas)
    drawAppInfo(app, canvas)
    drawGameOver(app,canvas)

runApp(width=800, height=600)