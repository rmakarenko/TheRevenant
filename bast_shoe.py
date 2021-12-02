current_string = ''
current_position = 0
current_state = []
undo_done = 0
possible_undo = 0
possible_redo = 0
undo_chain = 0
lastUndo = False

def BastShoe(command):

    global current_string
    global current_position
    global current_state
    global undo_done
    global possible_undo
    global possible_redo
    global undo_chain
    global lastUndo

    if command.split(' ')[0] == '1' and len(command.split(' ')) > 2:  # here in this block user input is handled and operations are performed

        for i in range(1, len(command.split(' ')) - 1):  # adding splitted by spacebars parts of the input command
            current_string = current_string + command.split(' ')[i] + ' '
        current_string = current_string + command.split(' ')[len(command.split(' ')) - 1]  # last element will not have spacebar after it

        current_state.append(current_string)
        current_position = len(current_state) - 1
        #undo_done = 0
        # possible_undo = possible_undo + 1
        possible_redo = 0

        if not lastUndo:  # if lastUndo == False we will add 1 to the undoChain
            undo_chain = undo_chain + 1
        else:
            undo_chain = 1

        lastUndo = False

        return current_string

    elif command.split(' ')[0] == '1' and len(command.split(' ')) == 2:  # here in this block user input is handled and operations are performed

        current_string = current_string + command.split(' ')[1]
        current_state.append(current_string)
        current_position = len(current_state) - 1
        #undo_done = 0
        # possible_undo = possible_undo + 1
        possible_redo = 0

        if not lastUndo:  # if lastUndo == False we will add 1 to the undoChain
            undo_chain = undo_chain + 1
        else:
            undo_chain = 1

        lastUndo = False

        return current_string

    elif command.split(' ')[0] == '2' and len(current_string) - int(command.split(' ')[1]) > 0:  # operation 2

        buffered_string = current_string
        current_string = ''
        for i in range(len(buffered_string) - int(command.split(' ')[1])):
            current_string = current_string + buffered_string[i]
        current_position = current_position + 1
        current_state.append(current_string)
        # undo_done = 0
        # possible_undo = possible_undo + 1

        if not lastUndo:  # if lastUndo == False we will add 1 to the undoChain
            undo_chain = undo_chain + 1
        else:
            undo_chain = 1

        lastUndo = False

        return current_string

    elif command.split(' ')[0] == '2' and (len(current_string) - int(command.split(' ')[1]) <= 0):  # operation 2, returning empty string

        current_string = ''
        current_position = current_position + 1
        current_state.append(current_string)
        # undo_done = 0
        # possible_undo = possible_undo + 1

        if not lastUndo:  # if lastUndo == False we will add 1 to the undoChain
            undo_chain = undo_chain + 1
        else:
            undo_chain = 1

        lastUndo = False

        return current_string

    elif command.split(' ')[0] == '3' and int(command.split(' ')[1]) < len(current_string) and int(command.split(' ')[1]) >= 0  :  # operation 3
        return current_string[int(command.split(' ')[1])]
    elif command.split(' ')[0] == '3' and (int(command.split(' ')[1]) < len(current_string) or int(command.split(' ')[1]) >= 0):  # operation 3
        return ''

    elif command.split(' ')[0] == '4' and current_position > 0 and undo_chain > 0:  # operation 4, undo
        current_position = current_position - 1
        current_string = current_state[current_position]
        undo_done = undo_done + 1
        undo_chain = undo_chain - 1
        lastUndo = True

        return current_string

    elif command.split(' ')[0] == '4' and current_position > 0 and undo_chain == 0:  # operation 4, undo nothing to undo
        lastUndo = True
        return current_string

    elif command.split(' ')[0] == '4' and current_position == 0 and undo_chain > 0:  # operation 4, undo, when position is 0
        current_position = current_position
        current_string = ''
        undo_done = undo_done + 1
        undo_chain = undo_chain - 1
        lastUndo = True
        return current_string

    elif command.split(' ')[0] == '4' and current_position == 0 and undo_chain == 0:  # operation 4, undo, undo nothing to undo
        lastUndo = True
        return current_string

    elif command.split(' ')[0] == '5' and undo_done <= 0:  # operation 5, redo. undo_done <=0, so nothing we need to do except returning current string,

        return current_string

    elif command.split(' ')[0] == '5' and undo_done > 0 and current_position < len(current_state) - 1:  # operation 5, redo and position is not last
        current_position = current_position + 1
        current_string = current_state[current_position]
        undo_done = undo_done - 1
        undo_chain = undo_chain + 1
        return current_string

    elif command.split(' ')[0] == '5' and undo_done > 0 and current_position == len(current_state) - 1:  # operation 5, redo and position is last

        undo_chain = undo_chain + 1
        undo_done = undo_done - 1
        return current_string
    else:
        return current_string
