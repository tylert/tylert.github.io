SHELL := /usr/bin/env bash

GENERATED_FILES = \
  matrix_cm_storm_qfr-i.png \
  matrix_durgod_k3x0.png

.PHONY: all
all: $(GENERATED_FILES)

%.svg: %.txt
	@svgbob_cli -o $@ $^

%.png: %.svg
	@magick $^ $@

.PHONY: clean
clean:
	@rm -f $(GENERATED_FILES)
