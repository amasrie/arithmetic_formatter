def arithmetic_formatter(list, answer = False):
    if len(list) > 5:
        return "Error: Too many problems."
    else:
        line1 = ""
        line2 = ""
        line3 = ""
        line4 = ""
        first = True
        for elem in list:
            separator = elem.split(" ")
            if separator[1] != "+" and separator[1] != "-":
                return "Error: Operator must be '+' or '-'."
            elif not (separator[0].isnumeric()) or not (separator[2].isnumeric()):
                return "Error: Numbers must only contain digits."
            elif len(separator[0]) > 4 or len(separator[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
            else:
                if not first:
                    line1 += "    "
                    line2 += "    "
                    line3 += "    "
                    line4 += "    "
                first = False
                op1 = separator[0]
                op = separator[1]
                op2 = separator[2]
                res = int(op1) + int(op2) if op == "+" else int(op1) - int(op2)
                line1 += "  "
                line2 += op + " "
                line3 += "--"
                line4 += " "
                lop1 = len(op1)
                lop2 = len(op2)
                lres = len(str(res))
                diff = abs(lop2 - lop1)
                max = lop2 if lop2 > lop1 else lop1
                if lres == lop1 or lres == lop2:
                    line4 += " "
                line4 += str(res)
                for _ in range(diff):
                    if lop2 > lop1:
                        line1 += " "
                    else:
                        line2 += " "
                for _ in range(max):
                    line3 += "-"
                line2 += op2
                line1 += op1
        lines = line1 + "\n" + line2 + "\n" + line3
        lines = lines if not answer else lines + "\n" + line4
        return lines

#print(arithmetic_formatter(["32 + 8", "1 - 3801", "999.9 + 9999", "523 - 49"], True))


