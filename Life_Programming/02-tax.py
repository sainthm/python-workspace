# 부가가치세 계산기

# 소비자 가격 = 물건 가격 * 1.1
# 물건 가격 = 소비자가격 * (1/1.1)
# 부가세 = 물건 가격 * 0.1 = 소비자 가격 * (1/11)

# 시나리오
# 세 가지 서비스가 존재
# a 서비스: 23만원, b 서비스: 40만원, c 서비스: 67만원
# 부가세 유무에 따른 지불 비용 출력 예제

price = [23, 40, 67]

def service_price():
    service = input('이용하실 서비스 종류를 입력하세요, a/b/c: ')
    valueAdded = input('부가세는 별도입니까?, y/n: ')
    if valueAdded == 'y':
        if service == 'a':
            result = 23 * 1.1
        if service == 'b':
            result = 40 * 1.1
        if service == 'c':
            result = 67 * 1.1
    if valueAdded == 'n':
        if service == 'a':
            result = 23
        if service == 'b':
            result = 40
        if service == 'c':
            result = 67
    print(round(result, 1), '만 원입니다.')

# IF 문이 너무 많이 쓰여서 개선 필요

service_price()