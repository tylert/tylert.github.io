package main

import (
	"fmt"
	"github.com/anarcher/shortuuid"
)

// https://github.com/anarcher/shortuuid
// https://pkg.go.dev/github.com/anarcher/shortuuid

// https://github.com/skorokithakis/shortuuid
// https://pypi.org/project/shortuuid/

func main() {
	// default alphabet '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz' (base57)
	// desired alphabet '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz' (base58)
	id := shortuuid.NewWithAlphabet("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz")
	fmt.Println(id)
}
