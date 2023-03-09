from random import shuffle
from time import perf_counter


mas = [x for x in range(1, 10001)]
shuffle(mas)


class Sorting:
    def __init__(self, array: list):
        self.array = array
        self.index = len(self.array)

    def bubble_sorting(self) -> list:
        start0 = perf_counter()
        # we need one fewer circles than the numbers of the array cause of
        # the last object is already sorted
        for circle in range(self.index - 1):
            # adding minus one circle to avoid repeating comparison between
            # 2 already sorted objects
            for i in range(self.index - 1 - circle):
                if self.array[i] > self.array[i + 1]:
                    # change objects places if the left is more than the right
                    self.array[i], self.array[i + 1] = self.array[i + 1], \
                    self.array[i]
        end0 = perf_counter()
        print(end0-start0, 'bubble sort')
        return self.array

    def selection_sorting(self) -> list:
        start1 = perf_counter()
        # i equals to the numbers of sorted values
        for i in range(self.index):
            # take the first object as the minimum
            min_value = i
            # iterating over unsorted objects
            for j in range(i + 1, self.index):
                if self.array[j] < self.array[min_value]:
                    min_value = j
            # the first object is changed with the lowest object
            self.array[i], self.array[min_value] = self.array[min_value], \
            self.array[i]
        end1 = perf_counter()
        print(end1 - start1, 'selection sort')
        return self.array

    def insertion_sorting(self) -> list:
        start2 = perf_counter()
        # start from the second object(index=1), cause of it is believed
        # that the first object is already sorted
        for i in range(1, self.index):
            inserted_elem = self.array[i]
            # save the link to the past object
            past_elem = i - 1
            # if sorted objects more than inserted_elem
            while past_elem >= 0 and self.array[past_elem] > inserted_elem:
                self.array[past_elem + 1] = self.array[past_elem]
                past_elem -= 1
            # insert object
            self.array[past_elem + 1] = inserted_elem
        end2 = perf_counter()
        print(end2 - start2, 'insertion sort')
        return self.array

    def heapify(self, array, heap_length, i):
        # Initialize largest as root
        largest = i
        left_branch = (2 * i) + 1
        right_branch = (2 * i) + 2

        # if left branch of root exists and is
        # bigger than root
        if left_branch < heap_length and array[left_branch] > array[largest]:
            largest = left_branch

        # the same with the right branch
        if right_branch < heap_length and array[right_branch] > array[largest]:
            largest = right_branch

        # change root if largest is not root anymore
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            # Heapify the new root element to ensure it's the largest
            self.heapify(array, heap_length, largest)

    def heap_sort(self):
        start3 = perf_counter()
        # Build a maxheap from the list
        # the second means stop before the -1(the first el of the list)
        # 3rd means repetition in reverse direction,
        # reducing i by 1
        for i in range(self.index, -1, -1):
            self.heapify(self.array, self.index, i)

        # move Max Heap root to the list end
        for i in range(self.index - 1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heapify(self.array, i, 0)

        end3 = perf_counter()
        print(end3 - start3, 'heap sort')
        return self.array


def merge_lists(f_array, s_array):
    sorted_list = []
    # pointing on the first elems of first and second arrays
    f_array_index = s_array_index = 0
    # checking if elem index is smaller the array
    while f_array_index < len(f_array) and s_array_index < len(s_array):
        # finding the smaller elem from 2 lists
        if f_array[f_array_index] < s_array[s_array_index]:
            sorted_list.append(f_array[f_array_index])
            f_array_index += 1
        else:
            sorted_list.append(s_array[s_array_index])
            s_array_index += 1
    # one of the lists may stop and the another one can be continued
    # we need to check which one
    if f_array_index < len(f_array):
        sorted_list += f_array[f_array_index:]
    if s_array_index < len(s_array):
        sorted_list += s_array[s_array_index:]
    return sorted_list


def merge_sort(array: list):
    # if array contains only 1 el then its already sorted
    if len(array) <= 1:
        return array
    # finding the array's middle
    middle = len(array) // 2
    # sorting and merging left and right
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    # merging sorted lists to the final list
    return merge_lists(left, right)


def quicksort(array: list, fst: int, lst: int) -> list:
    # if 1 elem >= last elem, it means the list already sorted
    if fst >= lst:
        return array

    i, j = fst, lst
    # take the list middle as the root(pivot)
    root = array[(fst+lst)//2]

    while i <= j:
        while array[i] < root:
            i += 1
        while array[j] > root:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    quicksort(array, fst, j)
    quicksort(array, i, lst)
    return array


Sorting(mas).bubble_sorting()
Sorting(mas).selection_sorting()
Sorting(mas).insertion_sorting()
Sorting(mas).heap_sort()
start = perf_counter()
merge_sort(mas)
end = perf_counter()
print(end-start, 'merge sort')
start_ = perf_counter()
quicksort(mas, 0, len(mas)-1)
end_ = perf_counter()
print(end_-start_, 'quicksort')
