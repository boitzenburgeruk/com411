import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.escape_characters as escape_characters
import basics.output.ascii_art as ascii_art
import basics.input.user_input as user_input
import basics.input.ascii_robot as ascii_robot
import basics.input.data_types as data_types
import basics.input.string_operators as string_operators
import basics.decisions.simple_decision.if_ as if_
import basics.decisions.simple_decision.if_else as if_else
import basics.decisions.simple_decision.if_elif_else as if_elif_else
import basics.decisions.simple_decision.modulo_operator as modulo_operator
import basics.decisions.simple_decision.comparison_operators as comparison_operators
import basics.decisions.simple_decision.counter as counter
import basics.decisions.nested_decision.nested as nested
import basics.decisions.nested_decision.nestception as nestception
import basics.decisions.or_operator as or_operator
import basics.decisions.and_operator as and_operator
import basics.repetitions.while_loop.simple as simple_while
import basics.repetitions.while_loop.count as count
import basics.repetitions.while_loop.ascii as ascii
import basics.repetitions.while_loop.len as length
import basics.repetitions.while_loop.sum_100 as sum_100
import basics.repetitions.while_loop.sum_user_numbers as sum_user_numbers
import basics.repetitions.while_loop.factorial as factorial
import basics.repetitions.for_loop.simple as simple_for
import basics.repetitions.for_loop.count_down as count_down
import basics.repetitions.for_loop.range as range_file
import basics.repetitions.for_loop.characters as characters
import basics.repetitions.for_loop.reverse
import basics.repetitions.for_loop.membership_operators as membership_operators
import basics.repetitions.nested_loop.nested as nested_loop
import basics.repetitions.nested_loop.nesting as nesting
import basics.functions.ascii_code as ascii_code
import basics.functions.ascii_character as ascii_char
import basics.functions.simple_function as simple_function
import basics.functions.function_with_nesting as function_nest
import basics.functions.function_with_parameter as function_para
import basics.functions.function_with_loop as function_loop
import basics.functions.function_with_parameters as function_paras
import basics.functions.multiple_functions as mulitple_functions
import basics.functions.return_values as return_values
import basics.functions.function_calls as function_calls
import basics.modules.guess_the_number as guess_the_number

def run_block_a():
    response = str(input("Which program in 'Block A: Basics' do you wish to run? "))
    if response == "simple_message":
        simple_message.run()
    elif response == "multiline_message":
        multiline_message.run()


def run():
    while True:
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if response == "a":
            run_block_a()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")


run()