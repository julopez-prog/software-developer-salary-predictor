# software-developer-salary-predictor
Predicts your salary income based on your inputs such as years of coding, education, and country

## Inspiration
The tech industry is a global industry with a lot of competition. Many aspiring developers all around the world find it difficult to assess their skillsets to calculate their assets. While I was brainstorming an idea, I noticed that I found a dataset about recent surveys on software developers with their revelant information. I was insipred to build this tool in order to make use of the data. 

## What it does
The Software Developer Salary Predictor is a dual-purpose web application. On the predict page, users can input their country, education level, and years of experience to check their estimated annual salary in USD. On the Explore page, the app provides visual insights into the dataset. This includes distribution of data with visuals like pie charts and line graphs

## How we built it
I used the Stack Overflow Developer Survey 2025 as the reference for the salaries. I also used Pandas to filter through the raw survey results by handling outliers by capping salaries between $10,000 and $250,000 to maintain model reliability. Using scikit-learn, I implemented a regression model and used Label Encoders to transform categorical variables into numerical ones. The UI was built entirely in Streamlit to allow for a seamless transition from a Python script to a hosted web app. I used Pickle to package the trained model and encoders into a single saved_steps.pkl file for easy deployment.

## Challenges we ran into
My biggest change was that I had no prior knowledge about machine learning and data analytics when joining this hackathon. I watched several Youtube videos about data science to apply the knowledge into the hackathon. I had a hard time understanding the concepts of Python Libraries like Numpy, Pandas, etc and the deployment of the website using Streamlit and Github. Yet, I manage to learn these quickly and comprehensively

## Accomplishments that we're proud of
I am proud of the data cleaning part and its applications where I transformed a messy and real-world dataset into a format where the model can predict sensible predictions. I also make the website work with limited time on my hands. I read the information about GitHub which I learned the "Terminal" way with git push and git commit.

## What we learned
This project reinforced the importance of robust environment management where you should be careful handling very gigantic datasets because the entire track of the project would collapse when one name or one salary. We should also be responsible in using libraries since every library in Python have important purposes. Other aspects of the project like the 

## What's next for Software Developer Salary Predictor
I would like to add more datasets in the future to improve precision and accuracy where the experience wouldn't just be in years or the inclusion of other countries. I also want to enhance the algorithm in getting the correlation coefficients.

Hard to estimate salary incomes specially when you want to be a software developer in the future? This is a close and excellent estimate of what you might expect!
