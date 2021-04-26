import random
def roll():
    diceList = []
    for _ in range(1,6):
        diceList.append(random.randint(1,6))
        diceList.sort()
    return diceList

def rollAgain(reRollValue, lst):
    if reRollValue == "":
        return lst
    else:
        reRoll = list(map(int, reRollValue.split(",")))
        for i in reRoll:
            lst[i-1] = random.randint(1,6)
        return lst

def rolledN(lst, n):
    if n in lst:
        return lst.count(n) * n
    else:
        return 0

def threeOfAKind(lst):
    for item in lst:
        if lst.count(item) >= 3:
            return sum(lst)
    return 0 

def fourOfAKind(lst):
    for item in lst:
        if lst.count(item) >= 4:
            return sum(lst)
    return 0

def fullHouse(lst):
    fullHouseDict = {}
    for num in lst:
        if num not in fullHouseDict:
            fullHouseDict[num] = 0
        fullHouseDict[num] += 1
    itemCount = []
    for _, value in fullHouseDict.items():
        itemCount.append(value)
    itemCount.sort()
    if itemCount == [2,3] or itemCount == [5]:
        return 25
    else:
        return 0

def smallStraight(lst):
    testLst = list(set(lst))
    testLst.sort()
    if min(testLst) + 1 not in testLst:
        testLst.remove(min(testLst))
    elif max(testLst) - 1 not in testLst:
        testLst.remove(max(testLst))
    possibilities = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
    if testLst in possibilities:
        return 30
    comparisonLst = list(range(min(lst),max(lst) +1))
    if sorted(lst) == comparisonLst:
        return 30
    else:
        return 0

def largeStraight(lst):
    comparisonLst = list(range(min(lst),max(lst) +1))
    if sorted(lst) == comparisonLst:
        return 40
    else:
        return 0

def Yahtzee(lst):
    for item in lst:
        if lst.count(item) == 5:
            return 50
    return 0

def Chance(lst):
    return sum(lst)

def main():
    players = ["Player 1", "Player 2"]
    player1Score = {
        "Ones" : -1,
        "Twos" : -1,
        "Threes" : -1,
        "Fours" : -1,
        "Fives" : -1,
        "Sixes" : -1,
        "Three of a Kind": -1,
        "Four of a Kind" : -1,
        "Full House" : -1,
        "Small Straight" : -1,
        "Large Straight" : -1,
        "Yahtzee" : -1,
        "Chance" : -1 
        }
    player2Score = {
        "Ones" : -1,
        "Twos" : -1,
        "Threes" : -1,
        "Fours" : -1,
        "Fives" : -1,
        "Sixes" : -1,
        "Three of a Kind": -1,
        "Four of a Kind" : -1,
        "Full House" : -1,
        "Small Straight" : -1,
        "Large Straight" : -1,
        "Yahtzee" : -1,
        "Chance" : -1 
        }
    player1YatzeeBonusCount = 0
    player2YatzeeBonusCount = 0
    for i in range(1,14):
        print("Round", i)
        for player in players:
            print("It is " + player + "'s Turn")
            originalRoll = roll()
            turns = 1
            indexOfRolls = []
            possibleScore = {
                "Ones" : 0,
                "Twos" : 0,
                "Threes" : 0,
                "Fours" : 0,
                "Fives" : 0,
                "Sixes" : 0,
                "Three of a Kind": 0,
                "Four of a Kind" : 0,
                "Full House" : 0,
                "Small Straight" : 0,
                "Large Straight" : 0,
                "Yahtzee" : 0,
                "Chance" : 0
                }
            for index, _ in enumerate(originalRoll):
                indexOfRolls.append(index+1)
            print("Die Number:\t",*indexOfRolls, sep = " ")
            print("Die Value:\t",*originalRoll, sep = " ")
            while turns < 3:
                while True:
                    try:
                        reRoll = input("Enter Die Number to Re-Roll or Nothing to Keep Dice (Separate with commas for multiple dice numbers): ")
                        newRoll = rollAgain(reRoll, originalRoll)
                        break
                    except:
                        print("Invalid Die Number")
                indexOfNewRolls = []
                for index, _ in enumerate(newRoll):
                    indexOfNewRolls.append(index+1)
                print("Die Number:\t",*indexOfNewRolls, sep = " ")
                print("Die Value:\t", *newRoll, sep = " ")
                originalRoll = newRoll
                turns +=1
            ones = rolledN(newRoll, 1)
            twos = rolledN(newRoll, 2)
            threes = rolledN(newRoll, 3)
            fours = rolledN(newRoll, 4)
            fives = rolledN(newRoll, 5)
            sixes = rolledN(newRoll, 6)
            threekind = threeOfAKind(newRoll)
            fourkind = fourOfAKind(newRoll)
            fullhouse = fullHouse(newRoll)
            smallstraight = smallStraight(newRoll)
            largestraight = largeStraight(newRoll)
            yahtzee = Yahtzee(newRoll)
            chance = Chance(newRoll)
            possibleScore["Ones"] = ones
            possibleScore["Twos"] = twos
            possibleScore["Threes"] = threes
            possibleScore["Fours"] = fours
            possibleScore["Fives"] = fives
            possibleScore["Sixes"] = sixes
            possibleScore["Three of a Kind"] = threekind
            possibleScore["Four of a Kind"] = fourkind
            possibleScore["Full House"] = fullhouse
            possibleScore["Small Straight"] = smallstraight
            possibleScore["Large Straight"] = largestraight
            possibleScore["Yahtzee"] = yahtzee
            possibleScore["Chance"] = chance
            print("Your Possible Scores are:")
            for item, score in possibleScore.items():
                print("{}\t{}".format(item,score))
            validScoreName = False
            while validScoreName == False:
                finalScore = input("Where do you want your current roll to go (Type the score name exactly how you see it) ")
                if finalScore.strip() in possibleScore:
                    finalScore = finalScore.strip()
                    if player == "Player 1":
                        while player1Score[finalScore] >= 0:
                            if finalScore == "Yahtzee":
                                print("You have just scored another Yahtzee, and 100 points will be added to your final score")
                                player1YatzeeBonusCount += 1
                            else:
                                redoScore = input("You already have a score in this bracket, type in another place for your current roll to go ")
                                finalScore = redoScore.strip()
                        player1Score[finalScore] = possibleScore[finalScore]
##                        for item, score in player1Score.items():
##                            print("{}\t{}".format(item, score))
                    elif player == "Player 2":
                        while player2Score[finalScore] >= 0:
                            if finalScore == "Yahtzee":
                                print("You have just scored another Yahtzee, and 100 points will be added to your final score")
                                player2YatzeeBonusCount += 1
                            else:
                                redoScore = input("You already have a score in this bracket, type in another place for your current roll to go ")
                                finalScore = redoScore.strip()
                        player2Score[finalScore] = possibleScore[finalScore]
##                        for item, score in player2Score.items():
##                            print("{}\t{}".format(item, score))
                    validScoreName = True
                else:
                    print("Invalid Score Name")
                    validScoreName = False
    player1TotalScore = 0
    player2TotalScore = 0
    upperSection = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]
    lowerSection = ["Three of a Kind","Four of a Kind","Full House","Small Straight", "Large Straight","Yahtzee","Chance"]
    player1UpperSectionScore = 0
    player2UpperSectionScore = 0
    for i in upperSection:
        player1UpperSectionScore += player1Score.get(i)
        player2UpperSectionScore += player2Score.get(i)
    if player1UpperSectionScore >= 63:
        player1UpperSectionScore += 35
    if player2UpperSectionScore >= 63:
        player2UpperSectionScore += 35
    player1LowerSectionScore = 0
    player2LowerSectionScore = 0
    for j in lowerSection:
        player1LowerSectionScore += player1Score.get(j)
        player2LowerSectionScore += player2Score.get(j)
    player1YahtzeeBonus = player1YatzeeBonusCount * 100
    player2YahtzeeBonus = player2YatzeeBonusCount * 100
    player1TotalScore = player1UpperSectionScore + player1LowerSectionScore + player1YahtzeeBonus
    player2TotalScore = player2UpperSectionScore + player2LowerSectionScore + player2YahtzeeBonus
    print("Player 1's final score is: ", player1TotalScore)
    print("Player 2's final score is: ", player2TotalScore)
    if player1TotalScore > player2TotalScore:
        print("Player 1 Won")
    else:
        print("Player 2 Won")
main()
