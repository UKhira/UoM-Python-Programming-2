# Get the list of all keys
scores = {'Sunil':78, "Kamal":79, 'Kumara':56}
all_keys = list(scores.keys())
print(all_keys)




# Get the list of all values
all_values = list(scores.values())
print(all_values)


for key in scores:
    print(key, scores[key])                 #dic(x) = this means 'x' key of dic
                                            #dic[x] = this means value of the 'x' key of dic