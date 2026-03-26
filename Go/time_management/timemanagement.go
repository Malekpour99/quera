// https://quera.org/problemset/181680
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
	timeInfo := strings.Split(scanner.Text(), " ")
	workDuration, _ := strconv.Atoi(timeInfo[0])
	studyDuration, _ := strconv.Atoi(timeInfo[1])
	interferenceDuration, _ := strconv.Atoi(timeInfo[2])
	aggregatedDuration := workDuration + studyDuration - interferenceDuration
	restDuration := 24 - aggregatedDuration

	fmt.Println(restDuration)
}
