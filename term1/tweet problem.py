#tweet problem
tweet=input("input tweet")
def lengthcheck (string1):
    if len(string1)<=20:
        return "good"
    else:
        return "bad"


#main problem
print("this post is",lengthcheck(tweet),"to post")
