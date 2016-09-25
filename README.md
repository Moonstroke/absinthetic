# Absinthetic
## Array-based esolang

Absinthetic is a *portmanteau word* between *Absinthe* (a green shade, of hex code `#88C641`) and *synthetic*, which is one characteristic of the language.

Absinthetic is somehow influenced by others languages, mostly [`Python`](https://www.python.org/) and [`O5AB1E`](https://github.com/Adriandmen/05AB1E).  
It is written in Python3 and is currently ***absolutely not complete***.

## Syntax

There is a single varaible, called the *retenue*, that stores the return value of the previous command.

Each character is a single command, like most esolangs. It uses `UTF-8` encoding.  
These commands are:  

    ? input
    ¿ input and allow empty input (in that case push 0)
    ! print retenue or the adressed value / cat if retenue is empty
    ¡ print and set element to 0 (pop)
    _ push the retenue in the array
    < index --
    > index ++
    $ return value of the adress
    @ return adress of the index
    # convert string -> integer
    b bin string
    o oct string
    d decimal string (int -> string)
    h hex string
    ŀ split string into chars / 
    ± numeric opposite of retenue
    + sum                 of retenue and adressed value
    - difference          "     "     "      "      "
    × product             "     "     "      "      "
    ∕ floor div           "     "     "      "      "
    % remainder           "     "     "      "      "
    ` power               "     "     "      "      "
    « bitwise left shift  "     "     "      "      "
    » bitwise right shift "     "     "      "      "
    & bitwise AND         "     "     "      "      "
    | bitwose OR          "     "     "      "      "
    ^ bitwise XOR         "     "     "      "      "
    ¬ bitwise negation of retenue
    √ retenue-th or square root of adressed value
    ° 10 power retenue
    ² 2 power retenue
    ø null value (reset retenue)
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9 that digit (supports multi-digits integers)
    
