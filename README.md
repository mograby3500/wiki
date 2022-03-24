# Wiki
Project 1 for CS50 web programming with pyhton and javascript

# Overview
Wikipedia-like online encyclopedia.

# Specifications
The website covers the following aspects:
- ### Home Page:
  Displays all of Entries that are present on the site, clicking any entry will take the user to that entry's page.
  
- ### Entry Page:
  - Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, will render a page that displays the contents of that encyclopedia entry.
  - If an entry is requested that does not exist, the user will be presented with an error page indicating that their requested page was not found.
  - If the entry does exist, the user will be presented with a page that displays the content of the entry.
- ### Search:
  - Allows the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
  - If the query matches the name of an encyclopedia entry, the user will be redirected to that entry’s page.
  - If the query does not match the name of an encyclopedia entry, the user will instead be taken to a search results page that displays a list of all encyclopedia     entries that have the query as a substring. For example, if the search query were ytho, then Python should appear in the search results.

- ### New Page: 
  - Clicking “Create New Page” in the sidebar will take the user to a page where they can create a new encyclopedia entry.
  - Users are able to enter a title for the page and, in a textarea, they are able to enter the Markdown content for the page.
  - Users are able to click a button to save their new page.
  - When the page is saved, if an encyclopedia entry already exists with the provided title, the user will be presented with an error message.
    Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.
- ### Markdown to HTML Conversion: 
  - On each entry’s page, any Markdown content in the entry file is converted to HTML before being displayed to the user. This is done using the "markdown" python library


# Topics
Built with HTML, CSS and Python using Django
