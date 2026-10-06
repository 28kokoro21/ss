def associative():

    # Associative Law for Addition
    print("\nAssociative law for Addition")

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))

    lhs = a + (b + c)
    rhs = (a + b) + c

    print("LHS =", lhs)
    print("RHS =", rhs)

    if lhs == rhs:
        print("Associative law satisfied")
    else:
        print("Associative law not satisfied")


    # Associative Law for Multiplication
    print("\nAssociative law for Multiplication")

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))

    lhs = a * (b * c)
    rhs = (a * b) * c

    print("LHS =", lhs)
    print("RHS =", rhs)

    if lhs == rhs:
        print("Associative law satisfied")
    else:
        print("Associative law not satisfied")


    # Associative Law for Boolean AND
    print("\nAssociative law for Boolean AND")

    a = bool(int(input("Enter value of a (0/1): ")))
    b = bool(int(input("Enter value of b (0/1): ")))
    c = bool(int(input("Enter value of c (0/1): ")))

    lhs = a and (b and c)
    rhs = (a and b) and c

    print("LHS =", lhs)
    print("RHS =", rhs)

    if lhs == rhs:
        print("Associative law satisfied")
    else:
        print("Associative law not satisfied")


    # Associative Law for Boolean OR
    print("\nAssociative law for Boolean OR")

    a = bool(int(input("Enter value of a (0/1): ")))
    b = bool(int(input("Enter value of b (0/1): ")))
    c = bool(int(input("Enter value of c (0/1): ")))

    lhs = a or (b or c)
    rhs = (a or b) or c

    print("LHS =", lhs)
    print("RHS =", rhs)

    if lhs == rhs:
        print("Associative law satisfied")
    else:
        print("Associative law not satisfied")


associative()