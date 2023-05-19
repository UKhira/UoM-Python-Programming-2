#Let's find out when list has duplication values how can we find the count of each unique values repeated by using a dictionary
Names = ['Amal', 'Kamal', 'Sunil', 'Saman', 'Amal', 'Amal', 'Saman', 'Nimal', 'Kamal', 'Ajith', 'Kamal', 'Saman', 'Nimal', 'Kamal', 'Sunil', 'Sarath']

# Create an empty dictionary
count = dict()

for name in Names :                 # Iterate through thr Names list
    if name not in count:           # Checking if the name is already in count dict
        count[name] = 1             # Add new element to count dict with value 1
    else:
        count[name] += 1            # Increment value by one if name is already in count dict

print(count)                        #finally print the count dict