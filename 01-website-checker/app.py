"""
Website Checker App: checks if a website is using 
a secure protocol or not
"""

print("🔍 WEBSITE URL CHECKER 🔍")
# Ask user for a website
site = input("\nEnter a website URL: ")
# Check protocol
if site.startswith("https://"):
    print("🔐 This website uses HTTPS (secure)")
elif site.startswith("http://"):
    print("👀 This website uses HTTP (not secure)")
else:
    print("❌ This doesn't look like a complete URL")
