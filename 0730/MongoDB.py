from pymongo import MongoClient

def submit_userinfo(userid, userpw):
    # print(userid, userpw)

    with open('0730/mongoDB_account.txt', 'r') as f:
        mongo_uri = f.readline()

    try:
        client = MongoClient(mongo_uri)
        db = client["MCTX"]
        collection = db["userinfo"]

        collection.insert_one({"id": userid, "password": userpw})

        # result = collection.find_one({"id": userid})
        # print(f"Retrieved Document #1: {result}")

        # result = collection.find_one({"id": "test2"})
        # print(f"Retrieved Document #2: {result}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        return client.close()
    

def get_userinfo(userid, userpw):
    with open('0730/mongoDB_account.txt', 'r') as f:
        mongo_uri = f.readline()

    try:
        client = MongoClient(mongo_uri)
        db = client["MCTX"]
        collection = db["userinfo"]

        result = collection.find_one({"id": userid, "password": userpw})
        print(f"res: {result}")

        if result == None:
            print('해당 계정 정보 없음')
            return 'Fail To Login'

        else:
            print('로그인 성공')
            return 'Success To Login'

        # result = collection.find_one({"id": "test2"})
        # print(f"Retrieved Document #2: {result}")

    except Exception as e:
        print(f"Error: {e}")
        return 'Error'