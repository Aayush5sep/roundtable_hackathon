## Roundtable Hackathon Project Details
   - Aayush Goyal, B.Tech EE 1st Year, DTU
   - Aaryaveer Bhardwaj, B.Tech EE 1st Year,DTU
   - Vishal Kumar Roy, B.Tech ME 1st Year, DTU

# User Authentication
    - Login,Logout,SignUp options available.
    - SqLite Database used for storing models i.e. any types of details.
   - Check Users Folder

# Special Admin Access Login Details
    Username: hackathon
    Password: boonsredoc
   - Login with the above details and you get access to special options in the links section.
  
# Order Tracking and DashBoard
    - Successfully Created the System to Google OAuth , access gmails from the user and web-scrape them using GMAIL API.
    - However, Credentials.json file deleted for Security Purposes. So, wouldn,t work online in the server.
    - Scraping SMS for orders is still in development Phase.
   - Function Details in Tracking/Views.py auth(),tracking()
  
# Affiliate Link Adding Error Details
    - Due to requirement of Purchased License,adding a link may give **Proxy Error**. 
    - However,The Code works perfectly fine when running the webapp locally on your own PC.
   - Code in Affiliates/Views.py add_link(),addpage()
  
# Reward System
    - Created Model for storing the Rewards
    - Order Successfull confirmation Scraping in Development
   -Model/Class details in Affiliates/Views.py() and Users/Views.py()
   
# Search Product Functionality
    - Search for Products and their Affiliate Links
    - Function checks the added Products and give matches for Name,Website,Seller,Influencer
   - Search Logic in Affiliates/Views.py()
