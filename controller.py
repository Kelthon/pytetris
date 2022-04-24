from typing import Dict
from pygame.rect import Rect
from Blocks import BLUE_RICKY, CLEVELANDZ, HERO, ORANGE_RICKY, RHODE_ISLAND_Z, TEWEE, Block
    
def readjust_pieces(list_square:list, line):
    for i in list_square:
        if i.y < line:
            i.y += 20

def line_checker(list_square:list, line_size=20):
    line = []
    height = 420
    while height > 0:
        for item in list_square:
            if item.y == height:
                line.append(item)
        if len(line) >= 10:
            for i in line:
                for j in list_square:
                    if i == j:
                        list_square.remove(i)
            readjust_pieces(list_square, height)    
            return True 
        line.clear()
        height -= line_size  
    return False 
    
def move_inspector_left (block: Block, rect: Rect):
    block.Build()
    all_pieces = block.anchor, block.primary, block.secondary, block.tertiary
    for i in all_pieces:
        if i.left <= rect.left:
            return False
    return True
    
def move_inspector_right (block: Block, rect: Rect):
    block.Build()
    all_pieces = block.anchor, block.primary, block.secondary, block.tertiary
    for i in all_pieces:
        if i.right >= rect.right:
            return False
    return True 

def move_inspector_top (block: Block, rect: Rect):
    block.Build()
    all_pieces = block.anchor, block.primary, block.secondary, block.tertiary
    for i in all_pieces:
        if i.top <= rect.top:
            return False
    return True

def move_inspector_bottom (block: Block, rect: Rect):
    block.Build()
    all_pieces = block.anchor, block.primary, block.secondary, block.tertiary
    for i in all_pieces:
        if i.bottom >= rect.bottom:
            return False
    return True

def rotation_inspector (block: Block, rect: Rect):
    if block.type == HERO:
        return hero_next_rotation(block, rect)
    elif block.type == CLEVELANDZ or block.type == RHODE_ISLAND_Z:
        return clrhZ_next_rotation(block, rect)
    elif block.type == ORANGE_RICKY or block.type == BLUE_RICKY or block.type == TEWEE:
        return obZ_next_rotation(block, rect)
    else:
        return True  

def hero_next_rotation(block: Block, rect: Rect):
    if ((block.rotate == 'default' or block.rotate == 'second') and block.anchor.right >= rect.right - block.size * 2
        or block.anchor.top <= rect.top or block.anchor.bottom >= rect.bottom):
        return False
    return True

def clrhZ_next_rotation(block: Block, rect: Rect):
    for i in (block.anchor, block.primary):
        if (i.right >= rect.right or i.left <= rect.left or block.anchor.top <= rect.top or 
        block.anchor.bottom >= rect.bottom):
            return False
    return True

def obZ_next_rotation(block: Block, rect: Rect):
    if (block.anchor.left <= rect.left or block.anchor.right >= rect.right or block.anchor.top <= rect.top
        or block.anchor.bottom >= rect.bottom):
        return False
    return True

def equals_bottom(block: Block, rect: Rect):
    block.Build()
    all_pieces = block.anchor, block.primary, block.secondary, block.tertiary
    for i in all_pieces:
        if i.bottom == rect.bottom:
            return True
    return False

def blocksCollide(block: Block, rects_list: Dict[Rect, float]):
    block.Build()
    all_pieces = block.anchor, block.primary, block.secondary, block.tertiary
    for i in all_pieces:
        for rect in rects_list:
            if i.colliderect(rect) or (i.x == rect.x and i.bottom == rect.top):
                return True
    return False

def blockdivisor(block: Block):
    block.Build()
    all_pieces = block.anchor, block.primary, block.secondary, block.tertiary
    squares_list = []
    for i in all_pieces:
        squares_list.append(Rect(i.x, i.y, block.size, block.size))
    return squares_list
