import json
from difflib import get_close_matches

data = json.load(open('app1/data.json','r'))

def findmean(a):
    if a in data:
        return data[a]
    elif a.title() in data:
        return data[a.title()]
    elif len(get_close_matches(a, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(a, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(a, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The Word doesn't exist"

word = input("Enter the word:")
ans = findmean(word.lower())

i = 1;
print("Here's your answer:")
if type(ans) == list:
    for item in ans:
        print("%d.%s"% (i,item))
        i+=1;
else:
    print(ans)
