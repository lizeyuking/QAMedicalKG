from question_classifier import *
from question_parser import *
from answer_search import *
#基本算法就是利用模式匹配，匹配用户输入的句子中解析出来的关键词
'''问答类'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()      #进入分类模块
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '没能理解您的问题，我数据量有限。。。能不能问的标准点'
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)

if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        question = input('咨询:')
        answer = handler.chat_main(question)
        print('客服机器人:', answer)

