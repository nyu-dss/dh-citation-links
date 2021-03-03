# dh-citation-links
web form to enter data for research project

to use:
- clone/download files
- open index.html in a browser
- enter the data. once you've entered the data for a given article, use the "submit article data" button. this stores the data using the [web storage api](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API).
- you can then begin entering data for the next article. currently, the form does not reset after clicking the "submit article data" button, so you will have to manually delete the data or write over it.
- when you are finished entering data, click the "save session data" button. this prompts you to save all data on your local computer as a .json file.
- note that you will have separate .json files for each data entry session.

to fix:
- clear form after submit
- would be nice to continuously append to same file
- after data entry, script to merge files/objects and JSON.parse()
