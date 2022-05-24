import re
import os
import random

grid = [["pr", "se", "lo", "ar", "ra"],
        ["va", "null", "null", "null", "null"],
        ["null", "null", "null", "null", "null"],
        ["null", "null", "null", "null", "null"],
        ["null", "null", "null", "null", "null"]]
turtle_pos = "00"
prev_pos_list = []
current_instruction = None
output_str = ""
temp_list = ["", ""]
current_index = 0
draw = True
var = {}
final_string = ""
math_str = ""
debug_out = False
compiled_instruct = ""


def evaluate(instructions_to_eval):
    error = None
    if instructions_to_eval[0] not in "<>^v$@.":
        error = "1_NOT_RECOG"
    if re.match("@.*\.", instructions_to_eval) is False:
        error = "2_INVALID_SYNTAX"
    return error


def output():
    for row in output_grid:
        total_str = ""
        for pixel in row:
            total_str += pixel + " "
        print(total_str)


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


clearConsole()

print("turtlelang v0.2.5")
print("An esolang where you control a turtle and each position is an opcode")
print("Type \"help\" for help, \"exit\" to exit and \"open\" to open a .TURT file")

while True:
    instructions = input(">> " + "\033[1;35;40m")
    if instructions == "exit":
        print("\033[0;37;40m")
        quit(0)
    elif instructions == "help":
        print("Docs are still in writing")
    elif instructions == "open":
        file_path = input("File path:")
        with open(file_path) as f:
            lines = f.readlines()
        instructions = lines[0]
    elif instructions == "debug":
        if debug_out:
            debug_out = False
        else:
            debug_out = True
    elif instructions == "compile":
        print(compiled_instruct)
    else:
        if evaluate(instructions) is None:
            for instruction in instructions:
                if current_instruction is None:
                    if instruction == "$":
                        if draw:
                            draw = False
                        else:
                            draw = True

                    if instruction == ">":
                        if int(turtle_pos[1]) + 1 <= 4:
                            turtle_pos_x = int(turtle_pos[1]) + 1
                            turtle_pos_y = int(turtle_pos[0])
                            if draw:
                                prev_pos_list.append(turtle_pos)
                            turtle_pos = str(turtle_pos_y) + str(turtle_pos_x)
                        current_instruction = None
                    elif instruction == "<":
                        if int(turtle_pos[1]) - 1 >= 0:
                            turtle_pos_x = int(turtle_pos[1]) - 1
                            turtle_pos_y = int(turtle_pos[0])
                            if draw:
                                prev_pos_list.append(turtle_pos)
                            turtle_pos = str(turtle_pos_y) + str(turtle_pos_x)
                        current_instruction = None
                    elif instruction == "^":
                        if int(turtle_pos[0]) - 1 >= 0:
                            turtle_pos_x = int(turtle_pos[1])
                            turtle_pos_y = int(turtle_pos[0]) - 1
                            if draw:
                                prev_pos_list.append(turtle_pos)
                            turtle_pos = str(turtle_pos_y) + str(turtle_pos_x)
                        current_instruction = None
                    elif instruction == "v":
                        if int(turtle_pos[0]) + 1 <= 4:
                            turtle_pos_x = int(turtle_pos[1])
                            turtle_pos_y = int(turtle_pos[0]) + 1
                            if draw:
                                prev_pos_list.append(turtle_pos)
                            turtle_pos = str(turtle_pos_y) + str(turtle_pos_x)
                        current_instruction = None

                    elif instruction == "@":
                        current_instruction = grid[int(turtle_pos[0])][int(turtle_pos[1])]
                        if debug_out:
                            print("Current instruction set to", current_instruction)
                else:
                    if current_instruction == "pr":
                        if instruction != ".":
                            output_str += instruction

                        else:
                            final_string += output_str
                            if debug_out:
                                print("Instruction", current_instruction, "finished executing with output:", output_str)
                            output_str = ""
                            current_instruction = None

                    elif current_instruction == "se":
                        if instruction == "|":
                            current_index += 1
                        elif instruction == ".":
                            try:
                                temp_list[1] = int(temp_list[1])
                            except ValueError:
                                temp_list[1] = temp_list[1]
                            print(temp_list)
                            var[temp_list[0]] = temp_list[1]
                            if debug_out:
                                print("Instruction", current_instruction, "finished executing with output:",
                                      temp_list[0], "=",
                                      temp_list[1])
                            current_instruction = None
                            current_index = 0
                            temp_list = ["", ""]
                        else:
                            temp_list[current_index] += instruction

                    elif current_instruction == "lo":
                        if instruction == "|":
                            current_index += 1
                        elif instruction == ".":
                            for i in range(int(temp_list[0])):
                                final_string += temp_list[1]
                            if debug_out:
                                print("Instruction", current_instruction, "finished executing with output: looped",
                                      temp_list[1], temp_list[0], "times")
                            current_instruction = None
                            current_index = 0
                            temp_list = ["", ""]
                        else:
                            temp_list[current_index] += instruction
                    elif current_instruction == "ar":
                        if instruction == ".":
                            if debug_out:
                                print("Instruction", current_instruction, "finished executing with output:", math_str,
                                      "=",
                                      str(eval(math_str)))
                            current_instruction = None
                            final_string += str(eval(math_str))
                            math_str = ""
                        else:
                            math_str += instruction
                    elif current_instruction == "ra":
                        if instruction == ".":

                            if debug_out:
                                print("Instruction", current_instruction, "finished executing with output:")
                            current_instruction = None
                            final_string += str(random.randint(int(temp_list[0]), int(temp_list[1])))
                            temp_list = ["", ""]
                            current_index = 0
                        elif instruction == "|":
                            current_index += 1
                        else:
                            temp_list[current_index] += instruction
                    elif current_instruction == "va":
                        if instruction == ".":
                            final_string+=var[output_str]
                            output_str=""
                            current_instruction = None
                        else:
                            output_str+=instruction


            compiled_instruct += instructions
        else:
            print(evaluate(instructions))

    output_grid = [["⬜", "⬜", "⬜", "⬜", "⬜"],
                   ["⬜", "⬜", "⬜", "⬜", "⬜"],
                   ["⬜", "⬜", "⬜", "⬜", "⬜"],
                   ["⬜", "⬜", "⬜", "⬜", "⬜"],
                   ["⬜", "⬜", "⬜", "⬜", "⬜"]]

    for pos in prev_pos_list:
        output_grid[int(pos[0])][int(pos[1])] = "⬛"

    output_grid[int(turtle_pos[0])][int(turtle_pos[1])] = "▣"

    print("\033[0;37;40m" + final_string)

    output()
    final_string = ""
    print("")
