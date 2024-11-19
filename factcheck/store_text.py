import os

def save_to_txt(post_url, paragraphs, filename):
    if not os.path.exists("texts"):
        os.makedirs("texts")
    
    filepath = os.path.join("texts", filename)
    
    try:
        with open(filepath, "a", encoding="utf-8") as file:
            file.write(f"Post URL: {post_url}\n")
            file.write("\n".join(paragraphs))
            file.write("\n\n")

        print(f"Texts from post {post_url} are saved!")
    except Exception as e:
        print(f"Error while writing to file: {e}")
