Short Description:
This is all the files related to my obligatory assignment #02 in web science.

Content:

In this assignment you will extract information from the
following wiki page:
https://en.wikipedia.org/wiki/Star_Wars:_The_Rise_of_Skywalker

> 1.1 You have to extract all links from the page as well
as where they point to (tip: look for the “href” attributeCancel changes
in “<a>” tags).  You must print out absolute link
reference.

> 1.2 You have to extract all images src attribute from
the page.You must print out absolute link reference.
  
> 2.1 Analysing code. 
The following python code is used to extract some
information about the awards that the movie has
won. With the following python code, we were able
to select the table data that has 'Won' value and
print out some related information by accessing its
parent element. However, it is not printing the
columns with Award, and Date of ceremony
values for all selected items. Why it is not printing
the column value for Award  and Date of
ceremony information for the selected awards? 
Analyse the table structure and python code and
provide an answer in plain text (max length 100
words). Optional: You may provide a DOM tree with
your answer. 
  
> 3. In this assignment you have to write a scraper that will work as follows. 
a. Start crawling from https://en.wikipedia.org/wiki/Web_scraping  
b. Using BeautifulSoup's find_all() function get all the links from 'See also' section  
c. for each link do the following
       c.1 Load selected article page  
       c.2. Print out selected articles first paragraph. 
