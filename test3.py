A = {'Aqua Bike': 55, 'BlackHole Coaster': 140, 'Giant House': 89, 'Grandcar': 70,
     'Heart wheel': 85, 'Horror Tower': 110, 'Hurricane': 160, 'Kart Rider': 100,
     'Pegasus': 80, 'Spaceship': 60, 'Raptor': 115, 'Sky Cab': 90, 'Sky Coaster': 180,
     'Snow Town': 200, 'Super Splash': 130, 'Tornado': 170, 'Vikings': 150,
     'Water Fun': 125, '4D Adventure': 120}


class Heartland:
    def __init__(self):  # ประกาศตัวแปร
        self.arrayA = []

    def arrayM(self):  # ฟังก์ชันสร้าง array เพื่อเก็บเฉพาะราคาของเครื่องเล่น
        self.arrayA = []
        for x in A:
            if A[x] != 0:
                self.arrayA.append(A[x])
        return self.arrayA

    def insert(self, name, cost):  # เพิ่มเครื่องเล่น/ปรับราคา
        A[name] = cost  # แก้ไขในลิสต์ A
        self.arrayM()  # สร้าง array เก็บราคาใหม่

    def delete(self, name):  # ลบเครื่องเล่น
        if name in A:
            A[name] = 0  # แก้ไขราคาเครื่องเล่นที่ต้องการลบในลิสต์ A ให้เป็น 0
        else:
            print('"%s" not found' %name)  # กรณีไม่พบชื่อที่ต้องการลบ
        self.arrayM()  # สร้าง array เก็บราคาใหม่

    def bst(self):
        pass


H = Heartland()

H.delete('Water Fun')
#print(A)
H.insert('Aqua Bike', 50)
H.delete('W')
#print(A)
H.insert('Ap', 5)
#print(A)
H.insert('Water Fun', 125)
#print(A)
H.insert('Snow Town', 500)
# print(A)
print(H.arrayA)

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class SLList:
    def __init__(self):
        self.first = Node("Infor")

    def append(self,data):
        self.appendList(data,self.first)

    def appendList(self,data,slist):    # data = "C" ,slist = B
        data = str(data)
        if slist.next == None:          # B.next
            slist.next = Node(data)     # B.next -> C
        else:
            self.appendList(data,slist.next)

    def show(self,slist):
        if slist == None:
            return
        elif slist.next == None:
            print(slist.data)
        else :
            print(slist.data + " -> " , end = "")
            self.show(slist.next)

    def searchage(self,data,slist):
        if slist == None:
            return "Not Found "+str(data)
        elif slist.data == data:
            return int(slist.next.data)
        else:
            return self.searchage(data,slist.next)

    def searchheight(self,data,slist):
        if slist == None:
            return "Not Found "+str(data)
        elif slist.data == data:
            return int(slist.next.next.data)
        else:
            return self.searchheight(data,slist.next)

    def searchcard(self,data,slist):
        if slist == None:
            return "Not Found "+str(data)
        elif slist.data == data:
            return slist.next.next.next.data
        else:
            return self.searchcard(data,slist.next)

    def inforname(self):  # เพิ่มชื่อลูกค้า
        name = input("Name:")
        if name.isalpha()==True:
            self.append(name)
            self.inforage()
        else:
            print("Please enter letters only")
            self.inforname()

    def inforage(self):  # เพิ่มอายุลูกค้า
        age = input("Age:")
        try:
            age = int(age)
            self.append(age)
        except:
            print("Please enter a number")
            self.inforage()


    def card(self,data):
        self.append(data)

list = SLList()
list.inforname()
list.card("S")
# name = input("Name:")
# list.append(name)
# age = input("Age:")
# list.append(age)
# height = input("Height:")
# list.append(height)
# name = input("Name:")
# list.append(name)
# age = input("Age:")
# list.append(age)
# height = input("Height:")
# list.append(height)

list.show(list.first)

print(list.searchage("A",list.first))

H.insert('Water', 15)
#print(A)
H.insert('Snow Town', 500)
# print(A)
list.inforname()
list.card("N")
list.show(list.first)

print(list.searchheight("p",list.first))

list.inforname()
list.card("B")
list.show(list.first)

print(list.searchcard("t",list.first))
