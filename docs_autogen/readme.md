# docs autogen

parts of the documentation are generated using some tools.

These files are:

```
simpleui git repository
├── docs/
│   ├── manual.md                   << output file
│   └── call_reference.md           << output file
├── docs_autogen/
│   ├── manual
│   │   ├── manual.py               << translator with CWD = repo root
│   │   └── markdown_source_files/
│   ├── call_reference
│   │   ├── call_reference.py       << translator with CWD = repo root
│   │   └── markdown_source_files/
```
