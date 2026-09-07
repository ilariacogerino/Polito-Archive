import copy

from dictionary import Dictionary as d, Dictionary
import richWord as rw
import time


class MultiDictionary:

    def __init__(self, dict = Dictionary()):
        self.dict = dict

    def printDic(self, language):
        self.dict.loadDictionary(language)
        self.dict.printAll()

    def searchWord(self, words, language):
        self.dict = self.dict.loadDictionary(language)

        print("------------------------------")
        print("Using contains")
        time1=self.containsResearch(words)

        print("------------------------------")
        print("Using linear research")
        time2=self.linearResearch(words,time1)

        print("------------------------------")
        print("Using dichotomic research")
        self.dichotomicResearch(words,time2)


    def containsResearch(self, words):
        errors = []

        for word in words:
            if word not in self.dict:
                errors.append(word)
        for err in errors:
            print(err)
        time1 = time.process_time()
        print(f'Time elapsed: {time1}')
        return time1


    def linearResearch(self, words, time1):
        errors = []
        right = []

        for word in words:
            for d in self.dict:
                if word == d:
                    right.append(d)

        for word in words:
            if word not in right:
                errors.append(word)
                print(word)

        time2 = time.process_time()
        print(f'Time elapsed: {time2-time1}')
        return time2


    def dichotomicResearch(self, words,time2):
        errors = []
        rights = []
        dp = copy.deepcopy(self.dict)


        for word in words:
            d = dp[:]
            flag = False
            while d:
                half = len(d)//2
                if d[half]==word:
                    rights.append(word)
                    flag=True
                    break
                elif word < d[half]: #the word is in the first half
                    d = d[:half]
                else:
                    d = d[half+1:]


        for word in words:
            if word not in rights:
                errors.append(word)
                print(word)

        time3 = time.process_time()
        print(f'Time elapsed: {time3-time2}')






