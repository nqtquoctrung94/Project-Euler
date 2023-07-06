import requests
import nbformat as nbf
from bs4 import BeautifulSoup

class ProjectEuler_Notebook():
    def __init__(self, question_num):
        self.question_num = question_num
        self.title = "problem_{:04d}".format(self.question_num)
        self.notebook = nbf.v4.new_notebook()

    def _get_question_content(self):
        '''This function use GET request to get question's content
        So far I have not work on cleaning the url
        '''
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        }
        response = requests.get(f'https://projecteuler.net/minimal={self.question_num}', headers=headers)

        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")
            soup_text = soup.get_text()
            soup_cleaned = soup_text.replace("\n","<br>\n").replace("$<br>","$\n") # Disgusting code to clean string
            return soup_cleaned
        else:
            print(response)
            return None
        
    def _fill_content(self):
        '''Document: https://nbformat.readthedocs.io/en/latest/api.html#module-nbformat.v4'''
        
        self.notebook['cells'] = [
            # Title and question
            nbf.v4.new_markdown_cell(f"# [Question {self.question_num}](https://projecteuler.net/problem={self.question_num})"),
            nbf.v4.new_markdown_cell(self._get_question_content()),

            # Solution 
            nbf.v4.new_markdown_cell("# Solution"),
            nbf.v4.new_code_cell("def solution():\n\tpass"),

            # Run and check
            nbf.v4.new_markdown_cell("# Run"),
            nbf.v4.new_code_cell("%%time\nsolution()")
        ]

    def create(self):
        self._fill_content()
        nbf.write(self.notebook, fr'in_progress\{self.title}.ipynb')

ProjectEuler_Notebook(10).create()