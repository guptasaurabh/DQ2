import datetime

def generateQuizId():
    qid='Qz'+str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+str(datetime.datetime.now().day)+str(datetime.datetime.now().microsecond)
    return qid


def generateQuestionId():
    qid='Qn'+str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+str(datetime.datetime.now().day)+str(datetime.datetime.now().microsecond)
    return qid


def generateOptionId():
    oid='OP'+str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+str(datetime.datetime.now().day)+str(datetime.datetime.now().microsecond)
    return oid

def generateSectionId():
    sid='SC'+str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+str(datetime.datetime.now().day)+str(datetime.datetime.now().microsecond)
    return sid
    