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

func (enc base58Encoder) Encode(uu uuid.UUID) string {
	return base58.Encode(uu[:])
}

func (enc base58Encoder) Decode(str string) (uuid.UUID, error) {
	return uuid.FromBytes(base58.Decode(str))
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
	uu, err := uuid.NewRandom()
	return uu, err
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

func main() {
	// default alphabet '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz' (base57)
	// desired alphabet '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz' (base58)

	enc := base58Encoder{}
	// uu, err := genv3("python.org", "DNS")
	uu, err := genv4()
	// uu, err := genv5("python.org", "DNS")

	// uu, err := uuid.Parse("cd5d0bff-2444-5d26-ab53-4f7db1cb733d")
	// uu, err := enc.Decode("SMqCfPLDiH5aTTgLmGR4np")

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	id := enc.Encode(uu)
	fmt.Println(id)
}

// https://github.com/skorokithakis/shortuuid  python implementation that is compatible
// https://pypi.org/project/shortuuid/  python implementation that is compatible
// https://github.com/yeqown/go-qrcode  generating a barcode bitmap
// https://github.com/signintech/gopdf  generating a PDF
