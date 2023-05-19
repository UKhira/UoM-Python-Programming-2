# adding an element
scores = {'Sunil':78, "Kamal":79, 'Kumara':56}
scores['Chamara'] = 56
print(scores)


# updating an element
scores['Kamal'] = 69            #Yhis will update Kamal's score 79 to 69
scores['Kumara'] += 12          #This will update Kumara's score by adding 12 to Kumara's initial mark(56+12=68)
print(scores)