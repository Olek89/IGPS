IGPS
====
That simulator is used to prove possibility of providing distributed calculation based on 
a simple communication protocol implemented in multihreading system based on Python. 
It also show how a valid architecture allows to build complex solutions based on script language.

The "Main.py" reads configuration file based on which a number of new nodes are created - 
- each having its own communication thread. On beacon signal received from the fake stimuli. 
In results nodes starts to communicate in between based on a TCP/IP and provides distributed calculations,
which are then combined into the result matrix.
