# argapp-ws - The argapp workspace

# Overview

TODO: The product's purpose.

Features:
 * TODO: A bullet list of features, with explanation (1-2 sentences).

Limitations:
 * TODO: A bullet list of limitations, with explanation (1-2 sentences).

# Installation

## Prerequisites

### OS

TODO: A bullet list of supported OS.

### TODO: {language} versions

TODO: A bullet list of supported language versions. `{language}` must be replaced with the language name.

### Software

TODO: A bullet list of software to install, if there are no steps provided.

## Steps

TODO: Installation steps for a simple case. May be split into several sub-sections.

# CLI

# API

# Requirements

**Requirement ID**: 0004

**Criterion ID**: 000004

## Rules

 * The workspace must contain a directory named `test`. May be nested.
 * Each requirement must have a corresponding directory `test/{RID}`.
 * `test/{RID}` must contain at least one `test_{RID}*` text file that covers at least one criterion.<br>
   The file can be a language-specific set of tests, or just a plain text with manual steps.
 * The criterion must be mentioned in the file as `test_{CID}` next to the test body.<br>
   It can be a language-specific identifier, a comment, or just a plain text.
 * Each criterion must be covered.
 * The test results are placed under `results/{RID}`.

## Requirement 0000

[Installation -> Prerequisites -> OS](https://github.com/deohayer/argapp#os)

 * Linux, tested with:
    * Ubuntu 18.04
    * Ubuntu 19.10
    * Ubuntu 20.04
    * Ubuntu 21.10
    * Ubuntu 22.04

### Criterion 000000

All tests with `.py` extension are run via pytest for each specific OS.<br>
For each specific test and OS, the results are put into the corresponding result files:
 * `results/{RID}/test_{RID}*{OS}*.log` - pytest execution result.
 * `results/{RID}/test_{RID}*{OS}*.txt` - 0 (pass) or 1 (fail).

## Requirement 0001

[Installation -> Prerequisites -> Python versions](https://github.com/deohayer/argapp#python-versions)

 * 3.6
 * 3.7
 * 3.8
 * 3.9
 * 3.10
 * 3.11

### Criterion 000001

All tests with `.py` extension are run via pytest for each specific Python version.<br>
For each specific test and version, the results are put into the corresponding result files:
 * `results/{RID}/test_{RID}*{version}*.log` - pytest execution result.
 * `results/{RID}/test_{RID}*{version}*.txt` - 0 (pass) or 1 (fail).

## Requirement 0002

[Installation -> Steps](https://github.com/deohayer/argapp#steps)

To install, run the following:
```bash
pip3 install argapp
```

### Criterion 000002

The latest release can be installed using
```bash
pip3 install argapp
```

## Requirement 0003

[Installation -> Steps](https://github.com/deohayer/argapp#steps)

To enable the completion, install [argcomplete](https://pypi.org/project/argcomplete).<br>
Refer to its documentation for the details on installation and usage.

### Criterion 000003

An argcomplete-compliant Python script written with argapp offers completion for "--".
