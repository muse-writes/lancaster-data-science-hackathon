# Beamer slides Makefile
# Build with `make`, clean with `make clean`.

TEX      := main.tex
PDF      := $(TEX:.tex=.pdf)
LATEXMK  := latexmk
# XeLaTeX is required for the Metropolis theme / Fira Sans fonts.
LATEXMK_FLAGS := -xelatex -interaction=nonstopmode -halt-on-error -shell-escape

.PHONY: all clean view

all: $(PDF)

$(PDF): $(TEX) $(wildcard *.bib) $(wildcard images/*)
	$(LATEXMK) $(LATEXMK_FLAGS) $(TEX)

view: $(PDF)
	@command -v xdg-open >/dev/null 2>&1 && xdg-open $(PDF) \
		|| command -v open >/dev/null 2>&1 && open $(PDF) \
		|| echo "Open $(PDF) manually."

clean:
	$(LATEXMK) -C $(TEX)
	rm -rf $(foreach ext,aux bbl bcf fdb_latexmk fls log out run.xml snm synctex.gz toc vrb,$(basename $(TEX)).$(ext))
