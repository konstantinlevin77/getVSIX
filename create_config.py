import pathlib

default_config = """# You can sort the results by Relevance | Installs | UpdatedDate | Publisher | Name
# | PublishedDate | Rating | Trending
SortBy=Installs

# You can determine how many results do you want to see, it can be 10 maximum.
Top=5
"""

def create_default_config():
    file_path = pathlib.Path("config")
    print(not(file_path.is_file() and file_path.exists()))
    if not(file_path.is_file() and file_path.exists()):
        with open("config",mode="w") as F:
            F.writelines(default_config)
