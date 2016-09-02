class VirtualSequence(object):
    ''' Uses a base sequence (a type with index-accessable values) along
    with a system of marks to emulate a longer sequence of values. Longer
    sequences can potentially be stored in a fraction of the ammount of memory
    that would be needed to store the full sequence as a list.
    The longer sequence would consist of multiple iterations of the base
    sequence with some values deviating from the base sequence.
    Example:
        Suppose we have the two sequences s1 = [2,4] and s2 =  [2,4,3,4,2,5]
        Notice that s2 is just 3 iterations of s1, with 2 values changed:
            [2,4, 2,4, 2,4]
            [2,4, 3,4, 2,5]
        So, if we want to create a virtual sequence for s2, we could
        use s1 as the base sequence, and add the following marks:
            Mark 1) IterationIndex: 1, PositionIndex: 0, NewValue: 3
            Mark 2) IterationIndex: 2, PositionIndex: 1, NewValue: 5
    '''
    def __init__(self, base_sequence, marks):
        self.base_sequence = base_sequence
        self.marks = marks
        
    def __iter__(self):
        self.current_iteration = 0
        self.current_position = 0
        # TODO make this condition correct
        while True:
            # Past the last term in the base sequence
            if self.current_position >= len(self.base_sequence):
                # Loop to beginning
                self.current_position = 0
                self.current_iteration += 1
            # TODO make this check based on the max mark iteration & seq. length
            if self.current_iteration >= 9:
                break
            # Get the term
            yield self.value_at(self.current_iteration, self.current_position)
            # Proceed to next term
            self.current_position += 1
            
    def __getitem__(self, index):
        # TODO implement
        return -1
        
    def marked(self, iteration, position):
        ''' Determines if the specified location has mark(s) applied.
        
        Returns: True if the specified location is marked, False otherwise.
        '''
        # TODO finish implementing and update if/when self.marks is reformatted
        for mark in self.marks:
            if iteration == mark[0] and position == mark[1]:
                return True
        return False
        
    def value_at(self, iteration, position):
        ''' Get the value of the specified virtual series location. 
        If there are multiple marks at the same location, the last mark value
        is returned. If there are no marks, the value of the base series
        at the specified position is returned.
        '''
        result = self.base_sequence[position]
        for mark in self.marks:
            if iteration == mark[0] and position == mark[1]:
                result += mark[2] - result
        return result
        
    
class SumVirtualSequence(VirtualSequence):
    ''' A special type of virtual sequence where the marks indicate that the
    term after the mark in the sequence should be removed from the sequence
    and added to said marked term. Marks will need to be applied recursively.
    '''
    def __init__(self, base_sequence, marks):
        super(SumVirtualSequence, self).__init__(base_sequence, marks)
        
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
        # TODO finish implementing and update if/when self.marks is reformatted
        result = [self.base_sequence[position], 0]
        for mark in self.marks:
            if iteration == mark[0] and position == mark[1]:
               result[1] += 1
        return result


bs = [2,4]
s2_marks = [[1,0,3],[2,1,5]]
s2_sum_marks = [[1,0],[2,1]]
vs = VirtualSequence(bs, s2_marks)
i = 0
# print vs[0]
for value in vs:
    i += 1
    if i > 100:
        break
    print value