import numpy as nu
import streamlit as st


st.title("WELCOME TO THE BRAINROT QUIZ GAME")
st.write("//RULES//")
st.write(
    "1. This is a multiplayer game but you do need to specify how many players will be playing for a specific round ")
st.write("2. There will be a total of 5 questions and each question containing two marks")
st.write("3. No negative markings")
st.write(
    "4. Lastly enjoy the game and share your reviews on it too so that I could enhance your experience the next time")

questions = {"What is the name of the surreal YouTube series blamed for brain-rot? ": {
                 "options": ["Skibidi Toilet", "Royce Rolls", "67", "69"], "answer": "Skibidi Toilet"},
             "Another word for charisma in Gen-Z slang?": {"options": ["skee", "rizz", "69", "shawty"], "answer": "rizz"},
             "What TikTok trend celebrates snack-plates as dinner?": {
                 "options": ["Girl Dinner", "snackies", "bigback", "tiktok"], "answer": "Girl Dinner" },
             "Which U.S. state is jokingly blamed for weird internet events? ": {
                 "options": ["Washington DC", "Texas", "Arkansas", "Ohio"], "answer": "Ohio" },
             "Surreal blue feline meme that swept TikTok in 2023?": {"options": ["avatar", "fishes", "smurfs", "cats"],
                                                                     "answer": "smurfs"},
             "Which of the following is not an italian brainrot word?": {
                 "options": ["tung tung sahar", "pizza", "ballerina cappucino", "mimimi"], "answer": "pizza"},
             "Which type of water is famous right now?": {"options": ["blue", "dirty", "mango", "coconut"],
                                                          "answer": "coconut"},
             "In 2026 which nationality is considered to be 'the new blacks'? ": {
                 "options": ["Mexicans", "Filipinos", "Indians", "Australians"], "answer": "Indians"},
             "Which word has recently been over excessively used by the younger generation?": {
                 "options": ["skee", "nonchalant", "crazy", "deadass"], "answer": "nonchalant"},
             "Who is everyone's sunshine? ": {"options": ["lebron", "darius", "Jynxi", "Ishowspeed"], "answer": "lebron"},
             "Which drink has recently gained popularity in 2026 ?": {"options": ["boba", "tea", "matcha", "water"],
                                                                      "answer": "matcha"}
             }
roundno = 0
no = 0
ugh = 0
wtv = 1000
wtv1 = 2000
wtv2 = 3000
def game():
    global roundno
    global ugh
    global wtv
    global wtv1
    global wtv2
    roundno = roundno + 1
    play = st.text_input("How many players will be playing in this round: ", placeholder=" enter a number ", key = wtv1)
    wtv1 = wtv1 + 1
    no_players = int(play)
    name = []
    global no
    no = 0

    for i in range(no_players):
        playername = st.text_input(f"Name of Player {i + 1} ", key = wtv2)
        wtv2 = wtv2 + 1
        name.append(playername)
    st.title(f"ROUND {roundno}")
    for i in name:
        user_ans = []
        correct_ans = []
        st.subheader(f"{i}'s turn :")
        if "key" not in st.session_state:
          st.session_state.key = nu.random.choice(list(questions.keys()), size=5, replace=True)
        for idx, q in enumerate(st.session_state.key):
            st.write(f"Q{idx+1} {q}")
            correct_ans.append(questions[q]["answer"])
            choice = 0
            choice = st.radio("Select ur answer : ", questions[q]["options"], key=f"{ugh}")
            ugh = ugh + 1
            user_ans.append(choice)
        user_ans = nu.array(user_ans)
        correct_ans = nu.array(correct_ans)
        score = nu.sum(user_ans == correct_ans)
        score = score * 2
        wtv = wtv + 1
        if st.button("Submit", key = wtv):
            st.write(f"{name[no]} SCORE: {score}/10")
            st.write("Thanks for playing mwah")
            score = 0

        no = no + 1

    rno = st.radio(f"Do you wanna go for ROUND {roundno + 1}:", ["Yes","No"])
    if (rno == "Yes"):
        game()
    else:
        st.error("Sad to see u not play")


yes_no = st.radio("Choose an option:",["Yes", "No"])
if yes_no== "Yes":
    game()
else:
    st.error("Sad to see u not play")
