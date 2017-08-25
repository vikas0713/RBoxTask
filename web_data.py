"""
This script stores all javascript, stylesheet and other assests related to the web
Created By : Vikas Verma
"""
import random

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
        self.save_page(1)   # Random argument passed for use of unique name

    def stylesheets(self):
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
                    else:
                        pass
                else:
                    pass
            except:
                pass

    def javascript(self):
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
                else:
                    pass
            except:
                pass

    def save_images(self):
        img_directory = self.directory + "img/"
        self.create_folder(img_directory)
        for img in self.parsed_html.findAll("img"):
            try:
                src = img["src"]
                img_data = self.simple_request(src)
                if img_data:
                    with open(img_directory+self.generate_random_name(), "wb") as fp:
                        fp.write(img_data)
                else:
                    pass
            except:
                pass

    def save_page(self, i):
        if self.is_exists(self.directory+"page"+str(i)+".html"):
            self.save_page(i+1)
        else:
            with open(self.directory+"page"+str(i)+".html", "w") as fp:
                fp.write(u''.join(self.raw_html).encode('utf-8').strip())
            fp.close()
            self.stylesheets()
            self.javascript()

    def generate_random_name(self):
        name = ""
        choices = "ehienaijfisdfnkldfdnfsndfndsfkndnbvzxcasdfghjkl08447489949f"
        while len(name)<5:
            name = random.choice(choices)
        return name+".jpg"




