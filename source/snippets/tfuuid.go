package main

import (
	"fmt"
	"github.com/btcsuite/btcutil/base58"
	"github.com/google/uuid"
	"github.com/lithammer/shortuuid"
)

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

	// Generate a new shortUUID (UUIDv4)
	id := shortuuid.NewWithEncoder(enc)

	// Shorten an existing UUID
	// uu, _ := uuid.Parse("8966e5ee-445e-401b-a921-bf5020c516d2")
	// id := enc.Encode(uu)
	// Hy5v2PaRjQhVB172zb6fpD

	// Lengthen an existing shortUUID
	// id, _ := enc.Decode("Hy5v2PaRjQhVB172zb6fpD")
	// 8966e5ee-445e-401b-a921-bf5020c516d2

	// Generate a UUIDv5
	// uu := uuid.NewSHA1(uuid.NameSpaceDNS, []byte(name))
	// uu := uuid.NewSHA1(uuid.NameSpaceOID, []byte(name))
	// uu := uuid.NewSHA1(uuid.NameSpaceURL, []byte(name))
	// uu := uuid.NewSHA1(uuid.NameSpaceX500, []byte(name))
	// id := enc.Encode(uu)

	fmt.Println(id)
}

// https://registry.terraform.io/providers/hashicorp/external/latest/docs/data-sources/data_source
// https://github.com/lithammer/shortuuid  go implementation
// https://pkg.go.dev/github.com/lithammer/shortuuid  go implementation
// https://github.com/skorokithakis/shortuuid  python implementation that is compatible
// https://pypi.org/project/shortuuid/  python implementation that is compatible
// https://github.com/yeqown/go-qrcode  generating a barcode bitmap
// https://github.com/signintech/gopdf  generating a PDF
// https://github.com/mkyc/go-terraform  making this stuff more Terraform-friendly
// https://github.com/gruntwork-io/terratest  making this stuff more Terraform-friendly
// https://www.terraform.io/language/functions/uuid  inspiration for how this might get used
// https://www.terraform.io/language/functions/uuidv5  inspiration for how this might get used
