from typing import Callable, Iterator, Union, Optional, List, Type
from typing import List, Set, Dict, Tuple, Optional
import numpy as np
import pandas as pd

OptList = Type[List]
OptFloat = Type[Union[None, float]]
OptStr = Type[Union[None, str]]


class Point:
	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y

	def distCalc(self, second_point):
		return np.sqrt((self.x - second_point.x) ** 2 + (self.y - second_point.y) ** 2)


class RunOrtho:
	def __init__(self, start_point: Point, end_point: Point,
	             picks_list: List = None, ort_list: List = None, writen_length: float = None, type: str = None):
		'''
		Creates and calculates length and fixed picks (if given)
		'''
		self.sp = start_point
		self.ep = end_point
		self.picks_list = picks_list
		self.ort = ort_list
		self.true_pick_list = []  # true_pick_list
		self.writen_length = writen_length
		self.correction = []
		self.proportion = []
		self.coords = []
		self.coords_np = np.zeros((len(picks_list), 2))

		# Setting type
		if type == 'm' or type == 'link':
			self.t = ' (' + type + ')'
		elif type != None:
			self.t = None
			print("Wrong type of the measurement: m, link")

		self.dist = np.sqrt((self.sp.x - self.ep.x) ** 2 + (self.sp.y - self.ep.y) ** 2)

		# Fixing picks
		if isinstance(self.picks_list, list):
			if self.picks_list[-1] > self.dist:
				for pick in self.picks_list:
					self.proportion.append(0)
					self.correction.append(0)
					self.true_pick_list.append(pick)
			else:
				delta = self.dist - self.writen_length
				for pick in self.picks_list:
					self.proportion.append(pick / self.writen_length)
					self.correction.append(delta * self.proportion[-1])
					self.true_pick_list.append(pick + self.correction[-1])

		# Calculating distance
		self.dist = np.sqrt((self.sp.x - self.ep.x) ** 2 + (self.sp.y - self.ep.y) ** 2)

	def fixedPicksDfTable(self):

		return pd.DataFrame(
			columns=['Adj Forward' + self.t, 'Correction', 'Proportion', 'Side' + self.t, 'Forward' + self.t, 'Point'],
			data=list(zip(self.true_pick_list, self.correction, self.proportion,
			              self.ort, self.picks_list, range(1, len(self.picks_list) + 1))))

	def coordinates(self):
		angle = np.arctan2(self.ep.y - self.sp.y, self.ep.x - self.sp.x)
		for i, pick in enumerate(self.true_pick_list):
			if self.ort[i] < 0.0:
				x = self.sp.x + pick * np.cos(angle) + self.ort[i] * np.sin(angle)
				y = self.sp.y + pick * np.sin(angle) - self.ort[i] * np.cos(angle)
				self.coords.append(Point(x, y))
				self.coords_np[i, :] = np.array([x, y])
			else:
				x = self.sp.x + pick * np.cos(angle) + self.ort[i] * np.sin(angle)
				y = self.sp.y + pick * np.sin(angle) - self.ort[i] * np.cos(angle)
				self.coords.append(Point(x, y))
				self.coords_np[i, :] = np.array([x, y])
		return self.coords, self.coords_np
