# WeThere: The Weather Forecasting Tool
WeThere is a command-line tool that retrieves the current weather forecast for a specified city. It leverages the OpenWeatherMap API to fetch weather data and parses it using Python. This solution demonstrates how GitHub Copilot can assist with API usage, data parsing, and error handling.<br><br>
![WeThere Demo](demo.png)
###### Figure 1: WeThere in action
###### Demo Video is also uploaded in the repository.

## Github Copilot Usage (GitHub use case)
In this submission, I used the GitHub Copilot AI-powered code completion tool to assist with writing the code for the Weather Forecasting Tool. GitHub Copilot helped in several ways:

* API Usage: GitHub Copilot provided suggestions and completions for working with the OpenWeatherMap API. It helped with generating the API request URL, handling the API response, and accessing specific weather data fields.

* Data Parsing: Copilot suggested code snippets and logic for parsing the JSON response from the API. It provided recommendations for extracting weather details like description, temperature, humidity, wind speed, etc., from the JSON data structure.

* Error Handling: Copilot assisted with suggesting common HTTP status codes and their corresponding error messages. It provided a starting point for handling various API response errors, such as city not found, invalid API key, too many requests, internal server error, and more.

* Command-Line Argument Processing: Copilot helped with generating code for processing command-line arguments, including checking for the presence of arguments, validating argument values, and determining the desired output format (e.g., table format).

By leveraging GitHub Copilot's suggestions and completions, I was able to write the code more efficiently and effectively. It saved time by providing helpful code snippets and reducing the need for manual research. It also ensured that the code followed best practices and handled potential errors appropriately.GitHub Copilot significantly assisted in developing the Weather Forecasting Tool, making the submission more robust and complete.

## Architecture Diagram
![WeThere Architecture Diagram](Architecturaldiagram.png)
## Prerequisites
Before using the WeThere tool, make sure you have the following:

* Python installed on your system.

* An API key from OpenWeatherMap. You can obtain a free API key by signing up on their website.

## Installation
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using the following command: <br>
`
pip install -r requirements.txt
`
4. Create a file named `.env` in the project directory and add the following line to it: <br>
`
API_KEY=<your-api-key>
`
5. Run the tool using the following command: <br>
`
python forecast.py <city-name>
`

## Usage
The tool accepts a Three argument, the name of the city for which you want to fetch the weather forecast and two optional arguments, the unit of temperature and the format of the output. Below is the list of all the arguments that can be used with the tool:

* Flags: <br>
`-h, --help` - Show the help message and exit. <br>
`-t` - Display data in tabular format. <br>
`-c` - Display Temperature in Celsius. <br>
`-f` - Display Temperature in Fahrenheit. <br>
`-k` - Display Temperature in Kelvin. <br>

*Note: `-c`, `-f` and `-k` can't be used together.*

## Code Explanation
The WeThere tool consists of the following components:

* The asciart function: Prints an ASCII art representation of WeThere.
* Loading environment variables: Uses the dotenv library to load the OpenWeatherMap API key from the .env file.
* The getWeather function: Retrieves the weather details for a specified city using the OpenWeatherMap API. It also handles potential errors and prints the corresponding error messages.
* The footer function: Prints the developer information and GitHub repository link.
* The main function: Calls the asciart function, the getWeather function, and the footer function based on user input.
* Execution flow: When the script is executed, the main function is called, processing the command-line arguments to obtain the city name and optional table format flag.

## Error Handling
The WeThere tool incorporates error handling to ensure a smooth user experience. It handles the following scenarios:

* Invalid city name: The tool checks if the provided city name contains only alphabetic characters. If not, it displays an error message.
* Missing command-line argument: If no city name is provided as a command-line argument, it displays an error message and exits.
* API response errors: The tool handles various HTTP status codes returned by the OpenWeatherMap API and prints corresponding error messages to provide meaningful feedback.

WeThere is a powerful command-line weather forecasting tool that demonstrates the usage of the OpenWeatherMap API, data parsing in Python, and effective error handling. Feel free to customize and enhance the tool according to your requirements. Enjoy forecasting the weather with WeThere!