
def print_itemmenu():
    print("0. 끝내기")
    print("1. 아이템추가")
    print("2. 아이템삭제")
    print("3. 아이템확인")
    print("4. 아이템사용")

#아이템 추가시 수량도 인자로 받기
#인벤토리 전역함수, 인자로 받아서 처리
#call by reference
def add_item(item,  amount, t_invetory):
    if check_item(item, t_invetory):
        t_invetory[item]+= amount
        print(item+"의 수량이 "+str(t_invetory[item])+"이 되었습니다.")
    else:
        t_invetory[item]= amount
        print(item+"이 추가되었습니다.")


def remove_item(item, t_invetory):
    if check_item(item, t_invetory):
        t_invetory[item]= 0
        print(item+"을 제거하였습니다.")
    else:
        print(item+"이 존재하지 않습니다.")

def consume_item(item, invetory):
    if check_item(item, inventory):
        if inventory[item]<=0:
            print("현재 아이템의 수량이 적어서 사용할 수 없습니다.")
        else:
            inventory[item]-=1
            print(item+"의 수량은 "+str(inventory[item])+"입니다.")
    else:
        print(item+("이 존재하지 않습니다."))

def check_item(item, t_invetory):
    return item in inventory


#while문 아이템 함수로 구현하기
def use_item(inventory):
    while True:
        print_itemmenu()
        option=int(input("메뉴 번호를 입력하세요"))

        if option == 0:
            print("종료합니다.")
            break

        elif option==1:
            item=input("아이템을 입력하세요")
            amount=int(input("수량을 입력하세요"))
            add_item(item, amount,inventory)
            #인자로 받기 수정필요

        elif option==2:
            item=input("아이템을 입력하세요")
            remove_item(item,inventory)

        elif option==3:
            print(inventory)

        elif option==4:
            item=input("아이템을 입력하세요")
            consume_item(item, inventory)

        else:
            print("잘못된 번호를 입력하셨습니다.")

inventory={}

#캐릭터 만들기
character={}
select_character= None

def new_character(name, t_character):
    if check_character(name, t_character):
        print("이미 존재하는 캐릭터의 이름입니다.")
    else:
        inventory={}
        t_character[name]=inventory

    
def check_character(name, t_character):
    return name in t_character

def print_charactermenu():
    print("0. 끝내기")
    print("1. 캐릭터추가")
    print("2. 캐릭터 이름출력")
    print("3. 캐릭터 선택")
    print("4. 캐릭터 인벤토리 조작")



while True:
    print_charactermenu()
    option=int(input("메뉴 번호를 입력하세요"))
    if option == 0:
        print("종료합니다.")
        break

    elif option==1:
        name=input("캐릭터 이름을 입력해주세요")
        new_character(name, character)
            
    elif option==2:
        i=1
        print("----------")
        for name in character.keys():
            print(str(i)+". "+name)
            i+=1
        print("----------")

    elif option==3:
        temp_name= input("선택할 캐릭터의 이름을 입력해주세요")
        if check_character(temp_name, character):
            selct_character= temp_name
            print(selct_character+"이 선택되었습니다.")
        else:
            print("존재하지 않는 캐릭터입니다.")

    elif option==4:
        if selct_character==None:
            print("3번 메뉴로 캐릭터를 선택해주세요")
        else:
            print("선택된 캐릭터는 "+selct_character+"입니다.")
            inventory=character[selct_character]
            use_item(inventory)

    else:
        print("잘못된 번호를 입력하셨습니다.")

#캐릭터 이름으로 식별
#캐릭터 인벤토리
#캐릭터 장착기능
