# Abbreviate Journal Names in LaTeX Bibliography

This utility abbreviates journal names in BibLaTeX entries per ISO-4 standard. It outputs 3 files:
1. **abbrvref.bib** -- the abbreviated entries.
1. **jourabrv.bib** -- BibLaTeX strings for the abbreviated journal names.
1. **jourfull.bib** -- BibLaTeX strings for the full journal names (in case you need to revert).

Results may be imperfect, so always check the output for errors.

### Example usage

```python
from iso4abrv import iso4abrv

iso4abrv(open('example.bib').read())
```
Then in LaTeX:
```latex
\bibliography{jourabrv,abbrvref}
```
