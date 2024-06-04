def parser(input):
    """
    :type input: file
    :rtype: string:tape1,tape2 
    """
    with open(input, 'r',encoding='utf-8') as file:
        for line in file:

            if '#' in line:
                parts = line.split('#')
 
                tape1 = ['B'] + list(parts[0].strip()) + ['B']

                tape2 = ['B'] + list(parts[1].strip()) + ['B']
            
            else:
                tape1 = ['B'] + list(line) + ['B']
                tape2 = ['B'] * len(tape1)

        return tape1,tape2
    
def TM(tape1,tape2,transitions):

    state = 'qS'
    final = 'qF'

    head1 = 0
    head2 = 0


    file =open('steps.txt', 'w')

    while state != final:

        symbol1 = tape1[head1]
        symbol2 = tape2[head2]

        if (state, symbol1, symbol2) in transitions:
            new_symbol1,new_symbol2,direction1,direction2,new_state = transitions[(state, symbol1, symbol2)]
        else:
            return "Rejected"

        tape1[head1] = new_symbol1
        tape2[head2] = new_symbol2
        
        if direction1 == 'R':
            head1 += 1
        elif direction1 == 'L':
            head1 -= 1
        elif direction1 == 'S':
            pass

        if direction2 == 'R':
            head2 += 1
        elif direction2 == 'L':
            head2 -= 1
        elif direction2 == 'S':
            pass

        file.write(
            f"""
State {state}
Tape1 : Symbol {symbol1} -> New Symbol {new_symbol1}, Direction {direction1}, Postion {head1-1} -> new Postion {head1}
Tape2 : Symbol {symbol2} -> New Symbol {new_symbol2}, Direction {direction2}, Postion {head2-1} -> new Postion {head2}
New State {new_state}
Tape1:
{str(tape1)}
Tape2:
{str(tape2)}
            """)
        
        state = new_state

    file.close()    
    return "Accepted"




input = "TM.txt"
tape1,tape2 = parser(input)

transitions={

    ('qS', 'B', 'B'): ('B', 'B', 'R', 'R', 'q0'),

    # # 2 is substring of 1
    
    # ('q0', '0', '1'): ('0', '1', 'R', 'S', 'q0'),
    # ('q0', '1', '0'): ('1', '0', 'R', 'S', 'q0'),

    # ('q0', '0', '0'): ('0', '0', 'R', 'R', 'q1'),
    # ('q0', '1', '1'): ('1', '1', 'R', 'R', 'q1'),
    
    # ('q1', '0', '0'): ('0', '0', 'R', 'R', 'q1'),
    # ('q1', '1', '1'): ('1', '1', 'R', 'R', 'q1'),
    
    # ('q1', '0', '1'): ('0', '1', 'S', 'L', 'q2'),
    # ('q1', '1', '0'): ('1', '0', 'S', 'L', 'q2'),

    # ('q1', '0', 'B'): ('0', 'B', 'R', 'B', 'qF'),
    # ('q1', '1', 'B'): ('1', 'B', 'R', 'B', 'qF'),
    # ('q1', 'B', 'B'): ('B', 'B', 'L', 'L', 'qF'),

    # ('q2', '0', '1'): ('0', '1', 'S', 'L', 'q2'),
    # ('q2', '1', '0'): ('1', '0', 'S', 'L', 'q2'),
    # ('q2', '0', '0'): ('0', '0', 'S', 'L', 'q2'),
    # ('q2', '1', '1'): ('1', '1', 'S', 'L', 'q2'),

    # ('q2', '0', 'B'): ('0', 'B', 'S', 'R', 'q0'),
    # ('q2', '1', 'B'): ('1', 'B', 'S', 'R', 'q0'),
    
    # # Palindrome
    # ('q0', '0', 'B'): ('0', '0', 'R', 'R', 'q0'),
    # ('q0', '1', 'B'): ('1', '1', 'R', 'R', 'q0'),

    # ('q0', 'B', 'B'): ('B', 'B', 'L', 'L', 'q1'),

    # ('q1', '1', '1'): ('1', '1', 'L', 'S', 'q1'),
    # ('q1', '1', '0'): ('1', '0', 'L', 'S', 'q1'),
    # ('q1', '0', '1'): ('0', '1', 'L', 'S', 'q1'),
    # ('q1', '0', '0'): ('0', '0', 'L', 'S', 'q1'),

    # ('q1', 'B', '1'): ('B', '1', 'R', 'S', 'q2'),
    # ('q1', 'B', '0'): ('B', '0', 'R', 'S', 'q2'),

    # ('q2', '1', '1'): ('1', '1', 'R', 'L', 'q2'),
    # ('q2', '0', '0'): ('0', '0', 'R', 'L', 'q2'),

    # ('q2', 'B', 'B'): ('B', 'B', 'L', 'R', 'qF'),

    # 0^n 1^n
    ('q0', '0', 'B'): ('0', '0', 'R', 'R', 'q0'),
    ('q0', '1', 'B'): ('1', 'B', 'S', 'L', 'q1'),

    ('q1', '1', '0'): ('1', '0', 'R', 'L', 'q1'),

    ('q1', 'B', 'B'): ('B', 'B', 'L', 'R', 'qF'),



}

print(TM(tape1,tape2,transitions))