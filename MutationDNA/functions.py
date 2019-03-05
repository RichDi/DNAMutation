
def checkForMutation(dna):
    for string in dna:
        count = 0
        base = string[0]
        for d in string:
            if d == base:
                count += 1
                if count == 4:
                    return True
            else:
                base = d;
                count = 1
    return False

def reorganizedna(dna):
    n_dna = ["","","","","",""]
    for string in dna:
        for idx, letter in enumerate(string):
            n_dna[idx] += letter
            
    return n_dna    

def hasMutation(dna):
    n_dna = reorganizedna(dna)
    if checkForMutation(dna) or checkForMutation(n_dna):
        return True
    else:
        return False




