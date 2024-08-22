def distribute_apples():
    print("Enter the number of apples and people separated by a space:")
    n, m = map(int, input().split())
    
    # рассчитываем количество яблок у каждого человека
    apples_per_person = n / m
    remaining_apples = n % m
    
    # выводим результат в целыми яблоками
    print(f"Каждому достанется по {apples_per_person} яблок, {remaining_apples} яблок(о) осталось.")
    
if __name__ == "__main__":
    distribute_apples() 