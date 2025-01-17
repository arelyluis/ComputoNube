import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

data_path = os.path.join(os.path.dirname(__file__), "../public_html/data/social_media_entertainment_data.csv")
print(data_path)
df = pd.read_csv(data_path)


platform_preference = df.groupby(['Age', 'Primary Platform']).size().unstack().fillna(0)
platform_preference.plot(kind='bar', stacked=False, figsize=(15, 8))
plt.title('Platform Preference by Age')
plt.xlabel('Age')
plt.ylabel('Number of Users')
plt.legend(title='Platform', loc="lower right")
plt.savefig("../public_html/images/tiempo_redes.png")
plt.close()


activity_columns = ['Daily Social Media Time (hrs)', 'Daily Entertainment Time (hrs)', 
                    'Daily Gaming Time (hrs)', 'Physical Activity Time (hrs)', 
                    'Reading Time (hrs)', 'Work/Study Time (hrs)', 'Daily Messaging Time (hrs)', 'Daily Video Content Time (hrs)', 
                    'Average Sleep Time (hrs)', 'Screen Time (hrs)', 'Daily Music Listening Time (hrs)']

average_time = df[activity_columns].mean().sort_values()

average_time.plot(kind='barh', figsize=(20, 6), color='green')
plt.title('Average Time Spent on Activities')
plt.xlabel('Average Time (hrs)')
plt.ylabel('Activity')
plt.savefig("../public_html/images/tiempo_promedio3.png")
plt.close()
