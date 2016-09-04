''' Unit tests for the containers module. '''
import containers


print("\n\n~~~Unit tests for the containers.VirtualList class~~~")
print("Sample Values:")
base_sequence_1 = [2,4]
complete_sequence_1 = [2,4, 2,5, 3,4, 2,4, 8,7, 10,4]
marks_1 = [
	[1*len(base_sequence_1) + 1, 5],
	[2*len(base_sequence_1) + 0, 3],
	[4*len(base_sequence_1) + 0, 8],
	[4*len(base_sequence_1) + 1, 7],
	[5*len(base_sequence_1) + 0, 10]
	]
print("base_sequence_1 = ", base_sequence_1)
print("complete_sequence_1 = ", complete_sequence_1)
print("marks_1 = ", marks_1)

print("\n~~~Verify Instantiation~~~")
print("virtual_list_1 = containers.VirtualList(base_sequence_1)")
virtual_list_1 = containers.VirtualList(base_sequence_1)
print("type(virtual_list_1):", type(virtual_list_1))
print("virtual_list_2 = containers.VirtualList(base_sequence_1, marks_1)")
virtual_list_2 = containers.VirtualList(base_sequence_1, marks_1)
print("type(virtual_list_2):", type(virtual_list_2))

print("\n~~~Verify Length~~~")
print("len(virtual_list_1):", len(virtual_list_1))
print("len(virtual_list_2):", len(virtual_list_2))

print("\n~~~Verify Getting Unmarked Elements~~~")
print("virtual_list_1[0]:", virtual_list_1[0])
print("virtual_list_1[1]:", virtual_list_1[1])
print("virtual_list_2[0]:", virtual_list_2[0])
print("virtual_list_2[7]:", virtual_list_2[7])
print("virtual_list_2[11]:", virtual_list_2[11])

print("\n~~~Verify Getting Marked Elements~~~")
print("virtual_list_2[3]:", virtual_list_2[3])
print("virtual_list_2[8]:", virtual_list_2[8])
print("virtual_list_2[10]:", virtual_list_2[10])

print("\n~~~Verify Iteration and Contents~~~")
print("virtual_list_1:", [a for a in virtual_list_1])
print("virtual_list_2:", [a for a in virtual_list_2])

print("\n~~~Verify Setting a Mark~~~")
print("virtual_list_1[0] = 42")
virtual_list_1[0] = 42
print("virtual_list_1[0]:", virtual_list_1[0])
print("virtual_list_1:", [a for a in virtual_list_1])
print("virtual_list_2[1] = 52")
virtual_list_2[1] = 52
print("virtual_list_2[1]:", virtual_list_2[1])
print("virtual_list_2:", [a for a in virtual_list_2])

print("\n~~~Verify Overriding/Changing a Mark~~~")
print("virtual_list_1.marks:", virtual_list_1.marks)
print("virtual_list_1[0] = 21")
virtual_list_1[0] = 21
print("virtual_list_1[0]:", virtual_list_1[0])
print("virtual_list_1:", [a for a in virtual_list_1])
print("virtual_list_1.marks:", virtual_list_1.marks)
print("virtual_list_2.marks:", virtual_list_2.marks)
print("virtual_list_2[10] = 33")
virtual_list_2[10] = 33
print("virtual_list_2[10]:", virtual_list_2[10])
print("virtual_list_2:", [a for a in virtual_list_2])
print("virtual_list_2.marks:", virtual_list_2.marks)

print("\n~~~Verify to_index(self, iteration, position)~~~")
print(
	"virtual_list_1.to_index(0, 1) == 1:",
	virtual_list_1.to_index(0, 1) == 1
	)
print(
	"virtual_list_2.to_index(1, 1) == 3:",
	virtual_list_2.to_index(1, 1) == 3
	)

print("\n~~~Verify is_marked(self, iteration, position)~~~")
print(
	"virtual_list_1.is_marked(0, 0) (True):",
	virtual_list_1.is_marked(0, 0)
	)
print(
	"virtual_list_1.is_marked(0, 1) (False):",
	virtual_list_1.is_marked(0, 1)
	)
print(
	"virtual_list_2.is_marked(2, 0) (True):",
	virtual_list_2.is_marked(2, 0)
	)

print("\n~~~Verify value_at(self, iteration, position)~~~")
print(
	"virtual_list_1.value_at(0, 1) == 4 (True):",
	virtual_list_1.value_at(0, 1) == 4
	)
print(
	"virtual_list_2.value_at(5, 0) == 33 (True):",
	virtual_list_2.value_at(5, 0) == 33
	)
