import pygame
import random
import tkinter as tk
from tkinter import messagebox
from mode_2.snake2 import Snake2
from mode_2.cube import Cube
import sys

sys.path.insert(1, 'mode_2/snake2.py')
sys.path.insert(1, 'mode_2/Cube.py')
rows = 20


class Mode2:
  def __init__(self, game):
    self.game = game
    self.s = Snake2((255, 0, 0), (10, 10))
    self.snack = Cube(self.random_snack(rows, self.s), color=(0, 255, 0))
    self.s.reset((10, 10))
    self.game_over = False

  def draw_grid(self, w, rows, surface):
      size_btw = w // rows
      x = 0
      y = 0
      for i in range(rows):
          x += size_btw
          y += size_btw
          pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
          pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

  def redraw_window(self, surface):
      global rows, width
      surface.fill((0, 0, 0))
      self.s.draw(surface)
      self.snack.draw(surface)
      self.draw_grid(width, rows, surface)
      pygame.display.update()

  def random_snack(self, rows, item):
      positions = item.body

      while True:
          x = random.randrange(rows)
          y = random.randrange(rows)
          if len(list(filter(lambda z: z.pos == (x, y), positions))):
              continue
          else:
              break
      return x, y

  def message_box(self, subject, content):
      root = tk.Tk()
      root.attributes("-topmost", True)
      root.withdraw()
      messagebox.showinfo(subject, content)
      try:
          root.destroy()
      except:
          pass

  def main(self):
      global width, test
      width = 500
      test = True
      pygame.display.init()
      ecran = pygame.display.set_mode((width, width),)
      #s = Snake2((255, 0, 0), (10, 10))
      #snack = Cube(self.random_snack(rows, s), color=(0, 255, 0))
      flag = True
      clock = pygame.time.Clock()
      score = 0

      while flag:
          pygame.time.delay(70)
          clock.tick(35)
          self.s.move()
          if self.s.body[0].pos == self.snack.pos:
              self.s.add_cube()
              score += 1
              self.snack = Cube(self.random_snack(rows, self.s), color=(0, 255, 0))

          for x in range(len(self.s.body)):
            if self.s.body[x].pos in list(map(lambda z: z.pos, self.s.body[x + 1:])):
              self.message_box("You lost!", "You scored " + str(score) + " points")
              self.s.reset((10, 10))
              Cube.__new__(Cube)
              self.game.__init__()
              break

          self.redraw_window(ecran)
