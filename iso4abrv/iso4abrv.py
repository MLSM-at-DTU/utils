import bibtexparser
from iso4 import abbreviate
import nltk

import re


def iso4abrv(bibtex_references_as_string):
    def _abrv(full):
        return re.sub(pattern=r'\s+',
                      repl=' ',
                      string=abbreviate(full))

    def _to_bibkey(full):
        return ''.join(
            filter(str.isalnum,
                   map(lambda word: word[0].upper(), _abrv(full=full).split(' '))
                   )
        )

    def _get_journals(bib_strings):
        return frozenset(map(
            lambda e: e['journal'],
            filter(lambda e: 'journal' in e,
                   bibtexparser.loads(bib_strings).entries)))

    def _journals_to_bib(bib_strings):
        return dict(map(
            lambda full: (full, {'bibkey': _to_bibkey(full), 'abrv': _abrv(full)}),
            _get_journals(bib_strings)
        )
        )

    def _to_bibstring(bibkey, value):
        return '@STRING{%s = "%s"}' % (bibkey, value)

    nltk.download('wordnet')
    parsed = bibtexparser.loads(bibtex_references_as_string)
    mapping = _journals_to_bib(bib_strings=bibtex_references_as_string)
    for entry in filter(lambda e: 'journal' in e, parsed.entries):
        entry['journal'] = mapping[entry['journal']]['bibkey']
    abbreviated = bibtexparser.dumps(parsed)
    with \
            open('abbrvref.bib', 'w') as outref_f, \
            open('jourabrv.bib', 'w') as outabrv_f, \
            open('jourfull.bib', 'w') as outfull_f:
        outref_f.write(
            re.sub(pattern=r'journal\s+=\s+[{]([^}]*)[}]',
                   repl=r'journal = \1',
                   string=abbreviated))
        outabrv_f.write('\n'.join(map(
            lambda full: _to_bibstring(mapping[full]['bibkey'], mapping[full]['abrv']),
            mapping
        )))
        outfull_f.write('\n'.join(map(
            lambda full: _to_bibstring(mapping[full]['bibkey'], full),
            mapping
        )))
