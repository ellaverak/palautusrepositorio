from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_toml = toml.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        name = parsed_toml["tool"]["poetry"]["name"]
        des = parsed_toml["tool"]["poetry"]["description"]
        dep = list((parsed_toml["tool"]["poetry"]["dependencies"]).keys())
        dev_dep = list((parsed_toml["tool"]["poetry"]["dev-dependencies"]).keys())
        return Project(name, des, dep, dev_dep)
