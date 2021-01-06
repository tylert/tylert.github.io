package main

import (
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	// http.Handle("/", http.FileServer(http.Dir(".")))
	http.Handle("/", handlerWrapper(http.FileServer(http.Dir("."))))
	http.HandleFunc("/moo", moo)

	// XXX FIXME TODO Stick in a stylesheet too

	fmt.Println(":8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		panic(err)
	}
}

func handlerWrapper(h http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		fmt.Println(r.URL)
		h.ServeHTTP(w, r)
	})
}

func moo(w http.ResponseWriter, r *http.Request) {
	pngBytes, err := ioutil.ReadFile("moo.png")
	if err != nil {
		panic(err)
	}
	encodedString := base64.StdEncoding.EncodeToString(pngBytes)

	fmt.Println(r.RemoteAddr + " /moo")

	// XXX FIXME TODO Stick in a stylesheet too

	w.Header().Set("Content-Type", "text/html")
	w.Write([]byte("<!DOCTYPE html><html><head></head><body>"))
	w.Write([]byte("<div>"))
	w.Write([]byte(r.RemoteAddr))
	w.Write([]byte("</div>"))
	w.Write([]byte("<img src=\"data:image/png;base64,"))
	// base64 encoded payload
	w.Write([]byte(encodedString))
	w.Write([]byte("\"></body></html>"))
}

// https://stackoverflow.com/questions/46021330/how-can-i-read-a-header-from-an-http-request-in-golang
// https://www.alexedwards.net/blog/golang-response-snippets
// https://tutorialedge.net/golang/creating-restful-api-with-golang/#building-our-router
// https://www.sanarias.com/blog/1214PlayingwithimagesinHTTPresponseingolang
// https://www.devdungeon.com/content/working-images-go
// https://freshman.tech/snippets/go/image-to-base64/
// https://stackoverflow.com/questions/50889810/go-set-header-for-all-handlers
// https://golang.org/doc/articles/wiki/
// https://cryptic.io/go-http/
// https://medium.com/rungo/running-multiple-http-servers-in-go-d15300f4e59f
// https://golang.org/src/net/http/server.go
