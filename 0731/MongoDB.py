import pymongo

def submit_userinfo(id, pw):
    with open('0730/mongoDB_account.txt', 'r') as f:
        url = f.readline()

    try:
        client = pymongo.MongoClient(url)
        db = client['Typing']
        collection = db['userinfo']

        collection.insert_one({'id':id, 'password':pw, 'typing_info':0})
        print('회원가입 성공')

    except Exception as e:
        print(f'erorr: {e}')

    finally:
        return client.close()
 
def get_userinfo(id, pw):
    with open('0730/mongoDB_account.txt','r') as f:
        url = f.readline()

    try:
        client = pymongo.MongoClient(url)
        db = client['Typing']
        collection = db['userinfo']

        result = collection.find_one({'id':id, 'password':pw})
        if result == None:
            print('계정 정보 없음')
            return 'Fail'
        
        else:
            print('로그인 성공')
            return 'Success'
        
    except Exception as e:
        print(f'error: {e}')

def get_score(id):
    with open('0730/mongoDB_account.txt', 'r') as f:
        url = f.readline()

    try:
        client = pymongo.MongoClient(url)
        db = client['Typing']
        collection = db['userinfo']

        result = collection.find_one({'id':id})
        # print(result['typing_info'])
        return result['typing_info']
    
    except Exception as e:
        print(f'error: {e}')
        return 'Erorr: get_score'

def modify_score(id):
    with open('0730/mongoDB_account.txt', 'r') as f:
        url = f.readline()

    try:
        client = pymongo.MongoClient(url)
        db = client['Typing']
        collection = db['userinfo']

        origin_score = collection.find_one({'id':id})
        origin_score = origin_score['typing_info']

        result = collection.update_one({'id':id}, {'$set':{'typing_info': 1 + origin_score}})
            #update_one - https://blog.naver.com/kira_design_lab/222691662713   |   https://www.bearpooh.com/170 
        return '변경 완료'
    
    except Exception as e:
        print(f'error: {e}')