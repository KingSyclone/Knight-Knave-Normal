from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")
ANormal = Symbol("A is Normal")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")
BNormal = Symbol("B is Normal")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")
CNormal = Symbol("C is Normal")

# Puzzle 0
# A says "I am both a knight and a knave." (A ∨ B) ∧ ¬ (A ∧ B)
knowledge0 = And(
    And(Or(AKnave,AKnight),
    Not(And(AKnave,AKnight))),
    Implication(AKnave,Not(And(AKnight,AKnave))),
    Implication(AKnight,(And(AKnight,AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    And(Or(AKnave,AKnight), Not(And(AKnave,AKnight))),
    And(Or(BKnave,BKnight), Not(And(BKnave,BKnight))),
    Implication(AKnave,Not(And(AKnave,BKnave))),
    Implication(AKnight,(And(AKnave,BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    And(Or(AKnave,AKnight), Not(And(AKnave,AKnight))),
    And(Or(BKnave,BKnight), Not(And(BKnave,BKnight))),
    Implication(AKnight,Or(And(AKnave,BKnave),And(AKnight,BKnight))),
    Implication(AKnave,Not(Or(And(AKnave,BKnave),And(AKnight,BKnight)))),
    Implication(BKnight,Or(And(AKnave,BKnight),And(BKnave,AKnight))),
    Implication(BKnave,Not(Or(And(AKnave,BKnight),And(BKnave,AKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    And(Or(AKnave,AKnight), Not(And(AKnave,AKnight))),
    And(Or(BKnave,BKnight), Not(And(BKnave,BKnight))),
    And(Or(CKnave,CKnight), Not(And(CKnave,CKnight))),
    Implication(BKnave,Not(CKnave)),
    Implication(BKnight,CKnave),
    Implication(CKnave,Not(AKnight)),
    Implication(CKnight,AKnight),
    Implication(AKnave,Not(Or(AKnight,AKnave))),
    Implication(AKnight,Or(AKnight,AKnave))
)

# Puzzle 4
# B says "A said 'I am a knave'."
# C says "B is a knave."
knowledge4 = And(
    And(Or(AKnave,AKnight), Not(And(AKnave,AKnight))),
    And(Or(BKnave,BKnight), Not(And(BKnave,BKnight))),
    And(Or(CKnave,CKnight), Not(And(CKnave,CKnight))),
    Implication(CKnave,BKnight),
    Implication(CKnight,BKnave),
    Implication(BKnave,Not(And(AKnave,CKnave))),
    Implication(BKnight,And(AKnave,CKnave)),
    Implication(Or(AKnave,AKnight),BKnave),
)


# Puzzle 5
# B says "A said 'There is one knight among us'."
# C says "B is a knave."
knowledge5 = And(
    And(Or(AKnave,AKnight), Not(And(AKnave,AKnight))),
    And(Or(BKnave,BKnight), Not(And(BKnave,BKnight))),
    And(Or(CKnave,CKnight), Not(And(CKnave,CKnight))),
    Implication(CKnave,BKnight),
    Implication(CKnight,BKnave),
    Implication(BKnight,And(AKnave,CKnave)),
    Implication(BKnave,CKnight),
    Implication(Or(AKnave,AKnight),BKnave)
)

# Puzzle 6
# A says "At least one of us is a knave"
# B says nothing.
knowledge6 = And(
    And(Or(AKnave,AKnight), Not(And(AKnave,AKnight))),
    And(Or(BKnave,BKnight), Not(And(BKnave,BKnight))),
    Implication(AKnave,AKnight),
    Implication(AKnight,Or(AKnave,BKnave))
)

# Puzzle 7
# A says "Either I am a knave or B is a knight"
# B says nothing.
knowledge7 = And(
    And(Or(AKnave,AKnight), Not(And(AKnave,AKnight))),
    And(Or(BKnave,BKnight), Not(And(BKnave,BKnight))),
    Implication(AKnave,And(AKnight,BKnave)),
    Implication(AKnight,Or(AKnave,BKnight))
)

# Puzzle 8
# A says "All of us are knaves."
# B says "Exactly one of us is a knight."
knowledge8 = And(
    And(Or(AKnave,AKnight), Not(And(AKnave,AKnight))),
    And(Or(BKnave,BKnight), Not(And(BKnave,BKnight))),
    And(Or(CKnave,CKnight), Not(And(CKnave,CKnight))),
    Implication(AKnave,Or(Or(BKnight,CKnave),Or(CKnight,BKnave))),
    Implication(AKnight,AKnave),
    Implication(BKnight,And(AKnave,CKnave)),
    Implication(BKnave,And(AKnight,CKnight))
)

# Puzzle 9
# A says "I am a knave, but B isn't."
# B says nothing.
knowledge9 = And(
    And(Or(AKnave,AKnight), Not(And(AKnave,AKnight))),
    And(Or(BKnave,BKnight), Not(And(BKnave,BKnight))),
    Implication(AKnave,BKnave),
    Implication(AKnight,And(BKnight,AKnave))
)

# Puzzle 10
# A says "B is a knave."
# B says "A and C are of the same type."
knowledge10 = And(
    And(Or(AKnave,AKnight), Not(And(AKnave,AKnight))),
    And(Or(BKnave,BKnight), Not(And(BKnave,BKnight))),
    And(Or(CKnave,CKnight), Not(And(CKnave,CKnight))),
    Implication(AKnave,BKnight),
    Implication(BKnight,And(AKnave,CKnave)),
    Implication(AKnight,BKnave),
    Implication(BKnave,And(AKnight,CKnave)),
)

# Puzzle 11
# A says "I am normal"
# B says "That is true."
# C says "I am not normal."
knowledge11 = And(
    And(Or(AKnave,AKnight), Not(And(AKnave,AKnight))),
    And(Or(AKnave,ANormal), Not(And(AKnave,ANormal))),
    And(Or(ANormal,AKnight), Not(And(ANormal,AKnight))),
    And(Or(BKnave,BKnight), Not(And(BKnave,BKnight))),
    And(Or(CKnave,CKnight), Not(And(CKnave,CKnight))),
    And(Or(BKnave,BNormal), Not(And(BKnave,BNormal))),
    And(Or(CKnave,CNormal), Not(And(CKnave,CNormal))),
    And(Or(BNormal,BKnight), Not(And(BNormal,BKnight))),
    And(Or(CNormal,CKnight), Not(And(CNormal,CKnight))),
    Or(And(AKnave,BKnight,CNormal),And(AKnight,BKnave,CNormal),And(ANormal,BKnight,CKnave),And(ANormal,BKnave,CKnight),And(AKnave,BNormal,CKnight),And(AKnight,BNormal,CKnave)),
    Implication(AKnight,And(ANormal,Not(AKnight))),
    Implication(AKnave,Not(ANormal)),
    Implication(BKnight,ANormal),
    Implication(BKnave,Not(ANormal)),
    Implication(CKnight,And(Not(CKnave),Not(CNormal))),
    Implication(CKnave,CNormal),
)

# Puzzle 12
# A says "B is a knight."
# B says "A is a knave."
knowledge12 = And(
    And(Or(AKnave,AKnight), Not(And(AKnave,AKnight))),
    And(Or(AKnave,ANormal), Not(And(AKnave,ANormal))),
    And(Or(ANormal,AKnight), Not(And(ANormal,AKnight))),
    And(Or(BKnave,BKnight), Not(And(BKnave,BKnight))),
    And(Or(BKnave,BNormal), Not(And(BKnave,BNormal))),
    And(Or(BNormal,BKnight), Not(And(BNormal,BKnight))),
    Or(And(ANormal,Not(BNormal)),And(BNormal,Not(ANormal))),
    Implication(AKnight,BKnight),
    Implication(BKnight,AKnave),
    Implication(ANormal,And(Not(AKnight),Not(AKnave))),
    Implication(BNormal,And(Not(BKnight),Not(BKnave))),
    Implication(AKnave,And(Not(BKnight),Not(BNormal))),
    Implication(BKnave,AKnight),
)

# Puzzle 13
# A says "I am normal"
# B says "That is true."
# C says "I am not normal."
knowledge13 = And(
    And(Or(Or(AKnave,AKnight),ANormal), Not(And(And(AKnave,AKnight),ANormal))),
    And(Or(Or(BKnave,BKnight),BNormal), Not(And(And(BKnave,BKnight),BNormal))),
    And(Or(Or(CKnave,CKnight),CNormal), Not(And(And(CKnave,CKnight),CNormal))),
    Or(
        And(And(AKnight, BKnave), CNormal),
        And(And(AKnight, CKnave), BNormal),
        And(And(BKnight, AKnave), CNormal),
        And(And(BKnight, CKnave), ANormal),
        And(And(CKnight, AKnave), BNormal),
        And(And(CKnight, BKnave), ANormal),
    ),
    Implication(AKnight,And(ANormal,Not(AKnight))),
    Implication(AKnave,Not(BKnight)),
    Implication(ANormal,Or(BNormal,BKnight)),
    Implication(BKnight,And(ANormal,CNormal)),
    Implication(BNormal,Or(ANormal,AKnave)),
    Implication(BKnave,Not(ANormal)),
    Not(And(ANormal,CNormal)),
)

# Puzzle 14
# A says "C is normal."
# B says "I am the (k)night."
# C says "B is telling the truth."
# Given A is a knight
knowledge14 = And(
    And(Or(Or(AKnave,AKnight),ANormal), Not(And(And(AKnave,AKnight),ANormal))),
    And(Or(Or(BKnave,BKnight),BNormal), Not(And(And(BKnave,BKnight),BNormal))),
    And(Or(Or(CKnave,CKnight),CNormal), Not(And(And(CKnave,CKnight),CNormal))),
    Or(
        And(And(AKnight, BKnave), CNormal),
        And(And(AKnight, CKnave), BNormal),
        And(And(BKnight, AKnave), CNormal),
        And(And(BKnight, CKnave), ANormal),
        And(And(CKnight, AKnave), BNormal),
        And(And(CKnight, BKnave), ANormal),
    ),
    AKnight,
    Implication(AKnight,CNormal),
    Implication(BKnight,Or(CNormal,CKnight)),
    Implication(BKnave,Or(CNormal,CKnave)),
    Implication(BNormal,Or(CNormal,Or(CKnight,CKnave))),
    Implication(CKnight,Or(BNormal,BKnight)),
    Implication(Or(CNormal,CKnave),Or(BNormal,BKnave)),
    Implication(CKnave,Not(AKnight)),
    Not(And(ANormal,CNormal)),
    Not(And(BNormal,CNormal)),
    Not(And(CNormal,BNormal)),
)


def main():
    symbols = [AKnight, AKnave, ANormal, BKnight, BKnave, BNormal, CKnight, CKnave, CNormal]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
        ("Puzzle 4", knowledge4),
        ("Puzzle 5", knowledge5),
        ("Puzzle 6", knowledge6),
        ("Puzzle 7", knowledge7),
        ("Puzzle 8", knowledge8),
        ("Puzzle 9", knowledge9),
        ("Puzzle 10", knowledge10),
        ("Puzzle 13", knowledge13),
        ("Puzzle 14", knowledge14),
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
