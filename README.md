# Weather App Final
 weather app final project for OIM3600 by Ryan Dong

## Project overview
Creating a weather checking website that was easy to use.

## Usage guidelines
### Installation Requirements
must install requirements in requirements.txt folder, so in terminal run command 
`pip install -r requirements.txt`

### Loading the website
Then with uvicorn run for webiste url'
`uvicorn main:app --reload`

### Access deployed website
rdong1.pythonanywhere.com

### Running Tests
Run in terminal:
`pytest`

## Dependencies
used API from Open weather (api.openweathermap.org), used all dependencies in requirements.txt

## Project Structure
- static: Stores static images to be deployed onto the page
- templates: Contains html templates used by Jinja to pass data and populate the elements
- tests: Contains all test files for pytest
- main.py: The entry execution point, determines routing and data distribution

## Acknowledgements
chatgpt, google, friends