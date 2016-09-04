from sys import version_info

assert version_info[0] == 3


class VirtualList(object):
    ''' Uses a base sequence (a type with index-accessable values) along
    with a system of marks to emulate a longer sequence of values. Longer
    sequences can potentially be stored in a fraction of the ammount of memory
    that would be needed to store the full sequence as a list.
    The longer sequence would consist of multiple iterations of the base
    sequence with some values deviating from the base sequence.
    ~~~~~~~~~~~~~~~~
    Example:
        Suppose we have the two sequences s1 = [2,4] and s2 =  [2,4,3,4,2,5]
        Notice that s2 is just 3 iterations of s1, with 2 values changed:
            [2,4, 2,4, 2,4]
            [2,4, 3,4, 2,5]
        So, if we want to create a virtual sequence for s2, we could
        use s1 as the base sequence, and add the following marks:
            Mark 1) IterationIndex: 1, PositionIndex: 0, NewValue: 3
            Mark 2) IterationIndex: 2, PositionIndex: 1, NewValue: 5
    ~~~~~~~~~~~~~~~~
    Arguments:
        base_sequence
            The sequence used as the repeating base pattern for the series.
            Changes made to base_sequence will be reflected in the virtual
            list, except inserting, appending, deleting, and so on will
            cause undetermined behavior.
        (optional) marks
            Any value changes to make initially to the virtual list.
    '''
    def __init__(self, base_sequence, marks=None):
        # The repeating pattern underlaying the virtual list
        self.base_sequence = base_sequence
        # The marks indicating changes in values
        self.marks = {}
        # Stored for optimization purposes
        self.iterations_of_base = 1
        # Add initial marks
        if marks is not None:
            for m in marks:
                self[m[0]] = m[1]
            
    def __len__(self):
        return self.iterations_of_base * len(self.base_sequence)

    def __getitem__(self, key):
        if type(key) is not int:
            raise TypeError
        elif key >= len(self):
            raise IndexError
        else:
            return self.marks.get(
                key, self.base_sequence[key % len(self.base_sequence)]
                )

    def __setitem__(self, key, value):
        if type(key) is not int:
            raise TypeError
        else:
            self.marks[key] = value
            self.iterations_of_base = max(
                self.iterations_of_base,
                1 + (key // len(self.base_sequence))
                )

    def __delitem__(self, key):
        # TODO implement
        pass

    def __iter__(self):
        return (self[i] for i in range(len(self)))

    def to_index(self, iteration, position):
        ''' Convert an iteration and position into an index value. This 
        function will not account for or skip elements marked DELETED.
        ~~~~~~~~~~~~~~~~
        Arguments:
            iteration
                The number of preceeding iterations (meaning 
                iteration = 0 would be in the first base sequence iteration.)
            position
                The index within the base sequence.
        ~~~~~~~~~~~~~~~~
        Returns:
            The index value corresponding to the input arguments.
        '''
        return iteration * len(self.base_sequence) + position

    def is_marked(self, iteration, position):
        ''' Checks if there is a mark for the given arguments.
        ~~~~~~~~~~~~~~~~
        Arguments:
            iteration
                The number of preceeding iterations (meaning 
                iteration = 0 would be in the first base sequence iteration.)
            position
                The index within the base sequence.
        '''
        return self.to_index(iteration, position) in self.marks
        
    def value_at(self, iteration, position):
        ''' Get the value given the base sequence iteration and position. '''
        return self.marks.get(self.to_index(iteration, position), self[position])
        
    
class SumVirtualList(VirtualList):
    ''' A type of virtual list where a marked term is combined with the next
    element(s) in the sequence, effectively equivalent to the following
    operations on a non-virtual list:
        a_list = [2, 3, 4, 5]  # a_list[2] is the marked element
        a_list[2] += a_list.pop(2 + 1)  # next element
    '''
    def __init__(self, base_sequence, marks=None):
        super().__init__(base_sequence, marks)
        
    def __iter__(self):
        self.current_iteration = 0
        self.current_position = 0
        while True:
            next_position = self.current_position + 1
            result = 0
            if self.marked(self.current_iteration, self.current_position):
                temp = self.value_at(self.current_iteration, self.current_position)
                result += temp[0]
                next_position += temp[1]
            # Get the term
            yield result
            # Proceed to next term
            self.current_position = next_position
            # Previous term is the last term in the sequence
            if next_position >= len(self.base_sequence):
                # Loop to beginning
                self.current_position = 0
                self.current_iteration += 1
            # Proceed to next term in sequence
            else:
                self.current_position = next_position
            # TODO make this check based on the max mark iteration & seq. length
            if self.current_iteration >= 9:
                break
                
    def __getitem__(self, index):
        # TODO implement
        return -1
        
    def value_at(self, iteration, position):
        ''' Calculates the value of the specified virtual location.
        
        Returns:
            A 2-element list; element 0 is the resulting value, element 1
            is the number of terms traversed (always at least one when there
            are marks applied to the specified location.)
        '''
        result = [super().value_at(iteration, position), 0]
        # TODO implement
        return result
