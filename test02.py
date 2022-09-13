A = {'Aqua Bike': 55, 'BlackHole Coaster': 140, 'Giant House': 89, 'Grandcar': 70,
     'Heart wheel': 85, 'Horror Tower': 110, 'Hurricane': 160, 'Kart Rider': 100,
     'Pegasus': 80, 'Spaceship': 60, 'Raptor': 115, 'Sky Cab': 90, 'Sky Coaster': 180,
     'Snow Town': 200, 'Super Splash': 130, 'Tornado': 170, 'Vikings': 150,
     'Water Fun': 125, '4D Adventure': 120}


class Heartland:
    def __init__(self):  # ประกาศตัวแปร
        pass

    def arrayM(self):  # ฟังก์ชันสร้าง array เพื่อเก็บเฉพาะราคาของเครื่องเล่น
        arrayA = []
        for x in A:
            if A[x] != 0:
                arrayA.append(A[x])
        return arrayA

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

    def heapify(A, n, i):
        largest = i  # หาค่าที่ใหญ่ที่สุดในรูท
        l = 2 * i + 1     # ซ้าย = 2*i + 1
        r = 2 * i + 2     # ขวา = 2*i + 2
 
        if l < n and A[largest] < A[l]: #ถ้าฝั่งซ้ายมีค่ามากกว่ารูท ค่านั้นจะเป็นค่าที่ใหญ่ที่สุด
            largest = l
 
        if r < n and A[largest] < A[r]: #ถ้าฝั่งขวามีค่ามากกว่าค่าmax ค่านั้นจะเป็นค่าที่ใหญ่ที่สุด
            largest = r
 
        if largest != i: #ถ้าค่ารูทนั้นไม่ได้มีค่าใหญ่ที่สุด
            A[i], A[largest] = A[largest], A[i]  # สลับกับรูทที่มีค่าใหญ่ที่สุด แล้วทำการHeapต่อไป
 
            heapify(A, n, largest)
 
 
    def heapSort(A):
        n = len(A)
 
        for i in range(n//2 - 1, -1, -1): #สร้างค่าMAX HEAP
            heapify(A, n, i)
 
        for i in range(n-1, 0, -1):
            A[i], A[0] = A[0], A[i]  # สลับค่าที่ใหญ่กว่าขึ้นไปข้างบน
            heapify(A, i, 0)


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
print(A)
H.insert('Snow Town', 500)
print(A)

heapSort(A)
n = len(A)
print("Sorted array is")
for i in range(n):
    print("%d" % A[i])



