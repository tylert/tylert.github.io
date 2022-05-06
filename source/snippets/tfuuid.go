package main

import (
	"fmt"
	"github.com/btcsuite/btcutil/base58"
	"github.com/google/uuid"
	"github.com/lithammer/shortuuid"
)

// https://github.com/lithammer/shortuuid
// https://pkg.go.dev/github.com/lithammer/shortuuid

// https://github.com/skorokithakis/shortuuid
// https://pypi.org/project/shortuuid/

type base58Encoder struct{}

func (enc base58Encoder) Encode(u uuid.UUID) string {
	return base58.Encode(u[:])
}

func (enc base58Encoder) Decode(s string) (uuid.UUID, error) {
	return uuid.FromBytes(base58.Decode(s))
}

func main() {
	// default alphabet '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz' (base57)
	// desired alphabet '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz' (base58)
	enc := base58Encoder{}
	id := shortuuid.NewWithEncoder(enc)
	fmt.Println(id)
}
