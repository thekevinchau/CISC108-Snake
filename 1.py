
from designer import *
from random import randint

World = { 'snake': DesignerObject,
          'snake speed': {"x": int, "y": int},
          'timer': DesignerObject,
          'obstacles': [DesignerObject],
          'time': int,
          'food': [DesignerObject],
          'counter': DesignerObject,
          'segments': [DesignerObject],
          'head x': [int],
          'head y': [int],
           }


SNAKE_SPEED = 10
def create_snake()-> DesignerObject:
    '''
    Consumes nothing and produces an image of a snake head.
    
    Args:
        No arguments
    
    Returns:
        (DesignerObject): An image of the imported snake head.
        
    
    '''
    snake = image('snakehead.png')
    snake['scale'] = .1
    return snake
    

def create_world() -> World:
    '''
    Consumes nothing but returns a new dictionary with values for the World dictionary.
    
    Args:
        No arguments
        
    Returns:
        World: A dictionary storing values into the keys of the world definition.
    '''
    return { 'snake': create_snake(),
             'snake speed': {"x": SNAKE_SPEED, "y": 0},
             'food': create_food(),
             'time': 0,
             'timer': text('black', 'Timer', 20, 400,50),
             #'obstacle': create_obstacle(),
             'obstacles': [],
             'food': [],
             'score': 0,
             'segments': [],
             'head x': [],
             'head y': [],
             }

def move_snake(world: World):
    world['snake']['x'] += world['snake speed']['x']
    '''
    Consumes the World dictionary and updates the horizontal speed of the snake head,
    having it move constantly as the game updates. 
    
    Args:
        World(dict): The World dictionary
    
    Returns:
        Returns nothing
    '''
    

    
def move_snake_y(world: World):
    '''
    Consumes the World dictionary and updates the vertical speed of the snake head,
    having it move constantly as the game updates.
    
    Args:
        World(dict): The World dictionary.
    
    Returns:
        Returns nothing
        
    
    '''
    world['snake']['y'] += world['snake speed']['y']
    
 
def head_left(world: World):
    '''
    Consumes the World dictionary and adjusts the horizontal speed of the snake head to account for its movemnent
    to the left. Also mirrors the snake's head to match the direction it is moving towards.
    
    Args:
        World(dict): The World dictionary.
        
    Returns:
        Returns nothing
    '''
    world['snake speed']['x'] = -SNAKE_SPEED
    world['snake']['flip_x'] = True
    world['snake speed']['y'] = 0

    
def head_right(world: World):
    '''
    Consumes the World dictionary and adjusts the horizontal speed of the snake head to account for its movement to the right.
    
    Args:
        World(dict): The World dictionary.
        
    Returns:
        Returns nothing
    '''
    world['snake speed']['x'] = +SNAKE_SPEED
    world['snake']['flip_x'] = False
    world['snake speed']['y'] = 0
    

def head_up(world: World):
    '''
    Consumes the World dictionary and adjusts the vertical speed of the snake head to account for its movement upwards. In this case,
    the snake 
    
    Args:
        World(dict): The World dictionary.
        
    Returns:
        Returns nothing
    '''
    world['snake speed']['y'] = -SNAKE_SPEED
    world['snake speed']['x'] = 0

def head_down(world: World):
    '''
    Consumes the World dictionary and adjusts the vertical speed of the snake head to account for its movement downwards. In this case,
    the snake speed will be positive since the window's pixels increase as it goes downwards.
    
    Args:
        World(dict): The World dictionary.
        
    Returns:
        Returns nothing
    '''
    world['snake speed']['y'] = +SNAKE_SPEED
    world['snake speed']['x'] = 0


def bump_wall_y(world: World):
    '''
    Consumes the world dictionary and checks if the game is beyond the vertical boundaries of the window. If so, the game will
    stop.
    
    Args:
        World(dict): The World dictionary.
        
    Returns:
        Returns nothing
    
    '''
    if world['snake']['y'] > get_height():
        stop()
        world['timer']['text'] = 'GAME OVER!'
    elif world['snake']['y'] <0:
        world['timer']['text'] = 'GAME OVER!'
        stop()
    

def bump_wall_x(world: World):
    '''
    Consumes the world dictionary and checks if the game is beyond the horizontal boundaries of the window. If so, the game will stop.
    
    Args:
        World(dict): The World dictionary
        
    Returns:
        Returns nothing
    '''
    if world['snake']['x'] > get_width():
        stop()
    elif world['snake']['x'] < 0:
        stop()
        
def control_snake_x(world: World, key: str):
    '''
    Consumes the world dictionary and a string regarding the key, and checks which horizontal directional key is pressed,
    and changes the snake's direction accordingly.
    
    Args:
        World(dict): The World dictionary
    
    Returns:
        Nothing
    '''
    if key == 'left':
        head_left(world)
    elif key == 'right':
        head_right(world)
        
def control_snake_y(world: World, key: str):
    '''
    Consumes the World dictionary and a string regarding the key,
    and checks which vertical directional (up arrow or down arrow) key is pressed and changes the snake's
    direction accordingly.
    
    Args:
        World(dict): The World dictionary
        
    Returns:
        Returns nothing
    '''
    if key == 'up':
        head_up(world)
    elif key == 'down':
        head_down(world)

def create_food() -> DesignerObject:
    '''
    Consumes nothing and returns an image of the imported food. The chosen food is a mouse. The food is spawned in
    random positions across the game window.
    
    
    Args:
        No arguments.
    
    Returns:
        (DesignerObject): An image of the imported mouse image depicted as food.
        
    '''
    food = image('mouse.png')
    food['scale'] = .05
    food['x'] = randint(20, (get_width()/10)*10)
    food['y'] = randint(20, (get_height()/10)*10)
    return food

def spawn_food(world: World):
    '''
    Consumes the World dictionary and spawns between 1 to 4 food pieces randomly across the game window.
    The create_food function is called here and appends to the list of food that will be on the screen.
    
    Args:
        World(dict): The World dictionary
        
    Returns:
        Returns nothing
    '''
    limit_food = len(world['food']) < 4
    random_chance = randint(1, 4)
    if limit_food and random_chance:
        world['food'].append(create_food())

def timer(world: World):
    '''
    Consumes the World dictionary and displays a text box showing the time alive in the game.
    
    Args:
        World(dict): The World dictionary
        
    Returns:
        Returns nothing
    '''
    world['timer']['text'] = 'TIME ALIVE: ' + str(world['time'])
    world['time'] += 1/30
    
    
def collide_snake_food(world):
    '''
    Consumes the World dictionary and checks if the snake head collides with the food.
    Upon collission, the food will disappear and respawn elsewhere on the screen. For each
    food particle eaten, the snake will gain another body segment.
    
    Args:
        World(dict): The World dictionary
        
    Returns:
        Returns nothing
   
    
    '''
    eaten_food = []
    for food in world['food']:
        if colliding(world['snake'], food):
            eaten_food.append(food)
            segment = circle('green', 13, 0, 0)
            world['segments'].append(segment)
            create_snake
    world['food'] = filter_from(world['food'], eaten_food)
    
def create_obstacle() -> DesignerObject:
    '''
    Consumes nothing and returns a DesignerObject representing a black rectangle with dimensions 35x35.
    
    
    Args:
        No arguments
        
    Returns:
        (DesignerObject): A black rectangle with dimensions 35x35.
    '''
    obstacle = rectangle('black', 35, 35)
    obstacle['x'] = randint(0,(get_width()*30)/30)
    obstacle['y'] = randint(0, (get_height()*30)/30)
    return obstacle

def spawn_obstacle(world: World):
    '''
    Consumes the World dictionary and spawns three obstacles in random locations within the game window.
    
    Args:
        World(dict): The World dictionary
    
    Returns:
        Returns nothing
    '''
    limit_obstacle = len(world['obstacles']) < 8
    random_chance = randint(1, 8)
    if limit_obstacle and random_chance:
        world['obstacles'].append(create_obstacle())
        
def collide_obstacle(world: World):
    '''
    Consumes the World dictionary and checks if the snake head collides with any of the three obstacles spawned in the game.
    
    Args:
        World(dict): The World dictionary
        
    Returns:
        Returns nothing
    
    '''
    for obstacle in world['obstacles']:
        if colliding(world['snake'], obstacle):
            pause()


    
def collide_snake_body(world):
    '''
    Consumes the World dictionary and checks if the snake head collides with the second segment and all the segments after. If so,
    the game will end.
    
    Args:
        World(dict): The World dictionary
        
    Returns:
        Returns nothing
    '''
    for segment in world['segments'][2:]:
        if colliding(world['snake'], segment):
            pause()


def filter_from(old_list: list, elements_to_not_keep) -> list:
    '''
    Consumes a list and filters out the food still present in the world and the food that has been eaten.
    The eaten food will disappear from the world because it does not get appended to the list that will be
    displayed on the screen.
    
    Args:
        World(dict): The World dictionary
    
    Returns:
        list: A list of the food that hasn't been eaten.
    
    '''
    new_values = []
    for item in old_list:
        if item not in elements_to_not_keep:
            new_values.append(item)
    return new_values

def add_position(world: World):
    '''
    Consumes a World dictionary and stores the snake head's x and y position into a list.
    
    Args:
        World(dict): The World dictionary
        
    Returns:
        Returns nothing
    '''
    world['head x'].append(world['snake']['x'])
    world['head y'].append(world['snake']['y'])
    
def set_position(world: World):
    '''
    Consumes a World dictionary and sets the position of the segments in the position of the snake's old head positon. 
    Each segment added on will be three pixels behind the segment before it, resulting in a snake-like movement.
    
    Args:
        World(dict): The World dictionary
        
    Returns:
        Returns nothing
    '''
    for segment in world['segments']:
        i = 0
        for segment in world['segments']:
            i+=3
            segment['x'] = (world['head x'])[len(world['head x'])-i]
            segment['y'] = (world['head y'])[len(world['head y'])-i]
    


#CREATES WORLD    
when('starting', create_world)
#MOVES SNAKE ON ITS OWN
when('updating', move_snake)
when('updating', move_snake_y)


when('updating', bump_wall_x)
when('updating', bump_wall_y)
when('updating', spawn_food)
when('updating', spawn_obstacle)
when('updating', collide_obstacle)
when('updating', add_position)
when('updating', timer)
when('updating', set_position)
when('updating', collide_snake_food)
when('updating', spawn_food)
when('updating', collide_snake_body)
when('typing', control_snake_x)
when('typing', control_snake_y)
start()