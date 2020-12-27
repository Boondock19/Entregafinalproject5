# Welcome to MedicPlace!

Hello this is my final project for cs50 harvards course, i´ve work very hard in doing, so i hope you will find it to your liking, im deeply proud of it.

## How the idea came to me:

Im from Venezuela,the country has really poor stadistics in economy,and thus in medical attention, most of venezuelans cant pay up the cost of medic consults and the hopitals are in a wicked state, so i thought i could create a page that is based in medical content, and besides we are in times of the Covid-19.

## What is MedicPlace:

As i said before is a page based on medical content, in the page doctors can create an user for them as well a profile, the doctor then can create articles in which they can inform the people of new advance in science, in treatments for diseases, methods on how to take care of oneself and love ones, opinions on others articles and more!. Besides the articles, doctors can create entrys of medicines (In venezuela we often have to change the brand and even the principal ingredient of a treatment, because it might be scarce or too expensive) in which they can explain for what purporse is used, principal ingredients,negative effects,contraindications (Very important!), and set it into a category of medicine (I will explain better below).

## Structure of the Website:

The Website has about 7-8 diferrent pages, first is the **layout.html**, its basically a navbar which has several links in it, for movement between pages, and the register,login and logout links.In this navbar not every user can see all the links, the links to create an article or a medicine entry can only be seen by users that are doctors, every other user can only see the medicine entrys, articles and profiles of doctor or other users.Finally this layout is present in every html file in the website.

In the **index.html** we have the index view in this page we have 3 list, the first one is a list of links to all the doctors that are registered, every links shows the first and last name of each doctor.The second list is for the different types of medicines, there is a link for every type of medicine (I did my research! but in any case if you see that the list is lacking one type you can contact me in 15-10627@usb.ve).The last list is a list of links for every article in the page.

**Register.html** is the basic register page it has a form which ask for firstname, lastname,age,email,username and password, it also ask the user if he/she is a doctor and with some javascript it shows or hides a input form for a doctor to write the clinic or hospital they work in.

**Login.html** simply shows a form that ask for the username and password, is the user in login without problems then its taken to the index page.

Then we have **data_sheet.html** this page works like a profile it shows the users firstname,lastname,age (if they are a normal user) and it also shows the workplace for the doctors and a rating system which the users can click to rate the doctors rating. The database loads different pages based in the user status (Doctor or not) if the page is from a doctor it also shows a list of links of article the doctor has written.

**New_Medic_article.html** loads a page with a form in where the doctors can fill the article's title and content, it also shows at the start of the page an brief explication of what they can write of and are redirected to the article's page.

**Medic_article.html** displays an article,this is, its title, content and which doctor create it. If the doctor who created the page is the request.user it displays an edit button and a delete button. The edit button lets the doctor edit the title and content of the article with javascript in the same page and it gets a response back from the server and shows it to the user. The delete button on the other hand is a form that sends a post request to the database and reedirects the user to the index page.Finally the articles have a feature of comments so they display a comment section for each article, every user (normal and doctors) can comment out and edit such comments (the edit is made with javascritp via a post request send to the database and the response is shown in the page).

**Medicine_type.html** shows a list of links for every entry of a certain type of medicine, it displays the brand name and the principal ingredient. If there isnt any entry in a type of medicine it shows a message.

**New_Medicine.html**  shows a form in which the doctors can write down the name of the medicine,type of medicine,summary and principal ingredient, then the user is redirected to the Medicine.html entry.

**Medicine.html** is the last page of the website and it displays the contents of a medicine entry, which is its name,type of medicine, the doctor who created it and summary. As in articles the doctor who created it the medicine can edit it via javascript with a post request to the database.

## Models of the Website!:

For this page i created seven models:

#### User:

Which uses the AbstractUser model, and its very convenient for users models. 

#### Medic:

I created the Medic and Normal_user model so i could differentiate the users type. For  the Medic model i used a foreignkey to the User model, asked a firstname,lastname,age,clinic, a rate which starts in 0, a summatory of rates and how many rates have been used, both start at 0 as well. For this model i created a function to calculate the promedy of the rate for a doctor.

#### Normal_user:

I created the Medic and Normal_user model so i could differentiate the users type. For  the Normal_user model i used a foreignkey to the User model, asked a firstname,lastname (both charfields) and age (intergerfield).

#### Medic_Article:

For the Medic_Article model i used two foreignkeys one to User and the other to Medic, so i could tell which user/doctor created it, besides this i asked form a title(charfield) and content(textfield, so we can represent it with breaklines) of the article.

#### Article_comment:

This models asks for four fields, two are foreingkeys one tho User and the other one to Medic_Article, the other to fields are one for comment (textfield) and the other for Date(datetimefield)

#### type_of_medicine:

Type of medicine just has one field and its a charfield, all the types are created via admin-site.

#### medicine:

Finally for medicine model i used 5 fields, two for foreingkeys which are: One to Medic and the other to type_of_medicine. For the other three fields i used two charfields ( title and pricipal ingredient) and the other one for the summary its a textfield.


## Views of the Website!:

For this page these are the views:
#### index:

In this view the server querys all the medics,articles and type of medicines objects, with the purpose of displaying lists. This view also verifies if the request.user is a medic, the page needs to check this otherwise it wont show all the links in the navbar. 

#### login_view:

The login_view is the standard login view, it loads a form and if it gets a post request, the database checks if the user exists, if it does the user is loged in and is taken to de index page.

#### register_view:

For this page the register_view its a litle more complex, it shows a form that ask for username,email,password,confirmation of the password,firstname,lastname,age, an is_dr parameter that is used for differentiate the creation of a Medic user or a Normal_User user. If is_dr is "yes" then it will ask for the clinic parameter as well and create a new medic user, if is_dr is "no" it will create  Normal_User user and if everything goes well the user is loged in and redirected to index page.This view has several checks about the filling of the inputs an displays a message in case an error ocurrs.

#### logout_view:

This view simply logs out the user.

#### data_sheet:

This view ask for the id of the user owner of the datasheet or profile, the first thing the view does is filter out if the user is a medic or a Normal_User with the id, it then tries to get a medic object with the id, if it does exist then is_medic is true else is_medic is false, with this variable we show the content of the page.Then if the filter works, we should have an array with one element so we check the len of the arrays and the one that is > 0 is the one will load the variable for the view,we pass down 2 variables data_sheet_user which gets the object of the resulting model,Page_type that the page uses to check which html load.

#### Rate_Dr:

This view is used inside the datasheet page and it can only be used in a medic page, and by user that are diferent from the owner of the profile ( this is done by checking if the request.user is the same user.id than the medic object).This view is for submmiting rating for the doctor is done via javascript and the database sents a jsonresponse back, it gets the value from the buttons on the page and Medic promedio method and saves the Medic object instance. This view is csrf exempt and gets the id from the data-set of html elements via javascript

#### New_Article_view:

This view loads a form for the doctor users, and in request.post gets the user.id to get the medic instanceand then create a new Medic_Article model and saving it, then the user is redirected to the index page.

#### Article_view:

This view asks for the id of the article to get its instance and get the comments for this especific article, it then checks if the user is medic for the links in navbar,then it also checks if the request.user is the owner of the article and sets a boolean value for the varaible is_owner which is used to show the buttons for edit and delete the article. This view has two possible post requests, one is for deleting the article and is filter by an try and except check(checks if a hidden input has been recieved) if the try works then it deletes the article and sends the user to the index page, otherwise it goes to the other post that is for the comment section of the page, this post only receives a comment parameter and with that it creates a comment instance which will be filled with the user (request.user), the article.id and the comment parameter, saves the comment instance and loads again the article page.

#### Edit_Article_view:

This view can only be seen by medic users and via a button in an article created by then  (done by the is_owner variable of the article_view), this view asks for the id of the article and shows the same form that is used to create a new article but it already has loaded the content of the article in each input, such that the user only has to make some changes and then save those changes.If a post request is made the view simply gets the parameters and saves them in the article instance and redirects the user to the articles page.

#### Edit_Article_comment_view:

Edit article is a view made for fetch requests, it needs the id of the comment for the motive of getting the comment instance to save the changes, the id is from a data-set from the html and via javascript the view then processes the id and content parameters and saves the changes, finally it creates lines in case the are "enter spaces" between the comment content, and sends back this content to the page via jsonresponse. This view is csrf exempt

#### Medicine_type_view:

The medicine type view querys the list of medicines for an type of medicine, via id, if the list is < 1 then it displays a message else loads the list of medicines. 

#### Medicine_view:

The medicine view loads the entry of a medicine model instance, it also gets the user of the medic who wrote the entry, because the template needs it to check if the request.user is equall to the user of the medic who wrote the entry, then if they are the same it displays an edit button, otherwise it wont. It also loads all the medicine types because the edit function of the medicines is done via javacript in the same page and it needs to display the list of types.

#### New_Medicine_view:

New medicine view loads a form for the medic user to do a post request, upon a post requests it gets all the parameters and creates a new Medicine object instance, then saves it, and loads the medicine view page for that object instance.

#### Edit_medicine_view:

This view is used in the medicine view, is only used via javacripts in a fetch request, and it needs the id of the medicine entry, which it gets from the data-set in the html from the javascript, it then gets the entry with the id, and saves in the data base the changes done by the user, returns back a jsonreponses for the front-end of the page.


## javascripts archives of the Website!:

There are 4 javascript archives in the page:

#### Register.js:

this script loads only on the register page, and it for the only purpose of showing or hidding an input for the clinic parameter, and is based in two eventlisteners one for a "yes" option and another for "no". The first changes the style to block while the other one changes the style to none of several divs.

#### rate.js:

rate.js only works on the datasheet of a medic user, and is used to make a post request to the database, to change the rate parameter of a medic object.It selects all the rating buttons and adds an eventlitener to them, this event gets the data-value of the button and sends it to the database via a fetch with the id of the medic which is stored in get_dr via a data-btn_id. It then changes the textContend of the spans elements and disables the buttons to avoid further rating.

#### edit_comment.js:

This script is used to edit the comments in the articles, it gets the id of the comment via the data-comment-id from the edit button, it then selects, two p tags ( one is displaying the actual content of the comment, the other is for the new content) and one textarea (used for the post request). It then adds an eventlistener and depending on the textcontent of the button it shows or hides the inputs and p tags, finale it ueses the edit_comment fuction to send a post request to the database and displays the response in one of the p tags.

#### edit_medicine.js:

This script is pretty similar to the edit_comment.js the only difference is the ammount of selectors, but the idea is the same, this script is used to edit a medicine entry with an edit button. With this button the script gets the id of the medicine entry, it then selects all the different p tags and input tags (select and textarea as well), then with an eventlistener and checking the textcontent of the button the script hides and shows the edit fields and the content fields, the last part of the script uses the edit_entry funtion to send a post request via a fetch to the database to change the content of the page and the entry, and finally sets the textcontent of the page to the new content. 