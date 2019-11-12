import pandas as pd
from IPython.display import HTML, Javascript

HEADER = '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="bootstrap.min.css" />
        <style>             
        </style>
    </head>
    <body>
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                    <a class="navbar-brand" href="Home.html">Lattitude</a>                    
                    <div class="collapse navbar-collapse" id="navbarNavDropdown" style="display: flex; justify-content: flex-end;">
                      <ul class="navbar-nav">
                        <li class="nav-item dropdown">
                          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Plots
                          </a>
                          <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                            <a class="dropdown-item" href="maxTemp.html">Max Temperature</a>
                            <a class="dropdown-item" href="humidity.html">Humidity</a>
                            <a class="dropdown-item" href="cloudiness.html">Cloudiness</a>
                            <a class="dropdown-item" href="windSpeed.html">Wind Speed</a>
                          </div>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="comparison.html">Comparison</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="data.html">Data</a>
                        </li>
                      </ul>
                    </div>
            </nav>
            <div class="container">  
            <br>        
            <h2>Data</h2>
            <hr>
            <strong>the following table includes all of the data used for plotting during this project</strong>
            <br>
            <br>
'''
FOOTER = '''        
            
        </div>
        
        <div class="card text-center">                
                <div class="card-footer text-muted">
                  Copyright Coding Bootcamp 2019
                </div>
        </div>
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </body>
</html>
'''


df = pd.read_csv("weather_api_data.csv")
# https://stackoverflow.com/questions/18096748/pandas-dataframes-to-html-highlighting-table-rows
with open('data.html', 'w') as f:
    f.write(HEADER)
    f.write(df.to_html(classes=['table']))    
    f.write(FOOTER)
