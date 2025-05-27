package main

import (
	"fmt"
	"time"
)

func worker(workerId int, jobs <-chan int, result chan<- int) {
	for jobId := range jobs {
		fmt.Println(workerId, "started job: ", jobId)
		time.Sleep(1 * time.Second)
		fmt.Println(workerId, "processed job: ", jobId)
		result <- jobId * 2
	}
}

func main() {
	const numJobs = 5
	const workers = 3
	jobs := make(chan int)
	result := make(chan int, numJobs)

	for i := 0; i < workers; i++ {
		go worker(i+1, jobs, result)
	}

	for i := 0; i < numJobs; i++ {
		jobs <- i + 1
	}
	close(jobs)

	for i := 0; i < numJobs; i++ {
		<-result
	}
	/**
	for r := range result {
		fmt.Println(r)
	}**/

}
