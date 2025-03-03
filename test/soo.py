from collections import Counter
from itertools import chain

def solution(tickets, roll, shop, money):
    max_golden_tickets = 0
    ticket_price = sorted([(t.split(' ')[0], int(t.split(' ')[1])) for t in tickets], key=lambda x: x[1])
    
    # 새로고침을 몇 번 했는지에 따른 최대 가격 수를 계산하며 업데이트 
    # 새로고침은 (shop의 길이 - 1) 만큼 가능
    for i in range(1, len(shop)):
        golden_tickets = 0
        left_money = money - roll * i # 새로고침 후 남은 잔액 
        if left_money < 3: # 티켓을 최소 3개 사려면 하나 당 가격이 1인 상품 3개를 사야 하므로 돈이 3은 남아야 함
            continue
        chained_list = list(chain(*shop [:i+1] ))
        counts = Counter(chained_list)
        # 3개 이상 등장한 값만 선택한 배열 생성
        filtered_by_counts = []
        for ticket_name, count in counts.items():
            if count >= 3:
                find_three_time = count // 3
                for _ in range(find_three_time):
                    filtered_by_counts.append(ticket_name)
                    
        # 저렴한 것부터 구매 가능한지 확인
        for name, price in ticket_price:
            if left_money < 0:
                break
            if name in filtered_by_counts:
                cnt = filtered_by_counts.count(name)
                for _ in range(cnt):
                    if left_money - price * 3 >= 0:
                        left_money -= price * 3
                        golden_tickets += 1

        max_golden_tickets = max(max_golden_tickets, golden_tickets)

    return max_golden_tickets

tickets = ["A 1", "B 2", "C 5", "D 3"]
roll = 10
shop = [["B", "C", "B", "C"], ["A", "A", "A", "B"], ["D", "D", "C", "D"]]
money = 30
print(solution(tickets, roll, shop, money))