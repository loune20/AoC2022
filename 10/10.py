#https://aoc.just2good.co.uk/2022/10
data = []
with open("input.txt") as input:
    data = input.read().splitlines()

class CrtComputer():
    DISPLAY_WIDTH = 40
    DISPLAY_HEIGHT = 6
    LIT = "#"

    def __init__(self, instructions):
        self._x = 1 #CPU register
        self._instructions = self._convert_to_instructions(instructions)
        self._ip = 0 #instruction pointer
        self.cycle = 0
        self._doing = [] #list of the instruction being done + its duration
        self.running_program = True #false when instructions are complete
        self._display_posn = [0,0]
        self._display = [[" " for _  in range(CrtComputer.DISPLAY_WIDTH)]
                            for _ in range(CrtComputer.DISPLAY_HEIGHT)]

    @property
    def x(self):
        return self._x
    
    @property
    def signal_strength(self):
        return self.cycle * self.x

    def _convert_to_instructions(self, data):
        instructions = []
        for i in data:
            line_words = i.split()
            instr = line_words[0]
            val = None
            if len(line_words) >1:
                val = int(line_words[1])
            instructions.append((instr, val))
        return instructions

    def tick(self): #One CPU cycle
        #print(self)
        if len(self._doing) > 0: #instruction is being processed
            self._doing[1] -= 1
            if self._doing[1] == 0: #complete the running instruction
                instruction = self._doing[0]
                self.__getattribute__(f"_op_{instruction[0]}")(instruction)
                #print(f"Completed instruction: {instruction}")

                self._start_next_instruction() #and start the next one
        else: #this is the first instruction
            self._start_next_instruction()
        self._update_display()
        self.cycle += 1

    def _start_next_instruction(self): #call the appropriate implementation methode for an instruction
        instruction = self._instructions[self._ip]
        #print(f"Starting instruction: {instruction}")
        if instruction[0] == "addx":
            self._doing = [instruction, 2]
        elif instruction[0] == "noop":
            self._doing = [instruction, 1]
        self._ip += 1 #increment instruction pointer
        if self._ip == len(self._instructions): #finished
            self.running_program = False

    def _op_addx(self, instruction):
        self._x += instruction[-1]

    def _op_noop(self, _):
        pass
        #takes one cycle, but does nothing

    def render_display(self):
        return("\n".join("".join(row) for row in self._display))

    def _update_display(self):
        x_posn = self._display_posn[0] #current horizontal pixel position
        if x_posn in range(self.x-1, self.x+2): #if horizontal position within sprite position
            self._display[self._display_posn[1]][x_posn] = CrtComputer.LIT

        if x_posn<CrtComputer.DISPLAY_WIDTH-1: #display position across row, then down, one pixel at a time each tick
            self._display_posn[0] += 1
        else:
            self._display_posn[0] = 0
            self._display_posn[1] += 1

    def __repr__(self):
        return(f"{self.__class__.__name__}(Cycle={self.cycle};x={self._x},pixel={self._display_posn})")

interesting_cycles = [20, 60, 100, 140, 180, 220]
signal_strength_sum = 0
crt_computer = CrtComputer(data)
while crt_computer.running_program:
    crt_computer.tick()
    if crt_computer.cycle in interesting_cycles:
        signal_strength_sum += crt_computer.signal_strength
    
print("Partie 1 :",signal_strength_sum)
print(f"Part 2:\n{crt_computer.render_display()}")