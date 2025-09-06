Project Overview:

1.Overview: This web-based dashboard allows users to input a search query (brand, movie, or trending topic) and fetches recent public data (tweets, news headlines). It then performs sentiment analysis and visualizes the results in an interactive dashboard.

2.Screenshots:
Input:--
<img width="1899" height="912" alt="Screenshot 2025-09-06 165724" src="https://github.com/user-attachments/assets/4921220f-5594-4a7b-8ed4-91a1184fb514" />
Output:--
<img width="1896" height="896" alt="Screenshot 2025-09-06 165810" src="https://github.com/user-attachments/assets/c95f6f8a-80e7-40e5-b220-37dcffd099ba" />
<img width="1894" height="903" alt="Screenshot 2025-09-06 165834" src="https://github.com/user-attachments/assets/bab91055-00b3-4a92-ab4b-73da1849eea3" />

3.Data Source: Twitter API, news APIs, or public datasets.

4.Rationale: It provides real-time public reactions, which is ideal for sentiment analysis of trends. News headlines give structured textual content for accurate sentiment detection.

5.Sentiment Analysis Model
Model Used:  pre-trained models like VADER, TextBlob (VADER is lightweight and optimized for social media text, providing polarity scores efficiently.Provides polarity scores (positive, negative, neutral) quickly and accurately.Easy integration with Python projects.)


Project Features:
Input a search query and fetch real-time data.
Analyze sentiment of tweets and news headlines.
Visualize results with interactive charts (bar, pie, line).
Filter results by date, source, or sentiment.

Future Improvements:
Integrate more social media platforms (Instagram, Reddit).
Use transformer-based models like BERT for higher accuracy.
Implement sentiment trend prediction over time.
