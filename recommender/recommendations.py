import pandas as pd
import nltk
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import ViewHistory
from products.models import Sizevariant
from products.models import product as Product

# Initialize the stemmer and vectorizer
stemmer = SnowballStemmer('english')
tfidf_vectorizer = TfidfVectorizer(tokenizer=lambda x: tokenize_and_stem(x))


def tokenize_and_stem(text):
    tokens = nltk.word_tokenize(text.lower())
    stems = [stemmer.stem(t) for t in tokens]
    return stems


def get_recommendations(user_id, top_n=4):
    nltk.download('punkt')


    # Step 1: Fetch the most visited product IDs
    user_view_history = ViewHistory.objects.filter(user_id=user_id).order_by('-visited_times')
    if not user_view_history.exists():
        return []
    
    most_visited_product_ids = list(user_view_history.values_list('product_id', flat=True)[:top_n])

    # Step 2: Use the fetched IDs to filter the Tshirt objects
    most_visited_products = Product.objects.filter(id__in=most_visited_product_ids)


    # Step 2: Prepare data for TF-IDF vectorization
    tshirts_data = Product.objects.all()
    tshirts_df = pd.DataFrame(list(tshirts_data.values('id', 'name', 'desc')))
    tshirts_df['stemmed_tokens'] = tshirts_df.apply(lambda row: tokenize_and_stem(f"{row['name']} {row['desc']}"), axis=1)

    # Create a TF-IDF matrix for all products
    tshirts_df['text'] = tshirts_df.apply(lambda row: f"{row['name']} {row['desc']}", axis=1)
    tfidf_matrix = tfidf_vectorizer.fit_transform(tshirts_df['text'])

    # Calculate similarity scores
    similar_products = []
    for product in most_visited_products:
        product_text = f"{product.name} {product.desc}"
        product_tfidf = tfidf_vectorizer.transform([product_text])
        cosine_similarities = cosine_similarity(product_tfidf, tfidf_matrix).flatten()

        # Get the indices of the most similar products
        similar_indices = cosine_similarities.argsort()[-(top_n+1):-1][::-1]  # Exclude the product itself

        similar_product_ids = tshirts_df.iloc[similar_indices]['id'].values
        similar_products.extend(similar_product_ids)

    # Remove duplicates and limit the number of recommendations
    similar_product_ids = list(dict.fromkeys(similar_products))[:top_n]

    products = []

    for i in similar_product_ids:
        products.append(Product.objects.get(id=i))

    return products


def search_products(search_keyword, top_n=5):
    nltk.download('punkt')

    # Step 1: Prepare data for TF-IDF vectorization
    tshirts_data = Product.objects.all()
    tshirts_df = pd.DataFrame(list(tshirts_data.values('id', 'name', 'desc')))
    tshirts_df['stemmed_tokens'] = tshirts_df.apply(lambda row: tokenize_and_stem(f"{row['name']} {row['desc']}"), axis=1)

    # Create a TF-IDF matrix for all products
    tshirts_df['text'] = tshirts_df.apply(lambda row: f"{row['name']} {row['desc']}", axis=1)
    tfidf_matrix = tfidf_vectorizer.fit_transform(tshirts_df['text'])

    # Step 2: Transform the search keyword into a TF-IDF vector
    search_tfidf = tfidf_vectorizer.transform([search_keyword])

    # Step 3: Calculate similarity scores between the search keyword and all products
    cosine_similarities = cosine_similarity(search_tfidf, tfidf_matrix).flatten()

    # Get the indices of the most similar products
    similar_indices = cosine_similarities.argsort()[-top_n:][::-1]

    similar_product_ids = tshirts_df.iloc[similar_indices]['id'].values

    products = []
    for i in similar_product_ids:
        tshirt = Product.objects.get(id=i)
        size_variants = Sizevariant.objects.filter(tshirt=tshirt)
        for size_variant in size_variants:
            product = {
                'tshirt': tshirt,
                'size': size_variant
            }
            products.append(product)

    return products