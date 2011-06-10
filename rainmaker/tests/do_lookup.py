import rainmaker

from mock import patch

import json
import mock
import unittest


BART_OBJ = {u'status': 200, u'interests': {u'Football': True, u'Golf': True, u'Business': True, u'Tennis': True, u'Sports & Recreation': True, u'Blogging': True, u'News & Current Events': True, u'Basketball': True, u'Baseball': True, u'Social Networks': True, u'Online Journals': True, u'Technology': True, u'Online News': True}, u'socialProfiles': [{u'url': u'http://www.facebook.com/bart.lorang', u'username': u'bart.lorang', u'birthday': u'08/16/1979', u'type': u'facebook', u'id': u'651620441'}, {u'url': u'http://twitter.com/lorangb', u'username': u'lorangb', u'type': u'twitter', u'id': u'5998422'}, {u'url': u'http://www.linkedin.com/in/bartlorang', u'username': u'bartlorang', u'type': u'linkedin', u'id': u'bartlorang'}, {u'url': u'http://about.me/lorangb', u'type': u'about.me'}, {u'url': u'http://www.flickr.com/people/39267654@N00/', u'type': u'flickr', u'id': u'39267654@N00'}, {u'url': u'http://profiles.friendster.com/6986589', u'type': u'friendster'}, {u'url': u'https://profiles.google.com/lorangb', u'username': u'lorangb', u'type': u'google profile', u'id': u'lorangb'}, {u'url': u'http://www.myspace.com/137200880', u'type': u'myspace'}, {u'url': u'http://picasaweb.google.com/lorangb', u'type': u'picasa'}, {u'url': u'http://tungle.me/bartlorang', u'username': u'bartlorang', u'type': u'tungle.me', u'id': u'bartlorang'}, {u'url': u'http://youtube.com/lorangb', u'type': u'youtube'}, {u'url': u'http://profiles.friendster.com/6986589', u'type': u'friendster'}], u'demographics': {u'maritalStatus': u'Single', u'gender': u'Male', u'age': u'31', u'homeOwnerStatus': u'Own', u'locationGeneral': u'Denver, Colorado, United States', u'influencerScore': u'81-90', u'householdIncome': u'250k+', u'children': u'No'}, u'organizations': [{u'startDate': u'2010-01', u'name': u'Forseti Holdings, LLC', u'title': u'Chairman & CEO'}, {u'startDate': u'2010-01', u'name': u'Rainmaker Technologies', u'title': u'CEO'}, {u'isPrimary': True, u'name': u'Forseti Holdings LLC', u'title': u'Chairman & CEO'}, {u'isPrimary': False, u'name': u'CloudCenter LLC', u'title': u'Chairman & CEO'}, {u'isPrimary': False, u'name': u'DTS'}], u'photos': [{u'url': u'http://graph.facebook.com/651620441/picture?type=large', u'type': u'facebook'}, {u'url': u'https://lh5.googleusercontent.com/-EkI-dQC-4iM/AAAAAAAAAAI/AAAAAAAAAAA/o2NExlQVurA/photo.jpg?sz=200', u'type': u'google profile'}, {u'url': u'http://profile.ak.fbcdn.net/hprofile-ak-snc4/41508_651620441_4210927_n.jpg', u'type': u'facebook'}, {u'url': u'http://photos.friendster.com/photos/98/56/6986589/4262265956117t.jpg', u'type': u'friendster'}, {u'url': u'http://c2.ac-images.myspacecdn.com/images01/128/l_d7f2149dcb61b290b25232bf4c7968b9.jpg', u'type': u'myspace'}, {u'url': u'http://images.plaxo.com/fetch_image?path=249108119662_0_-413637613', u'type': u'plaxo'}, {u'url': u'http://a1.twimg.com/profile_images/712689472/Me.png', u'type': u'twitter'}, {u'url': u'https://secure.gravatar.com/avatar/956b7dca7c77a12c43ebe9ae09dfaba8', u'type': u'gravatar'}, {u'url': u'http://media.linkedin.com/mpr/mpr/shrink_80_80/p/2/000/086/2c8/2444fae.jpg', u'type': u'linkedin'}], u'contactInfo': {u'emailAddresses': [u'lorangb@gmail.com'], u'givenName': u'Bart', u'familyName': u'Lorang', u'fullName': u'Bart Lorang'}}

BART_SAMPLE = """\
{
 "status": 200,
 "contactInfo": {
 "familyName": "Lorang",
 "givenName": "Bart",
 "fullName": "Bart Lorang",
 "emailAddresses": 
 [
   "lorangb@gmail.com"
 ]
},
 "interests": { 
 "Football": true,
 "Sports & Recreation": true,
 "Business": true,
 "Online News": true,
 "Baseball": true,
 "Tennis": true,
 "News & Current Events": true,
 "Basketball": true,
 "Blogging": true,
 "Social Networks": true,
 "Online Journals": true,
 "Golf": true,
 "Technology": true
},
 "organizations": 
[
 {
   "name": "Forseti Holdings, LLC",
   "title": "Chairman & CEO",
   "startDate": "2010-01"
 },
 {
   "name": "Rainmaker Technologies",
   "title": "CEO",
   "startDate": "2010-01"
 },
 {
   "name": "Forseti Holdings LLC",
   "title": "Chairman & CEO",
   "isPrimary": true
 },
 {
   "name": "CloudCenter LLC",
   "title": "Chairman & CEO",
   "isPrimary": false
 },
 {
   "name": "DTS",
   "isPrimary": false
 }
],
 "demographics": {
 "influencerScore": "81-90",
 "householdIncome": "250k+",
 "age": "31",
 "homeOwnerStatus": "Own",
 "locationGeneral": "Denver, Colorado, United States",
 "children": "No",
 "gender": "Male",
 "maritalStatus": "Single"
},
 "socialProfiles": 
[
 {
   "type": "facebook",
   "url": "http://www.facebook.com/bart.lorang",
   "id": "651620441",
   "birthday": "08/16/1979",
   "username": "bart.lorang"
 },
 {
   "url": "http://twitter.com/lorangb",
   "id": "5998422",
   "type": "twitter",
   "username": "lorangb"
 },
 {
   "url": "http://www.linkedin.com/in/bartlorang",
   "id": "bartlorang",
   "type": "linkedin",
   "username": "bartlorang"
 },
 {
   "url": "http://about.me/lorangb",
   "type": "about.me"
 },
 {
   "url": "http://www.flickr.com/people/39267654@N00/",
   "id": "39267654@N00",
   "type": "flickr"
 },
 {
   "url": "http://profiles.friendster.com/6986589",
   "type": "friendster"
 },
 {
   "url": "https://profiles.google.com/lorangb",
   "id": "lorangb",
   "type": "google profile",
   "username": "lorangb"
 },
 {
   "url": "http://www.myspace.com/137200880",
   "type": "myspace"
 },
 {
   "url": "http://picasaweb.google.com/lorangb",
   "type": "picasa"
 },
 {
   "url": "http://tungle.me/bartlorang",
   "id": "bartlorang",
   "type": "tungle.me",
   "username": "bartlorang"
 },
 {
   "url": "http://youtube.com/lorangb",
   "type": "youtube"
 },
 {
   "type": "friendster",
   "url": "http://profiles.friendster.com/6986589"
 }
],
 "photos": 
[
 {
   "url": "http://graph.facebook.com/651620441/picture?type=large",
   "type": "facebook"
 },
 {
   "url": "https://lh5.googleusercontent.com/-EkI-dQC-4iM/AAAAAAAAAAI/AAAAAAAAAAA/o2NExlQVurA/photo.jpg?sz=200",
   "type": "google profile"
 },
 {
   "url": "http://profile.ak.fbcdn.net/hprofile-ak-snc4/41508_651620441_4210927_n.jpg",
   "type": "facebook"
 },
 {
   "url": "http://photos.friendster.com/photos/98/56/6986589/4262265956117t.jpg",
   "type": "friendster"
 },
 {
   "url": "http://c2.ac-images.myspacecdn.com/images01/128/l_d7f2149dcb61b290b25232bf4c7968b9.jpg",
   "type": "myspace"
 },
 {
   "url": "http://images.plaxo.com/fetch_image?path=249108119662_0_-413637613",
   "type": "plaxo"

 },
 {
   "url": "http://a1.twimg.com/profile_images/712689472/Me.png",
   "type": "twitter"

 },
 {
   "type": "gravatar",
   "url": "https://secure.gravatar.com/avatar/956b7dca7c77a12c43ebe9ae09dfaba8"
 },
 {
   "type": "linkedin",
   "url": "http://media.linkedin.com/mpr/mpr/shrink_80_80/p/2/000/086/2c8/2444fae.jpg"
 }
]
}
"""

class TestRainmakerAPI(unittest.TestCase):
    def setUp(self):
        self.rainmaker = rainmaker.RainMaker("SOME_API_KEY")
        
    @patch.object(rainmaker.RainMaker, 'helper')
    def testSampleData(self, helper):
        helper.return_value = json.loads(BART_SAMPLE)
        
        self.assertEqual(self.rainmaker.do_lookup(), BART_OBJ)
    
    #Test the helper functions
