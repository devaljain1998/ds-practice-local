package main

import (
	"context"
	"fmt"
	"os"
	"os/signal"
	"sync"
	"time"
)

func worker(ctx context.Context, id int, jobs <-chan int, wg *sync.WaitGroup) {
	defer wg.Done()
	for {
		select {
		case <-ctx.Done():
			fmt.Printf("Worker %d shutting down.\n", id)
			return
		case job, ok := <-jobs:
			if !ok {
				fmt.Printf("Worker %d: job channel closed.\n", id)
				return
			}
			fmt.Printf("Worker %d processing job %d\n", id, job)
			time.Sleep(1 * time.Second) // simulate processing
		}
	}
}

func main() {
	const workerCount = 4
	const totalJobs = 10

	jobs := make(chan int, totalJobs)
	ctx, cancel := context.WithCancel(context.Background())
	var wg sync.WaitGroup

	// Start workers
	for i := 1; i <= workerCount; i++ {
		wg.Add(1)
		go worker(ctx, i, jobs, &wg)
	}

	// Handle interrupt (Ctrl+C)
	stop := make(chan os.Signal, 1)
	signal.Notify(stop, os.Interrupt)

	go func() {
		<-stop
		fmt.Println("\nReceived shutdown signal. Cancelling context...")
		cancel()
	}()

	// Send jobs
	for i := 1; i <= totalJobs; i++ {
		select {
		case <-ctx.Done():
			fmt.Println("Main: Context cancelled, stopping job submission.")
			break
		case jobs <- i:
		}
	}
	close(jobs)

	// Wait for all workers to finish
	wg.Wait()
	fmt.Println("All workers finished. Exiting.")
}
