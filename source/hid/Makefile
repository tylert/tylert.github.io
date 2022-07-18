SHELL := /usr/bin/env bash

GENERATED_FILES = \
  keyboard_matrix_cm_storm_qfr-i.png \
  keyboard_matrix_durgod_k3x0.png \
  keyboard_matrix_yak87.png

.PHONY: all
all: $(GENERATED_FILES)

%.png: %.txt
	@MAVEN_OPTS=-Djava.aws.headless=true ditaa --overwrite --round-corners $^ $@

.PHONY: clean
clean:
	@rm -f $(GENERATED_FILES)
