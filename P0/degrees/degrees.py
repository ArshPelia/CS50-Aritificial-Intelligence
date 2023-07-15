import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
# it maps names to a set of corresponding ids 
#   (it’s possible that multiple actors have the same name).
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
# maps each person’s id to another dictionary with values for the 
#   person’s name, birth year, and the set of all the movies they have starred in.
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
# maps each movie’s id to another dictionary with values for that movie’s title, 
#   release year, and the set of all the movie’s stars
movies = {}

def load_data(directory):
    """
    Load data from CSV files into memory(dictionaries).
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    # if len(sys.argv) > 2:
    #     sys.exit("Usage: python degrees.py [directory]")
    # directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    directory = './small'

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")

""" 
Our states are people. 

Our actions are movies, which take us from one actor to another (it’s true that a movie could
    take us to multiple different actors, but that’s okay for this problem). 
        path_cost = 1 # cost for each action (movies/degree of separation)
            i.e. unweighted graph

Our initial state and goal state are defined by the two people we’re trying to connect. 

By using breadth-first search, we can find the shortest path from one actor to another.
 """

def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.

    For example, if the return value of shortest_path were [(1, 2), (3, 4)], 
        that would mean that the source starred in movie 1 with person 2, 
        person 2 starred in movie 3 with person 4, and person 4 is the target.
    """
    
    # TODO
    # raise NotImplementedError

    que = QueueFrontier()
    explored = []
    que.add(Node(people.get(source), None, None))
    for i in range(len(que.frontier)):
        node = que.frontier[i]
        print(node.state["name"])




def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
