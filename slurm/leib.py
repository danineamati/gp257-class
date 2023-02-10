
# A Python Function to calculate Pi using the Leibniz formula.


def leibniz(num_terms: int):
    """Use the Leibnize formula up to num_terms, return the output."""
    
    # First, we need to assert that the number of terms is an integer.
    # Otherwise, we will get an error (or will be rounding a float).
    assert isinstance(num_terms, int) f"The entry num_terms is {num_terms} of type {type(num_terms)}, but it should be an integer."

    # Now we calculate the sequence
    leib_approx = 0 # Start at 0 and add terms from there.
    
    for i in range(num_terms):
        # Calculate the denominator
        # i = 0 -> denominator = 1
        # i = 1 -> denominator = 3
        # i = 2 -> denominator = 5
        # etc.
        denominator = 2 * i + 1
        # Modulo should be cheaper than exponent.
        # For an even number, the modulo is zero and we will add
        # For an odd number, the modulo is one and we will subtract
        parity = i % 2

        # Calculate the next term and put it in the series.
        if parity == 0:
            leib_approx += 4 / denominator
        elif parity == 1:
            leib_approx -= 4 / denominator
        else:
            raise Exception(f"Parity is {parity}, but should only be zero or one")
    
    # We have finished the sum and can return the result
    return leib_approx

if __name__ == "__main__":
    la_10 = leibniz(10)
    print(f"\nApproximation of Pi at 10 is {la_10}\n")


