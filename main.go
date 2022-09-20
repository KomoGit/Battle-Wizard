package main

import (
	"fmt"
	"math/rand"
	"os"

	"github.com/eiannone/keyboard"
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
		char, _, err := keyboard.GetSingleKey()
		keyCode := char
		inputInterpreter(int(keyCode))
		if err != nil {
			panic(err)
		}
	}
}
func inputInterpreter(char int) {
	switch char {
	case 65, 97:
		fmt.Println("Pressed A")
	case 66, 98:
		fmt.Println("Pressed B")
	case 0:
		os.Exit(0)
	default:
		fmt.Println(char)
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
