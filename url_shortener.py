import pyshorteners

def shorten(url):
    link = pyshorteners.Shortener()
    return link.tinyurl.short(url)

if __name__ == "__main__":
    url = input("Enter URL: ")
    print(f"\n{shorten(url)}")