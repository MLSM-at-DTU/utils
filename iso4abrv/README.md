# Abbreviate Journal Names in Bibliography

This utility abbreviates journal names in BibLaTeX entries per ISO-4 standard.

Creates 3 files:
1. **abbrvref.bib** -- the abbreviated entries.
1. **jourabrv.bib** -- BibLaTeX strings for the abbreviated journal names.
1. **jourfull.bib** -- BibLaTeX strings for the full journal names.

### Example usage

```python
iso4abrv(open('example.bib').read())
```
Then in LaTeX:
```latex
\bibliography{jourabrv,abbrvref}
```
