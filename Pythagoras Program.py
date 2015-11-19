sides  = int(raw_input("Choose which equation to enter. Choose out of AB=C(1) AC=B(2)  or BC=A(3) "))
if sides == 1:
    print "OK"
    A = int(raw_input("What is the length of side A? "))
    B = int(raw_input("What is the length of side B? "))
    # After finding side A and B, I must multiply them to the second power and add to find C.
    A_2 = A ** 2

    B_2 = B ** 2

    C_2 = A_2 + B_2
    # Then I must find the sqaure root.
    C = C_2 ** 0.5

    print "The hypotenuse's length is", C

elif sides  == 2:
    print "OK"
    A = int(raw_input("What is the length of side A? "))
    C = int(raw_input("What is the length of side C? "))
    # After finding side B and C, I must multiply them to the second power, but instead of adding, I must subtract C^2 by A^2 and the sqaure root to find B.
    A_2 = A ** 2

    C_2 = C ** 2

    B_2 = C_2 - A_2

    B = B_2 ** 0.5

    print "Side B's length is", B
elif sides == 3:
    print "OK"
    B = int(raw_input("What is the length of side B? "))
    C = int(raw_input("What is the length of side C? "))
    # The final equation is exactly like the first page, but you substitute in B^2 for A^2 and C^2 for B^2.
    B_2 = B ** 2

    C_2 = C ** 2

    A_2 = B_2 + C_2
    # Then I must find the sqaure root.
    A = A_2 ** 0.5

    print "Side A's length is", A
else:
    print "That is not one of the specified numbers or symbols please choose either 1, 2, or 3."
# I basically recopied everything in case they printed the wrong number.
# So I could give another chance.
    sides  = int(raw_input("Choose which equation to enter. Choose out of AB=C(1) AC=B(2)  or BC=A(3) "))
    if sides == 1:
        print "OK"
        A = int(raw_input("What is the length of side A? "))
        B = int(raw_input("What is the length of side B? "))
        # After finding side A and B, I must multiply them to the second power and add to find C.
        A_2 = A ** 2

        B_2 = B ** 2

        C_2 = A_2 + B_2
        # Then I must find the sqaure root.
        C = C_2 ** 0.5

        print "The hypotenuse's length is", C

    elif sides  == 2:
        print "OK"
        A = int(raw_input("What is the length of side A? "))
        C = int(raw_input("What is the length of side C? "))
        # After finding side B and C, I must multiply them to the second power, but instead of adding, I must subtract C^2 by A^2 and the sqaure root to find B.
        A_2 = A ** 2

        C_2 = C ** 2

        B_2 = C_2 - A_2

        B = B_2 ** 0.5

        print "Side B's length is", B
    elif sides == 3:
        print "OK"
        B = int(raw_input("What is the length of side B? "))
        C = int(raw_input("What is the length of side C? "))
        # The final equation is exactly like the first page, but you substitute in B^2 for A^2 and C^2 for B^2.
        B_2 = B ** 2

        C_2 = C ** 2

        A_2 = B_2 + C_2
        # Then I must find the sqaure root.
        A = A_2 ** 0.5

        print "Side A's length is", A
