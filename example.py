#/usr/bin/env python

from fsm import Machine

states = ["q1", "q2", "q3"]
alphabet = ["0","1"]

transitions = {
    "q1": {"0": "q1", "1": "q2"},
    "q2": {"0": "q3", "1": "q2"},
    "q3": {"0": "q2", "1": "q2"},
}

start = "q1"
end = ["q2"]

machine = Machine.from_arguments(states, alphabet, transitions, start, end)

machine.run(123) # fail
machine.run("") # fail
machine.run("1") # pass
machine.run("11") # pass
machine.run("0100101") # pass
