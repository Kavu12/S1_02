# SAE S1.02  COMMUNITY DETECTION #

# Module contenant les tests unitaires des fonctions #

def test_create_network():
    assert create_network(["Alice", "Bob"]) == {'Alice': ['Bob'], 'Bob': ['Alice']}
    assert create_network(["Bob", "Charlie", "Alice", "Bob"]) == {'Bob': ['Charlie', 'Alice'], 'Charlie': ['Bob'], 'Alice': ['Bob']}
    assert create_network(["Alice", "Bob","Dominique","Alice"]) != {'Alice' : ['Bob'], 'Alice' : ['Dominique']}
    print("test ok")


def test_get_people():
    assert get_people({
  "Alice" : ["Bob", "Dominique"],
  "Bob" : ["Alice", "Charlie", "Dominique"],
  "Charlie" : ["Bob"],
  "Dominique" : ["Alice", "Bob"]
}) == ["Alice", "Bob", "Charlie", "Dominique"]
    assert get_people({
        "Alice" : ["Dominique"],
        "Dominique" : ["Alice"]
    }) == ["Alice", "Dominique"]
    assert get_people({
        "Charlie" : ["Bob"],
        "Dominique" : ["Charlie"],
        "Bob" : ["Alice", "Charlie"]
    }) != ["Bob", "Dominique", "Charlie", "Patrick"]
    print("test ok")


def test_are_friends():
    assert are_friends(dico, "Alice", "Bob") == True
    assert are_friends(dico, "Dominique", "CHArlie") == False
    assert are_friends(dico, "Bob", "Patrick") == False
    print("test ok")

def test_all_his_friends():
    assert all_his_friends(dico, "Charlie", ["Bob"]) == True
    assert all_his_friends(dico, "Charlie", ["Dominique"]) == False
    assert all_his_friends(dico, "Alice", ["Bob","Charlie"]) != True
    print("test ok")

def test_is_a_community():
    assert is_a_community(dico, ["Bob", "Dominique"]) == True
    assert is_a_community(dico, ["Alice", "Bob"]) != False
    assert is_a_community(dico, ["Alice", "Patrick"]) == False
    print("test ok")

def test_find_community():
    assert find_community(dico, ["Alice", "Bob", "Dominique", "Patrick"]) == ["Alice", "Bob", "Dominique"]
    assert find_community(dico, ["Alice", "Bob"]) == ["Alice", "Bob"]
    assert find_community(dico, ["Charlie", "Alice", "Bob", "Dominique"]) == ["Charlie", "Bob"]
    print("test ok")

def test_order_by_decreasing_popularity():
    assert order_by_decreasing_popularity(dico, ["Charlie", "Alice"]) == ['Alice', 'Charlie']
    assert order_by_decreasing_popularity(dico, ["Bob", "Charlie", "Alice"]) == ["Bob", "Alice", "Charlie"]
    assert order_by_decreasing_popularity(dico, ["Bob", "Charlie", "Dominique"]) != ["Dominique", "Charlie", "Bob"]
    print("test ok")

def test_find_community_by_decreasing_popularity():
    assert find_community_by_decreasing_popularity(dico) == ["Bob", "Alice", "Dominique"]
    assert find_community_by_decreasing_popularity(dico) != ["Bob", "Alice", "Dominique", "Charlie"]
    assert find_community_by_decreasing_popularity(dico) != ["Alice", "Bob", "Dominique"]
    print("test ok")

def test_find_community_from_person():
    assert find_community_from_person(dico, "Charlie") == ["Charlie", "Bob"]
    assert find_community_from_person(dico, "Bob") != ['Bob', 'Charlie', 'Dominique']
    assert find_community_from_person(dico, "Dominique") == ['Dominique', 'Bob', 'Alice']
    print("test ok")

dico2 = {
        "Alice" : ["Charlie", "Bob"],
  "Bob" : ["Alice", "Charlie"],
  "Charlie" : ["Bob", "Dominique", "Alice"],
  "Dominique" : ["Charlie"]
}

def test_find_max_community():
    assert find_max_community(dico) == ["Alice", "Bob", "Dominique"]
    assert find_max_community(dico2) == ["Alice", "Charlie", "Bob"]
    assert find_max_community(dico) != ["Alice", "Charlie", "Bob"]
    print("test ok")