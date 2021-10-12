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
import basics.repetitions.for_loop.reverse as reverse
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
    elif response == "escape_characters":
        escape_characters.run()
    elif response == "ascii_art":
        ascii_art.run()
    elif response == "user_input":
        user_input.run()
    elif response == "ascii_robot":
        ascii_robot.run()
    elif response == "data_types":
        data_types.run()
    elif response == "string_operators":
        string_operators.run()
    elif response == "if_":
        if_.run()
    elif response == "if_else":
        if_else.run()
    elif response == "if_elif_else":
        if_elif_else.run()
    elif response == "modulo_operator":
        modulo_operator.run()
    elif response == "comparison_operators":
        comparison_operators.run()
    elif response == "counter":
        counter.run()
    elif response == "nested":
        nested.run()
    elif response == "nestception":
        nestception.run()
    elif response == "or_operator":
        or_operator.run()
    elif response == "and_operator":
        and_operator.run()
    elif response == "simple_while":
        simple_while.run()
    elif response == "count":
        count.run()
    elif response == "ascii":
        ascii.run()
    elif response == "length":
        length.run()
    elif response == "sum_100":
        sum_100.run()
    elif response == "sum_user_numbers":
        sum_user_numbers.run()
    elif response == "factorial":
        factorial.run()
    elif response == "simple_for":
        simple_for.run()
    elif response == "count_down":
        count_down.run()
    elif response == "range_file":
        range_file.run()
    elif response == "characters":
        characters.run()
    elif response == "reverse":
        reverse.run()
    elif response == "membership_operators":
        membership_operators.run()
    elif response == "nested_loop":
        nested_loop.run()
    elif response == "nesting":
        nesting.run()
    elif response == "ascii_code":
        ascii_code.run()
    elif response == "ascii_char":
        ascii_char.run()
    elif response == "simple_function":
        simple_function.run()
    elif response == "function_nest":
        function_nest.run()
    elif response == "function_para":
        function_para.run()
    elif response == "function_loop":
        function_loop.run()
    elif response == "function_paras":
        function_paras.run()
    elif response == "multiple_functions":
        mulitple_functions.run()
    elif response == "return_values":
        return_values.run()
    elif response == "function_calls":
        function_calls.run()
    elif response == "guess_the_number":
        guess_the_number.run()
    else:
        print("Error: File name not recognised")


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