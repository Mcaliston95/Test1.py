testScorestring = int(input("enter the test score:"))
classRankstring = int(input("enter the class rank:"))

if testScorestring >= 90:
    if classRankstring >= 25:
        print("accept")
    else:
        print("reject")
        
else:
    if testScorestring >= 80:
        if classRankstring >= 50:
            print("accept")
        else:
            print("reject")
    else:
        if testScorestring >= 70:
            if classRankstring >= 75:
                print("accept")
            else:
                print("reject")
                
        else:
            print("reject")
            