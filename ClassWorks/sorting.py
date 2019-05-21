class Array:

    def __init__(self,data):
        self.data = data

    def sort(self):


    def search(self, item):
        for idx, elem in enumerate(self.data):
            if elem == item:
                return idx
        return -1


    def bubble_sort(self, arr: list) -> list:
        length = len(arr)
        for i in range(length):
            for j in range(length-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr


    def __repr__(self):
        return  ','.join(self.data)




if __name__ == "__main__":
    arr = Array([3,5,9,1,2,4])
    arr.sort()
    print(arr)  # 1, 3, 4, 5, 6
    print(arr.search(5))   # 4


