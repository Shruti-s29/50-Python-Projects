from question_data import Question_list
class Question():
    def __init__(self,text,answer) :
        self.question_text = text
        self.question_answer = answer

class QuizBrain():
    def __init__(self,q_list):
        self.que_num = 0
        self.score = 0
        self.que_list = q_list

    def still_has_que(self):
        return self.que_num < len(self.que_list)

    def next_question(self):
        current_que = self.que_list[self.que_num]
        #print(current_que)
        self.que_num +=1
        user_ans = input(f"Q.{self.que_num}:{current_que.question_text} (True/False) ?\n")
        self.check_ans(user_ans,current_que.question_answer)

    def check_ans(self,user_input,correct_ans):
        if user_input.lower()==correct_ans.lower():
            print("---- Yeah!! You got it right !! -----")
            self.score +=1

        else:
            print("---- Ouch! That's a wrong answer ---- ")
        
        print(f"Your score is :{self.score}/{self.que_num}")
        print("--------------------------------------------")
#-----------------------------------------------------------------------------
# ------------------- Main -------------

Question_bank = []
for que in Question_list:
    que_text = que["text"]
    que_ans = que["answer"]
    # print(que_text,que_ans)
    new_que_obj = Question(que_text,que_ans)
    Question_bank.append(new_que_obj)
#print(Question_bank)
quiz = QuizBrain(Question_bank)

while quiz.still_has_que():
    quiz.next_question()

print("-------------The Game is Finished------------\n ----------Hope You Enjoyed------------")