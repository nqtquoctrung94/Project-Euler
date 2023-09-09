import requests
import nbformat as nbf
from bs4 import BeautifulSoup

class ProjectEuler_Notebook():
    def __init__(self, question_num):
        self.question_num = question_num
        self.name = "problem_{:04d}".format(self.question_num)
        self.notebook = nbf.v4.new_notebook()

    def _get_question_title(self):
        """This function use GET request to get the question's title from <head> - <title>.
        There is no question title in minimal ver, so we have to access it from the main page
        """
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        }
        response = requests.get(f'https://projecteuler.net/problem={self.question_num}', headers=headers)

        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.find('head').find('title').get_text()
            title = title.replace(f"{self.question_num}","") # Remove the head part
            title = title.replace(" - Project Euler","") # Remove the tail part
            return title
        else:
            print(response)
            return None

    def _get_question_content(self):
        """This function use GET request to get question's content.
        It is cleaner to access the minimal link, less cleaning to do.
        So far I have not work on cleaning the url inside the content (some question require downloading the dataset)
        """
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        }
        response = requests.get(f'https://projecteuler.net/minimal={self.question_num}', headers=headers)

        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")
            soup_text = soup.get_text()
            content = soup_text.replace("\n","<br>\n").replace("$<br>","$\n") # Disgusting code to clean string
            return content
        else:
            print(response)
            return None
        
    def _fill_content(self):
        """Document: https://nbformat.readthedocs.io/en/latest/api.html#module-nbformat.v4"""
        
        self.notebook['cells'] = [
            # Title and question
            nbf.v4.new_markdown_cell(f"# [Question {self.question_num}](https://projecteuler.net/problem={self.question_num})"),
            nbf.v4.new_markdown_cell(f"#{self._get_question_title()}\n{self._get_question_content()}"),

            # Solution 
            nbf.v4.new_markdown_cell("# Solution"),
            nbf.v4.new_code_cell("def solution():\n\tpass"),

            # Run and check
            nbf.v4.new_markdown_cell("# Run"),
            nbf.v4.new_code_cell("%%time\nsolution()")
        ]

    def create(self):
        self._fill_content()
        nbf.write(self.notebook, fr'python-solutions\{self.name}.ipynb')
        print(f"Successfully created notebook {self.name}.ipynb")

ProjectEuler_Notebook(67).create()