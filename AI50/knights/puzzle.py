from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
    Or(AKnight, AKnave),  # A Can be a knight or knave
    Not(And(AKnight, AKnave)),  # but not both
    
    Implication(AKnight, And(AKnave, AKnight)),  # If A is actually a Knight his sentence is true
    Implication(AKnave, Not(And(AKnave, AKnight)))  # If A is a actually a Knave his sentence is false
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO 
    Or(BKnight, BKnave),  # B Can be a Knight of Knave
    Not(And(BKnight, BKnave)),  # But not both
    Or(AKnight, AKnave),  # A Can be a Knight of Knave
    Not(And(AKnave, AKnight)),  # But not both
    
    Implication(AKnight, And(AKnave, BKnave)),  # If A is actually a Knight his sentence is true
    Implication(AKnave, Not(And(AKnave, BKnave)))  # If A is actually a Knave his sentece is false

    # B says nothing
)

# puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO

    # A can be  knight or a knave but not both
    Or(AKnave, AKnight),
    Not(And(AKnave, AKnight)),

    # B can be knight or a knave but not both
    Or(BKnave, BKnight),
    Not(And(BKnave, BKnight)),

    # A is a knight if his Statements are true else he is a Knave
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    
    # B is a knight if his Statements are true else he is a Knave
    Implication(BKnight, Or(And(AKnight, BKnave), And(BKnight, AKnave))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(BKnight, AKnave)))),
)


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    
    # A can be  knight or a knave but not both
    Or(AKnave, AKnight),
    Not(And(AKnave, AKnight)),

    # B can be knight or a knave but not both
    Or(BKnave, BKnight),
    Not(And(BKnave, BKnight)),
    
    # C can be knight or a knave but not both
    Or(CKnave, CKnight),
    Not(And(CKnave, CKnight)),

    # Statements
    # A is a knight if his Statements are true and knave otherwise
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    
    # B is a knight if his Statements are true and knave otherwise
    Implication(BKnight, And(Implication(Or(AKnight, AKnave), AKnave), CKnave)),
    Implication(BKnave, And(Not(Implication(Or(AKnight, AKnave), AKnave)), Not(CKnave))),

    # C is a knight if his Statements are true and kanve otherwise
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight)),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
