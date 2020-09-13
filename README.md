# [newsHUB]()

## Author: [kelvin Kiplagat](https://github.com/kelvin-daniel)

## Description
A news application that allows a user to view news articles from their favourite news source in any category. The user can also access the article in the creators website.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed per category |
| Display articles from a news source | **Click a news source** | Redirected to a page with a list of articles from the source |
| Display the preview of an article | **On page load** | Each article displays an image, title, description and publication date |
| Read an entire article | **Click an article** | Redirected to the news source's site to read the entire article |

### Prerequisites

You need the following to start working on the project on your local computer:

* A computer running on either Windows, MacOS or Ubuntu operating system installed with the following:

```
-Python 
-Flask
-Pip
-virtualenv
-A text  Editor
```

## Getting Started

* Clone this repository to your local computer.
* Ensure you have python installed in your computer.
* From the terminal navigate to the cloned project folder.
* Create a virtual environment and access the folder via your virtual amchine.
* Visit https://newsapi.org/ and register for an API key.
* Create start.sh file and in it write the following lines:
```
 export NEWS_API_KEY='<Your-Api-Key>'
 python manage.py server
```
* Run ```chmod +x start.sh``` follwoed by ``` ./start.sh ``` while in the project folder to start the project.
* Once started, the project can be accessed on your localhost using the address: ``` localhost:5000 ```.
* Alternatively the application can be accessed by visiting https://ppolle-news-highlights.herokuapp.com@@@@

## Technologies Used

* Python
* Boostrap
* Flask

## Contact

kaymutor@gmail.com

## License

MIT License
Copyright (c) 2020 Kelvin Kiplagat