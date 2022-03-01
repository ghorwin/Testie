import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 128, 0)

# Call this function so the Pygame library can initialize itself
pygame.init()

clock = pygame.time.Clock()

# This sets the name of the window
pygame.display.set_caption('My first game')

# Create an 800x600 sized screen
size = [800, 600]
screen = pygame.display.set_mode(size)

# Joysticks/Gamepads
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
	# No joysticks!
	print("Error, I didn't find any joysticks.")
else:
	# Use joystick #0 and initialize it
	joystick = pygame.joystick.Joystick(0)
	joystick.init()
	print("Using {}".format(joystick.get_name()) )


# Current position
x_coord = 10
y_coord = 10

done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	# Bildschirm löschen		
	screen.fill(BLACK)
	
	if joystick_count != 0:
	
#		axes = joystick.get_numaxes()
#		print("Number of axes: {}".format(axes))
	
#		for i in range(axes):
#			axis = joystick.get_axis(i)
#			if (axis != 0):
#				print(screen, "  Axis {} value: {:>6.3f}".format(i, axis))
	
		buttons = joystick.get_numbuttons()
#		print(screen, "Number of buttons: {}".format(buttons))
	
		for i in range(buttons):
			button = joystick.get_button(i)
			if button != 0:
				print(screen, "  Button {:>2} value: {}".format(i, button))
	
#		hats = joystick.get_numhats()
#		print(screen, "Number of hats: {}".format(hats))
	
		# Hat position. All or nothing for direction, not a float like
		# get_axis(). Position is a tuple of int values (x, y).
#		for i in range(hats):
#			hat = joystick.get_hat(i)
#			if hat != (0,0):
#				print(screen, "  Hat {} value: {}".format(i, str(hat)))
			
		# This gets the position of the axis on the game controller
		# It returns a number between -1.0 and +1.0
		hat = joystick.get_hat(0)
		horiz_axis_pos = hat[0]
		vert_axis_pos = -hat[1]
	
		# Move x according to the axis. We multiply by 10 to speed up the movement.
		# Convert to an integer because we can't draw at pixel 3.5, just 3 or 4.
		x_coord = x_coord + int(horiz_axis_pos * 10)
		y_coord = y_coord + int(vert_axis_pos * 10)
	
	pygame.draw.rect(screen, ORANGE, [x_coord, y_coord, 45, 45])
	
	# Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
		
	clock.tick(60)
	
pygame.quit()

