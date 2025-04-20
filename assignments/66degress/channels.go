import "fmt"

func foo1(chan string) {
	fmt.Println("foo1")
	chan <- "something"
}

func oddPrinter(int n, oddChannel <-chan int) {
	i := 1 
	while i < n {
		oddChannel <- i
		i += 2
	}
	return
}

func evenPrinter(int n, evenChannel <-chan int) {
	i := 0
	while i < n {
		evenChannel <- i
		i += 2
	}
	return
}

func main() {
	messages := make(chan string)
	go foo1(messages)
	// Wait for this function to complete
	<- messages

	oddChannel := make(chan int)
	evenChannel := make(chan int)

	go oddPrinter(10, oddChannel)
	go evenPrinter(10, evenChannel)

	while true {
		select {
		case num <- evenChannel:
			fmt.Println(num)
		case num <- oddChannel:
			fmt.Println(num)
		default:
			fmt.Println("waiting")
		}
	}  		
}