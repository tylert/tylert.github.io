package main

import (
	"errors"
	"fmt"
	"os"

	"github.com/btcsuite/btcd/btcutil/base58"
	"github.com/google/uuid"
	// "github.com/nicksnyder/basen"
)

func Genv3(name string, space string) (uuid.UUID, error) {
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

func Genv4() (uuid.UUID, error) {
	lluu, err := uuid.NewRandom()
	return lluu, err
}

func Genv5(name string, space string) (uuid.UUID, error) {
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

type base58Encoder struct{}

func (enc base58Encoder) Encode(lluu uuid.UUID) string {
	return base58.Encode(lluu[:])
}

func (enc base58Encoder) Decode(shuu string) (uuid.UUID, error) {
	return uuid.FromBytes(base58.Decode(shuu))
}

func main() {
	// base57    '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
	// base58    '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
	// base62    '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	// base64    '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
	// base64url '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'

	// lluu, err := Genv3("python.org", "DNS")
	// lluu, err := Genv4()
	// lluu, err := Genv5("python.org", "DNS")
	lluu, err := uuid.Parse("cd5d0bff-2444-5d26-ab53-4f7db1cb733d")

	enc := base58Encoder{}
	// lluu, err := enc.Decode("SMqCfPLDiH5aTTgLmGR4np")
	shuu := enc.Encode(lluu)

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	fmt.Println(lluu)
	fmt.Println(shuu)
}

// https://github.com/yeqown/go-qrcode  generating a barcode bitmap
// https://github.com/signintech/gopdf  generating a PDF
// https://datatracker.ietf.org/doc/html/draft-peabody-dispatch-new-uuid-format-03
// https://datatracker.ietf.org/doc/html/draft-msporny-base58-03
