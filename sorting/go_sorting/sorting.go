package main

import "fmt"

func main() {
	sample := []int{3, 4, 5, 2, 1, 6, 8, 7}
	bubbleSort(sample)
}

func bubbleSort(arr []int) {
	len := len(arr)
	for i := 0; i < len-1; i++ {
		for j := 0; j < len-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
	fmt.Println("\nAfter Bubble Sorting")
	fmt.Println(arr)
}
