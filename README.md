This project consists of python scripts which is basically works as a crawler.

Make sure that you have installed the requirements of the project that is included in the requirements.txt.
 1. pip install -r requirements.txt

To run the project we can pass Root URL from command line also.

 1. python main.py www.example.com

If you forgot to enter the URL from command line , Don't worry , after running the script without passing command line argument
 you will be asked to enter the root URL again or you can choose from the menu given on the screen.


CrawlTheWeb class will crawl the links and after that it will create the folder into same directory of the respective
domain and then fetches all the HTML, CSS, JS and Images from the sources  and save it into its respective directory.

By: Vikas Verma