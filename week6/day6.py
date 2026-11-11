import pandas as pd
# Create a DataFrame from a dictionary and inspect it
data = {
    "name": ["Eric", "James", "Amina", "Sara"],
    "score": [85, 72, 91, 68],
    "city": ["Nairobi", "Mombasa", "Nairobi", "Kisumu"]
}
df = pd.DataFrame(data)
print(df)
print("\nShape:", df.shape)

import pandas as pd
data = {"name": ["Eric","James","Amina","Sara"], "score": [85,72,91,68], "city": ["Nairobi","Mombasa","Nairobi","Kisumu"]}
df = pd.DataFrame(data)
# Filter to show only students from Nairobi with score above 80
result = df[(df['city'] == 'Nairobi') & (df['score'] > 80)]
print(result)