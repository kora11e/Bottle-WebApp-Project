<h1> Bottle Application Project </h1>

<h2>Overview</h2>

The project was created as a final assignment for python programming classes. It utilizes MySQL Database, Bottle web framework and JavaScript on-site functionalities.

<h2> Steps to run the application:</h2>

1. To run the program unzip the package and and open tn in IDE (preferably VSCode).
2. Make sure Python 3.3 or higher version is installed on your computer and you have live server installed.
3. Run the file main.py by using command:
```python
python main.py
```
4. Once the server is running open the local environment on port 8080 or copy the path below and paste it into browser:
```
http://127.0.0.1:8080/
```

<h2> Web Application Functionalities </h2>
The website uses Model View Controller architecture to enable agile approach in coding consecutive features. The application contains main model file defining routing to static elements elements (CSS, JOSN data, JavaScript scripts), 7 views, error message callers and data manipulation techniques.

The program provides input for .csv files and allows to open them on the side. The further subpages support HTTP methods GET, POST, DELETE to operate on a custom SQL database and finally implement browser snake game.

<h2>File/folder structure:</h2>

1. DB - folder space for sqlite database and CSV file
2. ~~__pycache__ - internal framework cache files~~
3. static - folder for static files including:
	css stylesheets,
	fonts from Google fonts website,
	single json file (legacy),
	Java Script code
4. views - applcation views; all in .tpl format
5. independent files: executable main.py, git attributes, environmental variables and project legacies

The projects consists of 5 accessible webpages and 3 internal methods. 
All of them can be accessed after running the app from main window.
