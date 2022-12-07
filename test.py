#class선언

#- object는 안 적어도 자동상속이 된다.
#- 클래스명은 snakecase형이 아닌camelcase로 작성
class SoccerPlayer(object):

#Attribute
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
    def __str__(self):
        return "%s, %d" % (self.name,self.back_number)

abc = SoccerPlayer("saka", "RW", 7)
print(abc)

#self는 생성된 인스턴스 자신을 가르킴