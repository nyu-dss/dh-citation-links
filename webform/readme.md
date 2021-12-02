# Data entry web form
web form to enter data for research project

to use:
- clone/download files
- open index.html in a browser
- enter the data. once you've entered the data for a given article, use the "submit article data" button. this stores the data using the [web storage api](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API).
- you can then begin entering data for the next article. currently, the form does not reset after clicking the "submit article data" button, so you will have to manually delete the data or write over it.
- when you are finished entering data, click the "save session data" button. this prompts you to save all data on your local computer as a .json file.
- note that you will have separate json files for each data entry session.

data cleanup:
once you've saved the data from the form, there are a few additional clean-up steps required for each json file in order to create valid json:
- the output file has a quotation mark (") as the very first and very last character in the file. replace the opening quotation mark with an opening square bracket (\[), and replace the closing quotation mark with a closing square bracket (])
- if the output file contains multiple objects (i.e. you clicked "submit article data" multiple times before clicking "save session data"), then you'll need to also remove some additional and extraneous quotation marks. in short, run the following find & replace query,
find: `}","{`
replace: `},{`
- remove all backslashes (\). if your data legitimately contains backslashes, you have my sympathy.

to fix:
- clear form data after clicking submit
- would be nice to continuously append to same file
- after data entry, script to do data cleanup tasks
