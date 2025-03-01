# SAE S1.02  COMMUNITY DETECTION #

# Module contenant les fonctions #

from test_community_detection import *

dico = {
  "Alice" : ["Bob", "Dominique"],
  "Bob" : ["Alice", "Charlie", "Dominique"],
  "Charlie" : ["Bob"],
  "Dominique" : ["Alice", "Bob"]
}

list_of_friends = ["Alice", "Bob","Dominique","Alice","Bob","Charlie","Dominique","Bob"]


# Question 1 #

def create_network(list_of_friends):

    ''' La fonction create_network est une fonction qui renvoie un dictionnaire avec les couples d'amis
    du tableau list_of_friends.'''

    dico = {} # dictionnaire vide
    i = 0
    while i < len(list_of_friends): # parcourir tous les éléments du tableau list_of_friends
        if i % 2 == 0 :
            if list_of_friends[i] in dico:
                dico[list_of_friends[i]].append(list_of_friends[i+1])
            elif list_of_friends[i] not in dico:
                dico[list_of_friends[i]] = [list_of_friends[i+1]]
        elif i % 2 == 1:
            if list_of_friends[i] in dico:
                dico[list_of_friends[i]].append(list_of_friends[i-1])
            elif list_of_friends[i] not in dico:
                dico[list_of_friends[i]] = [list_of_friends[i-1]]
        i += 1
    return dico

o = create_network(list_of_friends)
#print(o)


# Question 3 #

def get_people(network):

    ''' La fonction get-people est une fonction qui renvoie un tableau avec la liste
    des personnes dans le cercle de réseau d'un tableau.'''

    liste = [] # tableau vide
    i = 0
    while i < len(network): # parcourir le tableau network
        if network[i] not in liste :
            liste.append(network[i])
        i += 1
    return liste

p = get_people(list_of_friends)
#print(p)


# Question 4 #

def are_friends(network, person1, person2):

    ''' La fonction are_friends est une fonction qui retourne True si deux personnes
    (person1 et person2) sont amis, et retourne False sinon.'''

    if person2 in network[person1]: # parcourir le cercle d'amis de person1 afin de savoir si person2 en fait partis
        return True # si oui la fonction retourne True
    return False # sinon la fonction retourne False


q = are_friends(list_of_friends, "Alice", "Charlie")
#print(q)


# Question 5 #

def all_his_friend(network, person, group):

    ''' La fonction all_his_friend est une fonction qui retourne True si une personne
    est amie avec toutes les personnes du groupe et False sinon.'''

    for i in range(len(group)): # parcourir le tableau group
        if group[i] not in network[person]: # chercher si la personne est amie avec toutes les personnes du groupe
            return False # si non, la fonction retourne False
    return True # si oui, la fonction retourne True

r = all_his_friend(list_of_friends, "Alice", dico)
#print(r)


# Question 6 #

def is_a_community(network, group):

    ''' La fonction is_a_community est une fonction qui retourne True si le groupe est
    une communauté et False sinon.'''

    for l in range(len(group)):
        for i in range(len(group)):
            if group[i] not in network[group[l]] and group[l] != group[i]:
                return False
    return True

s = is_a_community()
#print(s)


# Question 7 #

def find_community(network, group):

    ''' La fonction find_community est une fonction qui retourne une communauté
    en partant  d'une communauté vide'''

    community = []
    t = []
    for i in range(len(group)):
        t.append(group[i])

        if is_a_community(network,t):
            community.append(group[i]) #Ajout de la personne dans le tableau

        elif not is_a_community(network, t):
            t.pop()

    return community

t = find_community()
#print(t)


# Question 8 #

def order_by_decreasing_popularity(network):

    '''"Paramètre: dico, groupe de personne" \
    "Return: un tableau qui contient les personnes qui ont
     le plus d'amis à ce qui ont le moins. "'''
    for i in range(len(group)-1):
        for l in range(len(group)-1):
            if len(network[group[l]])< len(network[group[l+1]]):
                group[l], group[l+1] = group[l+1], group[l]
    return group

u  = order_by_decreasing_popularity()
#print(u)


# Question 9 #

def find_community_by_decreasing_popularity(network):

    '''"Paramètre: dico" \
    "Return: un tableau contenant ceux qui ont plus d'un ami"'''

    t = get_people(network)
    popularity = order_by_decreasing_popularity(network, t)
    return find_community(network,popularity)

v = find_community_by_decreasing_popularity()
#print(v)


# Question 10 #

def find_community_from_person(network, person):

    '''"Paramètre: dico, une personne du dico" \
    "Return: un tableau contenant la personne choisi en paramètre
    et ses amis si ils sont dans le dico"'''

    community = [person]
    popularity = order_by_decreasing_popularity(network,network[person])

    for i in range(len(popularity)):
        if all_his_friends(network,popularity[i],community):
            community.append(popularity[i])

    return community

w = find_community_from_person()
#print(w)


# Question 12#

def find_max_community(network):

    '''"Paramètre: dico" \
"Return: un tableau qui est la plus grande communauté du dico"'''

    person = get_people(network)
    maximum = find_community_from_person(network, pers[0])
    for i in range(len(person)):
        if len(find_community_from_person(network,person[i]))> len(maximum):
            maximum = find_community_from_person(network, person[i])

    return maximum

x = find_max_community()
#print(x)