def test():
    troom, tcond=map(int,input().split())
    mode=input()
    tend=troom

    match mode:
        case "heat":
            if (tcond>troom):
                tend=tcond
        case "freeze":
            if (tcond < troom):
                tend = tcond
        case "auto":
            tend=tcond
    print(tend)
