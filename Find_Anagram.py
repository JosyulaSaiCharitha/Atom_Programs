def panagram(a):
    alpha="abcdefghijklmnopqrstuvwxyz"
    for i in alpha:
        if i not in a.lower():
            return False
    else:
        return True
if (panagram("The quick brown fox jumps over the lazy dog")==True):
    print("Panagram")
else:
    print("Not")
