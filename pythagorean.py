# This is my introductory sentence.
print "Hello! This program allows you to calculate one side of a right triangle using the Pythagorean Theorem.\n"
def beginning() :
    sides  = int(raw_input("""1. Choose 1 to calculate the length of side C using sides A and B.\n2. Choose 2 to calculate the length of side B using sides A and C.\n3. Choose 3 to calculate the length of side A using sides B and C.\n4. Choose 4 to exit the program and return to the terminal.\n\nWhat would you like to do? """))
    # I have the user to choose which two sides to enter because the equation to solve for different sides is different depending on which to side you want to find out.
    if sides == 1:
        print "OK"
        A = int(raw_input("What is the length of side A? "))
        B = int(raw_input("What is the length of side B? "))
        # After finding the length of sides A and B, I must multiply them both to the second power, add, and square root the answer to find the length of side C.
        A_2 = A ** 2

        B_2 = B ** 2

        C_2 = A_2 + B_2
        # Then I must find the sqaure root.
        C = C_2 ** 0.5

        print "The hypotenuse's length is", C
        beginning()
    elif sides  == 2:
        print "OK"
        A = int(raw_input("What is the length of side A? "))
        C = int(raw_input("What is the length of side C? "))
        # This is nearly the same as the first one, but has a few differences.
        # After finding side B and C, I must multiply them to the second power, but instead of adding, I must subtract C^2 by A^2 and the sqaure root to find B.
        A_2 = A ** 2

        C_2 = C ** 2

        B_2 = C_2 - A_2

        B = B_2 ** 0.5

        print "Side B's length is", B
        beginning()
    elif sides == 3:
        print "OK"
        B = int(raw_input("What is the length of side B? "))
        C = int(raw_input("What is the length of side C? "))
        # The final equation is exactly like the first page, but you substitute in B^2 for A^2 and C^2 for B^2.
        # First, you find the length of sides B and C. Then, you multiply them both to the second power, add the two numbers that you just multiplied to the second power, and find the square root.
        B_2 = B ** 2

        C_2 = C ** 2

        A_2 = B_2 + C_2
        # Then I must find the sqaure root.
        A = A_2 ** 0.5

        print "Side A's length is", A
        beginning()
    elif sides == 4:
        loop = 0
        # This ends the program.
    else:
        print "That's not a valid option. Please choose 1, 2, 3, or 4."
        # The user has to choose their numbers again with the correct characters.
        beginning()


beginning()
