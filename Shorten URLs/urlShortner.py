import pyshorteners

print("#"*50)
print("A script to shorten URLs".center(50))
print("#"*50)

link = input("\nEnter the link you want shortened: ")

short = pyshorteners.Shortener()

shortened_url= short.tinyurl.short(link)

print(f"The shortened URL: {shortened_url}")