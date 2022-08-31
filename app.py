from flask import Flask, render_template, request, session
import sqlite3
import chatterbot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = 'fgh456fdgdscv34sdv456nsd'
app.config['SESSION_TYPE'] = 'filesystem'

# delete old trained file
if os.path.exists("database.sqlite3"):
  os.remove("database.sqlite3")
  print('Old DB deleted.')

chatbot = chatterbot.ChatBot(
    'Chatty',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I donot understand. I am still learning.',
            'maximum_similarity_threshold': 0.3,
        }

    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',

)

trainer = ListTrainer(chatbot)
trainer.train([
"Hello",
"Hello Sir, How can i help you?",
"Hi",
"Hello Sir, How can i help you?",
"Good morning",
"Hello Sir, How can i help you?",
"Good afternoon",
"Hello Sir, How can i help you?",
"Bank Name?",
"XYZ Bank, Please visit (xyzbank.com) for more info",
"What is your bank name",
"XYZ Bank, Please visit (xyzbank.com) for more info",
"What is your bank location?",
"Dhaka, Bangladesh",
"bank location",
"Dhaka, Bangladesh",
"location",
"Dhaka, Bangladesh",
"address?",
"Dhaka, Bangladesh",
"address",
"Dhaka, Bangladesh",
"phone number?",
"Please Sir, you can call us 24/7 - 0123456789",
"Phone Number",
"Please Sir, you can call us 24/7 - 0123456789",
"number?",
"Please Sir, you can call us 24/7 - 0123456789",
"number",
"Please Sir, you can call us 24/7 - 0123456789",
"phone?",
"Please Sir, you can call us 24/7 - 0123456789",
"phone",
"Please Sir, you can call us 24/7 - 0123456789",
"branches?",
"we have about 200+ branches over the country",
"how many have you branch?",
"we have about 200+ branches over the country",
"How many Branch?",
"we have about 200+ branches over the country",
"time?",
"Sir, we are open on Govt. working Days",
"open time?",
"Sir, we are open on Govt. working Days",
"When you are open?",
"Sir, we are open on Govt. working Days",
"openning time?",
"Sir, we are open on Govt. working Days",
"Account Type?",
"There are different types of account, Savings, Current, Student account",
"account?",
"There are different types of account, Savings, Current, Student account",
"locker?",
"Yes sir, we have locker",
"locker system?",
"Yes sir, we have locker",
"have you any locker?",
"Yes sir, we have locker",
"locker",
"Yes sir, we have locker",
"open account?",
"Contact a Agent",
"how to open account?",
"Contact a Agent",
"how to create account?",
"Contact a Agent",
"create account",
"Contact a Agent",
"close account?",
"Contact a Agent",
"How to close account",
"Contact a Agent",
"ok",
"Thank You",
"Welcome",
"Thank You.",
"I want to take loan",
"Yes, It's Possible. Please Contact A agent.",
"Loan",
"Yes, It's Possible. Please Contact A agent.",
"credit card",
"Yes, You Can Take a Credit Or debit card",
"Credit Card",
"Yes, You Can Take a Credit Or debit card",
"services",
"Please Visit Our Bank Website, You can see Everythings.",
"What is the rate of interest applicable on the Super Savings Account?",
"Interest @ 3% pa is applicable on the Super Savings Account.",
"Savings Account?",
"Interest @ 3% pa is applicable on the Super Savings Account.",
"What is the rate of interest?",
"Interest @ 3% pa is applicable on the Super Savings Account.",
"When is interest credited to the Super Savings Account?",
"Interest on your Super Savings Account will be calculated and credited quarterly.",
"When will I receive my account statement?",
"You will receive your account statement the month following every financial year quarter i.e. July, October, January and April.",
"I receive my account statement?",
"You will receive your account statement the month following every financial year quarter i.e. July, October, January and April.",
"Can I use any branch across Bangladesh to operate my account?",
"Yes, you can access and operate your account from any branch of Bank across Bangladesh You can electronically transfer funds from one account to another account in any branch across cities. You can withdraw and deposit cash upto 50,000tk per day at any branch.",
"Can I use any branch",
"Can I use any branch across Bangladesh to operate my account?",
"Yes, you can access and operate your account from any branch of Bank across Bangladesh You can electronically transfer funds from one account to another account in any branch across cities. You can withdraw and deposit cash upto 50,000tk per day at any branch.",
"Can I open a Demat Account with my Super Savings Account?",
"Yes, you can open Demat Accounts with your Super Savings Account.",
"Can I open a Savings Account",
"Yes, you can open Savings Account.",
"Do I get, International Debit cum ATM Card, SMS Banking, Internet Banking, and PhoneBanking?",
"Yes. These services have been introduced to make banking a convenient and a hassle-free option for you. The International Debit cum ATM Card has been packed with additional features to convert it to a virtual bank.",
"Do I get, International Debit cum ATM Card?",
"Yes. These services have been introduced to make banking a convenient and a hassle-free option for you. The International Debit cum ATM Card has been packed with additional features to convert it to a virtual bank.",
"Do I get, International Debit SMS Banking ?",
"Yes. These services have been introduced to make banking a convenient and a hassle-free option for you. The International Debit cum ATM Card has been packed with additional features to convert it to a virtual bank.",
"Do I get, International Debit Internet Banking?",
"Yes. These services have been introduced to make banking a convenient and a hassle-free option for you. The International Debit cum ATM Card has been packed with additional features to convert it to a virtual bank.",
"Do I get, International Debit PhoneBanking?",
"Yes. These services have been introduced to make banking a convenient and a hassle-free option for you. The International Debit cum ATM Card has been packed with additional features to convert it to a virtual bank.",
"What is the withdrawal limit on my International Debit cum ATM Card?",
"You can withdraw upto 25,000 tk per day from your International Debit cum ATM card. You can also use your International Debit cum ATM card at other bank ATM.",
"What is the withdrawal limit ?",
"You can withdraw upto 25,000 tk per day from your International Debit cum ATM card. You can also use your International Debit cum ATM card at other bank ATM.",
"withdrawal limit",
"You can withdraw upto 25,000 tk per day from your International Debit cum ATM card. You can also use your International Debit cum ATM card at other bank ATM.",
"What are the services that are available through ATMs, Internet Banking, Phone Banking, SMS Banking?",
"ATMs Besides cash withdrawals, some of the important things that you can do through the International Debit cum ATM card"

"What is the minimum and maximum tenor for which Retail Term Deposit can be kept with abc Bank?",
"The minimum and maximum tenor for general/Senior citizen is 15 days and 20 years, respectively.",
"Retail Term Deposit can be kept with abc Bank",
"The minimum and maximum tenor for general/Senior citizen is 15 days and 20 years, respectively.",
"What is the minimum and maximum amount for which a Retail Term Deposit can be made with IDBI Bank?",
"The minimum amount is 10,000/- and the maximum amount under Retail Term Deposit is 99,99,999/-",
"What is the minimum and maximum amount Term Deposit?",
"The minimum amount is 10,000/- and the maximum amount under Retail Term Deposit is 99,99,999/-",
"What is the frequency Term Deposit of IDBI Bank?",
"The interest is compounded on a quarterly rest under cumulative/ reinvestment option",
"What is the interest rate applicable for Term Deposits?",
"The Interest Rates on term deposit of the bank is subject to change from time to time and the same is provided on the website of the Bank and also available at every branch.",
"How do I avail abc Home Loan?",
"You can apply for abc Home Loan by selecting any one of following ways.",
"How will IDBI Bank decide my Home Loan Eligibility?",
"We will assess your loan eligibility based on your age, qualification, income, number of dependents, spouse income, stability and continuity of your occupation, assets, liability base and your savings history and based on the value of the property proposed to be purchased.",
"What is the maximum Home Loan Amount I can get?",
"Home Loans are available maximum up to INR 10 Cr.",
"maximum Home Loan Amount",
"Home Loans are available maximum up to INR 10 Cr.",
"What is the maximum Loan tenure that I can have under abc Home Loan?",
"abc Home Loans have maximum repayment tenure of up to 30 years. Actual tenure of loan is subjected to bank’s discretion.",
"Can I get the Home Loan eligibility without selecting the property?",
"Yes. We can extend in-principle sanction based on your repayment capacity. Accordingly based on the loan amount sanctioned, you may search the property. For final sanction, property identified for the purpose should meet our criteria.",
"What security will I have to provide?",
"The security for the loan is a first mortgage of the property proposed to be financed with the proceeds of abc Home Loans by way of equitable mortgage by deposit of title deeds with memorandum of entry. The Bank will also decide the requirement of additional security if required for the process of loan application.",
"What security",
"The security for the loan is a first mortgage of the property proposed to be financed with the proceeds of abc Home Loans by way of equitable mortgage by deposit of title deeds with memorandum of entry. The Bank will also decide the requirement of additional security if required for the process of loan application.",
"What is the EMI and how is the EMI calculated on my Home Loan?",
"EMI is equated into monthly installments. This comprises of Principal as well interest component. Interest charged under Home Loan is on reducing Balance.",
"How do I repay my Home Loan EMI?",
"You may repay your Home Loan by way of SI (Standing Instruction) with abc Account or by way of ECS (Electronic Clearing System) instruction on your non abc account.",
"How do I reduce my interest cost under Home Loan?",
"You can reduce your interest cost by availing our product Home Loan Interest Saver. to konw the details. please call 1122",
"For what purpose I can avail Personal Loan?",
"To meet unexpected financial crunch / do away expensive Credit Card funds. At abc Bank you can avail Personal Loan for household buys, education of your children, hospitalization or any immediate payments. No end usage of funds stipulated. May even apply Personal Loan to meet Margin Money requirement of your Home Loan.",
"Personal Loan?",
"To meet unexpected financial crunch / do away expensive Credit Card funds. At abc Bank you can avail Personal Loan for household buys, education of your children, hospitalization or any immediate payments. No end usage of funds stipulated. May even apply Personal Loan to meet Margin Money requirement of your Home Loan.",
"What is an EMI?",
"EMI means Equated Monthly Instalment which includes principal and interest. You repay your loan by way of EMIs by giving standing instructions to debit your SB account with us. EMI is recovered every month on a predetermined date.",
"What documents are generally sought for Personal Loan approval?",
"Along with loan application you need to submit identity and residence proof, latest salary slip, form no.16, last six month’s bank statement. Loan application needs to be complete in all respects, you have to affix a photograph on the application at the provided place in application for the Personal Loan.",
"How interest is charged?",
"Interest is charged at predetermined rate on reducing balances. It is debited to loan account at monthly rests i.e end of every month.",
"What is the rate of interest?",
"For current rate of interest please contact nearest abc Bank branch.",
"Who can apply for Personal Loan with abc Bank?",
"Salaried class individuals having Savings bank account with any of the branch of abc Bank can apply for personal loan. Salaried Individuals having saving bank account i.e. liability relation with bank for 3 years or preferred customers having one year banking relation with us.",
"Why to avail Personal Loan from abc Bank?",

"Personal Loan from abc Bank?",
"Attractive rate of interest",

"What is the amount of loan that is sanctioned?",
"Minimum: 25,000 Maximum: 5,00,000",
"What is the validity of the cards?",
"These cards are valid for a period of 2 years from the date of production. (Marked on the face of the card) & card is not valid for payments in Bangladesh, India, Pakistan",
"How many times can I reload my card?",
"Your abc Bank WCC/ GCC is valid for a period of two years. Within this period, you can reload* your card as many times as you like. In case you are reloading your card after you have come back from your trip abroad i.e., before your next trip, you will need to fill up the reload form, pay either by debit to your IDBI Bank account or by cheque and provide a copy of your new air ticket.",
"How do I replace my card?",
"Contact abc Branch, request for a Replacement Card to be sent to your current location. However, this will be done only after the Bank verifies your identity.",
"What is a Cash Card?", 
"Where can I use this Cash Card?",
"Can be used to make purchases at over 5.50 lakh establishments in Bangladesh. It can also be used to withdraw cash from over 1660 abc Bank ATMs and all shared network ATMs in Bangladesh.",
"What are the charges for this card?",
"There is a charge of 150/- per card at the time of issue. For every reload, a fee of 10/- per card needs to be paid.",
"What if my Cash Card is lost or stolen?",
"Original Purchaser or the Recipient of the Cash Card may report a card as lost. All you need to do is call up abc's Phone Banking centre 1122 and quote the Cash card reference number mentioned on the card mailer. The card will be deactivated immediately to prevent misuse. For MTNL / BSNL Customers call: 1123 and for Other Customers call: 1124.",
"What is a Debit Card?",
"A Debit Card is a card that gives you online access to your Bank Account. The abc Bank International Debit-cum-ATM Card allows you to purchase goods at Merchant Establishments and also gives you the freedom to withdraw cash from ATMs in Bangladesh and abroad. You can also use your Debit Card online for shopping, booking air/rail/movie tickets & utility bill payments.",
"Debit Card?",
"A Debit Card is a card that gives you online access to your Bank Account. The abc Bank International Debit-cum-ATM Card allows you to purchase goods at Merchant Establishments and also gives you the freedom to withdraw cash from ATMs in Bangladesh and abroad. You can also use your Debit Card online for shopping, booking air/rail/movie tickets & utility bill payments.",
"What is the difference between a Debit Card and a Credit Card?",
"A Debit Card is a buy now, pay now option while a Credit Card is a buy now, and pay later option. Therefore with a Debit Card there is no monthly repayment and hence no interest is charged. A Debit Card gives you all the convenience of a Credit Card and helps you regulate your spending.",
"What is the mode of payment for Debit Card?",
"There are no monthly outstanding in the case of Debit Card. Your account will be instantly debited to the extent of purchases made or the amount withdrawn from ATMs on the Debit Card.",
"Where can I use my Debit Card?",
"All Abc Bank ATMs",
"What are the transaction charges for using the Debit Card?",
"There is no charge if the card is used at an abc Bank ATM",
"Debit Card charges ",
"There is no charge if the card is used at an abc Bank ATM",
"How many accounts can I link to my Debit Card?",
"You can link up to 4 accounts to your Debit Card.",
"Do I have to pay any charges for the replacement of my lost/stolen Debit Card?",
"There is a charge of 110 inclusive of S.tax for replacement of a lost/stolen card.",
"Are there any daily limits for use of my card at ATMs?",
"For your security we have daily limits on the use of the card at ATMs and Merchant Locations.",
"What is the validity period of my Debit Card?",
"The Debit Card is valid for a period of 5 years from the date of issue of the card which is marked on the card front.",
"Can I exceed my credit limit?",
"There is no credit limit; you can only make purchases/withdrawal up to the available balance in your account ",
"Can I access uncleared funds?",
"No. Only cleared funds available in your account can be accessed through your Debit Card.",
"Do I need to retain a copy of my charge slip?",
"It is recommended to retain a copy of your charge slip and verify it against your account statement.",
"How do I obtain a Debit Card?",
"Open a Savings/Current Account* with abc Bank today and get an International Debit-cum-ATM Card.",
"How do I activate my card?",
"In order to safeguard your interests the Bank will be sending you an inactive Debit Card and will be sending your PIN separately. Your Card will get activated on its 1st use at any Bank ATM.",
"Can I get an additional card?",
"Additional cards are available to Joint Account holders. However, the operating instructions on the account should allow for financial transactions to be conducted by the Joint Account holders.",
"Can the customer exceed his credit limit?",
"There is no credit limit; the customer can only make purchases/withdrawal up to the available balance in his accoun",
"What is a Gift Card ?",
"A Gift Card is a card which you purchase from abc and then gift it to someone giving him/her the freedom to use that card to purchase gifts of his/her choice. This Card can be used to make purchases at over 9 lac merchant establishments in India that accept Visa Cards. It can also be used more than once, which means the person you are gifting to does not have to utilize the value on the card in one go and can keep making purchases on the card till the specified rupee amount has been spent. This card is available in denominations starting from 500 to 10,000 and is valid for a period of 1 year from the date of production of card, which is marked on the face of the card. The Gift Card is not reloadable.", 
"How do I buy this card?",
"All you need to do is walk into an abc branch, fill out a simple application form, deposit the amount to be loaded onto the card and collect your Gift Card pack instantly.",
"How do I use the GiftCard?",
"Present the card to the merchant, after selecting your  purchases",
"How do I check the Balance remaining on my card ?",
"You can walk into any abc ATM, insert your card, enter your PIN and do a Balance Enquiry to find out the balance remaining on your card. You can also request for a mini statement, which will give you details of the last 10 transactions on your card.",
"How do I report the loss of my card?",
"All you need to do is call up our 24-hour toll free number 1122, quote your Gift Card Reference Number. Your card will be deactivated immediately to prevent misuse.",
"What measures should I take to protect my Card?",
"Your card is only for your use. Please do not hand it over to anybody other than designated officers of the Bank",
"What is Phone Banking?",
"Phone Banking is a telephone banking service that gives information about your accounts on a 24*7 basis from anywhere, at any time.",
"How do you get started?",
"After account is opened, to avail phone Banking services customers can call Phone Banking and generate their 4-digit Telephone Identification Number (TIN) through Phone Banking executives.",
"How do you access your account?",
"Customer Id and your 4-digit TPIN is all that you need to access your account and avail Phone Banking services. ",
"How to use Phone Banking?",
"Dial our Toll Free Phone Banking numbers. After the welcome message, select the relevant menu option of your choice to avail services through Phone Banking Channel.",
"What are the Services available through Phone Banking Channel?",
"What is the daily transaction limit for the service?",
"The daily transaction (consolidated) limitof 25000/- per day will apply for all type of transactions under the browser channel.",
"Do I need to input a Transaction Password?",
"No. As mentioned above,the transaction password has been replaced by a dynamic SMS based OTP.",
"Can I use the existing SMS Banking as well as the Browser version?",
"Yes, existing SMS Banking users can also use the Browser version by submitting the Channel Registration Form.",
"What is an Automated Teller Machine (ATM)?",
"Automated Teller Machine is a computerized machine that provides the customers of banks the facility of accessing their accounts for dispensing cash and to carry out other financial transactions without the need of actually visiting a bank branch.",
"What type of cards can be used at an ATM?",
"The ATM cards/debit cards, credit cards and prepaid cards (that permit cash withdrawal) can be used at ATMs for various transactions.",
"What are the services/facilities available at ATMs?",
"How can one transact at an ATM?",
"For transacting at an ATM, the customer should insert/swipe their card in the ATM and enter their Personal Identification Number (PIN).",
"Can these cards be used at any bank ATM in the country?",
"Yes. The cards issued by banks in Bangladesh should be enabled for use at any bank ATM within Bangladesh.",
"What is a Personal Identification Number (PIN)?",
"What should be done if the card is lost/stolen?",
"The customer should contact the card issuing bank immediately on noticing the loss so as to enable the bank to block such cards.",
"Is there any minimum and maximum cash withdrawal limit per day?",
"Yes, banks set limit for cash withdrawal for their customers. The cash withdrawal limit for use at the ATM of the issuing bank is set by the bank during the issuance of the card.",
"Who will accept my payments using PayMate?",
"You can use this service at any of PayMate's over 13,000 accredited merchants consisting of online portals, leading voice portals and some key retail chains, This list of merchants is growing rapidly",
"What do I need to use PayMate?",
"All you need is a mobile phone and a savings or current account with IDBI Bank. To register for this service and get started, Customers can enroll for this revolutionary service by submitting a Registration format our nearest branch or through Internet Banking / ATM.",
"Is this service mobile phone or operator specific?",
"This service can be accessed through any mobile phone or through any mobile operator. PayMate works on even the most basic phone (GSM or CDMA) and does not require any mobile operator registration.The service is available for both post paid as well as prepaid mobile connections",
"Are my Account details secure?",
"Absolutely secure. Since you register for PayMate with your bank and not any third party vendor, your Bank account and other personal details remain within the Bank. Also as you do not reveal your card number, there is no possibility of it being misused.",
"How will I get my PIN?",
"As soon as you register for this service through submission of the registration form, you will receive a temporary 4 digit PIN via SMS on the registered mobile number. You will be prompted to immediately change the PIN over a secure IVR call before you initiate your first payment. Please note that unless you change your initially allotted 4 digit PIN, no transactions will be processed.",
"Can I change my PIN?",
"Sure. You can change the PIN any number of times as you wish. To change the PIN, SMS CP to 9870900876",
"How secure is the PayMate transaction?",
"You never disclose your account/card details, expiry date, CVV number etc to anyone. Each transaction has to be authorized by your 4-digit PIN which is known only to you. The PIN needs to be sent from your mobile number only thereby ensuring that you are the one authorizing the transaction.",
"How do I make a payment through this service?",
"Once you choose to pay via PayMate at any of the accredited merchants, all you have to share is your mobile number. You will instantly receive an IVR call asking for authorization of the payment by entering your 4 digit PIN. Once you reply to this call, within a few seconds your bank will authenticate the details and debit the amount to your account. You will instantly receive a confirmation of the same via SMS and the merchants system will also get updated with the status.",
"payment through this service?",
"Once you choose to pay via PayMate at any of the accredited merchants, all you have to share is your mobile number. You will instantly receive an IVR call asking for authorization of the payment by entering your 4 digit PIN. Once you reply to this call, within a few seconds your bank will authenticate the details and debit the amount to your account. You will instantly receive a confirmation of the same via SMS and the merchants system will also get updated with the status.",
"How do I use my PIN for authorising transactions?",
"While making the payment, all you need to do is to enter your PIN over a secure IVR call received at the time of payment.",
"Can I link my mobile number to more than one account?",
"No. Currently, a mobile number can be linked to only one savings or current account that you opt for at the time of registration.",
"What if there is a dispute in the product bought or amount charged?",
"In case of dispute on the product, you need to get in touch with the merchant & follow the process as you would in case of a cash or card purchase. In case of dispute in the amount charged, you have to get in touch with the bank and the same guidelines would apply as for any card based transaction.",
"What if my mobile number is changed?",
"You may call your bank and submit a letter intimating the change and modify the old number with the new one so that your account is de-linked from the old mobile number and linked to the new one.",
"What is my daily transaction limit?",
"Daily limits as per RBI guidelines will apply which currently are 10,000/- per day for purchase of goods and services.",
"What do I do if I need any information for any transaction?",
"In case of any additional queries or concerns, you can call our toll free Phone Banking number",
"What is eBill?",
"eBill is a feature that allows you to receive and pay electronic summary versions of paper bills directly through Payments.",
"eBill?",
"eBill is a feature that allows you to receive and pay electronic summary versions of paper bills directly through Payments.",
"How do eBills work?",
"eBills are delivered directly to your online Payments account. Once you arrange for electronic billing with a particular company, an eBill comes directly from that payee to your account. Examples of businesses that offer eBills include cable service providers, phone service providers, utility providers, and credit card companies.",
"eBills work?",
"eBills are delivered directly to your online Payments account. Once you arrange for electronic billing with a particular company, an eBill comes directly from that payee to your account. Examples of businesses that offer eBills include cable service providers, phone service providers, utility providers, and credit card companies.",
"Will I still receive paper statements when I have eBill?",
"Please check with each payee, as billing practices can vary from business to business.",
"How will I know if eBill is available for a payee?",
"If your payee is eligible for eBill, you will see a Setup eBill link next to their listing on your dashboard.",
"What are the primary benefits of eBill?",
"With eBill, everything you need is in one convenient location. Using eBill allows you to streamline your bill paying routine and have online access to your bills. That means you won't have to keep track of paper bills. In addition, you can view past bill summaries at a glance.",
"What information is included in an eBill?",
"Balance due, due date, and minimum payment amount are included in your eBill. If you need additional details, there will be a link that lets you login to your account on your payee's website, or you can check your paper statement.",
"How do I pay an eBill?",
"To pay an eBill, simply choose the account you want to pay from, enter the amount you want to pay, and schedule when you want the payment to be processed.",
"How do I know when I have received an eBill?",
"You can sign up to receive an electronic notice to alert you when an eBill has been delivered to your account. You can receive these notices in the form of emails or text alerts to provide an extra reminder when a payment is due.",
"What happens when my card expires?",
"Abc debit cards are re-issued every three years. All Custom Image Debit Cards re-issued upon the expiration date will be re-issued as a Abc branded debit card. You may order a new Custom Image Debit Card at any time at a cost of 500/-.",
"card expires?",
"Abc debit cards are re-issued every three years. All Custom Image Debit Cards re-issued upon the expiration date will be re-issued as a Abc branded debit card. You may order a new Custom Image Debit Card at any time at a cost of 500/-.",
"expires card?",
"Abc debit cards are re-issued every three years. All Custom Image Debit Cards re-issued upon the expiration date will be re-issued as a Abc branded debit card. You may order a new Custom Image Debit Card at any time at a cost of 500/-.",
"How long will it take to receive my card?",
"Once your image has been reviewed and approved, you can expect to receive your card within 7-10 business days.",
"what photos I can use?",
"Yes. In general, you must own the rights to the photo, and the photo cannot be considered offensive. Please review our Image Guidelines for the complete set of criteria for acceptable photos. Every image submitted is reviewed for compliance with the Image Guidelines, and must also follow the Visa® Issuing Guidelines as set by Visa® International. If your image is rejected, you will be notified by email within two business days.",
"What size and format does the photo need to be?",
"The photo needs to be a digital photo in JPEG, GIF, PNG, TIFF or BMP format. The image needs to be at least 840 x 840 pixels and at least 50KB (kilobytes) in size, not to exceed 10MB (megabytes). Our design service provides a tool to resize your picture to look the way you want. Please review the Upload Guidelines for further detail.",
"What happens if I lose my Custom Image Debit Card?",
"Notify the bank immediately if you have lost your debit card. If you would like your Custom Image Debit Card re-issued due to any reason, such as lost, stolen, name change, or damage to the card, there will be a $5 ATM/POS Replacement Card fee. The replacement fee will be debited from the primary checking account associated with the debit card.",
"Can I start using my card right away?",
"Your card will be ready to use within one hour after leaving the bank and may be used anywhere Visa® Debit cards are accepted.",
"How can I change my PIN?",
"To change your PIN anytime, call 1122 and follow the prompts. Have your card present when calling to change your PIN.",
"change my PIN?",
"To change your PIN anytime, call 1122 and follow the prompts. Have your card present when calling to change your PIN.",
"change PIN?",
"To change your PIN anytime, call 1122 and follow the prompts. Have your card present when calling to change your PIN.",
"PIN?",
"To change your PIN anytime, call 1122 and follow the prompts. Have your card present when calling to change your PIN.",
"Can I use my temporary card to pay bills?",
"Yes, you can use your temporary card to pay bills. If you use your card to pay a bill with a merchant where your card number and expiration date are saved, please ensure that you update the expiration date when you receive and activate your personalized card. Once you activate your personalized card, your temporary card will no longer work.",
"Is my card safe to use without my name on the front?",
"Yes, your card can be used anywhere Visa Debit cards are accepted. If you have issues using your card, call us at 1122",
"When should I expect to receive my personalized card?",
"Your personalized card should arrive in the mail within 7–10 business days. Please activate your personalized card as soon as you receive it and destroy your temporary card. Your temporary card will be active for only 60 days.",
"What should I do if my card is lost or stolen?",
"Report lost or stolen cards immediately by calling the First Bank & Trust lost & stolen card center at 1122",
"How do I access Mobile Banking?",
"iPhone, iPad, and Android users can download an app. Launch the App StoreSM or Google PlayTM on your mobile device, then search for Abc",
"How do I know if my transfer or bill payment was entered successfully?",
"If you have opted to Receive Text Message Alerts in your Mobile Settings on Digital Banking, each time you make a transfer or bill payment, a confirmation text message will be sent to your mobile phone. If you do not receive a confirmation text message, double-check to make sure the transaction went through.",
"What happens if I lose my mobile device?",
"Since your account data is not stored on your mobile device, your information cannot be stolen. When you replace your mobile device, simply edit your Mobile Settings and make any changes to the Wireless Provider and/or Phone Number.",
"What do I need to do if I get a new phone?",
"If you get a new phone but are using the same phone number and provider, no changes on your part are necessary. If you switch providers and/or phone numbers, log in to your Digital Banking account from a computer and update your information on the Options > Mobile Settings page. You will not receive a text message regarding Mobile Banking transactions if your phone number is not correct.",
"How do I search for a transaction?",
"You will be able to view all transaction history in the future, with 120 days' worth of transaction history imported when moving to the new mobile app. You can search transactions by using the magnifying glass in the transactions screen. You can also search by tags by using the gear in the transaction screen.",
"How do I delete a bill payment that I set up through my mobile device?",
"You can delete the payment from the main menu of the payment section by selecting the payment and clicking the trash can in the upper right corner.",
"Who do I contact if I am experiencing issues with Digital Banking?",
"Please call us at 1122 to report the issue you are experiencing.",
"Who is eligible to use Mobile Deposit?",
"Any abc Digital Banking customer is eligible to use Mobile Deposit.",
"Is there a fee to use Mobile Deposit?",
"No! Mobile Deposit is free to use.",
"What kind of device can I use?",
"Any iOS(Opens in a new Window) or Android™(Opens in a new Window) device can be used with Mobile Deposit.",
"How can I start using Mobile Deposit?",
"How do I use Mobile Deposit?",
"Simply log in to our Digital Banking app then choose Deposit. You will be prompted to take a picture of the front and back of the check, type the dollar amount to deposit, and choose the account where you want it deposited.",
"What types of accounts can I deposit into?",
"Deposit into any checking, savings, or money market account tied to your Digital Banking.",
"Is there a limit to the number of checks I can deposit?",
"Yes, 25 checks per day or month, whichever happens first, is the maximum number of checks that can be deposited with Mobile Deposit.",
"Is there a maximum dollar amount for Mobile Deposit?",
"Yes, 50,000/- per day or month, whichever happens first, is the dollar limit for Mobile Deposit.",
"What should I do with the paper check after depositing?",
"Securely store the paper check for 60 days after the date of deposit. After the 60 days, please shred the check.",
"When will I have access to the funds deposited?",
"If the deposit is submitted before 5 p.m., you generally will have access to use those funds the next business day.",
"Should I endorse the check before depositing?",
"Can I un-enroll from Mobile Deposit?",
"Yes! Simply contact your banker or call us at 1122",
"How will I know if there was a problem with my mobile deposit?",
"You will receive an email notification indicating whether the deposit was successful or not.",
"What is Payments?",
"Payments is an online service that allows you to pay almost any individual or company through your Digital Banking account. You determine whom you want to pay, when you want to make the payment, and which checking account you want the payment to come from. It's safe, secure, and easy to use.",
"Who can I pay with Payments?",
"You can pay almost any business or individual with a mailing address within the United States and Puerto Rico. For example, you can pay utilities, cable bills, credit cards, or individuals such as a landlord, babysitter, or relative.",
"How are online payments delivered?",
"Payments are sent either electronically or by paper check, depending on the method accepted by the person or company receiving the payment. The majority of payments are delivered electronically, which is the faster method. Your payment information, such as your account number, is sent via secure transmission. Payments made by paper check are mailed via the Bangladesh Postal Service.",
"Is Payments secure?",
"Paying bills online is one of the safest ways to pay your bills. Using Payments helps prevent identity theft caused by lost or stolen checkbooks, bills, and statements. It also increases your privacy because your account information, account numbers, and payment history can be accessed only within your private Digital Banking account. With real time access to your payment activity, you maintain tighter control of your bank account.",
"How long does it take before my payment is received?",
"Generally, your payment is delivered to and processed by the payee within 2-3 business days if sent electronically, or 7-10 business days if sent via paper check.",
"How are the scheduled payments processed with Payments?",
"Most scheduled payments are sent electronically and funds are withdrawn from your account on the day we send the payment. If a payee does not accept electronic payments, the payment will be sent via paper check.",
"Can I edit a payee address?",
"Yes. To edit payee information, select the payees name. From the payee details screen, select the edit link.",
"How late in the day can I edit or delete a payment?",
"Generally, you may edit or delete a scheduled payment before 2:00 pm Central Time on the day of the payment date by changing the information within Payments or by calling us at 1122 Certain exceptions apply, so please contact us if you are unable to cancel a payment.",
"When will the money be taken out of my account?",
"For an electronic payment, funds are debited from your account the day that you select the payment to send. In order to send an electronic payment on the same day, the payment must be submitted prior to 2:00 pm Central Time.",
"What if I do not have enough money in my account?",
"We will treat Payments check items just like any other check you write. Overdraft fees and return check fees may be applicable. Electronic payments are verified for funds availability. If your account has insufficient funds, the payment will be cancelled.",
"What is the cut-off time for payments?",
"Payments need to be entered by 2:00 pm Central Time in order to be processed that business day. Payments entered after 2:00 pm will be processed the following business day.",
"How far in advance can I enter a payment?",
"A recurring scheduled payment can be set up in advance to any date in the future. A one-time payment can be set up to be sent 5 years in the future.",
"Why did I receive a new credit card?",
"Who can I call if I have questions?",
"You may call 1122 for 24/7 Customer Service.",
"Why did I receive a new credit card?",
"New cards are issued upon expiration date. Your current card may be expiring soon.",
"What is a contactless-enabled chip card?",
"It is a card that allows a cardholder to “tap to pay” or to complete a transaction by holding their card over a contactless-enabled merchant terminal.",
"How will I know if I can perform a contactless payment?",
"Look for the Contactless Symbol at merchant terminals and simply tap your card to pay.",
"Who can I call if I have questions?",
"You may call 1122 for 24/7 Customer Service.",
"Can I pay extra into my home loan each month?",
"You can make additional repayments to your Standard Variable or Back to Basics Variable Home Loan at any time"


"How can I check what my current home loan repayments are?",
"You can see the amount youre required repay each period (weekly, fortnightly or monthly) for your home loan",
"How can I make repayments on my home loan?",
"Arrange an automatic regular repayment with from a nominated account (weekly, fortnightly or monthly) depending on which loan you have chosen"
"How do I find out my current interest rate for an existing loan?",
"If you have an existing Suncorp Bank Home or Personal Loan, your interest rate will appear on your statement. If you have Internet Banking simply click on the account number to display a summary of the loan which will include the current interest rate.",
"How much can I borrow to buy a home?",
"You can use our borrowing capacity calculator to get an estimate. Alternatively, you can complete our online pre-approval application form get a clearer idea of how much you can borrow.",
"How much deposit do I need for a Home Loan?",
"Depending on the purpose and size of your loan, Suncorp may provide finance of up to 95 percent of your property value. This amount includes Lenders Mortgage Insurance (LMI) if applicable, possible bank fees and some government fees.",
"Is mortgage offset available on my home loan?",
"This feature is available on the Standard Variable home loan, using our Everyday Options account when the accoun",
"What is a home loan pre-approval and how do I get it?",
"Pre-approval (sometimes referred to as conditional approval) will give you a good idea of how much you may be able to borrow from the bank. If a lender pre-approves you for a loan, they will do so for a specific amount, so you can house hunt properties you know you can afford.",
"What is Cashback and how do I access it?",
"Our Home Loan Cashback feature lets you redraw funds that you've paid in advance of your normal scheduled home loan repayments"
"What sort of fees or charges will apply to my home loan?",
"Various fees and charges may apply to a abc Bank Home Loan.",
"When do my payments start on a term loan?",

"Your minimum monthly repayments will begin one month from the date of settlement of your home loan. For example, if your home loan settled on the 2nd March, your first month’s repayment would be due on the 2nd April.",
"Who can borrow money for a home loan?",

"If you can meet our lending criteria  and are over 18 years old, you can apply for a Abc Bank home loan.",
"Will the bank require a property valuation to approve a home loan?",
"Yes. In most instances, a valuation will be required. Well advise you at the time of your application if this applies to you.",
"Can my parents act as guarantors for the loan?",
"Deposit KickStart lets owner-occupiers use the equity in the home of a family member towards the purchase of your new owner-occupied home – to help kick start your dream. With Deposit KickStart, you can avoid the need of paying Lenders Mortgage Insurance without the 20% deposit.",
"What is Lenders Mortgage Insurance (LMI)?",
"In the event you are borrowing more than 80 Percent of the value of a property from a Abc Bank, you will have to pay what’s called Lenders Mortgage Insurance (LMI). LMI is a cost that protects the bank in the event you are unable to pay your mortgage.",
"How do I register and manage my deposit account(s) online?",
"Our registration process is quick and easy—with a few simple steps. When you register, you will need to provide the last 4 digits of one of your Abc Bank account numbers and verify the security information provided when you opened your account. If you have multiple bank accounts with us, you will only need to register once as all your bank accounts are automatically linked to your online profile. To register for online banking",
"What are the User ID and Password guidelines?",
"Your User ID must be between 6-16 characters in length and can contain letters, numbers, and most special characters. Your Password must be 8-32 characters in length and must contain at least 1 letter and at least 1 number. Your Password is case sensitive and can contain most special characters.",
"What should I do if I forget my User ID or Password?",

"If you forget your User ID or Password. If you are still unable to log in, call us at 1122",
"I forget my User ID or Password?",
"If you forget your User ID or Password. If you are still unable to log in, call us at 1122",
"What is Passcode?",
"Passcode allows you to create a numerical 4-digit code which makes logging in faster and easier. You may enter only your Passcode instead of your full User ID and Password to access your account.",


])

@app.route('/')
def home():
    if session.get('logged_in') == True:
        user = session.get('name')
        return render_template("bot.html", userName=user)
    else:
        return render_template("login.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/verify')
def verifyLogin():
    name = ''
    email = request.args.get('email')
    password = request.args.get('pass')
    if email == '' or password == '':
        return 'fail'

    with sqlite3.connect('userDB.db') as db:
        cur = db.cursor()
        cur.execute("SELECT * FROM user WHERE email=? AND password=?",
                    (email, password))
        row = cur.fetchone()
        print(row)
        db.commit()
        if row == None:
            return 'fail'
        else:
            name = row[1]
            session['name'] = name
            session['logged_in'] = True
    return 'success'


@app.route('/register')
def register():
    name = request.args.get('name')
    email = request.args.get('email')
    password = request.args.get('pass')
    if name == '' or email == '' or password == '':
        return 'fail'

    with sqlite3.connect('userDB.db') as db:
        cur = db.cursor()
        cur.execute("INSERT INTO user (name,email,password) VALUES (?,?,?)",
                    (name, email, password))
        db.commit()

    session['name'] = name
    session['logged_in'] = True
    return 'success'


@app.route('/logout')
def logout():
    session.pop('name')
    session.pop('logged_in')
    return 'success'


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    resp = str(chatbot.get_response(userText))
    return resp


if __name__ == "__main__":
    app.run()
