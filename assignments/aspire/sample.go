// Write a Golang function that compares two nested map[string]interface{} JSON objects and returns the differences, excluding keys matching a pattern (e.g., keys containing "id" or "timestamp").

package main

import (
	"strings"
)

func main() {
	mp1 := make(map[string]interface{})
	mp["key"] = "string"
	mp["invalid"] = "some_invalid_string"
	mp["dkfnondg_timestamp"] = "dfinadiogfn"

	firstListMp := make(map[string]int)
	secondListMp := make(map[string]int)

	// This is my first map level
	for _, innerMap := range mp1 {
		// This is my second map level
		for key, val := range innerMap {
			// Filtering out the strings that contains "id" or "timestamp"
			if !strings.Contains("id") || !strings.Contains("timestamp") {
				firstListMp[key]++
			}
		}
	}

	mp2 := make(map[string]interface{})
	mp["key"] = "string"
	mp["invalid"] = "some_invalid_string"
	mp["dkfnondg_timestamp"] = "dfinadiogfn"

	// This is my first map level
	for _, innerMap := range mp2 {
		// This is my second map level
		for key, val := range innerMap {
			// Filtering out the strings that contains "id" or "timestamp"
			if !strings.Contains("id") || !strings.Contains("timestamp") {
				secondListMp[key]++
			}
		}
	}

	// I need to iterate over one map and check from another and maintain a differences list
	differences := make([]string, 0)
	for key, _ := range firstListMp {
		// check if this is in secondListMap:
		key2, found := secondListMp[key]
		if !found {
			differences = append(differences, key2)
		}
	}

	for key, _ := range secondListMp {
		// check if this is in secondListMap:
		key2, found := firstListMp[key]
		if !found {
			differences = append(differences, key2)
		}
	}

	return differences

}

// {
// 	"k1": {
// 		"key": eqor
// 		"timestamp": eaogk
// 		"d1":

// 	}
// }

// {
// 	"k1": {
// 		"key": eqor
// 		"timestamp": eaogk
// 		"d2":

// 	}
// }

// Output: d1, d2
