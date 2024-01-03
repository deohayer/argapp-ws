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

**Requirement ID**: TODO: 0000, a document-unique ID for a new requirement.

**Criterion ID**: TODO: 000000, a document-unique ID for a new criterion.

## Rules

 * The workspace must contain a directory named `test`. May be nested.
 * Each requirement must have a corresponding directory `test/{RID}`.
 * `test/{RID}` must contain at least one `test_{RID}*` text file that covers at least one criterion.<br>
   The file can be a language-specific set of tests, or just a plain text with manual steps.
 * The criterion must be mentioned in the file as `test_{CID}` next to the test body.<br>
   It can be a language-specific identifier, a comment, or just a plain text.
 * Each criterion must be covered.
 * The test results are placed under `results/{RID}`.
