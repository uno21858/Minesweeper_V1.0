import os
import sys
import random 
import pygame
import time


# Initialize pygame
pygame.init()
screenx, screeny = 800, 900   # Screen size
screen = pygame.display.set_mode((screenx, screeny))  # Create the screen
pygame.display.set_caption("Busca Minas")  # Window title
clock = pygame.time.Clock()  # Clock to control the game speed

# Variables for the grid
cell_size = 50  # cell size in pixels 50x50
rows = screeny // cell_size  # Number of rows
cols = screenx // cell_size  # Number of columns

# Game variables
cant_minas = 10  # Number of mines on the board
banderas = []  # Possitions of the flags

# Font settings
font = pygame.font.Font("freesansbold.ttf", 80)  
font_instrucciones = pygame.font.Font("freesansbold.ttf", 60)  
font_instrucciones1 = pygame.font.Font("freesansbold.ttf", 31)  
font_instruccionesENG = pygame.font.Font("freesansbold.ttf", 38)  
font_numeros = pygame.font.Font("freesansbold.ttf", 25)  

#Instructions text
txt_minas = font_instrucciones.render("Total mines = 10", True, 'black')

texto_linea1 = font_instrucciones1.render("1-. Utilice click izquierdo para destapar las casillas.", True, 'black')
texto_linea2 = font_instrucciones1.render("2-. Utilice click derecho para colocar banderas.", True, 'black')
texto_linea3 = font_instrucciones1.render("3-. El juego termina si destapa una mina.", True, 'black')
texto_linea4 = font_instrucciones1.render("4-. Gana si coloca banderas en todas las minas.", True, 'black')

texto_linea5 = font_instruccionesENG.render("1-. Use left click to uncover the boxes.", True, 'black')
texto_linea6 = font_instruccionesENG.render("2-. Use right click to place flags.", True, 'black')
texto_linea7 = font_instruccionesENG.render("3-. The game ends if you uncover a mine.", True, 'black')
texto_linea8 = font_instruccionesENG.render("4-. Win by placing flags on all mines.", True, 'black')


# Class for the buttons
class Button:
    """Represents a button with text, position, and enabled status."""

    def __init__(self, text, x_position, y_position, enabled):   # Name, position, and status
        self.x = x_position
        self.y = y_position
        self.text = text
        self.enabled = enabled
        self.width = 300
        self.height = 150

    def draw(self):
        """Draws the button on the screen."""
        button_text = font.render(self.text, True, 'black')

        button_rect = pygame.rect.Rect((self.x, self.y), (self.width, self.height))
        
        """
        the function to draw the button on the screen using pygame.draw.rect

        screen: The surface to draw on
        'gray': The color of the button
        button_rect: The rectangle to draw
        0: Fill the rectangle
        5: The border radius
        eg: pygame.draw.rect(screen, 'gray', button_rect, 0, 5)"""
        pygame.draw.rect(screen, 'gray', button_rect, 0, 5)  
        pygame.draw.rect(screen, 'black', button_rect, 2, 5)  

        if self.enabled:
            if self.click():
                pygame.draw.rect(screen, 'dark gray', button_rect, 0, 5)
            else:
                pygame.draw.rect(screen, 'light gray', button_rect, 0, 5)

        screen.blit(button_text, (self.x + (self.width - button_text.get_width()) // 2, self.y + \
                                  (self.height - button_text.get_height()) // 2))

    def click(self):
        """Checks if the button was clicked."""
        mouse_p = pygame.mouse.get_pos() 
        click = pygame.mouse.get_pressed()[0]  
        button_rect = pygame.rect.Rect((self.x, self.y), (self.width, self.height))
        if click and button_rect.collidepoint(mouse_p) and self.enabled:
            return True
        else:
            return False


def menu_inicio():
    """Main menu with buttons to play, see instructions, or exit the game."""
    menu = True
    button_jugar = Button("Play", 50, 450, True)
    button_salir = Button("Exit", 450, 450, True)
    button_instructions = Button("How?", 240, 180, True)
    
    while menu:
        screen.blit(txt_minas, (screenx // 2 - txt_minas.get_width() // 2, screeny // 2 + 350))
        pygame.display.flip()
        
        screen.fill((51, 51, 255))
        button_jugar.draw()  
        button_salir.draw()
        button_instructions.draw()
        
        if button_jugar.click():
            menu = False
        if button_instructions.click():
            menu = instrucciones()
        if button_salir.click():
            pygame.quit()
            sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False


def game_over():
    """Game over menu with buttons to play again or exit the game."""
    game_overr = True
    button_jugar = Button("Again?", 50, 400, True)
    button_salir = Button("Exit", 450, 400, True)

    while game_overr:
        screen.fill((255, 51, 51))
        button_jugar.draw()
        button_salir.draw()
        pygame.display.flip()

        if button_jugar.click():
            
            game_overr = False
            
        if button_salir.click():
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_overr = False

def instrucciones():
    """Instruction menu with options to return to the main menu or exit the game."""
    instructions = True
    button_jugar = Button("Return", 50, 650, True)
    button_salir = Button("Exit", 450, 650, True)

    while instructions:
        screen.fill((46, 227, 14))
        button_jugar.draw()
        button_salir.draw()
        # Text in spanish
        texto_instrucciones = font_instrucciones.render("Instrucciones:", True, 'black')
        screen.blit(texto_instrucciones, (screenx // 2 - texto_instrucciones.get_width() // 2, screeny // 2 - 400))
        screen.blit(texto_linea1, (screenx // 2 - texto_linea1.get_width() // 2, screeny // 2 - 300))
        screen.blit(texto_linea2, (screenx // 2 - texto_linea2.get_width() // 2, screeny // 2 - 260))
        screen.blit(texto_linea3, (screenx // 2 - texto_linea3.get_width() // 2, screeny // 2 - 220))
        screen.blit(texto_linea4, (screenx // 2 - texto_linea4.get_width() // 2, screeny // 2 - 180))
        # Text in english
        texto_instrucciones = font_instrucciones.render("Instructions:", True, 'black')
        screen.blit(texto_instrucciones, (screenx // 2 - texto_instrucciones.get_width() // 2, screeny // 2 - 130))
        screen.blit(texto_linea5, (screenx // 2 - texto_linea5.get_width() // 2, screeny // 2 - 75))
        screen.blit(texto_linea6, (screenx // 2 - texto_linea6.get_width() // 2, screeny // 2 - 35))
        screen.blit(texto_linea7, (screenx // 2 - texto_linea7.get_width() // 2, screeny // 2 + 5))
        screen.blit(texto_linea8, (screenx // 2 - texto_linea8.get_width() // 2, screeny // 2 + 45))

        pygame.display.flip()

        if button_jugar.click():
            instructions = menu_inicio()
        if button_salir.click():
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = False



#  Draw the grid of the game
def grids():
    """Draw the game grid."""
    for row in range(rows):
        for col in range(cols):
            color = (255, 255, 255)  # Color de las celdas
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size), 1)
            #  Da mas detalle al tablero
            color = "gray"  # Color de las celdas
            pygame.draw.rect(screen, color, (col * cell_size - 1, row * cell_size - 1, cell_size, cell_size), 1)
            color = "dark gray"  # Color de las celdas
            pygame.draw.rect(screen, color, (col * cell_size - 1.4, row * cell_size - 1.4, cell_size, cell_size), 1)


# for debugging
def tapar_minas(minas):
    """Covers the cells where the mines are exactly located."""
    for mina in minas:
        x, y = mina
        col = x // cell_size
        row = y // cell_size
        color = "darkgray"  
        pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))


def minas_random():
    """Generates random mine positions and stores them in a file."""
    try:
        cwd = os.getcwd()
        ruta = os.path.join(cwd, "coordenadas.txt")  
        if not os.path.exists(ruta):
            print("El archivo 'coordenadas.txt' no existe. Creándolo...")
            with open(ruta, "w") as file:
                coordenadas = [(x * 25, y * 25) for x in range(1, 32, 2) for y in range(1, 36, 2)]
                file.write(str(coordenadas))
                print(f"Archivo 'coordenadas.txt' creado con {len(coordenadas)} coordenadas.")

        with open(ruta, "r") as file:
            minas = eval(file.read())  
        minas_seleccionadas = random.sample(minas, cant_minas)
        
        return minas_seleccionadas

    except Exception as e:
        print(f"Error inesperado: {e}")
        return []

def dibujo_minas(minas):
    """Places or removes a flag at the clicked position."""
    for mina in minas:
        x, y = mina
        col = x // cell_size
        row = y // cell_size
        color = "black"  
        pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))


def colocar_bandera(pos):
    """Places or removes a flag at the clicked position."""
    x, y = pos
    grid_y = y // cell_size * cell_size + 25
    grid_x = x // cell_size * cell_size + 25

    if (grid_x, grid_y) in banderas:
        banderas.remove((grid_x, grid_y))
    else:
        banderas.append((grid_x, grid_y))


def dibujar_bandera():
    """Draws the flags on the board."""
    for bandera in banderas:
        pygame.draw.rect(screen, 'red', (bandera[0] - 25, bandera[1] - 25, \
                                         cell_size - 1.5, cell_size - 1.5))  # Dibujar la bandera


def Victory(minas):
    """Checks if the player has won by comparing the flags with the mine positions."""
    if len(banderas) != len(minas):
        return False
    
    if set(banderas) == set(minas):
        return True
    
    return False


def tapar_celdas():
        """Uncover only the cells that are marked as uncovered in the 'tapadas' matrix."""
        for row in range(rows):
            for col in range(cols):
                if tapadas[row][col]:  
                    color = "gray"  
                    pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))



def destapar_casillas(tablero, x, y, tapadas):
    """Uncovers cells around a clicked cell if it has a value of 0."""
    if not tapadas[x][y]:
        return
    tapadas[x][y] = False
    if tablero[x][y] > 0:
        return
    for i in range(max(0, x - 1), min(rows, x + 2)):
        for j in range(max(0, y - 1), min(cols, y + 2)):
            if tapadas[i][j]:  # Solo destapar si está tapada
                destapar_casillas(tablero, i, j, tapadas)

def poner_numeros_alrededor(minas):  
    """Place the numbers around the mines."""
    for mina in minas:
        x, y = mina
        col = x // cell_size
        row = y // cell_size

        for i in range(-1, 2):  
            for j in range(-1, 2):  
                vecino_row = row + i
                vecino_col = col + j

                if 0 <= vecino_row < rows and 0 <= vecino_col < cols:
                    if grid[vecino_row][vecino_col] != -1:  
                        grid[vecino_row][vecino_col] += 1
    



def dibujar_numeros():  
    """Draw the numbers in the cells."""
    for row in range(rows):
        for col in range(cols):
            if isinstance(grid[row][col], int):  # Si hay un número en la celda
                numero_texto = font_numeros.render(str(grid[row][col]), True, 'black')
                screen.blit(numero_texto, (col * cell_size + 18, row * cell_size + 15))
                



def click_en_mina(click_pos, minas): 
    """Check if the clicked position is on a mine."""
    margen = cell_size // 2  
    for mina in minas:
        mina_x, mina_y = mina
        if (mina_x - margen <= click_pos[0] <= mina_x + margen) and \
                (mina_y - margen <= click_pos[1] <= mina_y + margen):
            while True:
                screen.fill("red")
                pygame.display.flip()
                time.sleep(0.5)
                return True
    return False


def reiniciar_juego():
    """Reset the game state of the variables."""
    global minas, grid, tapadas, banderas  
    banderas = [] 
    minas = minas_random() 
    minas.sort()  
    grid = [[0 for _ in range(cols)] for _ in range(rows)]  
    tapadas = [[True for _ in range(cols)] for _ in range(rows)]  
    poner_numeros_alrededor(minas)


def main():
    playing = True  
    won = False  
    pygame.display.flip()  

    menu_inicio()  
    
    reiniciar_juego()  

    while playing:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                playing = False
            # Check if the player clicked on a cell
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = pygame.mouse.get_pos()  
                x, y = click_pos

                if event.button == 1:  
                    # Left click: uncover
                    if click_en_mina(click_pos, minas):
                        print("You lost")
                        time.sleep(1)
                        game_over()
                        menu_inicio()  
                        reiniciar_juego()  
                    else:
                        print("No mine")
                        destapar_casillas(grid, y // cell_size, x // cell_size, tapadas)               
                # Right click to place or remove flag
                elif event.button == 3:  
                    colocar_bandera(click_pos)  

        screen.fill("gray")  
        # All functions of drawing
        dibujo_minas(minas)  
        dibujar_numeros()  
        tapar_celdas()  
        #tapar_minas(minas) # for easy debugging  
        dibujar_bandera()  
        
        grids()  
        
        if Victory(minas):
            won = True
        if won:
            texto_ganar = font.render("You won!", True, 'black')
            screen.blit(texto_ganar, (screenx // 2 - texto_ganar.get_width() // 2, screeny // 2))
            pygame.display.flip()
            time.sleep(3)  
            playing = False  
            game_over()

        clock.tick(30)
        pygame.display.flip()  

    pygame.quit()  

if __name__ == "__main__":
    main()
