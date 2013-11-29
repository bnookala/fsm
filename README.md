# FSM

A quick and dirty implementation of a deterministic finite state machine.

## Quick Example

	from fsm import Machine

	# Define states, alphabet, transitions, start, and end

	machine = Machine.from_arguments(states, alphabet, 	transitions, start, end)
	ret_value = machine.run(some_input)

… or check out example.py in the root level directory.

## Documentation

### from_arguments
A **class method**, that returns a Machine instance. Use this to construct a Machine instance.

##### Arguments:  
-  **states**: a list of possible states for the Machine. Each state is a unique string.  
-  **alphabet**: a list of possible "choices" for each state. Each "letter" is a unique string. 
-  **transitions** - a dict that maps to dicts. Each key is a state. The dict that the key maps to is keyed by an alphabet letter, and maps to the next state:

		transitions = {
			'some_state': {
				'a': 'next_state', 
				'b': 'previous_state'
			},
		}
- **start** - a state to start the machine at.
- **end** - a list of acceptable end states.

##### Returns:
An instance of the state machine.

### run
An **instance** method, that runs an input on the machine instance.

##### Arguments:
**input** - a string input to run the Machine instance on.

##### Keyword Arguments:
**console_output** - Set this to False if you do not want to print to the console. (Defaults to True).

##### Returns:
A boolean indicating if the string passed or failed on the machine instance.
