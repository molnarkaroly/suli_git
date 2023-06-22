import xml.etree.ElementTree as ET
import os

def change_lives_value(benum, karnev):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, f'{karnev}Arcade.xml')
    tree = ET.parse(file_path)
    root = tree.getroot()
    player = root.find('player')
    lives = player.find('lives')
    lives.set('value', str(benum))
    tree.write(file_path)
