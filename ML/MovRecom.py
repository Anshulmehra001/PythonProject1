import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

# Load ratings
ratings = pd.read_csv(
    'ml-100k/u.data',
    sep='\t',
    names=['user_id', 'item_id', 'rating', 'timestamp']
)

# Load movie titles
titles = pd.read_csv(
    'ml-100k/u.item',
    sep='|',
    encoding='latin-1',
    usecols=[0, 1],
    names=['item_id', 'title']
)

# Pivot data into item-user matrix
user_item = ratings.pivot(
    index='item_id', columns='user_id', values='rating'
).fillna(0)

item_user_matrix = csr_matrix(user_item.values)

# Build and train KNN model
model = NearestNeighbors(
    metric='cosine',
    algorithm='brute',
    n_neighbors=10,
    n_jobs=-1
)
model.fit(item_user_matrix)

def get_movie_recommendations(movie_title, n_recommendations=5):
    # Find movie ID
    movie_id_series = titles.loc[titles.title == movie_title, 'item_id']
    if movie_id_series.empty:
        print(f"❌ '{movie_title}' not found in dataset")
        return []

    movie_id = movie_id_series.values[0]
    movie_idx = user_item.index.get_loc(movie_id)

    distances, indices = model.kneighbors(
        item_user_matrix[movie_idx],
        n_neighbors=n_recommendations + 1
    )

    recommendations = []
    for idx in indices.flatten()[1:]:
        rec_id = user_item.index[idx]
        rec_title = titles.loc[titles.item_id == rec_id, 'title'].values[0]
        recommendations.append(rec_title)
    return recommendations

if __name__ == "__main__":
    print("🍿 Item-based Movie Recommender | MovieLens‑100K\n")
    fav = input("Enter a movie you like:\n> ").strip()
    recs = get_movie_recommendations(fav, n_recommendations=5)

    if recs:
        print("\nYou might also enjoy:")
        for r in recs:
            print("▶", r)
    else:
        print("No recommendations found.")
