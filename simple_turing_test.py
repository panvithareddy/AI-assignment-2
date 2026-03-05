import random

print("=== Simple Turing Test Program ===")

# AI style replies
ai_answers = {
    1: "I am still learning about that topic.",
    2: "That question needs more context.",
    3: "Maybe there are multiple possibilities.",
    4: "Interesting thought, I will consider it.",
    5: "I cannot answer that clearly right now."
}

total_rounds = 3
correct_count = 0

for round_no in range(1, total_rounds + 1):

    print("\n--- Round", round_no, "---")
    
    user_question = input("Judge's Question: ")

    # Decide randomly who answers
    identity = random.randint(0,1)   # 0 = AI , 1 = Human

    if identity == 1:
        print("Human, please type your reply:")
        reply = input()
        actual = "human"
    else:
        key = random.randint(1,5)
        reply = ai_answers[key]
        actual = "machine"

    print("\nReply:", reply)

    judge_guess = input("Judge guess who answered (human/machine): ").lower()

    if judge_guess == actual:
        print("Judge guessed correctly.")
        correct_count += 1
    else:
        print("Judge guessed wrong.")

print("\nResult:", correct_count, "correct guesses out of", total_rounds)

if correct_count > total_rounds/2:
    print("Judge identified the machine successfully.")
else:
    print("Machine fooled the judge. Turing Test passed!")