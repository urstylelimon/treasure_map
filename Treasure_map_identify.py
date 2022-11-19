print("\n_____Here is yor 4 * 4 matrix._____\n")
row1 = ["⬜️","⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️","⬜️"]
row4 = ["⬜️","⬜️","⬜️","⬜️"]

map = [row1,row2,row3,row4]
print(f"{row1}\n{row2}\n{row3}\n{row4}")

position = input("Enter your position.Where you see the X : ")

row = int(position[0])
colum = int(position[1])

selected_row = map[row-1]
selected_row[colum - 1] = "X"

print("\n_____Here is your new matix with your entered location._____\n")
print(f"{row1}\n{row2}\n{row3}\n{row4}")