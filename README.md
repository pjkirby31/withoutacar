# withoutacar
## Inspiration
People talk about giving up their car and trying to be more environmentally friendly on a day to day basis, but only a few of those people ever really try. We wanted to create something that would let people easily see how they can implement alternative modes of transportation in their daily life. We are not forcing anyone to do anything, we are just providing the information so people can make a choice about how they want to get around.

## What it does
Withoutacar allows users to input their home address (or a nearby address) and their car's approximate MPG. We then ask users where they plan on going, and how many times they will visit that place. We specifically don't specify a time range because we wanted to allow users to make that choice. A user could input everywhere they plan to drive to over the next day, week, or even month.

We then use the Google Maps API to calculate the most time efficient mode of transportation (other than by car) and display that information to the user. The user can see each trip they plan on taking and how much longer it will take to travel there by bike, transit, or on foot. We also provide cumulative statistics about how much CO2, and money on gasoline a user would save if they went without a car.
 
## How we built it
We built a custom API that allows us to send our server information about where a user plans on traveling, and it will respond with information about the most efficient routes. Our API runs on a Flask server that we deployed on an Azure VM so we could access from our website. In order to find the most efficient travel methods, we utilize the Google Maps API. We also use the Google Maps API to power the address autocomplete that a user sees in our forms.

To host our website we set up a second Azure VM and use Apache to display our website. We wanted to do this so we could purchase a domain and connect it to our server, but we ended up not being able to do this.

## Challenges we ran into
We ran into challenges while setting up the servers and configuring them to host our API and website. We also ran into challenges during the ideation and design phase as we had a lot of trouble coming up with an idea that we all felt passionate about. While designing our website we had trouble trying to make a simple UI which doesn’t come with clunky form, but still had all the necessary components. Lastly, trying to connect external APIs and making sure that requests were successfully sent and receiving data back was tricky when our project was not all running on one machine.

## Accomplishments that we're proud of
1. We were able to build and deploy a website which anyone can view
2. We created a form that is simple, but effective
3. The report we provide to the user contains enough information to be informative, but it is not an overwhelming amount of data
4. The API we created for our project is fast and can handle a large amount of requests

## What we learned
We learned how to build and host a website on an Azure VM. We also learned how to use the Google Maps API for both address autocomplete and finding travel routes. 

## What's next for Withoutacar
We would like to improve the user experience on our website by improving the report generated about travel information. It would be cool to add a map so the user could see what route they might be taking with a bike versus with a car. We would like to incorporate more API’s into our report to get more accurate gasoline prices, walkability scores for a user’s location, and weather forecasts. We also want to add user leader boards and rewards for users who walk/bike the most to encourage more people to join our movement.

## Credits for external templates and APIs.
Google Maps API: https://developers.google.com/maps/documentation
Website Template: https://themefisher.com




