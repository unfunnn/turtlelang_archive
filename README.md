# turtlelang
An esolang where you control a turtle
## Usage
Each position the turtle is on has a different function, for example the top left is print

You move the turtle with ^, <, >, and v

Currently, only the first 7 positions have any function to them

You execute any function with the @ key, and quit executing it to move again with the . key

## Obligatory Hello World Program
>@Hello World.

Or if you want to make it more complex

>\>@greeting|Hello.<v@greeting.^@ world.
## Other examples
Cat program
> v>@userinp.<@userinp.

Adds two numbers together
>\>v@R1.@R2.>>^@var["R1"]+var["R2"].

## Current instruction positions

>00 (top left corner): Print (format: @message.)

>01: Set variable (format: @variable_name|variable_contents.)

>02: Loop (format: @amount_of_times_to_loop|thing_to_loop.)

>03: Arithmetic (format: @sum.)
(It is worth noting for arithmetic that you can access variables by doing var["variable_name"] because of how it works)

>04: Random (format: @start_number|end_number.

>10: printing a variable (format: @variable_name.)

>11: input (format: @variable_to_store_input_in.)

Can you tell this is my first time using github

