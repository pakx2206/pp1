def influencer(facebook,twitter,instagram):
    if facebook==twitter and twitter==True:
        return "A person can be a good influencer!"
    if facebook==instagram and instagram==True:
        return "A person can be a good influencer!"
    if instagram==twitter and twitter==True:
        return "A person can be a good influencer!"
    else:
        return "Person won't be a good influencer!"
    
print(influencer(True,True,False))
print(influencer(True,False,True))
print(influencer(False,True,True))
print(influencer(False,False,True))