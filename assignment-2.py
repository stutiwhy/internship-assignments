def add_book(title, author, genre): # function to create tuple from the user inputs
    bk = (title, author, genre)
    return bk

library = []
lset = set()
def add_to_library(bk): # function to add tuple made by add_book() to the library
    if bk not in library:
        library.append(bk)
        lset.add(bk)
        print("Book successfully added to the library !")
    else:
        print("Book already in library.")

def remove_from_library(title): # function to remove book from library
    for bk in library:
        if bk[0] == title:
            library.remove(bk)
            lset.remove(bk)
            print("Book successfully removed from the library !")
            return
    else:
        print("Book does not exist in library.")

def search_books(term): # function to search book from library
    for bk in library:
        if bk[0] == term:
            print(f"Title : {bk[0]}, Author : {bk[1]}, Genre : {bk[2]}")
        else:
            print("No books found by that name in the library.")

def list_books(): # function to list all library books
    if not library:
        print("The library has no books yet. Please go and add some.")
        return
    else:
        print("All the books in the library are listed as follows :")
        for bk in library:
            print(f"Title : {bk[0]}, Author : {bk[1]}, Genre : {bk[2]}")

def categorize_books(): # function to categorize books into genres and create new genre categories for the ones that don't exist
    global dgenre
    dgenre = {}

    for bk in library:
        title, author, genre = bk
        if genre not in dgenre:
            dgenre[genre] = []
        dgenre[genre].append(bk)

def  print_by_genre(user_genre): # function to print books by their category
    if user_genre in dgenre:
        print(f"Books in {user_genre} genre :")
        for bk in dgenre[user_genre]:
            print(f"Title : {bk[0]}, Author : {bk[1]}")
    else:
        print("No books found for that genre.")

ch1 = 0

while ch1 != 6:
    print("1. Add book.")
    print("2. Remove book.")
    print("3. Search book.")
    print("4. List all books.")
    print("5. List books by genre.")
    print("6. Exit")

    ch1 = int(input("Enter choice : "))

    if ch1 == 1:
        title = input("Enter book title : ")
        author = input("Enter book author : ")
        genre = input("Enter book genre : ")
        new_bk = (title, author, genre)
        add_to_library(new_bk)
        categorize_books()
    
    elif ch1 == 2:
        title = input("Enter title of the book to be removed : ")
        remove_from_library(title)

    elif ch1 == 3:
        term = input("Enter title of the book to be searched : ")
        search_books(term)
    
    elif ch1 == 4:
        list_books()
    
    elif ch1 == 5:
        user_genre = input("Enter genre to be searched : ")
        print_by_genre(user_genre)

    elif ch1 == 6:
        print("Good bye !")
        
    else:
        print("Invalid choice. Please enter a number between 1-6.")
