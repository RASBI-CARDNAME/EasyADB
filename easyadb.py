##made by Rasbi##

import os

##variable##

number=''  # menu number variable

##main code##

while True:
    print("-----EasyAdbTools------")
    print('FASTBOOT & ADB 드라이버가 설치되어있어야 합니다')
    print("--------------------")
    print("1. 리커버리로 재부팅\n2. Fastboot로 재부팅\n3. Fastboot 탈출\n4. ADB / Fastboot 사용\n5. 기타\n6. 종료")
    print("------------------------")
    number = input("Please select a number. => ")

    if number == '1':
        print("잠시만 기다려 주세요...")
        os.system('adb devices')
        os.system('adb reboot recovery')
        for i in range(0,20):
            print("\n")
        print("------------------------")
        print("리커버리로 부팅하였습니다.")
        print("------------------------")
        print("\n")

    elif number == '2':
        print("잠시만 기다려 주세요...")
        os.system('adb devices')
        os.system('adb reboot bootloader')
        for i in range(0,20):
            print("\n")
        print("------------------------")
        print("Fastboot로 부팅하였습니다.")
        print("------------------------")
        print("\n")

    elif number == '3':
        print("잠시만 기다려 주세요...")
        os.system('fastboot reboot')
        for i in range(0,20):
            print("\n")
        print("------------------------")
        print("재부팅하였습니다.")
        print("------------------------")
        print("\n")

    elif number == '4':
        print("\n")
        print("------------------------")
        input("ADB를 사용하려면 Enter를 눌러주세요....\n------------------------")
        os.system('cmd.exe')
        print("------------------------")
        for i in range(0,20):
            print("\n")
        print("\n")

    elif number == '5':
        print("\n")
        for i in range(0,20):
            print("\n")
        print("--------------------")
        print("Made by RASBI")
        print("최종 업데이트: 2023-12-22")
        print("--------------------")
        input("Press enter to continue...")
        print("--------------------")
        for i in range(0,20):
            print("\n")
        print("\n")

    elif number == '6':
        print("\n")
        print("--------------------")
        input("Press enter to continue....\n--------------------")
        os.system('adb kill-server')
        break  # 루프 종료

    else:
        print("\n")
        for i in range(0,20):
            print("\n")
        print("--------------------")
        print("올바른 입력이 아닙니다.")
        print("--------------------")
        input("Press enter to continue...")
        print("--------------------")
        for i in range(0,20):
            print("\n")
        print("\n")
