#/usr/bin/env python

GREEN_COLOR = '\033[92m'
RED_COLOR = '\033[91m'
END_COLOR = '\033[0m'

class Machine(object):
    def __init__(self, states, alphabet, transitions, start, accept_states):
        """Constructor for this state machine. Do not invoke directly, instead
        use the from_arguments classmethod ie;

        >>> machine = Machine.from_arguments(states, alphabet, transitions, start, end)
        >>> machine.run()
        """

        self._states = states
        self._alphabet = alphabet
        self._transitions = transitions
        self._start = start
        self._accept_states = accept_states


    def run(self, input, console_output=True):
        """Takes an input string, and runs it against the machine's states,
        and transitions.

        Args:
            input -- the input string to test.

        Keyword Args:
            console_output -- Set this to False if you do not want
                to print to the console. (Defaults to True).

        Returns:
            A boolean representing if the input passes through the state machine
            and

        """
        if not isinstance(input, str):
            if console_output:
                print RED_COLOR + "Error: input is not a string" + END_COLOR

            return False

        current_state = self._start

        for value in input:
            # If the value doesn't exist in the alphabet, break.
            if value not in self._alphabet:
                break

            # Get the transitions available from the current state.
            transition_map = self._transitions.get(current_state)

            # If there are no transitions available from the current state,
            # break the run loop.
            if not transition_map:
                break

            # Get the next state.
            next_state = transition_map.get(value)

            # If there is no next state, or the next state isn't in the list of
            # available states, break.
            if not next_state or (next_state not in self._states):
                break

            # Otherwise, transition.
            current_state = next_state

        if current_state in self._accept_states:
            if console_output:
                print GREEN_COLOR + "PASS" + END_COLOR

            return True
        else:
            if console_output:
                print RED_COLOR + "FAIL" + END_COLOR
                acceptable_states_string = ''.join(self._accept_states)
                print "Ended with state: {0} with acceptable end states: {1}".format(
                    current_state,
                    acceptable_states_string
                )

            return False

    @classmethod
    def from_arguments(cls, states, alphabet, transitions, start, end):
        """Main classmethod for building a machine.

        Arguments:
            states - a list of states within the machine.
            alphabet - a list defining the language the machine speaks.
            transitions - a map of maps that define state transitions.
            start - a start state.
            end - a list of acceptable end states.

        Returns:
            A Machine instance. Call .run on it with an input against
            the machine.
        """
        assert isinstance(states, list), "States is not a list"
        assert isinstance(alphabet, list), "Alphabet is not a list"

        # Make sure the start state is valid.
        assert start in states, \
                "Start state {0} is not within defined states".format(start)

        # Make sure the accept states are valid.
        for accept_state in end:
            assert accept_state in states, \
                    "Accept state {0} is not within defined states".format(accept_state)

        assert isinstance(transitions, dict), "Transitions is not a dict"

        return cls(states, alphabet, transitions, start, end)
