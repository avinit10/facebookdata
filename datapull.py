import requests
import json


# for this code to run you need to get access_token of the app you made
# after you have to extend that token to make is valid for more than because it expires in 2 hours 

#-----------------class creation to pull data from facebook---------------------------------------

class dataFromFacebook():

#-----------------access_ token for the particular facebook user-----------------------------------
    def __init__(self):

        self.token="" #Enter access token as string here
        self.api="https://graph.facebook.com/v7.0/me?fields="

#-----------------get_name function for getting the name of the user-------------------------------
    def get_name(self):
        api=self.api+"name"+"&access_token="+self.token
        data=requests.get(api)
        print(data.json()['name'])

#-----------------user_email function for getting user email---------------------------------------
    def user_email(self):
        api=self.api+"email"+"&access_token="+self.token
        data=requests.get(api)
        print(data.json()['email'])    

#-----------------get_post function for getting posts on from the user-----------------------------
    def get_post(self):
        api=("https://graph.facebook.com/v7.0/me?fields={}&access_token="+self.token).format("posts")
        data=requests.get(api)
        print(data.json()['posts'])

#-----------------get_comments_from_post for getting comments from a particular post----------------        
    def get_comment_from_post(self,post_id):
        self.post_id=post_id
        api="https://graph.facebook.com/v7.0/"+self.post_id+"/comments?access_token="+self.token
        data=requests.get(api)
        print(data.json())               

data=dataFromFacebook()
data.get_name()

#data.get_post()

#data.user_email()

#data.get_comment_from_post("<comment_id>")

