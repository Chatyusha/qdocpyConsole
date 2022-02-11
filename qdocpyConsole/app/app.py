from random import random
from secrets import randbelow
from qdocpy.parser import document
import pathlib
import re
import random

class App:
    def __init__(self,abs_paths,options_num=4):
        self.options_num = options_num
        self.qdoc_data = document.Qdoc(abs_paths)
        self.__Build_Quizzes()
    
    def __Build_Quizzes(self):
        self.qdoc_data.read_docs()
        self.qdoc_data.construct()
    
    def Show_Data(self):
        print(self.qdoc_data.to_doct())
    
    def get_Quiz(self,num):
        base_data = self.qdoc_data.quizzes[num]
        formed_data = {}
        formed_data["QuizSentence"] = base_data.raw_data
        formed_data["quizzes"] = []
        for i in base_data.answers:
            ptn = re.compile(i.get_re())
            formed_data["QuizSentence"] = ptn.sub(f"(  {i.number}  )",formed_data["QuizSentence"])

            answer_data = {}
            answer_data["answer"] = i.answer
            taggroup_len = len(self.qdoc_data.taggroup[i.tag])
            answer_data["dummies"] = random.sample(self.qdoc_data.taggroup[i.tag],min(taggroup_len,self.options_num)-1)
            while answer_data["answer"] in answer_data["dummies"]:
                answer_data["dummies"] = random.sample(self.qdoc_data.taggroup[i.tag],
                min(taggroup_len,self.options_num)-1)
            formed_data["quizzes"].append(answer_data)
        return formed_data
    
    def Interactive(self):
        qandas = self.get_Quiz(random.randint(0,len(self.qdoc_data.quizzes)-1))
        print(qandas["QuizSentence"])
        for i in qandas["quizzes"]:
            options = [i["answer"]] + i["dummies"]
            random.shuffle(options)
            for j, k in zip(range(0,len(options)),options):
                print(f"({j}) : {k}")
            ans = input("answer >> ")
            if ans == "q":
                exit(0)
            else:
                ans_num = int(ans)
                if options[ans_num] == i["answer"]:
                    print("正解")
                else:
                    print("ハズレ")

    def Start(self):
        while True:
            self.Interactive()