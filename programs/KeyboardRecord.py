import keyboard

def rec():
	keys = keyboard.record(until = 'ENTER')
	keyboard.play(keys)
