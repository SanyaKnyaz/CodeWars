'''
Simple Fun #58: Volleyball Positions
https://www.codewars.com/kata/5889f08eb71a7dcee600006c
'''
def volleyball_positions(formation, k):
    if k%6 == 0:
        return formation
    for i in range(0, k%6):
        curr = formation[1][0]
        formation[1][0] = formation[0][1]
        formation[0][1] = formation[1][2]
        formation[1][2] = formation[3][2]
        formation[3][2] = formation[2][1]
        formation[2][1] = formation[3][0]
        formation[3][0] = curr
    return formation