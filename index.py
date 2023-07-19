import asyncio
import json
from requests import request  # import our request function.


#geting all the elements

get = Element("get")
post = Element("post")
put = Element("put")
delete = Element("delete")


async def main():
     baseurl = "https://jsonplaceholder.typicode.com"

     # GET
     headers = {"Content-type": "application/json"}
     response = await request(f"{baseurl}/posts/2", method="GET", headers=headers)
     g = f"GET request=> status:{response.status}, json:{await response.json()}"
     get.write(g)

     # POST
     body = json.dumps({"title": "test_title", "body": "test body", "userId": 1})
     new_post = await request(f"{baseurl}/posts", body=body, method="POST", headers=headers)
     p = f"POST request=> status:{new_post.status}, json:{await new_post.json()}"
     post.write(p)

     # PUT
     body = json.dumps({"id": 1, "title": "test_title", "body": "test body", "userId": 2})
     new_post = await request(f"{baseurl}/posts/1", body=body, method="PUT", headers=headers)
     pu = f"PUT request=> status:{new_post.status}, json:{await new_post.json()}"
     put.write(pu)

     # DELETE
     new_post = await request(f"{baseurl}/posts/1", method="DELETE", headers=headers)
     d =f"DELETE request=> status:{new_post.status}, json:{await new_post.json()}"
     delete.write(d)

asyncio.ensure_future(main())