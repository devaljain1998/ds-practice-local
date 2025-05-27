package main

import (
	"fmt"
	"sync"
	"time"
)

func even(start, end int, signal chan int, result chan<- int, wg *sync.WaitGroup) {
	defer wg.Done()
	for i := start; i <= end; i += 2 {
		<-signal
		result <- i
		time.Sleep(5 * time.Millisecond)
		signal <- 1
	}
}

func odd(start, end int, signal chan int, result chan<- int, wg *sync.WaitGroup) {
	defer wg.Done()
	for i := start; i <= end; i += 2 {
		<-signal
		result <- i
		signal <- 1
	}
}

func main() {
	signal := make(chan int, 1)
	result := make(chan int)
	var wg sync.WaitGroup
	wg.Add(2)

	go even(0, 10, signal, result, &wg)
	go odd(1, 9, signal, result, &wg)

	signal <- 1

	// Start a goroutine to close result channel after both even and odd are done
	go func() {
		wg.Wait()
		close(result)
	}()

	// Read results until channel is closed
	for num := range result {
		fmt.Println(num)
	}
}
