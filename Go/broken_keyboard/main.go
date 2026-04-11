// https://quera.org/problemset/157641
// -----------------------------------
package keyboard

import (
	"strings"
	"unicode"
)

const shiftKey rune = '↑'

type Keyboard struct {
	durability int
	counts     map[rune]int
}

func NewKeyboard(durability int) *Keyboard {
	return &Keyboard{
		durability: durability,
		counts: map[rune]int{
			shiftKey: durability,
		},
	}
}

func (keyboard *Keyboard) Enter(inp string) string {
	var sb strings.Builder

	for _, r := range inp {
		var baseKey rune
		var needsShift bool
		var outputChar rune = r

		switch {
		case unicode.IsUpper(r):
			needsShift = true
			baseKey = unicode.ToLower(r)
		case r == '!':
			needsShift = true
			baseKey = '1'
		case r == '?':
			needsShift = true
			baseKey = '/'
		default:
			needsShift = false
			baseKey = r
		}

		if needsShift {
			if keyboard.counts[shiftKey] > 0 {
				keyboard.counts[shiftKey]--
			} else {
				outputChar = baseKey
			}
		}

		press_counts, exists := keyboard.counts[baseKey]
		if !exists {
			keyboard.counts[baseKey] = keyboard.durability
			press_counts = keyboard.durability
		}

		if press_counts > 0 {
			keyboard.counts[baseKey]--
			sb.WriteRune(outputChar)
		}
	}

	return sb.String()
}
