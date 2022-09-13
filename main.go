package main

import (
	"fmt"
)

//In this version of the game, the player won't die immediately after being hit by the wizard.
func main() {
	var pName string

	fmt.Print("Welcome Wizard, insert your name:")
	fmt.Scan(&pName)
	fmt.Printf("Your name is %s? What a stupid name.\n", pName)
}

//Struct is basically a class. It needs to be initialized via a method.
type Player struct {
	Name   string
	Level  int
	Health int
}

func generatePlayer(name string) *Player {
	p := Player{Name: name}
	return &p
}

/*func generatePlayer(name string) *Player {
	p := Player{Name: name}
	return &p
}*/
