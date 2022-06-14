package main

import (
	"errors"
	"fmt"
	"os"

	"github.com/btcsuite/btcutil/base58"
	"github.com/google/uuid"
	// "github.com/nicksnyder/basen"
)

type base58Encoder struct{}

func (enc base58Encoder) Encode(lluu uuid.UUID) string {
	return base58.Encode(lluu[:])
}

func (enc base58Encoder) Decode(shuu string) (uuid.UUID, error) {
	return uuid.FromBytes(base58.Decode(shuu))
}

func genv3(name string, space string) (uuid.UUID, error) {
	switch space {
	case "DNS":
		return uuid.NewMD5(uuid.NameSpaceDNS, []byte(name)), nil
	case "OID":
		return uuid.NewMD5(uuid.NameSpaceOID, []byte(name)), nil
	case "URL":
		return uuid.NewMD5(uuid.NameSpaceURL, []byte(name)), nil
	case "X500":
		return uuid.NewMD5(uuid.NameSpaceX500, []byte(name)), nil
	default:
		return uuid.Nil, errors.New("Invalid namespace")
	}
}

func genv4() (uuid.UUID, error) {
	lluu, err := uuid.NewRandom()
	return lluu, err
}

func genv5(name string, space string) (uuid.UUID, error) {
	switch space {
	case "DNS":
		return uuid.NewSHA1(uuid.NameSpaceDNS, []byte(name)), nil
	case "OID":
		return uuid.NewSHA1(uuid.NameSpaceOID, []byte(name)), nil
	case "URL":
		return uuid.NewSHA1(uuid.NameSpaceURL, []byte(name)), nil
	case "X500":
		return uuid.NewSHA1(uuid.NameSpaceX500, []byte(name)), nil
	default:
		return uuid.Nil, errors.New("Invalid namespace")
	}
}

// https://www.ietf.org/id/draft-peabody-dispatch-new-uuid-format-03.html
// ^^ UUIDv6, UUIDv7, UUIDv8

func main() {
	// default alphabet '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz' (base57)
	// desired alphabet '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz' (base58)

	enc := base58Encoder{}
	// lluu, err := genv3("python.org", "DNS")
	// lluu, err := genv4()
	// lluu, err := genv5("python.org", "DNS")
	// lluu, err := uuid.Parse("cd5d0bff-2444-5d26-ab53-4f7db1cb733d")
	lluu, err := enc.Decode("SMqCfPLDiH5aTTgLmGR4np")

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	shuu := enc.Encode(lluu)
	fmt.Println(shuu)
	fmt.Println(lluu)
}

// https://github.com/yeqown/go-qrcode  generating a barcode bitmap
// https://github.com/signintech/gopdf  generating a PDF
