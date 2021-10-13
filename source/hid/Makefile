SHELL := /usr/bin/env bash

GENERATED_FILES = \
  keyboard_matrix_1stplayer_dk_5_0.png \
  keyboard_matrix_cm_storm_qfr-i.png \
  keyboard_matrix_durgod_k3x0.png

.PHONY: all
all: $(GENERATED_FILES)

%.png: %.txt
	@ditaa --overwrite --round-corners $^ $@

.PHONY: clean
clean:
	@rm -f $(GENERATED_FILES)
