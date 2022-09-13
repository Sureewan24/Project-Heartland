import sys

A = {'Aqua Bike': 55, 'BlackHole Coaster': 140, 'Giant House': 89, 'Grandcar': 70,
     'Heart wheel': 85, 'Horror Tower': 110, 'Hurricane': 160, 'Kart Rider': 100,
     'Pegasus': 80, 'Spaceship': 60, 'Raptor': 115, 'Sky Cab': 90, 'Sky Coaster': 180,
     'Snow Town': 200, 'Super Splash': 130, 'Tornado': 170, 'Vikings': 150,
     'Water Fun': 125, '4D Adventure': 120}


class Heartland:
    def __init__(self):  # ประกาศตัวแปร
        self.arrayA = []
        self.minHeap = MinHeap(100)

    def arrayM(self):  # ฟังก์ชันสร้าง array เพื่อเก็บเฉพาะราคาของเครื่องเล่น
        self.arrayA = []
        for x in A:
            if A[x] != 0:
                self.arrayA.append(A[x])
        return self.arrayA

    def max(self,n1, n2):
        if n1 > n2:
            return n1
        else:
            return n2

    def sort(self):  # ฟังก์ชันเพื่อเรียงค่าใน arrayA จากน้อยไปมาก
        arrayA = self.arrayM()
        l = len(arrayA)
        for i in range(1, l + 1):
            for j in range(i - 1, 0, -1):
                if not max(arrayA[j], arrayA[j - 1]) == arrayA[j]:
                    temp = arrayA[j]
                    arrayA[j] = arrayA[j - 1]
                    arrayA[j - 1] = temp

        print(arrayA)

    def insert(self, name, cost):  # เพิ่มเครื่องเล่น/ปรับราคา
        A[name] = cost  # แก้ไขในลิสต์ A
        self.arrayM()  # สร้าง array เก็บราคาใหม่
        self.sort()  # นำอะเรย์เก็บราคามาเรียง

    def delete(self, name):  # ลบเครื่องเล่น
        if name in A:
            A[name] = 0  # แก้ไขราคาเครื่องเล่นที่ต้องการลบในลิสต์ A ให้เป็น 0
        else:
            print('"%s" not found' %name)  # กรณีไม่พบชื่อที่ต้องการลบ
        self.arrayM()  # สร้าง array เก็บราคาใหม่
        self.sort()  # นำอะเรย์เก็บราคามาเรียง

    def bst(self):
        bstA = H.arrayA
        for n in bstA:
            self.minHeap.insert(n)
        self.minHeap.Print()
        print(self.minHeap.level1)
        print(self.minHeap.level2)
        print(self.minHeap.level3)
        print(self.minHeap.level4)
        print(self.minHeap.level5)


class MinHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1
        self.level1 = []
        self.level2 = []
        self.level3 = []
        self.level4 = []
        self.level5 = []

    def parent(self, pos):
        return pos // 2

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def Print(self):
        self.level1 = []
        self.level2 = []
        self.level3 = []
        self.level4 = []
        self.level5 = []
        for i in range(1, 100):
            if self.Heap[i]!=0:
                if i ==1:
                    self.level1.append(self.Heap[i])
                elif i<=(1+2):
                    self.level2.append(self.Heap[i])
                elif i<=(1+2+4):
                    self.level3.append(self.Heap[i])
                elif i<=(1+2+4+8):
                    self.level4.append(self.Heap[i])
                elif i<=(1+2+4+8+16):
                    self.level5.append(self.Heap[i])

class Node :
    def __init__(self,data=None):
        self.data =data
        self.next = None

class slist :
    def __init__(self):
        self.first =None
    def append(self,data):
        self.appendList(data,self.first)
    def appendList(self,data,slist):
        data = str(data)
        if slist.next == None :
            slist.next = Node(data)
        else :
            self.appendList(data,slist.next)
    def show(self,slist):
        if slist == None :
            return
        elif slist.next == None:
            print(slist.data)
        else :
            print(slist.data + "->",end="")
            self.show(slist.next)
    def search(self,data,slist):
        if slist == None :
            return False
        elif slist.data ==data :
            return True
        else :
            return self.search(data,slist.next)
    def delete(self,data):
        slist=self.first
        temp = self.search(data,slist)
        if temp == False:
            return
        else :
            if slist.data == data
                self.first = slist.next
                slist =None
                return
        while temp ==True :
            if slist.data ==data :
                break
            prev = slist
            slist = slist.next
        prev.next = slist.next
        slist = None


H = Heartland()
H.sort()
H.delete('Water Fun')
print(A)
H.insert('Aqua Bike', 50)
H.delete('W')
print(A)
H.insert('Ap', 5)
print(A)
H.insert('Water Fun', 125)
#print(A)
H.insert('Snow Town', 500)
# print(A)
print(H.arrayA)
H.bst()

list=slist()
list.first =Node("A")