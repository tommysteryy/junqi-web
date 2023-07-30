from constants import Cards, Player, validCards, Game

def isInvalid(card):
    return card not in validCards

def fightSimple(redCard, blackCard):
    """
    Returns the winner of a fight where no special conditions apply, 
            and you can just compare sizes of the cards
    """
    if (redCard.value > blackCard.value):
        return Player.RED
    elif (redCard.value < blackCard.value):
        return Player.BLACK
    else:
        return Player.SELF_DESTRUCT

def fightWithGongBing(redCard, blackCard):
    """
    Returns the winner of a fight (@Player) where one of card1/card2 is a gongbing
    """
    if (redCard == Cards.gobi):
        if (blackCard == Cards.dile):
            return Player.RED
    else:
        if (redCard == Cards.dile):
            return Player.BLACK
    
    return fightSimple(redCard, blackCard)

def fightWithDiLei(redCard, blackCard):
    """
    Returns the winner of a fight when one of card1/card2 is a dilei. One of card1 and card2 must be.
    """
    if (redCard == Cards.dile):
        if (blackCard == Cards.gobi):
            return Player.BLACK
        elif (blackCard == Cards.zhda):
            return Player.SELF_DESTRUCT
        else:
            return Player.RED
    else:
        if (redCard == Cards.gobi):
            return Player.RED
        elif (redCard == Cards.zhda):
            return Player.SELF_DESTRUCT
        else:
            return Player.BLACK
        
def isImpossible(redCard, blackCard):
    return ((redCard == Cards.juqi) and (blackCard == Cards.dile) or 
            (redCard == Cards.dile) and (blackCard == Cards.juqi) or 
            (redCard == Cards.dile) and (blackCard == Cards.dile) or
            (redCard == Cards.dile) and (blackCard == Cards.dile) or
            (redCard == Cards.juqi) and (blackCard == Cards.juqi) or
            (redCard == Cards.juqi) and (blackCard == Cards.juqi))

    
def fightCard(redCard, blackCard):

    """
    returns two values:
     Val1 = Player.RED, Player.BLACK or Player.SELF_DESTRUCT
     Val2 = Game.CONTINUE or Game.Over
    """

    if (redCard == None) or (blackCard == None):
        raise ValueError("One of the cards is not right, please try again.")
    if (isImpossible(redCard, blackCard)):
        return Player.IMPOSSIBLE, Game.CONTINUE
    elif (redCard == Cards.juqi):
        return Player.BLACK, Game.OVER
    elif (blackCard == Cards.juqi):
        return Player.RED, Game.OVER
    elif (redCard == blackCard):
        return Player.SELF_DESTRUCT, Game.CONTINUE
    elif (redCard == Cards.zhda) or (blackCard == Cards.zhda):
        return Player.SELF_DESTRUCT, Game.CONTINUE
    elif (redCard == Cards.dile) or (blackCard == Cards.dile):
        return fightWithDiLei(redCard, blackCard), Game.CONTINUE
    else:
        ## will only have from gongbing to SiLing left, can do direct compare
        return fightSimple(redCard, blackCard), Game.CONTINUE
    

def fight(redCard, blackCard):

    red = Cards[redCard]
    black = Cards[blackCard]

    return fightCard(red, black)