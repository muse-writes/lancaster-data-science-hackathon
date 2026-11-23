## Slides

Beamer slides for the hackathon presentation, built with XeLaTeX.

### Build

```bash
make        # build main.pdf (XeLaTeX via latexmk)
make view   # build and open the PDF
make clean  # remove build artefacts
```

`main.tex` is the entry point. Edit the metadata block at the top and add
frames between `\begin{document}` / `\end{document}`.

### Code snippets

`listings` is set up by default with a readable light style. Mark any frame
containing verbatim code as `[fragile]`:

```latex
\begin{frame}[fragile]{Demo}
  \begin{lstlisting}[language=Python]
  pucks = load_mouse_brain_data()
  \end{lstlisting}
  Inline: \code{load_mouse_brain_data()}.
  Whole file: \lstinputlisting{../src/foo.py}
\end{frame}
```

`minted` (true syntax highlighting via Pygments) is also available — the
Makefile already passes `-shell-escape`. Uncomment the `minted` block near the
preamble of `main.tex` and use `\begin{minted}{python} ... \end{minted}` or
`\inputminted{python}{file.py}`.

### Dependencies

Requires a TeX distribution with `xelatex` and `latexmk` (e.g. TeX Live),
plus the `metropolis` Beamer theme and Fira Sans fonts. On Debian/Ubuntu:

```bash
sudo apt install texlive-latex-extra texlive-fonts-extra texlive-xetex \
                 latexmk fonts-firacode
```
