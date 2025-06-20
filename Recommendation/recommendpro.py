import pandas as pd
df = pd.read_csv("products.csv")
def recommend_products(skin_type, concern):
    recommended = df[
        (df['skin_type'].str.lower() == skin_type.lower()) &
        (df['concerns'].str.lower() == concern.lower())
    ]
    
    if recommended.empty:
        print(" Sorry, no matching products found.")
    else:
        print(f" Recommended Products for {skin_type} skin and {concern} concern:\n")
        for _, row in recommended.iterrows():
            print(f" {row['name']} - ₹{row['price']}")

print("Welcome to the Face Care Recommender ")
skin = input("Enter your skin type (dry/normal/oily): ")
concern = input("Enter your skin concern (acne/dullness/dryness/oily/sensitivity): ")

recommend_products(skin, concern)
