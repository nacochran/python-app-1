# project specific libraries
from library import *

# button library
from button import *

# simulations
from vector_slope_field import *
from fireworks import *

######################### go-to function scenes #########################
def to_simulations():
    globals['scene'] = 'simulationGallery'

def to_simulation_area():
    globals['scene'] = 'simulationArea'

def to_about():
    globals['scene'] = 'about'

def to_menu():
    globals['scene'] = 'menu'

def end_game():
    pygame.quit()
    sys.exit()

# initalize pygame canvas
pygame.init()

# set app name
pygame.display.set_caption("Final Project")

# load background image
BG = pygame.image.load("assets/background.jpg")

######################### buttons for each scene #########################
buttons = {
    'menu' : [],
    'about' : [],
    'simulationGallery' : [],
    'simulationArea' : []
}

######################### menu buttons #########################
buttons['menu'].append(Button(
    image = pygame.image.load("assets/button.jpg"),
    hover_image = pygame.image.load("assets/buttonhover.jpg"),
    pos = (640, 250), 
    size = (400, 100),
    text_input = "Simulations",
    font = get_font(55),
    color = "#d7fcd4",
    click_effect = addInterval,
    effect_args = [to_simulations, 10]
))
buttons['menu'].append(Button(
    image = pygame.image.load("assets/button.jpg"),
    hover_image = pygame.image.load("assets/buttonhover.jpg"),
    pos = (640, 400), 
    size = (400, 100),
    text_input = "About",
    font = get_font(55),
    color = "#d7fcd4",
    click_effect = addInterval,
    effect_args = [to_about, 10]
))
buttons['menu'].append(Button(
    image = pygame.image.load("assets/button.jpg"),
    hover_image = pygame.image.load("assets/buttonhover.jpg"),
    pos = (640, 550), 
    size = (400, 100),
    text_input = "Quit",
    font = get_font(55),
    color = "#d7fcd4",
    click_effect = end_game,
    effect_args = []
))

######################### about buttons #########################
buttons['about'].append(Button(
    image = pygame.image.load("assets/button.jpg"),
    hover_image = pygame.image.load("assets/buttonhover.jpg"),
    pos = (globals['width'] - 75, 50), 
    size = (100, 50),
    text_input = "Menu",
    font = get_font(20),
    color = "#d7fcd4",
    click_effect = addInterval,
    effect_args = [to_menu, 10]
))

######################### simulation-gallery buttons #########################
simulations = {
    'navigation' : {
        'math' : [
            "Vector Slope Field",
            "???",
            "???",
            "???",
            "???",
            "???"
        ],
        'chemistry' : [
            "???",
            "???",
            "???",
            "???",
            "???",
            "???"
        ],
        'physics' : [
            "Fireworks",
            "???",
            "???",
            "???",
            "???",
            "???"
        ],
        'astronomy' : [
            "???",
            "???",
            "???",
            "???",
            "???",
            "???"
        ]
    },
    'subprograms': {
        "vector slope field" : vectorSlopeField,
        "fireworks" : fireworksProgram
    }
}

buttons['simulationGallery'].append(Button(
    image = pygame.image.load("assets/button.jpg"),
    hover_image = pygame.image.load("assets/buttonhover.jpg"),
    pos = (globals['width'] - 75, 50), 
    size = (100, 50),
    text_input = "Menu",
    font = get_font(20),
    color = "#d7fcd4",
    click_effect = addInterval,
    effect_args = [to_menu, 10]
))

j = 0
for category in simulations['navigation']:
    i = 0
    for simulation in simulations['navigation'][category]:
        keyName = simulation.lower()
        buttons['simulationGallery'].append(Button(
            image = pygame.image.load("assets/button.jpg"),
            hover_image = pygame.image.load("assets/buttonhover.jpg"),
            pos = (190 + j*300, 400 + i*50), 
            size = (250, 50),
            text_input = simulation,
            font = get_font(20),
            color = "#d7fcd4",
            click_effect = addInterval,
            effect_args = [to_simulation_area, 10, keyName]
        ))
        i += 1
    j += 1

######################### simulation area buttons #########################
buttons['simulationArea'].append(Button(
    image = pygame.image.load("assets/button.jpg"),
    hover_image = pygame.image.load("assets/buttonhover.jpg"),
    pos = (globals['width'] - 75, 50), 
    size = (100, 50),
    text_input = "Back",
    font = get_font(20),
    color = "#d7fcd4",
    click_effect = addInterval,
    effect_args = [to_simulations, 10]
))