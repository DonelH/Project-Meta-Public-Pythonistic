Revisions---

Project code has seen substantial revision since last turned in. Most notable additions include changing the
project to MVC format and displaying the maps within the GUI. The maps are pulled from excel and use the data
scraped from the BeautifulSoups we have made to make chloropleth visuals. We have added a scraper for news articles
regarding COVID-19, with 5 trending articles being displayed on the bottom right corner. Furthermore, we
have added functions to the buttons while adding more buttons. Namely, we added a Developers button and a 
quit button. All three buttons have on click actions. More color was added to the trees displaying the COVID-19
information and the ability to change the map between Mexico, USA, and Canada was added. The User Guide has been
updated for our project and contains an actual step by step process on using the application. The User Guide has
been connected to the Tutorial button and should pop up as a pdf now. Furthermore, libraries
necessary for install have been added.

-------------------------------------------------------------------------------------------------------------------

State of the Code---
Currently, most of our code is functional. However, due to following different guides and tutorials,
consistency in naming conventions and spacing will not be superb. The use of different libraries which might come
with their own code etiquette has also affected consistency in coding.

What is done---

Each of the individual code scrapers for each 3 countries has been completed with only the USA scraper requiring
the additional functionality of writing to a csv file as well. The scraper for news has been completed as well which
lists news articles relating to COVID-19. The GUI which will contain all this information has been started, and a
lot of progress has been made there in the direction of how we want to present the information. Currently, only
the link between the scraper for Mexico and the information displayed is more direct. The other two nations have 
had their data manually input from the scrapers. The shape file for the basis of the map has been finished.
The countries and their states separated into polygons had to be accomplished manually but has resulted in the 
desired map. An overarching idea of how the project will end up looking has been made and can be seen within the 
wireframe. A lot of the heavy lifting has been accomplished with the exception of the map feature.

What needs to be done---

Though functional at the moment, the GUI, contained within the project_CS.py file, still requires a lot of work to
approach a satisfactory state. However, it'll flesh itself out as the other features work themselves out. Namely, 
the map functionality, the news section, and the buttons at the bottom of the GUI. The entire map feature of the 
project aside from the shape file which will serve as the foundation for it require work. The news feature needs 
to be narrowed down to displaying only a few, trending articles related to COVID-19. While mostly unimportant 
towards the core of the project with the exception of the refresh button, the buttons at the bottom of the GUI 
need to be ironed out. Refocusing back on the GUI, the information display that takes up the the upper and middle
left of the GUI has to be cleaned up in regards to pulling straight from the data scrapers rather than having the
information manually inputted. Finally, revising of code will have to be accomplished as we approach the deadline
to ensure our code isn't only functional but adheres to PEP8 and Zen of Python guidelines. Furthermore, consistency
in our coding will become more a priority as the app reaches a more functional state.

Who's doing what---

Cindy is in charge of the upper/mid left section of the information display and code relating to its implementation.
Carlan has taken over the news section and its end implementation. Eldon has been designated towards the exact
implementation of the map and research regarding it. If we manage to adequately finish our respective section, the
person will then hop on towards implementation of the buttons. 

Libraries needed to Pip Install---
lxml
pandas
bs4
openpyxl
PyQt5
requests

Other Requirements---
Internet connection needed since information is pulled from online sources
Excel is needed to view raw scraped data and to change chloropleth maps, if desired


