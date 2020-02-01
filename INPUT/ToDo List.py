## TODO's
​
- Choose a dataset you like from `kaggle.com`.
- Create a python script and name it `main.py`. Requirements for this script:
  - `main.py` must not have more than 100 lines.
  - It must receive at least 2 params via command-line arguments. Use `argparse` for this task. This parameters should be used to filter the dataset.
- Separate code into other `.py` files. Create functions or classes if needed.
- Filter the dataset with the params received from `main.py`
  - Note: You can clean the dateset beforehand in another script or do it directly in the `main.py` execution
- Enrich the dataset with external data, you can choose one of the following:
  - L1) Get data from an API.
  - L2) Use an API that requires authentication via token or oAuth.
  - L3) Do basic web scraping with python `requests` module.
  - L4) Perform advanced web scraping with `selenium`.
- Create some reports containing valuable data from the dataset. Output will be defined in next task.
  - L1) Simply sumarize the data and do some basic statistics (mean, max, min, std, etc.).
  - L2) Do domain based statistics or data aggregations.
  - L3) Create some plots
- Generate a report, you can choose one of the following
  - L1) Simple text report that will be printed in console `stdout`.
  - L2) Create a PDF report
  - L3) Send a mail to someone selected with the `--mailto` flag in your `main.py`. Include text report inside.
  - L4) Same as `L3` but with PDF attatched
  - L5 HARD MODE) Mail with PDF and plots inside pdf file.
- **NEW SEASON THIS BOOTCAMP** Advanced Mailing techniques
  - L1����‍♂️) Generate a HTML email with embedded images & visual report
  - L2��) Use a mail sending service API. `Sengrid` Free plan allows 40k emails/day with it's free plan
  - L3 WARNING ZONE��) Install & configure your own email server with `postfix`.
  - L4 REALLY HOT ZONE��) Get a Slack message every time someone opens an email from your service.����‍♂️
​
## How to deliver the project
​
- Create a new repo with the name `data-analysis-pipeline` in your github account. Do a PR with the link of your repo copy pasted inside `m1/pipelines-project/PROJECT-REPO.md` on our labs repo.
​
## Links & Resources
​
- https://docs.python.org/3/library/argparse.html
- https://github.com/n0shake/Public-APIs
- https://docs.python.org/3/library/smtplib.html
- https://realpython.com/python-send-email/
- https://2.python-requests.org/en/master/
- https://github.com/theskumar/python-dotenv
- https://selenium-python.readthedocs.io
- https://selenium-python.readthedocs.io/getting-started.html#example-explained
- https://pyfpdf.readthedocs.io/en/latest/
- https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
​
## Prolinks
​
- https://sendgrid.com/pricing/
- http://www.postfix.org/
- https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-on-ubuntu-16-04
- https://devops.ionos.com/tutorials/configure-a-postfix-relay-through-gmail-on-ubuntu/
- https://www.socketlabs.com/developers/