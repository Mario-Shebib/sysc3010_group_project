TARGET=L3-T-2_Proposal

# $(TARGET).pdf is phony so that we always call latexmk
.PHONY: $(TARGET).pdf all clean

all: $(TARGET).pdf

$(TARGET).pdf: $(TARGET).tex
	latexmk -pdf --bibtex -pdflatex="pdflatex -interaction=nonstopmode" -use-make $<

clean:
	latexmk -bibtex -C

