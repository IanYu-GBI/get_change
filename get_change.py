denominations = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01]

def main():
    get_change_summary(float(input('Enter the amount of change: ')))
    
def get_bill_num(num, denomination):
    bill_num = int(num / denomination)
    remainder = num - (denomination * bill_num)
    remainder = float(f'{remainder:.02f}')
    return bill_num, remainder

def get_change(num):
    denomination_dict = {}
    for denomination in denominations:
        bill_num, remainder = get_bill_num(num, denomination)
        denomination_dict[denomination] = bill_num
        num = remainder
    return denomination_dict

def get_change_summary(num):
    [print(f'{num} ${denomination}') for denomination, num in get_change(num).items() if num != 0]

if __name__ == "__main__":
    main()