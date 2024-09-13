class Solution:
    def reformatNumber(self, number: str) -> str:
        new_number = number.replace('-', '').replace(' ', '')
        answer = []
        while len(new_number) > 0:
            if len(new_number) > 4:
                answer.append(new_number[:3])
                new_number = new_number[3:]
            elif len(new_number) == 4:
                answer.append(new_number[:2])
                answer.append(new_number[2:])
                break
            else:
                answer.append(new_number)
                break
        return '-'.join(answer)