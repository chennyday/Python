'''
class IO:
    supportedSrcs = ['console', 'file']
    def read(src):
        if src not in IO.supportedSrcs: 
            print('Not supported')
        else: 
            print('Read from', src )
print(IO.supportedSrcs)
IO.read('file')
IO.read('internet')
'''

class Cars:
    # 建構式
    def __init__(self, color, seat):
        self.color = color  # 顏色屬性
        self.seat = seat  # 座位屬性
    # 方法(Method)
    def drive(self):
        print(f"My car is {self.color} and has {self.seat} seats.")

mazda = Cars('blue', 4)        
mazda.drive()
