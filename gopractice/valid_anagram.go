package anagram

import "reflect"

func isAnagram(s string, t string) bool {
	mp1 := make(map[rune]int)
	for _, ch := range s {
		mp1[ch]++
	}

	mp2 := make(map[rune]int)
	for _, ch := range t {
		mp2[ch]++
	}

	return reflect.DeepEqual(mp1, mp2)
}
