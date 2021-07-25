import instaloader  #module to download Instagram profile 

ig = instaloader.Instaloader()  #initialize 
dp = input("Enter Insta Username: ")  #input userID

ig.download_profile(dp,profile_pic_only=True)   #method to download profile
