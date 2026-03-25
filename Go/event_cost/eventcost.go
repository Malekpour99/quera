// https://quera.org/problemset/306523
// -----------------------------------

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	n, scnErr := strconv.Atoi(scanner.Text())
	if scnErr != nil {
		return
	}

	var totalCost int

	// can be simplified using range n but Quera compiler does not support it
	for i := 0; i < n; i++ {
		scanner.Scan()
		var costInfo []string = strings.Split(scanner.Text(), " ")
		attendeeCount, _ := strconv.Atoi(costInfo[0])
		costPerAttendee, _ := strconv.Atoi(costInfo[1])

		totalCost += attendeeCount * costPerAttendee
	}

	fmt.Println(totalCost)
}
