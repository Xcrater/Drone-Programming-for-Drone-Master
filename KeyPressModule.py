import pygame

def init():
    pygame.init()
    window = pygame.display.set_mode((500,500)) 

# Get 'key press' status of keys '<--', '-->' etc.
def getKey(keyName):
    ans = False
    for event in pygame.event.get(): pass
    
    #Get the keyboard status
    keyboardStatus = pygame.key.get_pressed()

    #This will return key constants like 'K_a' ,'K_TAB' etc.
    myKey = getattr(pygame, 'K_{}'.format(keyName))

    if keyboardStatus[myKey]:
        ans = True

    #update the pygame screen
    pygame.display.update()
    return ans

def main():
    # Print the status of 'w'
    """"
    print(getKey("w"))
    if getKey("LEFT"):
        print("Left Key is Pressed")

    if getKey("RIGHT"):
        print("Right key is pressed")
    """

if __name__ == '__main__':
    init()
    while True:
        main() 
