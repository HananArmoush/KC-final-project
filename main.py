print('DO YOU SUFFER FROM DEPRESSION??')
YOUR_NAME=input('INTER YOUR NAME ')
print(f'welcome {YOUR_NAME} This test gives a brief about your psychological state and the degree of depression in you, and it is not an accurtae diagostice method , so you most go to the psychiatrist to diagnose you')
print('choose from 1 to 4') 


def q_1():
    while True :
        try : 
            Q_1 = int(input('i lost the desire and pleasure of doing things i used to do'))
            if 1<=Q_1<=4 :
                return Q_1
            else:
                print('please input a value')
        except ValueError:
            print('please input a value')



def q_2():
    while True :
        try : 
            Q_2 = int(input('i feel sad '))
            if 1<=Q_2<=4 :
                return Q_2
            else:
                print('please input a value')
        except ValueError:
            print('please input a value')



def q_3():
    while True :
        try : 
            Q_3 = int(input('i find it hard to fall asleep, stay asleep or sleep for long periods'))
            if 1<=Q_3<=4 :
                return Q_3
            else:
                print('please input a value')
        except ValueError:
            print('please input a value')



def q_4():
    while True :
        try : 
            Q_4 = int(input('i feel lethargic and lazy '))
            if 1<=Q_4<=4 :
                return Q_4
            else:
                print('please input a value')
        except ValueError:
            print('please input a value')



def q_5():
    while True :
        try : 
            Q_5 = int(input('i feel bad for myself'))
            if 1<=Q_5<=4 :
                return Q_5
            else:
                print('please input a value')
        except ValueError:
            print('please input a value')



def q_6():
    while True :
        try : 
            Q_6 = int(input('i feel hard to concentrate '))
            if 1<=Q_6<=4 :
                return Q_6
            else:
                print('please input a value')
        except ValueError:
            print('please input a value')



def q_7():
    while True :
        try : 
            Q_7 = int(input('i started talking or moving very slowly or vice versa '))
            if 1<=Q_7<=4 :
                return Q_7
            else:
                print('please input a value')
        except ValueError:
            print('please input a value')



def q_8():
    while True :
        try : 
            Q_8 = int(input('i feel like there is no reason to live '))
            if 1<=Q_8<=4 :
                return Q_8
            else:
                print('please input a value')
        except ValueError:
            print('please input a value')



def q_9():
    while True :
        try : 
            Q_9 = int(input('i feel happy '))
            if 1<=Q_9<=4 :
                return Q_9
            else:
                print('please input a value')
        except ValueError:
            print('please input a value')


def answers():

    all_answers= q_1()+q_2()+q_3()+q_4()+q_5()+q_6()+q_7()+q_8()+q_9()

    if all_answers <= 9 :
        return 'your result indicates that there are no symptoms of depression'
    
    elif all_answers <= 14 :
        return 'your result indicates very mild symptoms or no symptoms, you may not suffer from depression'
    
    elif all_answers <= 20 :
        return 'your result indicates mild depressive symptoms , so we advise you to see a doctor '
    
    elif all_answers <= 26 :
        return 'Your result indicates that there are symptoms of moderate depression, so it seems that you may suffer from moderate psychological depression and we advise you to see a specialist psychologist.'
    elif all_answers <= 30 :
        return 'Your result indicates symptoms of moderate depression, so it seems that you suffer from moderate-intensity psychological depression, and we advise you to consult a specialist psychologist.'
    elif all_answers <= 36 :
        return 'Your result indicates that there are symptoms of severe depression, so it seems that you suffer from severe psychological depression, and we advise you to consult a specialist psychologist.'
    
print(answers())