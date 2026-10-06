def distributive():

    # Distributive Law of Multiplication over Addition
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))

    print("\nDistributive law of multiplication over Addition")

    lhs = a * (b + c)
    rhs = (a * b) + (a * c)

    print("LHS =", lhs)
    print("RHS =", rhs)

    print("Distributive law satisfied" if lhs == rhs
          else "Distributive law not satisfied")


    # Distributive Law of Boolean AND over OR
    print("\nDistributive law of Boolean AND over OR")

    a = bool(int(input("Enter value of a (0/1): ")))
    b = bool(int(input("Enter value of b (0/1): ")))
    c = bool(int(input("Enter value of c (0/1): ")))

    lhs = a and (b or c)
    rhs = (a and b) or (a and c)

    print("LHS =", lhs)
    print("RHS =", rhs)

    print("Distributive law satisfied" if lhs == rhs
          else "Distributive law not satisfied")


    # Distributive Law of Boolean OR over AND
    print("\nDistributive law of Boolean OR over AND")

    a = bool(int(input("Enter value of a (0/1): ")))
    b = bool(int(input("Enter value of b (0/1): ")))
    c = bool(int(input("Enter value of c (0/1): ")))

    lhs = a or (b and c)
    rhs = (a or b) and (a or c)

    print("LHS =", lhs)
    print("RHS =", rhs)

    print("Distributive law satisfied" if lhs == rhs
          else "Distributive law not satisfied")


distributive()