# Library

## Description
This project is a Library Management System,
designed to streamline the process of managing books and users in a library.
It provides a comprehensive solution for adding, searching, lending, and returning books,
while maintaining an organized database of library records.

Whether you're a librarian looking to manage inventory or a user searching for your next read,
this system offers intuitive and user-friendly features to enhance the library experience.

Simplifies book management by tracking titles, authors, genres, availability, and popularity.
Enables efficient lending and return operations with detailed logs.
Provides a graphical user interface (GUI) for easy navigation and interaction.

Link to GitHub with  video og simple use - https://github.com/Itamar000Git/Library.git  -  "record.mp4"

---

## Features

- **Feature 1**: Add and remove books
- **Feature 2**: Search books by title, author, genre or year
- **Feature 3**: Track borrowing and returns
- **Feature 4**: Generate reports on popular, available and loaned books
- **Feature 5**: Provide the option to sigh up to a waiting list for unavailable books
- **Feature 6**: Provide a screen that show all books by genres
- **Feature 7**: secured system, only sign up users can use the features above

## Installation
1. pandas: This library is used for data manipulation and handling CSV files.
2. tkinter: This built-in Python library is used for creating the graphical user interface (GUI).

*** probely needed to install the pandas package ***
"pip install pandas" from cmd or use python suggestion to download the package.


##Running instruction
#tests: Run one by one only, because the testers open window that need to be confirmed.

#Sign-in / Sign-up:
 1. sign up with a new user
 2. sign in with the username and password that you just sign up with, and move to the main menu window.
 Note: there is e default user (username:1,password:1)

#Main menu:
 1. For adding book: choose "add book" button.
    # Insert all book details, if the book already exist it will add a copies.
 2. For removing a book choose "remove book".
    #Write the FULL an ACCURATE title and if all copies available the book wil remove from library.
 3. For find wanted book choose "search book".
    #You have the freedom to find a book using any detail that you remember.
    #The option are: title, auther, genre, year.
    #You can also write part of the above details and submit,
     And the result will be all the book that starts with the same part detail in the same field.
     (for example if you write in the title field "The" you get list af all books that their title start with "The").
 4. For presenting a books with common detail choose "view books"
    #You can see a list with "all books", "loaned books", "available books", "popular books" and "books by genre".
    # popular books - chose by the number of loaned books (including waiting list).
    # books by genre - provide another screen that you can see all books that in the same genre.
 5. If you want to lend book  choose "lend book"
    # you need to provide the FULL an ACCURATE title name (if you not sure, try to search it up)
    # If the boos have available copies you can loan it,
      Otherwise you can enter to the waiting list and the first available copy arrive will save for you.
 6. If you want to return book choose "return book"
    # you need to provide the FULL an ACCURATE title name (if you not sure, try to search it up or look on the book)
    # If the book exist in the library we accept it.
 7. For logging out choose "logout" this will bring you to the sign-up sign in screen.

### Design pattern
This project incorporates several design patterns to ensure the codebase is modular, maintainable, and scalable.
Below are the main design patterns that being used in this project:

 ## Observer
  # The observer pattern being used as notification for all the users in the system.
  # The notification send when someone returns or adds a book that have a waiting list,
    So the librarian be able to give it to the next person in the waiting list.

 ## Factory
  # The factory pattern being use as creating all books by their different genre.
  # You can also see common use in the factory methodology in the "display_by_genre_gui",
    This Gui created with user gener choice.

 ## Strategy pattern
  # The strategy pattern being used in the search book methodology.
    We use the "startswith" method to provide a list with all the possible results.
  # The search_strategy class have an abstract method called "search",
    And all the inheritance classes need to implement it with their section.

 ## Decorator Pattern
  # In the Librarian file we have Validated decorator ("validate_input" and "validate_non_empty_data"),
    This function make sure that the data being inserted from the entries is valid.
  # Another decorator usage is in the notification implement,
    The Librarian class inheritance the observer and have implement the update method.

 ## Iterator
  # In the view_books file we used iterator that indicates each time on another book and display it to the screen.