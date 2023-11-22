
class QuizBrain:

    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_ans = input(f"Q.{self.question_num}: {current_question.text}(True/false): \n")
        self.check_ans(user_ans, current_question.answer)

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("you got it right")
        else:
            print("That's Wrong!!")
        print(f"The correct ans was: {correct_ans}")
        print(f"You correct answer is: {self.score}/{self.question_num}")


    
