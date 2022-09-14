package main

import (
	"fmt"
	"math/rand"
)

//In this version of the game, the player won't die immediately after being hit by the wizard.
func main() {
	var pName string
	fmt.Print("Welcome Wizard, insert your name:")
	fmt.Scan(&pName)
	fmt.Printf("Your name is %s? What a stupid name.\n", pName)
	fmt.Printf("You are level %d wizard.", generatePlayer(pName).Level)
}

//Struct is basically a class. It needs to be initialized via a method.
type Player struct {
	Name   string
	Level  int
	Health int
}
type Wizard struct {
	Name   string
	Level  int
	Health int
}

func generatePlayer(name string) *Player {
	var level int = rand.Intn(10-1) + 1
	p := Player{Name: name, Level: level, Health: 10}
	return &p
}
func generateWizard() *Wizard {
	var wizardNames = []string{"Homer",
		"Kwon",
		"Riah",
		"Uluq-UlDudush",
		"Ravenlord"}
	var wizardName string = wizardNames[rand.Intn(10-1)+1]
	var level int = rand.Intn(10-1) + 1
	w := Wizard{Name: wizardName, Level: level, Health: 10}
	return &w
}
