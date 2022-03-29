* docxstact is a simple CLI tool to extract embedded files from .docx documents.

Microsoft .doc files are basically just zipped .xml files, which contain
directories to store files that have been embedded within them. this simple tool
currently extracts only them and dumps them into the project directory.

* TODO
- get names of the documents that are embedded.
- allow user to choose extraction directories
- check if there are any documents embedded.
