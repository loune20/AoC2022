# Code re-written from : https://aoc.just2good.co.uk/2022/18
from collections import deque
from dataclasses import dataclass

@dataclass(frozen=True)
class Cube():
	x: int
	y: int
	z: int
	# Generate deltas for face only (when 2 out of 3 dimensions are 0)
	adj_deltas = [(dx, dy, dz)
			for dx in range(-1, 1+1)
			for dy in range(-1, 1+1)
			for dz in range(-1, 1+1)
			if (dx, dy, dz).count(0) == 2]

	def adjacent(self): #return the six adjacent cubes in a set
		return {Cube(self.x+dx, self.y+dy, self.z+dz) for dx, dy, dz in Cube.adj_deltas}

@dataclass
class Droplet():
	adj_faces = 6
	filled_cubes: set[Cube] #???

	def __post_init__(self) -> None:
		#bounds
		self._min_x = self._min_y = self._min_z = 0
		self._max_x = self._max_y = self._max_z = 0
		self._all_surface_area: int=0 #internal & external surface area
		self._internal = set() #???
		self._external = set() #????

		self._calculate_values()

	@property
	def all_surface_area(self):
		return self._all_surface_area

	def __repr__(self):
		return(f"Droplet(filled_cubes={len(self.filled_cubes)})") #nombre de cubes "remplis"

	# Determine total surface area of all filled cube (positions) + outer boundaries
	def _calculate_values(self):
		for filled_cube in self.filled_cubes: #for every filled cube (=input data)
			#determine the intersection of its adjacents cubes with the filled cubes (if adj cubes exists in data)
			#those are adjacent faces : not to be counted in the surface area (substract their count from 6)
			self._all_surface_area += Droplet.adj_faces - len(self.filled_cubes & filled_cube.adjacent())

			self._min_x = min(filled_cube.x, self._min_x)
			self._min_y = min(filled_cube.y, self._min_y)
			self._min_z = min(filled_cube.z, self._min_z)
			self._max_x = max(filled_cube.x, self._max_x)
			self._max_y = max(filled_cube.y, self._max_y)
			self._max_z = max(filled_cube.z, self._max_z)

	#Determine surface area of all cubes that can reach the outside
	def get_external_surface_area(self):
		cubes_to_outside = set() #cache of cubes we know have a path to outside
		no_path_to_outside = set() #store all internal empty cubes
		surfaces_to_outside = 0

		#Loop through cubes (data) and find those that can reach outside
		for cube in self.filled_cubes:
			for adjacent in cube.adjacent(): #for each adjacent cube
				if self._has_path_to_outside(adjacent, cubes_to_outside, no_path_to_outside):
					cubes_to_outside.add(adjacent)
					surfaces_to_outside += 1
				else:
					no_path_to_outside.add(adjacent)
		return surfaces_to_outside

	# BFS flood fill from given empty cube
	# Caches cubes that we know have a path to outside and cube that we know are internal
	def _has_path_to_outside(self, cube:Cube, cubes_to_outside: set[Cube], no_path_to_outside: set[Cube]):
		frontier = deque([cube])
		explored = {cube}

		while frontier:
			current_cube = frontier.popleft()

			# Check caches
			if current_cube in cubes_to_outside:
				return True #we know there is a path from here
			if current_cube in no_path_to_outside:
				continue #the cube doesn't have a path, no use checking neighbours

			if current_cube in self.filled_cubes:
				continue #path is blocked

			# Check if path followed is outside bounds
			if current_cube.x > self._max_x or current_cube.y > self._max_y or current_cube.z > self._max_z:
				return True
			if current_cube.x < self._min_x or current_cube.y < self._min_y or current_cube.z < self._min_z:
				return True

			# We want to llok at all the neighbours of this empty space
			for neighbour in current_cube.adjacent():
				if neighbour not in explored:
					frontier.append(neighbour)
					explored.add(neighbour)

		return False


def parse_cubes(input: list[str]) -> set[Cube]:
	cubes = set()
	for line in input:
		coords = tuple(map(int, line.split(",")))
		cubes.add(Cube(*coords)) #asterix to unpack coords
	return cubes

# Main
with open("input2.txt") as f:
	data = f.read().splitlines()
	
droplet = Droplet(parse_cubes(data))


print(droplet)
print("Part 1 :", droplet.all_surface_area)
print("Part 2 :", droplet.get_external_surface_area())
