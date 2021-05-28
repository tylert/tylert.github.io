SHELL := /usr/bin/env bash

GENERATED_FILES = keyboard_matrix_durgod_k3x0.png keyboard_matrix_cm_storm_quickfire_rapid_i.png

.PHONY: all
all: $(GENERATED_FILES)

%.png: %.txt
	@ditaa --overwrite --round-corners $^ $@

.PHONY: clean
clean:
	@rm $(GENERATED_FILES)
