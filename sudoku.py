def solveSudoku(self, board: List[List[str]]) -> None:
    """
        Do not return anything, modify board in-place instead.
    """

    columns = []
    for i in range(9):
        column = []
        for row in board:
            value = row[i]
            column.append(value)

        columns.append(column)

    boxes = []
    c_pointer = 0
    r_pointer = 0
    box = []
    while True:

        # Go next row
        while True:
            val = board[r_pointer][c_pointer]
            box.append(val)
            r_pointer += 1

            if r_pointer % 3 == 0:
                break

        # Go next column
        r_pointer -= 3
        c_pointer += 1

        # One box found
        if len(box) == 9:
            boxes.append(box)
            box = []

        # Go to next row of boxes
        if c_pointer == 9:
            c_pointer = 0
            r_pointer += 3

        if len(boxes) == 9:
            break

    empty_cells = {}
    for row_num in range(9):
        b = board[row_num]

        for col_num in range(9):
            val = b[col_num]

            if val == ".":

                box_num = (col_num//3) + (3*(row_num//3))
                val_num = f"{row_num}{col_num}{box_num}"

                all_possible_values = [f"{i+1}" for i in range(9)]
                possible_values = []

                row_check = [i for i in b if i != '.']
                col_check = [i for i in columns[col_num] if i != '.']
                box_check = [i for i in boxes[box_num] if i != '.']

                total_check = row_check + col_check + box_check

                for poss_val in all_possible_values:
                    if poss_val in total_check:
                        continue
                    else:
                        possible_values.append(poss_val)

                empty_cells[val_num] = possible_values

    # Fill in cells with only one possible value
    def one_value(self, all_empty_cells, sudoku_board):
        while True:
            removed_keys = {}
            # print(all_empty_cells)
            # print('')
            for key in all_empty_cells:

                values = all_empty_cells[key]

                if len(values) > 1:
                    continue

                # Update board
                cell_position = [int(key[0]), int(key[1])]
                val = "".join(values)
                sudoku_board[cell_position[0]][cell_position[1]] = val

                # Update col and box lists
                columns[int(key[1])][int(key[0])] = val
                boxes[int(key[2])][(int(key[0]) % 3) +
                                   3*(int(key[1]) % 3)] = val

                # Update list of removed keys
                removed_keys[key] = val

                break

            if removed_keys == {}:
                break

            # Remove keys and update possible values in dict
            for key in removed_keys:
                all_empty_cells.pop(key, None)

                affected_keys = []

                for k in all_empty_cells:
                    if k[0] == key[0] or k[1] == key[1] or k[2] == key[2]:
                        affected_keys.append(k)

                aff_val = removed_keys[key]

                for aff_key in affected_keys:
                    poss_vals = all_empty_cells[aff_key]

                    if aff_val in poss_vals:
                        poss_vals.remove(aff_val)
                        all_empty_cells[aff_key] = poss_vals

    one_value(self, empty_cells, board)
    if empty_cells == {}:
        return

    # Check all other empty cells in row, col, box for values that appear only once
    retry = False
    for key in empty_cells:
        related_keys_rows = []
        related_keys_col = []
        related_keys_box = []

        for k in empty_cells:
            if k == key:
                continue

            if k[0] == key[0]:
                related_keys_rows.append(empty_cells[k])

            if k[1] == key[1]:
                related_keys_col.append(empty_cells[k])

            if k[2] == key[2]:
                related_keys_box.append(empty_cells[k])

        related_keys_rows = sum(related_keys_rows, [])
        related_keys_col = sum(related_keys_col, [])
        related_keys_box = sum(related_keys_box, [])

        for poss_val in empty_cells[key]:
            if poss_val not in related_keys_rows or poss_val not in related_keys_col or poss_val not in related_keys_box:

                empty_cells[key] = [poss_val]

                retry = True
                break

    if retry == True:
        one_value(self, empty_cells, board)

    if empty_cells == {}:
        return

    def valid(row, col, num):
        for i in range(9):

            if board[row][i] == num:
                return False
            if board[i][col] == num:
                return False
            if board[(3*(row//3)) + i//3][(3*(col//3)) + i % 3] == num:
                return False

        return True

    def brute(row, col):
        if row == 9:
            return True
        if col == 9:
            return brute(row+1, 0)

        if board[row][col] == ".":
            for n in range(1, 10):
                if valid(row, col, str(n)):
                    board[row][col] = str(n)

                    if brute(row, col + 1):
                        return True
                    else:
                        board[row][col] = "."
            return False
        else:
            return brute(row, col + 1)

    brute(0, 0)
