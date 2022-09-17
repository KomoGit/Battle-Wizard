package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
)

//In this version of the game, the player won't die immediately after being hit by the wizard.
func main() {
	var pName string
	fmt.Print("Welcome Wizard, insert your name:")
	fmt.Scan(&pName)
	fmt.Printf("Your name is %s? What a stupid name. You are a level %d wizard\n", pName, generatePlayer(pName).Level)
	gameLoop(10)
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

func gameLoop(playerHealth int) {
	for playerHealth >= 0 {
		fmt.Printf("A wild wizard named %s appeared. He is level %d\n", generateWizard().Name, generateWizard().Level)
		fmt.Println("Press A to Attack\nPress B to Run Away")
		reader := bufio.NewReader(os.Stdin)
		char, _, err := reader.ReadRune()
		if err != nil {
			fmt.Print(err)
		}
		keyCode := char
		inputInterpreter(int(keyCode))
	}
}
func inputInterpreter(char int) {
	switch char {
	case 65:
		fmt.Println("Pressed A")
	case 97:
		fmt.Println("Pressed a")
	case 66:
		fmt.Println("Pressed B")
	case 98:
		fmt.Println("Pressed b")
	default:
		return
	}
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
	var wizardName string = wizardNames[rand.Intn(len(wizardNames))]
	var level int = rand.Intn(10-1) + 1
	w := Wizard{Name: wizardName, Level: level, Health: 10}
	return &w
}
