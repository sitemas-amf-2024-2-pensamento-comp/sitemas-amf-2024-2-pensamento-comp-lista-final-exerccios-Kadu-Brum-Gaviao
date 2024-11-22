valores = [(A, B, C) for A in [0, 1] for B in [0,1] for C in [0, 1]]

print(f"{'A':^3} {'B':^3} {'C':^3} {'A || (B && C)':^15} {'!A && B && C':^15} {'!(A && B && !C)':^15}")

for A, B, C in valores:
    exp1 = A or (B and C)
    exp2 = not A and B and C
    exp3 = not (A and B and not C)
    print(f"{A:^3} {B:^3} {C:^3} {str(exp1):^15} {str(exp2):^15} {str(exp3):^15}")