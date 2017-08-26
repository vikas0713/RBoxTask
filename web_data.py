"""
This script stores all javascript, stylesheet and other assests related to the web
Created By : Vikas Verma
"""
import random
import shutil

from base import Base


class WebData(Base):
    """
    Stores all assets of the website
    """
    def __init__(self, raw_html, directory, base_url):
        super(WebData, self).__init__()
        self.raw_html = raw_html
        self.directory = directory
        self.parsed_html = self.parse_raw_html(self.raw_html)
        self.base_url = base_url
        self.all_javascripts = []
        self.save_page(1)   # Random argument passed for use of unique name of HTMl web page

    def stylesheets(self):
        # Fetches CSS from webpage
        css_directory = self.directory+"css/"
        self.create_folder(css_directory)  # Creating Directory CSS
        for style in self.parsed_html.findAll("link"):
            try:
                if style["rel"]=="stylesheet":
                    if style["href"].startswith("/") and style["href"].endswith(".css"):
                        style_link = self.base_url+style["href"]
                        style_name = style["href"].split("/")[-1]
                    elif style["href"].endswith(".css"):
                        style_link = style["href"]
                        style_name = style["href"].split("/")[-1]
                    else:
                        style_name = None
                        style_link = None
                    if style_name and style_link:
                        if not self.is_exists(css_directory+ style_name):
                            css_data = self.simple_request(style_link)  # Fetch CSS from resource
                            with open(css_directory+style_name,"w") as fp:
                                fp.write(css_data)
                            fp.close()
                    else:
                        pass
                else:
                    pass
            except:
                pass

    def javascript(self):
        # Fetches JS files from webpage
        js_directory = self.directory + "js/"
        self.create_folder(js_directory)  # Creating Directory CSS
        for js_script in self.parsed_html.findAll("script"):
            try:
                if js_script["src"].startswith("/") and js_script["src"].endswith(".js"):
                    js_link = self.base_url + js_script["src"]
                    js_name = js_script["src"].split("/")[-1]
                elif js_script["src"].endswith(".js"):
                    js_link = js_script["src"]
                    js_name = js_script["src"].split("/")[-1]
                else:
                    js_name = None
                    js_link = None
                if js_name and js_link:
                    if not self.is_exists(js_directory + js_name):
                        js_data = self.simple_request(js_link)  # Fetch JS from resource
                        with open(js_directory + js_name, "w") as fp:
                            fp.write(js_data)
                        fp.close()
                else:
                    pass
            except:
                pass

    def save_images(self):
        # Fetches Images from the source
        img_directory = self.directory + "img/"
        self.create_folder(img_directory)
        for img in self.parsed_html.findAll("img"):
            if True:
                src = img["src"]
                if src.startswith("/"):
                    src = self.base_url+src
                    image_name = src.split("/")[-1]+".png"
                    img_data = self.basic_request(src)
                    if not self.is_exists(self.directory+image_name):
                        if img_data:
                            with open(img_directory+image_name, "wb") as fp:
                                for chunk in img_data.iter_content(1024):
                                    fp.write(chunk)
                            fp.close()
                        else:
                            pass
            else:
                pass

    def save_page(self, i):
        # Fetches HTML webpage from source
        if self.is_exists(self.directory+"page"+str(i)+".html"):
            self.save_page(i+1)
        else:
            with open(self.directory+"page"+str(i)+".html", "w") as fp:
                fp.write(u''.join(self.raw_html).encode('utf-8').strip())
            fp.close()
            self.stylesheets()
            self.javascript()
            self.save_images()



