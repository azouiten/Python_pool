languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

print("{}".format('\n'.join([str(elem)+" was created by "+languages[elem] for elem in languages.keys()])))