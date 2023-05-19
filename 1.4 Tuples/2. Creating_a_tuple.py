tuple_1 = (1, 'a', 2.34)                    # Tuple is like list, can store various type of data in it
print('tuple_1 :',type(tuple_1))

tuple_2 = 2, 'b', 5.2           # No parentheses
print('tuple_2: ',type(tuple_2))
print(tuple_2)                  # System will automatically add parentheses in output


# Tuple with a single element is a special case
tuple_3 = ('g')
print('tuple_3: ',type(tuple_3))            # Though we needed this to be a tuple system will take this as a string

# This is how to create a touple with single element
tuple_4 = ('g',)                            # Must include a comma at the end
#or
tuple_5 = "g",

print('tuple_4: ',type(tuple_4),'\ntuple_5: ',type(tuple_5))