

import requests
import json,ast
from pprint import pprint
from sets import Set
from pytz import timezone
from datetime import datetime,timedelta
import calendar



subject,numberofscholar=raw_input().split()
numberofscholar=int(numberofscholar)

#Getting the top answers with given tag
URL_TOP_ANSWER1 ='https://api.stackexchange.com/2.2/tags/'  
URl_TOP_ANSWER2='/top-answerers/all_time'

#Getting top answers of a given user with same tag to determine if he/she has given reply of the same tag ever
URL_TAG_USER_ANSWERS1='https://api.stackexchange.com/2.2/users/'
URL_TAG_USER_ANSWERS2='/top-answers'

#Getting the badge details of a user to check if he has any badge with 'Teacher' 
URL_USER_BADGE1='https://api.stackexchange.com/2.2/users/'
URL_USER_BADGE2='/badges'

#Getting the reputation change details of last one month
URL_USER_REPUTATION1='https://api.stackexchange.com/2.2/users/'
URL_USER_REPUTATION2='/reputation'

#Getting the user detail
URL_USER_DETAIL1='https://api.stackexchange.com/2.2/users/'

#Getting the date in UTC Strin as supported by stackexchange api
today=str(calendar.timegm(datetime.now().timetuple()))
oneMonthBefore=str(calendar.timegm((datetime.now()- timedelta(days=30)).timetuple()))

#parameters for rest api
url_user_param={
    'site'     : 'stackoverflow',
    'order'    : 'desc',
    'sort'     : 'reputation'  
    }
url_replutation_param={
    'site'     : 'stackoverflow',
    'fromdate' : oneMonthBefore,
    'todate'   : today
    }
url_user_badge={
    'site'     : 'stackoverflow',
    'order'    : 'desc',
    'sort'     : 'rank'  
    }
url_params_topAnswer = { 
    'site'     : 'stackoverflow'
    }
url_params_tagUsers_answers={
    'site'     : 'stackoverflow',
    'order'    : 'desc',
    'sort'     :'activity'       
    }
url_params_tags_answers={
    'site'     : 'stackoverflow',
    'order'    : 'desc',
    'sort'     :'popular' 
    }

page = 1
not_done = True
user_list = []

# replies are paginated so loop thru until none left
while not_done and numberofscholar>0:
    # url_params['page'] = page
    # get next page of users
    
    #Getting the top answers of given tag
    api_response = requests.get(URL_TOP_ANSWER1+subject+URl_TOP_ANSWER2,params=url_params_topAnswer)
    json_data = api_response.json()
    #rawData= api_response.json()    # pull the list of users out of the json answer
    #data = json.load(api_response.text)

    #Storing the user ID and url of their profile
    ll=json_data['items']
    for item_elem in ll:
        user_list.append({item_elem['user']['user_id']:item_elem['user']['link']})
        #user_list[item_elem['user']['user_id']]=item_elem['user']['link']
    # show progress each time thru loop
    for item_elem in user_list:
        userkey=list(item_elem.keys())[0]
        userUrl=item_elem[userkey]
        
        
        #Getting the response for answers of given tag by the user in whole life
        api_response_more_than_one_answer = requests.get(URL_TAG_USER_ANSWERS1+str(userkey)+'/tags/'+subject+URL_TAG_USER_ANSWERS2,params=url_params_tagUsers_answers)
        #pprint(api_response_more_than_one_answer.json())
        json_data_more=api_response_more_than_one_answer.json()
        listTemp=json_data_more['items']
        
        #Gdtting the badge details and storing the names in a set and checking if it contains Teacher or not
        api_response_badge=requests.get(URL_USER_BADGE1+str(userkey)+URL_USER_BADGE2,params=url_user_badge)
        json_data_badge=api_response_badge.json()
        ll=json_data_badge['items']
        badgeSet=Set()
        for item_elem1 in ll:
            badgeSet.add(item_elem1['name'])
            
        #getting the reputations and same way checking for reputation change of 200 or more
        api_respons_reputation=requests.get(URL_USER_REPUTATION1+str(userkey)+URL_USER_REPUTATION2,params=url_replutation_param)
        json_data_reputation=api_respons_reputation.json()
        reputationSet=Set()
        ll=json_data_reputation['items']
        for item_elem2 in ll:
            if('reputation_change' in item_elem2):
                reputationSet.add(item_elem2["reputation_change"])
        
        #Checking all the conditions
        if (len(listTemp)>2) and 'Teacher' in badgeSet:
            fl=0
            for repItem in reputationSet:
                if(int(repItem)>=200):
                    fl=1
                    break
            if fl==1:
                api_response_user=requests.get(URL_USER_DETAIL1+str(userkey),params=url_user_param)
                json_data_user=api_response_user.json()
                json_data_user=json_data_user['items']
                location=""
                displayName=""
                for t in json_data_user:
                    if('location' in t):
                        location=t['location']
                    if('display_name' in t):
                        nameUser=t['display_name']
                #location=json_data_user['items'][15]
                #nameUser=json_data_user['items'][19]
                print "userkey:",userkey,"....name:",nameUser,"....top_answer....location:",location,'....url:',userUrl
                
                #Continuing the process until it reaches required scholar
                numberofscholar=numberofscholar-1
        
        #print userkey,":",":",badgeSet,":",reputationSet
    #print  user_list
    #note only so man queries allowed per day


    # prepare for next iteration if needed
    page += 1
    not_done = json_data['has_more']


'''
Input:
cryptography 2

Output:
userkey: 3474 ....name: erickson ....top_answer....location: United States ....url: http://stackoverflow.com/users/3474/erickson
userkey: 148870 ....name: Amber ....top_answer....location: California ....url: http://stackoverflow.com/users/148870/amber

'''

