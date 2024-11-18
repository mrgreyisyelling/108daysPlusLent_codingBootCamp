https://www.youtube.com/watch?v=OvfGvtNzEOM&list=PLVP9aGDn-X0RgLnaYKPi9d3-K0YRAMY-T


0:12

[Music]

0:26

hello everyone welcome to the second day of the real world asset boot camp by

0:32

Chain clabs my name is Andre and I'm one of the developer relations Engineers here at chain clabs uh if you can hear

0:39

me see me Etc please drop in a chat where are you tuning in from and we are

0:45

going to easily start with today's lecture so this is the second day of the boot camp uh and also the final day so

0:54

like after after this day that's it we'll we'll have some some homework and some followup discussion on Discord but

1:01

but that's pretty much it um the the URL for the gitbook is the same as yesterday

1:08

so cl- d.g. tokenized rw-

1:15

b-224 right here in the chat and I'm going to uh quickly start sharing my

1:22

screen while you're uh while you're uh dropping your GMS in the chat

1:30

so yeah I see people joining us from Lisbon Madrid

1:36

India Naples so hello everyone

1:41

um oh there's Pakistan as well nice Okay cool so you should be able to see the

1:49

exercise number two page uh so this we are going to start

1:55

from from this page today so first we're going to have a quick recap of day one

2:00

and uh after that we're going to start with exercises for day day two so there is little to know Theory today just pure

2:09

coding and Engineering uh GM from Nigeria Cameroon Argentina Norway and

2:16

Toronto Canada hello hello everyone and GM to one and only Harry

2:23

here is you okay cool so we're going to start first by recapping what we have

2:29

done yesterday today and uh you know this is going to be uh these contracts

2:35

we deployed yesterday are going to be our base for today's workshops uh for

2:40

today's exercises sorry so yesterday we deployed uh our um real estate token.

2:49

contract which is essentially smart contract implementing ERC 11155 standard

2:54

and uh in a in a form or like uh fungible tokens representing non fible

3:00

asset and that non-fungible asset is actually that mock real estate uh from

3:05

zillow's API so we essentially tokenized mock real estate like a house uh using

3:12

uh using chaining functions and ERC 11155 standard and we've also deployed the issur smart contract which will use

3:19

just for issurance purposes we we basically minted that one token to Alice

3:25

or to your own wallet addresses so today we are going to continue using that real

3:31

estate token. that tokenized real estate and

3:36

we're going to plug it into two different use cases so first one is going to be real world asset rending

3:43

lending and borrowing our own mock version of landing and borrowing platform minimal version of landing and

3:50

borrowing platform for rail world speically for our own

3:56

ec155 uh real estate uh using Z from Z API and the second one will be an

4:02

English auction the the great part about earc 1155 standard is that you can

4:08

represent as I said non-fungible asset with certain amount of fible assets fible tokens meaning that you can have

4:15

like a fractionalized version of of non-fungible asset in our case that's a fractional version of real estate and if

4:22

I go back here to the previous diagrams we can see once again that we tokenized

4:30

this house using Z API like mock real estate and minted 20 year C 1155 tokens

4:37

20 tokens to Alice address meaning means that she or your wallet address now

4:43

possess 100% of that real estate of that tokenized real estate but if uh as we

4:50

wrote over here if Alice sends transfers or sells five of these 20 tokens to Bob

4:58

now Bob owns uh five out of 20 means like uh 25% of that not tokenized nonf

5:07

funable asset right so that's pretty much it what we've done uh yesterday and

5:14

if you missed yesterday's class you can re-watch it if you go to always stay

5:19

connected page this is the link to your official YouTube channel I'll also hear

5:24

is in a chat so you can subscribe to chain links official YouTube channel and

5:29

and over there you'll find the recording of day one also this video is currently

5:35

played live as a live stream on on YouTube but once we stop recording it

5:40

will be immediately available uh uh to to watch On Demand at

5:45

the same YouTube channel so you can always re-watch it at your own pace uh

5:51

later uh now we're going to start with with exercise number two

5:57

so uh these are the two cont contracts that we are going to create today I'm

6:02

going to start with the second one with the English auction because it's uh

6:07

because it's easier so as I said if Alice transfers her like five out of 20

6:15

those tokens whatever like 10 that mil then then then that means that Bob will

6:21

own 25% or 50% if she transfers 10 tokens of that tokenized rail Bo asset

6:27

of that house however Alice can also sell those 25% or 50% or 75% of or

6:36

whatever uh and she can do it by creating a decentralized auction and for

6:42

this purpose we're going to create a mini version of English auction smart smart contract uh but also there is

6:49

another one called Dutch auction which is quite popular uh on on on blockchain

6:55

as well uh these two are the probably the most popular ones but of course you

7:00

can just Implement auction uh on your own and this auction will be uh will be

7:07

simple Alice will deploy this contract she will send the portion of her

7:12

ec155 tokens like tokenized asset like the fraction of it and uh set the

7:18

minimum bidding amount then uh the the bidding will last for seven days and

7:23

anyone will be able to bid with the native coin uh of that blockchain so I'm

7:30

going to do it on Avalanche Fuji so that'll be that that'll be like anyone will pay can pay can bid sorry in ax

7:37

coins if I'm on ethereum spolia that will be in eth uh if I'm on polygon ammo

7:43

that'll be pole and etc etc so the the in our that means that in our smart

7:48

contract we will we will leverage the message. value keyword and the only constrain will be that the next bid must

7:56

be higher than the previous highest one uh also you can um uh you can um

8:04

withdraw your bids if you're not the highest highest bidder and after seven days uh uh anyone or we can even s like

8:13

training automation uh will close the auction so that's the broad idea we're

8:18

going to Deep dive into it more later but that's what we're going to be build

8:24

but first of all as exercise number one we're going to create this airw Landing smart contract which will leverage

8:30

chaining price fits and this one is much more complex and uh that's intentionally

8:35

because we want to show you the complex and uh the complex use cases that can be

8:41

built using uh chaining uh platform

8:46

right uh I see questions about English and Doc options in in a chat I'll answer

8:51

those later as we start explaining the exercise number three don't worry about that if you you can always uh read about

8:58

them in a in a getbook as well but but be patient so we're going to create uh for X number two rwl ending smart

9:06

contract so essentially we will learn certain lock certain amount of ERC 1155

9:12

tokens in it so again certain fraction of of those tokens like 35% 50% even

9:19

100% if if alet SPS that in order to get a loan in usdc in return so it's

9:25

stainable tokens uh the calculation for price because again we don't have proof of Zer

9:31

feed for mock real estate right we're going to leverage our get price details

9:37

function that we developed yesterday which essentially uh pings CH using

9:42

chaining functions pings Z API uh every single day automated by chin link automation you you remember time based

9:50

upkeep and it will return uh list price original RIS price and tax assessed

9:55

value in US Dollars we will use the following formula this one to calculate

10:03

the valuation of the of the of that real estate of that Alice's mock house and uh

10:11

we can see that W1 W2 and W3 um variables we have in uh in this um uh in

10:20

this formula those stands for weights so weight one weight two weight three uh we will see later but that means that uh

10:28

list price like like a has like a greater weight than tax assessed value

10:33

when we want to when we want to uh calculate devaluation this is just again a simple

10:40

example of what can be build and it's just tied to this mock AWA lending platform valuation will be calculated in

10:48

US dollars because we have list price original list price and tax list value in US Dollars and uh weights are just um

10:56

you know like constants essentially the thing is that we will talk about it but

11:01

we will need to convert US dollars to usdc because one usdc doesn't it does

11:08

not always equal $1 it's quite the opposite it's in the range between 0.99

11:14

something and 1.011 something so you know like uh that

11:21

that's how how the actual price of all of these stable coins are work so we're

11:27

going to uh we're going to use chain link price feeds uh specifically usdc in

11:33

terms of USD to convert US dollars to the actual usdc value and that usdc

11:39

value will be will be transferred back to Alice finally because this is lending

11:46

and borrowing uh Alice can always repay her debt in usdc and get her year c1155

11:52

tokens in return however if the value of real estate drops below the liquidation

11:57

threshold anyone can can liquidate this position and the Alice will lose all of

12:02

her ec155 tokens all the fractional share of an asset she can keep the usdc

12:08

though so the same the same mechanism as in a or maker or any popular defi

12:15

lending and borrowing platform you're already familiar with so that's the high

12:20

overview uh now we are going to start with the the actual development so once

12:27

again I'm going to remind you of yesterday's class yesterday we deployed

12:32

real estate token and issuer smart contract but we're interested now in real estate. token or contract to

12:40

Avalanche Fuji the original plan was to deploy this to ethereum sepolia but uh

12:45

gas fees has been ridiculously high on eolia over the last last week actually

12:52

so we decided to switch D and Fuji if you do not have enough aex coins or link

12:59

on Avalanche Fuji or on ethereum whatever you can deploy these contracts for homework and for these exercises to

13:06

any test net you want any test net you find convenient for usage in terms of fees any test net but you have enough uh

13:14

test net tokens and coins um it doesn't matter the only thing that matter is uh

13:21

that if you go to official docs and click quick links wherever you are there

13:26

is always this button quick links you just need to be sure that CCP data feeds functions and automation are supported

13:33

on this test network uh so you can complete all the steps and that's pretty much uh any any standard test Network

13:42

are there arbitrum sepolia Avalanche Fuji base seoa uh what else optimis sepolia

13:48

polygon ammo ethereum seoa and and others so as I said um multiple times

13:54

yesterday and on Discord feel free to use any test that you find Convenient uh because uh this token has implemented

14:01

ccip functionality in it natively so you can always crossr transfer to different

14:07

to different uh blockchains using chaining CCAP pretty pretty easy so don't worry about that as I said I'm

14:15

going to continue working on Avalanche Fuji because I've already deployed and set up my real estate token over

14:23

there um Okay cool so we have um

14:29

minted yesterday the token ID zero to Alice with bunch of different uh real

14:37

estate uh real estate token real estate details from the number of bedrooms to

14:43

the address of real estate Etc uh then we set up um time based automation to uh

14:51

call the update price details this function uh every single day on each 24

14:57

hours uh specifically it means night UTC uh in order to update price details

15:03

of this real estate and also for a test purposes you can call this function whenever you want from the owner address

15:10

as well uh but if I and you know all of these details can be find uh uh can be

15:18

find here so this is uh this is the the time based automation we set yesterday

15:26

and we can see that the latest run was at midnight UTC October 1st which is

15:32

which was um today right and yeah we can see that

15:37

uh little over 0.2 links yeah little over 0.2 0.02 links or actually sorry

15:45

spent for this uh for this run so we have plenty plenty of link to spare if I

15:52

now call get price details which is a view function right uh I should be able to see instead of 0000

15:59

um list price original list price and tax assess value of this token and we

16:05

can see uh these values I'm just going to copy them here because

16:12

it's a bit easier to follow so this is again list price in US Dollars this is

16:23

original list price in US Dollars and this is tax

16:30

assessed value again in US dollars so we can see it's uh that these values range

16:39

from 760,000 something dollars to even 700

16:46

7,000 to uh dollar to 700 almost 7003 uh

16:52

7003 uh $730,000 sorry

16:59

so this mean that initially when uh when the owner when Alice posted this mock

17:05

real estate for sale they put this price uh but since they haven't sold it yet

17:12

the current they updated price multiple times and the current one is this one $10,000 almost $10,000 easier so uh this

17:21

is constant but we're not going to change this is Le price that owner can change and tax assess value is actually

17:28

an external constant so owner cannot change that this is literally a as as

17:33

the variable said tax assessed value for this mock real estate and we're going to

17:39

use these two three values our smart contract will essentially going to call

17:45

the get price details function to put them inside this formula so once again

17:50

this is a formula for valuation where W stands for weight and we will have three

17:56

different weights uh that means that one of the like list price uh has like more

18:02

impact to the final valuation than Tax test value if the weight one is uh 0.5

18:09

or 50 like and uh 50% and the tax value is for example 20% or

18:15

0.2 um so this is all all just pure math and uh again this is mock version or

18:23

mock implementation of this landing and borrowing platform is extrem simply you don't need to implement it like this this is just an example

18:29

and also in a real world scenario you'll probably use proof of Reserve feed for

18:34

that asset instead of a pinging uh functions uh request pinging functions

18:40

sending functions request using chain automation every single day uh but we needed to do that in order to make this

18:47

mock version work and also it was a nice uh nice way to Showcase you what's

18:52

what's possible with chaining platform okay let's now create a new

18:58

folder called use cases in a root and a new file called aw lending. so again uh

19:08

read the gbo carefully listen to me carefully create a new folder called use

19:13

cases or however you want to call it doesn't matter and inside that folder in a root create rwl landing. smart

19:21

contract this is important because we are importing real estate token like this so if you don't want to have again

19:28

issues with compilation uh you should uh just carefully follow the instructions right

19:34

if you have issues like again this is uh medium to advanc boot cam so you should

19:40

probably be able to solve it this is solidity 101 essentially so nothing

19:46

nothing hard there again my compiler is uh uh set to

19:53

0.824 version of solidity compiler uh Optimizer is enabled turn to 200 runs

19:59

and for evm version I've set Paris because of

20:05

the uh because of the Cross chain stuff and compatibility between different different evm versions of different test

20:13

networks so okay I'm going to collapse all this stuff uh and I'm going to create new

20:21

folder called use cases and inside that folder airwa

20:27

Landing dosl I'm going to paste this code and

20:36

I'm going to quickly walk you through it function by function

20:43

actually so let's see what what first we're going to cover uh receiver Okay

20:53

cool so first of all you will see that this smart contract Imports IC

20:59

1155 receiver interface and this is important

21:05

because um ERC uh ERC 1155

21:12

token uh can be sent to externally owned accounts uh n natively but the same as

21:19

for erc721 like for nfts the same goes with your ERC 1155 if you want to send

21:25

your nft or ERC 11155 token to a Smart contract smart contract must implement

21:33

this interface must inherit this interface as specifically implement the

21:38

onc 1155 received which is this function

21:43

right so same as nfts right if you uh if

21:49

you uh want to send nft to a Smart contract you need to implement on erc1

21:54

erc721 received here for ERC 1155 we Implement on ear SE 1155 received all of

22:02

these details you can find in the in the official EAP that's part of the standard

22:08

it's pretty standard stuff and that's how we roll so for that's why our smart

22:13

contract needs to implement that you'll probably see not just for

22:20

forc 1155 but also for for nfts that in a lot of implementation

22:27

that on here 721 or 1155 received function is empty uh you will see just

22:35

something like this so just returning selector and nothing nothing more than that this is

22:42

wrong uh the you for production ready apps you need to implement at least two

22:49

uh two security uh two yeah let's say best practices or security measurements

22:54

the first one you want to always validate that message. sender is the address of real estate token. smart

23:02

contract so that's the first one and you want to all you want to receive only

23:09

tokens from that address to avoid any any potential issues you you obviously

23:17

need to return the selector but you also want to check this thing and also you

23:23

want to put non-reentrant modifier on top of this function because the these

23:28

tokens have uh have hooks usually in their implementation post transaction

23:34

hooks sometimes pre pre-transaction Hooks and hooks are dangerous because

23:39

can be used for performing various different types of re-entrancy attacks

23:45

so this is why we have this onc 1155 received function similarly there is

23:51

also on earc 1155 batch received function just following the earc 1155

23:58

standard and of course there is this supports interface view function uh

24:04

following the ERC 65 uh standard which is one of the

24:11

old standards pretty uh pretty common uh uh if you are not sure what this thing

24:19

does you can always just uh refer to the original EAP it's extremely

24:24

straightforward so that'll be it for this this part uh if you have any questions about about this smart

24:32

contract about its implementation or any details feel free to drop them in a chat I'll try to explain them in more

24:39

detail uh but yeah like the purpose of this exercise is to understand this more

24:44

advanced practices and uh design decisions for this smart contract because the exercise itself will going

24:50

to be extremely straightforward we just going to deploy this more contract which is you know nothing nothing hard

24:59

okay uh that's that for ERC 1155

25:06

receiver uh the second one is uh initial and liquidation

25:12

thresholds and for Simplicity reasons and in this mock example we hardcoded

25:18

this values in production we will see that there will be like

25:24

um multi special roles that can uh

25:30

update uh these values um depends on

25:36

governance voting or market conditions or whatever but we for simplistic reasons hardcoded them to 60 or

25:45

75% what that means and let's see uh let's see uh the the actual

25:55

code so we have two Ables uh LTV initial

26:01

threshold and LTV liquidation threshold just hardcoded as a mutable variable

26:06

immutable variables to 60 and 75 that means

26:11

that if L is fractional real estate worth for Simplicity reason reasons

26:19

$100 she will get uh maximum of six and let's say that one usdc equals $1 us

26:27

just for this exercise that means that she will get 60 usdc in return so she

26:34

borrows real estate worth of $100 100 bucks and she gets 60 usdc in return as

26:41

a loan once she repay those 60 usdc uh she will get her real estate back she

26:48

can do with that 60 60 USC whatever she wants but that's how how the defy loans

26:54

work however if price of her real estate drops below $75 like 75% of $100 of the

27:04

original price anyone will be able to liquidate its position and she will Lo

27:09

lose all of hers IRC 1155 tokens she can keep usdc though so that's the

27:15

liquidation event uh if you have any question about questions about initial

27:20

and liquidation thresholds feel free to throp them in the chat if you're familiar with how Maker Works for

27:26

example or a or I think even compound uh has those uh those values you you should

27:34

be able to understand this uh pretty easily and obviously for simplistic

27:40

reasons so we can have like a contract which is little over 200 lines uh long we we

27:47

just hardcoded this to 60 or on

27:52

75% uh we will here see the usage of these two variables

27:58

in both borrow and uh and liquidate uh

28:05

function so borrow you can for initial threshold because if she borrows

28:13

um for Real Estate of $100 she need to get 16 returns so that's why here and in

28:22

uh and in um and for liquidation threshold that's in liquidate fun

28:28

function obviously uh once we calculate it it's going to be yeah like this okay

28:37

cool the the third part um the third part is okay the

28:43

borrow function let's first analyze the borrow uh the borrow function

28:51

implementation uh

29:00

so we can see here that first of all there is a check if there is an active

29:05

loan for that toen ID and if there is uh if you already borrowed some usdc for

29:12

that token ID you cannot borrow any anymore again

29:17

this is for Simplicity reasons uh and um you know like uh

29:22

because it's much easier for you to understand some Concepts then we calculate the normal valuation and we

29:29

will go into that uh we'll deep dive into that soon but essentially uh we

29:35

will calculate the actual valuation using that math formula and then we will ping chaining price fits to convert uh

29:43

US dollars to usdc and finally we will uh we will get the normalized valuation

29:48

uh uh amount back in return so bear with me with

29:53

that but this line is going to be extremely important later so line 83 if

29:59

you want if if you want to memorize that if normal evolation is zero we're going

30:04

to revert and then we're going to calculate the loan amount so as I said

30:09

if um the value of an asset worths 100 bucks but you you can get 60% of that

30:17

well I mean $60 in return over here we're essentially calculating this loan

30:23

amount which should be like 60 60 and first we have uh here the slippage

30:32

tolerance access like the first slippage parameter so for slippage

30:38

production we uh we need to provide minimum loan amount and Max liquidation

30:43

thresholds values to protect against slippage so slippage is uh

30:50

unlikely here in this scenario but uh in general in defi space it it's it's

30:58

pretty pretty common thing so essentially you will create your let's

31:03

say you are using some decks like unisoft and you want to to swap token a

31:09

for token B and you create your transaction and it's in the M poool the

31:14

MV Searchers will try to extract value from it uh either by front running you

31:20

or creating a sandwich attack right and because of that you want to put a

31:25

slippage protection in place essentially this means that okay I'm calling the borrow function I'm loaning um this

31:34

amount of here 1155 tokens let's say 25% that I wanted to send to to Bob but I

31:41

want to calculate up front like completely offchain um the amount of usdc I expect

31:48

so let's say that again my fractionalized asset wors 100 bucks I

31:54

expect uh I expect a maximum of 60 60 usdc in return if $1 equals one usdc

32:02

but that's not the case always but in this hypothetical example but also what

32:08

if someone can manipulate um the price of my real estate or the price of usdc

32:15

highly unlikely in this scenario but with with erc20 tokens and with dexes

32:21

it's more likely and actually it's pretty common so that means that okay I might get up to $60 or 59 or 58 or

32:31

whatever but what's the minimum amount of usdc I'm willing to get in return for

32:38

this borrow and you can put as minimum loan amount 50 for example you

32:44

comfortable with or 55 with that uh with that range so if anyone TR tries to

32:52

sandwich attack you you have uh a slippage protection in place the same

32:57

thing goes for um for liquidation thresholds so for liquidation threshold

33:03

you want to put the maximum amount of liquidation threshold which again here

33:08

will be 75% but the ma actual maximum amount because it's it's going to

33:14

calculate the price of your real estate dynamically right and if liquidation

33:19

threshold amount uh is liquidation uh threshold yeah amount uh is to High uh

33:28

that means that let's say that it's uh somehow someone manipulate your price

33:34

and liquidation threshold amount is now set

33:40

to um 90% it's calculated to $90 sorry $90 so that means that if the price of

33:47

your real estate drops below $90 you'll get liquidated instead of uh 755 or less

33:54

which you expected so that's why you want to also put m threshold value in

33:59

place to Pro protect against slippage pretty standard stuff and protection is extremely similar simple so it will

34:06

calculate the loan amount if loan amount is less than minimum loan amount the

34:12

transaction will reverse so nothing will happen the same goes for slippage protection for liquidation threshold if

34:19

the calculated liquidation threshold is greater than Max liquidation threshold

34:25

again the transaction will revert and this this is uh slipage protection

34:31

essentially do we have yeah we don't have it anymore okay cool so that's

34:37

that's for slippage production uh and yeah the rest of the

34:42

the rest of the function implementation is extremely straightforward so you're transferring from Alice address to this

34:50

smart contract the amount like let's say five like 25% like five tokens for that

34:56

token ID for token I D zero to this smart contract um populating the details

35:02

of this struct so we can grab the details later specifically we are interested in uh the amount supplied

35:10

loan amount and liquidation threshold uh and and uh as a last step we're going to

35:19

from this smart contract transfer uh the loan amount in usdc to Alis or to

35:25

message. Sender so for this uh for this mini version of lending and borrowing

35:31

protocol to work we will need to fund it with some amount of usdc tokens on that

35:37

test net so we can perform actual swaps because if you don't have enough this will this part will also revert and

35:44

we're emitting some events okay uh let's now see the

35:51

calculation for normalized valuation I said that line 83 is one of the most

35:57

important ones so you want to focus on that one but let's see what this get

36:03

valuation in usdc function does let's see if I can go to here oh I can

36:12

nice so as I said and this is extremely extremely important part $1 is not

36:20

always equals to one usc1 US the T1 die or whatever if you ever see a smart

36:26

contract that hard coded this values to one or a UI that hardcoded this values

36:31

to one or does not have a protection against dpex and whatnot run away so you

36:37

you want uh to make sure that you calculate usdc or any amount actually of

36:45

uh stable tokens accurately using uh chain link price fits so in general qu

36:52

case as written here $1 is not equal to us one usdc the value can actually

36:57

between 0.999 something and 1.011

37:03

something uh so as I said extreme dangerous to hardcode these values to one

37:08

usdc and if you care about those last decimal places uh there is some kind of

37:15

arbitral opportunity maybe but not a lot but that's how it works in general case so what we need to do is to actually

37:24

Implement because again I said three times I think already the price details we are reading from the real estate

37:30

token are mock tokenized 1155 are in US Dollars actual cash US

37:37

dollars from the Z API we need to convert that value to usdc using

37:43

training price fed there is luckily usdc in USD training price fedit and if you

37:49

go to data. train. link and go to data feeds over there and

37:56

select um these are all Mains but there there like there's also like feeds for

38:02

testas but this is just uh for for you to view the the the

38:08

details of that usdc over of that feed you'll all here find usdc in terms of

38:15

USD feed and now it's actually exactly $1 which I didn't hope to but it was

38:25

0.9999 something uh yesterday but for example if I go

38:32

back to come on to usdt for example you will see it's

38:38

0.999 something so you see like stable coins vary in between this range and

38:45

here we can actually see uh the differences so you see

38:51

0.99999 [Music] 0.9976 exactly $1 uh um

38:59

999909 uh 99987 whatever uh then there

39:04

was uh where is z one point something I think over here yeah

39:09

1.1 that's what I'm talking about so uh it's it's in this tiny range so

39:17

you cannot you must not assume that it's always going to be $1 sometimes it will

39:22

be like it's currently but we must not assume

39:30

that um cool uh more on this later let's

39:37

actually take a look at the implementation of this function so this is the valuation in usdc right so here

39:47

first of all we have a call to get price details function of view function of that real estate token and if I go back

39:55

here and find that function here so you can see it's

40:01

blue one like a view one it will call this view function and these values will

40:06

be returned right we already saw them list price original race price text test

40:11

value all in US dollars so there will be part of this struct you can see price details. list

40:19

price price details do original list price Etc then here is the implementation of

40:25

the valuation formula

40:31

this one so this is the formula let's see weight times list price weight

40:37

original list price Etc this is the implementation these three weights you

40:42

can see are immutable values and also for Simplicity reasons we hardcoded them in Constructor to 50 30 and 20 so that's

40:51

50% 30% 20% so list price the current

40:56

list price has the most weight in this formula

41:03

okay here we we calculate valuation then there is a call to get USD price in USD

41:11

which is the function that will this one that will integrate uh that will call

41:18

the uh the chain link price F more on that in a minute so this will call chain link

41:25

price fed and returns of usdc price in USD so it will currently return uh one

41:33

but it can be 999 09 0 or one 1 0 1 Etc

41:41

okay so it will return something right in this range so this is this

41:48

variable then we need to uh normalize this valuation okay so

41:56

why is that so that's the second part uh let's analyze the important part of the code code working with training data fits

42:05

decimals so if we go to this data feed we can see

42:13

a lot of stuff over here the latest price the network uh trigger parameters

42:18

we're going to talk about it in a minute last update contract address um oracles that

42:25

reported price prices they reported and when and a lot

42:32

of stuff but if you go to the contract itself so we're going to open the contract itself here this is the

42:38

aggregator contract and if you go to read contract this is the proxy sorry and if

42:45

you click to decimals uh you will see that the number

42:51

of decimals for this feed is eight right

42:57

if I go to some other feed like BTC in terms of USD for example no let's see

43:03

BTC eth BTC th and again this is the remain so I'm

43:11

go to read

43:16

contract and call the decimals functions we function will see that the number of

43:22

decimals is 18

43:28

so these two values 8 and 18 are the most common decimals values in uh of

43:35

chaining price fits but they can be different values so why is that

43:41

important uh let's go to the actual uh to the actual

43:48

feed uh where is the latest

43:53

answer uh okay I'm going to take this value

43:59

I'm going to so this is returned from usdc price and USD this is returned from

44:04

the price F so it can be this value or let's go to uh

44:13

Teter just to grab the the act the different one uh okay let's let's lose

44:19

this one so if I go here this is also the same

44:24

feed read contract latest

44:30

answer okay can be like this perfect going to collapse all this

44:36

stuff and let's put it over here so this is usdc price in

44:43

USD can be something like this in certain in T1

44:50

it's this value and T2 it's this value Etc

44:57

so and we saw that decimals like feed decimals so this thing will return eight

45:04

feed decimals is eight for this particular feed can be also 18 or

45:10

whatever or whatever that means that if we get this value this is how we read

45:16

it on this this value we uh we shift for eight decimal places to get the final

45:23

result so that this means that

45:29

one because the feed is feed is usdc in terms of USD in

45:37

dollars that means that one usdc

45:44

equals 1 2 3 4 5 6 7

45:49

8 or like this so exactly $1 because of eight decimal places on the right so we

45:56

shift for eight decimal places uh in moment T number two one

46:04

usdc equal 1 2 3 4 5 6 7 8 so here decimal

46:16

places we're going to put one front zero and that means 0.9998

46:21

[Music] 9332 so this is why the feed decimals

46:26

are are important okay we also

46:31

saw uh that other feed which was let's say we have feed

46:41

uh BTC in terms of eth ether okay okay doesn't matter uh

46:50

ether and we know I hope we know from solidity that this syntax one ether

46:59

like mean uh has 18 zeros so one one 2 3

47:05

4 five 6 7 oh sorry six so that's 18 six

47:13

* 3 1 two 3 yeah six so this is the denominator so if I go

47:20

again to let's find uh let's find BTC in

47:26

terms of uh eth this one and let's query it really

47:37

quickly decimals is 18 again and uh latest answer is this one

47:44

okay and go back to remix and in T1 the price was one BTC equal this

47:54

amount of ether right

47:59

okay and let's say that we created another smart contract that allows us to

48:04

main nft or sell whatever for one Bitcoin like one Bitcoin but in it

48:11

accepts only ether for like ataps only message. value so how much message.

48:17

value you should send we're going to query chaining price feeds and the answer is going to be 1 2

48:25

3 4 5 6 7 8 9 10 11 12 13 14 15 16

48:32

17 so we can see that one Bitcoin equals almost 250 e at the moment if I'm not uh

48:41

mistaken with this thing uh but because both feed so feed has 18

48:51

decimals and ether has 18 decimals because both has the same number of

48:57

decimals our message do value will be

49:03

just this because we're just going to grab the value from the feed and

49:08

transfer whatever but here in our example for

49:13

usdc the fee decimals is eight but the USD token itself has six decimals so

49:21

usdc token has six deal okay

49:28

okay I saw in a comment it's 24 not 200 okay my bad it just one I missed the

49:33

like yeah okay that sounds more reasonable so one BTC is 24 something doesn't

49:41

matter but usdc has six decimals and if you go

49:46

to where we can find that let's go to uh support this is functions let's go

49:54

to let's go to ccip to grab the token of

49:59

address of a usdc token so it's right over here usdc I'm

50:05

going to open it even though I hardcoded it manually in my code if I

50:13

go uh prox should [Music]

50:19

be where is B where's decimals

50:27

oh here it is decimals it will return number

50:33

sixh Okay cool so that means that if I want to send to

50:39

transfer one usdc I essentially need to do uh usdc

50:45

token dot transfer from um Alice Bob and

50:53

one 1 2 3 4 5 6 one one and six zeros and this will essentially transfer one

51:00

usdc because of decimal places that means that if I

51:05

use this value returned that from the fee which

51:12

is 1 2 3 4 5 6 7 eight zeros so this is

51:17

that should be like one uh usdc equals $1 but if I use this plain value as I

51:24

did for Bitcoin in terms of USD I will not transfer one usdc I will

51:30

rather transfer 100 usdc back to Alis which is wrong right I'll I'll

51:35

mistakenly calculate more usdc than I should so to solve this problem I need

51:43

to normalize valuation in terms of decimals and we can see here uh why uh

51:49

we put this section in a gbook is as important because this is how you work

51:55

with decimal uh when you price feeds and um different types

52:05

of fc20 tokens because sometimes decimals won't

52:10

match that was intense but I hope you understand that actually it's pretty straightforward but here I'm going to

52:17

just collapse this here we're just adjusting the

52:23

valuation to use from eight decimals to use six decimals so the calculated

52:29

valuation in US dollars times the price of US dollars of the price from

52:38

usdc in terms of US dollar feed and we are multiply this by the number of us

52:43

decimals and then dividing with the number of feed decimals times 6 divided by

52:48

8 uh and we always first do multiplication then Division and solidity uh because of the loss of uh

52:56

prec U vulnerability that can happen but probably W if you just do

53:03

multiplication then Division and finally finally we are receiving the normalized

53:09

valuation value okay and let's actually try to oh

53:15

not yet we haven't deployed this contract yet okay we all going to see the actual normalized valuation value

53:21

later okay uh

53:28

okay cool let's now let's Now understand the final part and this is price update

53:41

frequency mayet filter usdc in terms of USD so there are

53:49

two trigger parameters uh okay let's start with this so chain link data feds is a new

53:55

implementation of push-based Oracle model so push based Oracle model means you have uh nod uh nodes node operators

54:04

in a dawn like decentralized oral Network this one over here so this is

54:10

the legend like all of these node operators they will constantly calculate

54:16

the price of uh this uh feed like usdc in terms of USD and using peer-to-peer

54:23

Network they will communicate between each other like gossiping like okay this is my price

54:30

what's your price whatever and they will share their prices and we can see here this one responded with 0.999 something

54:39

then 06 then 0 0.999 871 then this one is one Zer then this is 101 and

54:48

Etc um if then they will reach a consensus

54:54

on the on the final price and if that price

55:00

is and then it will compare that price with the latest reported price on the

55:06

smart contract because when we quering the price fits we're just reading

55:12

calling the view function on the proxy contract that will query the arator contract and essentially if you call the

55:18

latest answer you will see the latest price so the new calculated price will be compared against this one so that's

55:26

happen that's happening constantly and deviation threshold for

55:31

this feed is 0.1% that means that if the new price is

55:36

below or above this $1 currently reported on chain we will uh will like

55:43

the node the transmitter node uh from this Dawn will push the new update to on

55:50

train and if price if that happens every single block it will push it

55:57

nevertheless but it's not practical to to push new prices new calculated prices on every single block because it's

56:04

extremely costly to do something like that on on blockchain and you basically

56:10

um are um creating a lot of traffic which

56:15

increases the gas prices for anyone uh which is probably one of the reasons why

56:20

we have so many issues with ethereum seoa right now and for most Ed cases

56:25

because of the because differences are in final decimals and final two decimals

56:30

like pretty small uh small uh details most of the use cases won't care about

56:38

that so that's why there is a threshold parameter over here threshold parameter is not the same for every feed so you

56:44

must not assume that this is the same for any feed quite the opposite is different and can can be

56:50

different the second parameter is hardbeat and we can see the hardbeat here

56:56

you see how it comes down so if the price does not go below or above the

57:02

price deviation threshold there was no new updates the the once the heartbeat

57:09

passes and we can see three more hours until the new new push the the the

57:15

transmitter node for Theon will still uh push the new the new price update on

57:20

train nevertheless even though the price is exactly the same as the last rep reported one we see that the hardbeat

57:28

for this feed is set to 24 hours because this is stable token it and the price

57:34

the the price does not change that frequently however if you go to some other feed you might find uh different

57:42

value so we can see that the last update here was three hours ago uh for some more risk uh more risk

57:50

feed you'll find different Etc and the same goes for for example proof of RIS

57:56

Zer feeds like I know we're now mocking this part for our real estate but in

58:01

theory like in in the actual use case for example I don't know you're going to use cash goet proof Reserve feed for

58:07

whatever reason and it can have a different deviation threshold and

58:13

hardbeat threshold sometimes going to be one hour or whatever so you need to be

58:18

aware of those um okay cool let's see how that translates to our smart contract so I'm

58:25

going to delete this

58:31

thing and here we we see that we have uh view that we have a call to external

58:37

call to our smart contract that will return these two prices and here it's a call to internal function which is get

58:44

usdc price in USD here's the implementation of that

58:50

function if okay first of all uh let's go to docs the chain that link

58:57

I know that a lot of you will say data feeds are easy and they are easy and

59:02

then yet however when we have a hackathon I see multiple times

59:07

implementation like this so you hardcode the address of aggregator interface this

59:14

is BTC in terms of USD onoa and you just call the latest round data cool that's

59:19

cool get the answer return the answer and that's it so first of all you will need to deal

59:26

with decimals as I show it to you this is Bitcoin so you know like this feed in

59:32

terms of USD if you're dealing with red Bitcoin you need to go to grab Bitcoin uh to see number of decimals usdc on the

59:39

other part if you're dealing with stable tokens deal with that so you need to normalize decimals in first place

59:46

okay second second let's do uh like this so

59:53

first of all this is how you can normalize based on decimal places and

59:59

all the aggregators have this decimals function so we can always sare it like this you don't need to hardcode it or

1:00:06

whatever you do need to have a um a function that can update this data fit

1:00:13

but I'll going to talk about that in a minute so first of all uh besides the

1:00:19

actual price you want to check for round ID so

1:00:24

round idid will never be zero that's the invol in roundout ID if round ID is zero

1:00:29

that means that you're maybe triggering the wrong data feed you mistakenly put a different address or you put address of

1:00:38

feed that it's on ethereum but you're doing this with an avalanche and because you switch uh between codes you forgot

1:00:44

to change that or whatever or you're quaring the feed that is no longer work like it's depricated you don't have a

1:00:52

mechanism to update to a new feed or whatever so if for any reason R ID is

1:00:58

zero you must revert right even though the price is not zero price can be

1:01:04

whatever second second thing is the stainless

1:01:10

threshold so as we said already uh where is that there are these

1:01:19

okay this is us never mind there is this hard bit intervals right and

1:01:26

when you uh call the price fit you will see this update at at in uh time stamp so

1:01:34

this will be last update was 6 hours ago so that will be like a block Tim stamp of that period of time like six hours

1:01:42

ago now for your use case like let's imagine that something's wrong with this

1:01:47

feed or it's outdated or whatever and the last update was three days ago this

1:01:53

is extremely stale data this is the all price and we don't want to deal with all prices right and because of that you

1:02:00

want to put the hard bit or the stale threshold it can be the same as hard bit

1:02:06

here or you can be more strict and use your own whatever but over here if I

1:02:12

look for this variable we can see that we're paste uh we're storing that in a

1:02:19

storage variable over here and there is a function to update both aggregator

1:02:24

address and harbit if we want so if update ad is less than BL current block

1:02:31

time step minus whatever you put for stainless threshold this will also revert like you're you don't want to

1:02:37

deal with all the data uh and finally what I haven't

1:02:45

mentioned here yeah you always need to use latest

1:02:50

round data instead of latest answer because if you okay if you called latest

1:02:55

answer you just get the latest R answer but with L latest round data you also

1:03:01

get the round ID update add Etc so you can start a ad and update a ad so you

1:03:07

can so you can check that this is not zero so you can check that this is not stale Etc because okay this is the last

1:03:15

price but can be pushed like three days ago on chain and yeah you're just

1:03:21

comparing that okay set that and finally uh you might want to use strike catch

1:03:27

block here because again this function call can fail you call the address that

1:03:34

is not uh does not have latest round data implemented or whatever like this

1:03:41

can revert it's like feed is deos or what it's highly unlikely but there's a

1:03:46

possibility so you you might want to

1:03:53

uh might want to try uh to to to wrap

1:03:58

this call in inside the try catch block not necessary all the times I put this

1:04:05

code here just to show you how you can do it but this is like a last last thing

1:04:10

that you need to worry about also we're currently on Fuji but if you are dealing

1:04:19

with um any L2 with centralized sequencer like arbitrum optimism

1:04:24

whatever there is also another feed called uh sequencer uptime feed so you

1:04:30

also want to query that sequencer is up and running uh so you can proceed with

1:04:36

your computation um and yeah that's that's pretty much it I I'm not thinking

1:04:42

now because I spend like a lot of time here I might write a article or blog

1:04:48

post for smart cont design patterns I'm not sure yet but yeah if you want to subscribe I might if you if you think

1:04:54

that'll be like a good blog post to have everything in one place let me know and I might write it so uh that's like a

1:05:03

another thing but yeah that's pretty much it for for this function and for

1:05:09

this one for that matter okay what else we have here in gbook nothing more okay so we cover this

1:05:17

function cover this function cover this this this okay and borrow the functions

1:05:25

that left to be covered are repay and liquidate so repay is when Alice want to

1:05:31

repay her debt she has 60 usdc uh or 60 more maybe she earned some

1:05:39

more usdc somewhere but she wants to repay her debt and wants to get the ERC

1:05:44

1155 token stre Loan in return so it's extremely extremely simple function so

1:05:51

she will just provide a token ID of that tokenized house she fraction of du house

1:05:57

loaned uh we will get the details from a mapping basically return distrct if

1:06:03

amount loan is zero there is nothing to repace so we will revert we will uh follow the check effects interaction

1:06:10

pattern over here so we're having nonre modifier over here we're deleting uh the

1:06:16

the entry from the mapping so first making so checks here then uh you know

1:06:24

like interactions or effects here uh so internal uh internal logic inside smart

1:06:30

contract and finally we are making two external calls and emitting an event so we will just save transfer from Alice

1:06:38

account the usdc amount loan automatically like so she needs to approve at least this amount to be spent

1:06:45

by our smart contract otherwise it'll be return so we're we're not calculating this we're just getting that from

1:06:52

Storage from yeah from Storage from this truct because this is uh already calculated and we not don't

1:06:58

want to recalculate again because we want to be consistent and in return we're just uh transferring thec 1155

1:07:07

amount supplied again and this is how borrow is repaid if however price of

1:07:14

real estate drops below the liquidation threshold we can see that this is external function which means anyone can

1:07:21

call it anyone can call the liquidate function and it will uh recalculate

1:07:26

normalized valuation again to see the current valuation in usdc then it will calculate the amount

1:07:34

supplied divided by total Supply so because if Alice was

1:07:41

submitted five tokens but there are like 20 in existence so this is like 25% plus

1:07:46

the price and if that value is uh below the liquidation threshold as we here

1:07:53

over here uh this is extremely simple thing just for Simplicity we will just

1:07:58

delete that loan so it doesn't exist anymore uh but and you know in reality

1:08:05

you want to split uh liquidation uh profit between the Liquidator and the smart contract itself

1:08:13

that's how a and other other Protocols are doing it this is just for Simplicity

1:08:18

do not do it like this in production because for example we don't even have like a function to withdraw this here

1:08:25

1155 tokens from the smart contract for example which is extremely bad design but it's extremely simplified uh for the

1:08:33

purpose of this boot camp and that's it any questions about any part of this

1:08:39

code base I'll going to wait for a minute or

1:08:47

two okay see couple of comments that they would like a Blog about that so okay I'm going to write it

1:08:55

I'm going to write it and let's see if you where is my

1:09:02

Twitter uh it's over here it's over here and

1:09:11

it's it's over link is over there so if you subscribed to this

1:09:18

newsletter uh you will receive at some point to your inbox the article about uh

1:09:25

ver with data feds at some point I don't know when because I have a lot of a lot

1:09:30

of stuff to to do and to to finish and to wrap up for this year but at some

1:09:36

point in the next month or two or even less I'll probably write everything I

1:09:42

explained to you in a blog post so yeah just just subscribe to to that URL to

1:09:49

this URL and yeah I'll drop it at some point

1:09:56

um let me drop it in a uh in a chat as well yeah here it is

1:10:03

this is the the URL for the blog okay blog aside do you have any questions

1:10:08

about awl lending smart contract it's a lot I know uh even though it's like 200

1:10:15

lines only but there is like some kind of uh some kind of best practices and

1:10:20

Primitives that I want to spend some time on uh because again uh this is med

1:10:25

to Advanced bootcamp so I want to I wanted to show you some of this

1:10:30

stuff which are more more production ready than what you can find in beginner boot

1:10:39

camps if there are no uh questions I will proceed with deploying this smart

1:10:44

contract and then I will have a question for you okay cool so let's deploy this

1:10:51

contract to Avalanche Fuji so I need to provide the address of real estate token I need to provide the address of USBC

1:10:57

token the address of a fee and I um uh

1:11:02

and I uh will provide this

1:11:08

harit um can you do a quick recap without those deep details I already did

1:11:14

it multiple times so this is a contract that will allow

1:11:19

you to uh send some amount of your tokenized real estate asset and get us

1:11:25

tokens in return once you uh want want to repay your depbt

1:11:32

you'll Supply the same amount you loaned in usdc and the your 1155 tokens will be

1:11:39

sent back to you in return however if the price of your real estate drops below the certain liquidation threshold

1:11:45

anyone will be able to call the liquidate function and you will lose you will lose all of your 11 55 tokens you

1:11:52

can keep usdc okay cool let's proceed with the deployment so I'm going to compile this

1:11:59

once again I'm going to make sure I'm on Fuji which I

1:12:07

am still compiling okay here it is RW ending RW

1:12:13

ending all good so we need to provide the address of real estate token because it will query it for that view function

1:12:21

for for prices so this address the address of usdc so the address of usdc I

1:12:28

like to get it from CCAP page so uh this

1:12:34

is this 54 whatever and if you go here it's again 542 so that's the address and

1:12:42

we can also verify it here that this is USC like five for the same the same

1:12:48

thing so I'm going to paste that address aggregator the address of the

1:12:56

aggregator so I'm going to go to docs. chain. link I'm going to go to data

1:13:02

feeds I'm going to go to feed addresses I'm looking for Price feed address and

1:13:09

I'm looking for Avalanche so Avalanche specifically Avalanche Fuji testnet so

1:13:14

Avalanche testnet over here and because it's a testnet I'm going to show more

1:13:20

details because okay let's not show more details here first of all all I want to

1:13:25

find the usdc in terms of USD and here it is usdc in terms of USD 97f so I'm

1:13:32

going to copy that already here here 97 F so the same thing and this is the hard

1:13:38

bit that I want to provide and I can get it by showing more details over here and

1:13:45

we can see that for USD terms of USD it's 86,400 seconds so I'm going and here

1:13:53

8640 so 8640 over here

1:13:59

let's okay and I'm going to hit

1:14:05

transact so mathas pop up popped up you cannot see this but I'm confirming this

1:14:10

transaction and I'm waiting to uh to include in the next lock which just

1:14:16

happened confirm transaction and here is the RW Landing smart

1:14:22

contract now the question for you I said

1:14:28

that 83 line will be important here so

1:14:34

let's uh uh let's zoom out a bit so you can see the whole

1:14:39

implementation okay this is the borrow function okay borrow you don't need the arguments I

1:14:46

think so first of all we want to call

1:14:53

the the price of usdc in terms of USD and we can see that now it changed

1:15:01

it not anymore zero one z0 Z whatever it's not one $1 now

1:15:09

it's one two 3 4 5 6 7 8 decimal Zer so

1:15:15

one usdc currently

1:15:21

wors this amount of dollars okay so 0.9 we can see it it changes so that's why

1:15:26

we must not assume it's always one even though it was one the second is we are going to um we

1:15:34

are going to get the valuation of this token in usdc so get valuation in usdc

1:15:40

that's the one uh the one function which will call the get USD get real estate

1:15:48

token price details from functions those three uh values use that evaluation formula call the get the C price field

1:15:55

which is just called and normalized to six decimals and we should see a value

1:16:03

here so this is the valuation so normalized

1:16:09

valuation this value normalized valuation is let's collapse this is this

1:16:20

sorry is this value okay so this is normalized valuation let's say now that Alice wants

1:16:30

to uh borrow or to uh to land sorry in order to borrow usdc to land 25% of its

1:16:41

uh ownership of this fractionalized real estate so 25% will be five

1:16:50

tokens so 25% or five tokens

1:16:57

five real estate

1:17:02

tokens how much in return we

1:17:09

should how much usdc in return we should send to

1:17:17

Alice please drop your thinking in a chat this is question for you

1:17:30

take your time this is the ultimate test have you

1:17:36

UND have you like understood everything I I said for I was saying for the past 30 minutes I think slowly easy so how

1:17:45

much use the see roughly or at least formal or how to calculated we need to

1:17:50

send in return back to Alice

1:17:59

all the code is here at the

1:18:05

screen we have time by the way so I won't rush

1:18:15

you okay cool first of all we we have a text

1:18:21

for uh y or draan I'm not sure I pronounced

1:18:27

that name correctly I'm sorry he said or she said uh 100 89k

1:18:36

usdc uh okay we now need to somehow verify to

1:18:43

recalculate whether that amount is correct how we should do that so we can

1:18:49

be sure that this person hasn't just typed random amount

1:18:55

uh which I assume it's not but which formula or how we should calculate how

1:19:02

much usdc we can get nice even better we have with decimals so he definitely

1:19:08

calculated this so roughly uh

1:19:13

89.3 93 usdc should be sent from this

1:19:19

contract but you you don't like think for yourself and

1:19:25

and uh drop in in a chat why uh do you think this amount should be sent and how

1:19:32

we calculate it and Etc so this is the normaliz valuation we got from calling

1:19:37

the contract this is what smart contract calculated for us Alice wants to uh land

1:19:44

25% like 25% not the the all the whole amount of the whole fraction of the of

1:19:51

the house so that'll be five tokens because me we Meed yesterday 20 so five

1:19:56

is 25% of 20 and uh this is how we should

1:20:10

calculate okay cool we saw here from

1:20:19

TBO uh that he calculated that the valuation we got by calling that

1:20:25

function get valuation you see as if I go back

1:20:30

here uh if I go back over here okay

1:20:36

so this function return that so he multiply that by five which is the

1:20:43

amount and total Supply is 20 so this is this is normalized valuation this is 25

1:20:49

and yeah sorry this formula will gives us um the

1:20:57

normalized valuation however that will be like 4 100% that'll

1:21:03

mean that no matter like that'll me that price below for even a percentage down

1:21:10

we need to uh we need to uh we need to we can liquidate Alice so because of

1:21:17

that she she needs to get only 60% of that value and as Ramy said here so of that

1:21:26

value of this one that of normaliz valuation we need to get only 60% of that value so this uh

1:21:37

and also there is Kai said you need to convert that to usdc this function

1:21:42

valuation in usdc already converted this to usdc so this is in usdc so this is

1:21:50

usdc then we're multiplying this by five which is the amount dividing by 20

1:21:56

because that's 25% so let's calculate that shall we calulate or that's yeah calculator let's

1:22:04

do so that's what um this

1:22:11

amount can I type no oh come on uh okay

1:22:17

that'll be 7 five7 7 five s oh this is painful 4 3 0

1:22:28

4 1 4 5 I hope I don't have Tyles if I have I sorry so we're going to multiply

1:22:35

that that with five and divide this with 20 and we we got this value now we also

1:22:44

need to so this is 100% we need to calculate 60% of this value over here so

1:22:50

times 60 divided by 100 so 60% times 60 ided

1:22:59

100 okay so this is the usdc amount let's see if I can grab

1:23:07

it uh okay so this is loan amount so now

1:23:13

loan amount is this value if this value is

1:23:18

less than minimum loan amount it will it will revert but essentially we can see here that we're transferring loan amount

1:23:26

back in return and since this is usdc finally that means that this amount

1:23:32

is 1 two 3 four five six we put here so that'll

1:23:38

be uh that'll be okay like

1:23:44

this 113k something which I think someone

1:23:50

posted over here uh so roughly roughly this

1:23:58

amount okay however if we go

1:24:03

to Circle

1:24:10

facet this faucet grabs gives us 10 usdc so in order to not spam this faucet

1:24:21

and we most likely won't get this amount of USC easy even though if

1:24:28

we somehow manage to spam it we're all going to conclude our exercise here

1:24:33

because we're not going to do the actual uh borrowing on chain because like it's

1:24:39

ridiculous so what you can do if you want you can try to implement this in a

1:24:45

local environment so you can Fork mayet tet whatever and then you know your found your hardhead test you can e sorry

1:24:53

you can easily play with this or as a work around if you still want to see this in action instead of you when

1:25:01

you're deploying real estate lending over here instead of the actual usdc

1:25:07

token create your own mock usdc some simple year C20 token which will have uh

1:25:15

which will have um six decimals

1:25:20

and you can endlessly mint that token so if you go to for example wizard opens

1:25:26

zpp or something so that smart contract might look something like this so my so

1:25:32

that'll be mock usdc

1:25:37

so mock usdc we you can uh pre-int whatever

1:25:44

amount of you want however

1:25:49

whatever uh and you can also me make it um permit is important because us is

1:25:57

also has permit you can make it minable if you want and uh you will just need

1:26:04

to oh okay I'll just I cannot edit this

1:26:12

unfortunately that's that's unfortunate but let's say Mark

1:26:20

usdc and you can also emit function d

1:26:25

uh public view I think returns Y8 should be right and you will

1:26:33

just return six decimals right and what's wrong with this overwrite okay public

1:26:39

overwrite and yeah that's that's how you will implement it and because you can mint this token endlessly then you can

1:26:47

play with it on testet you're still going to use the actual usdc data but you don't need to spam uh use C faet

1:26:55

endlessly so yeah um because first of all you probably won't

1:27:03

be able to get this amount of tokens anyway and second of all you must never

1:27:09

just Spam faucets and grab tokens like tokens are for everybody there are much

1:27:15

easier ways to test stuff in Foundry and Har there's all especially Foundry

1:27:21

really powerful development Frameworks and you should spend your time there and test everything there test ns are just

1:27:28

for for final ux testing in my opinion at least okay cool that was exercise

1:27:34

number one um any

1:27:42

questions that are not already answered in a chat because I saw you're now

1:27:48

discussing discussing sorry discussing between yourselves

1:27:54

uh and yeah uh could we change threshold for testing purposes instead uh well no

1:28:02

because because these three values returned from Z API are high because

1:28:08

that's the value of mock real estate so it won't influence that much I mean you can set I don't

1:28:16

know wasn't initial threshold to 1% or whatever and it's going to be a really

1:28:23

low number but um you know it's better to do with your own mock token or uh in in Foundry or

1:28:32

hardhead it's much much easier and that's how basically um people that are writing

1:28:40

production ready contracts are doing their testing not intestines Okay cool so quick break like

1:28:48

30 seconds break and we are going to start with exercise number two

1:28:54

so for homework for this one you you can just deploy ourl ending to Al Fuji

1:29:01

that's that's fine that's enough because you know you can play with it call these few functions to see the calculations

1:29:09

but if you want to go step forward you can create your own mock dami version of usdc and uh play a bit on testnet uh do

1:29:17

not use actual usdc these are ridiculously high amount of tokens so

1:29:22

yeah

1:29:31

cool exercise number three okay

1:29:55

X number three is actually quite simple

1:30:00

and as I said we are going to just create an English auction to send a fraction of

1:30:09

this real estate tokens because again if you use RC71

1:30:15

standard uh you will need to transfer the whole the whole token like id1 or ID

1:30:22

777 and that's the whole portion the the powerful part about uh 1155 is that you

1:30:30

can represent that fungible asset with certain amount of nonf fundable

1:30:36

tokens um effectively making that funable asset a fractional fractionalized asset and I

1:30:44

said that I don't know how many times during this two days and we are going to um use this uh

1:30:54

feature of your 1155 standard to create an English auction where Alice can send

1:31:02

can sell this famously 25% like this five tokens to the highest bidder and it

1:31:08

will receive native coin of that blockchain aax in our case or e interum zolia in return

1:31:16

so there is also as I said besides English auction there's also Dutch

1:31:21

auction these are the two most popular decentralized auctions there's some more

1:31:26

but essentially these two are the most common we uh decided to go with English

1:31:32

auction because it's uh it's a bit easier so here how it works at least

1:31:38

this minimal implementation so Alice will deploy this contract and whoever

1:31:43

deploys this contract will be a seller so it's not like the general pus auction this is contract that specifically Alice

1:31:49

created to sell her fraction it's just for her so it's not General purpose for general purpose contracts it will be

1:31:56

bigger I have more features and I wanted to keep everything minimal and simple so it can fit uh on screen while I'm

1:32:03

sharing uh the code and it's not that hard to follow and let's say that's Alice okay when Alice calls the start

1:32:09

auction function we will see the start auction function the contract will lock automatically transfer the portion of

1:32:15

your C55 tokens she holds inside it she specified like the that

1:32:20

percentage auction lasts for seven days that's coded so during the next seven

1:32:26

days anyone can bid um so the bidding is in Native coin only like message. value

1:32:33

and anyone can bid by depositing uh amount greater than the current highest

1:32:39

bidder all biders can withdraw their bids excluding the current highest bidder obviously so whoever is the

1:32:46

current highest cannot like withdraw its own bid

1:32:51

logically if I'm not the current highest I want my bid I want my coins back because like I want I want buy or get on

1:33:01

these fraction of real estate tokens after the auction ends after seven days

1:33:06

the contract is designed that anyone can call the auction function like anyone even like chaining automation we can

1:33:13

automate that which will transfer this fraction real estate tokens to the

1:33:18

highest bidder and the highest bid back to Alice so inside the same use cases

1:33:26

folder again inside the folder name it however you want create the English

1:33:31

auction. file and I'm going to copy the content

1:33:38

and we are going to analyze this this contract so inside artifacts use cases

1:33:44

over here English

1:33:51

auction. pasted comp file and here it is if you're interested in Dodge auction

1:33:59

you can go to solidity by example it's a really good website and here should be

1:34:06

somewhere do auction so this is English the code is pretty similar to ours and

1:34:12

this is Dodge auction like the the difference is that these auctions are for nfts so uh this is the main uh

1:34:20

adjustment we needed to do and this is how how dod auction Works essentially you

1:34:27

can just Google them uh it's a slightly different primitive but you can definitely do that uh with with this

1:34:34

real estate token. well so that can be even like a nice exercise if you want to go beyond this workshop and this boot

1:34:42

camp uh once we Implement English auction you can maybe try to implement do doch auction by yourself that'll be

1:34:49

like a good a good example like not for homework like can not be necessary for

1:34:55

certificate but the the secret to becoming a grade developer is just

1:35:00

practice and coding and coding and repeating 10,000 hours whatever so you can just uh use this smart contract

1:35:08

which is for nfts and try to adjust it for our smart for our real estate token

1:35:13

which is 1155 and you can grab some ideas how you can adjust uh those uh by

1:35:20

following the inunction uh smart contract so if you go want to go Beyond um so you can uh create that for

1:35:27

homework and maybe post it in a in Discord or whatever tweet it tag me okay cool let's

1:35:35

understand the English auctions smart contract so this one as well uh has implemented this e ERC 1155 receiver

1:35:43

because this contract as well will need to be able to receive ERC 1155 tokens

1:35:49

and implementation of onc 1155 received and onc 11 55 bat received and support

1:35:55

interface are exactly the same as in our airw Landing so I'm not going to explain

1:36:00

them again extremely straightforward but um you know like you you need to be sure

1:36:07

that um message. sender is the actual real estate J at

1:36:13

least cool the in Constructor we as I said setting this immutable variable

1:36:19

seller to Alice to message the sender to whoever is the deployer of contract and we're just providing the address of

1:36:26

the real estate token dosl smart contract when we call the start auction

1:36:31

let's collapse this so start auction uh function will again check follow check

1:36:40

effect interaction pattern if auction is in progress it will revert if seller is

1:36:45

message. sender is not seller auction with reward so Alice will need to call it then it will transfer from Alice

1:36:52

address from seller's address to this smart contract the certain amount of tokens for a specific token ID so in our

1:36:59

case that will be token ID zero amount is five for 25% of 10 or 10 for 50% or

1:37:05

whatever data will be empty because we're not utilizing data but you can definitely explore if you want what data

1:37:13

has to do with in in the context of earc 1155 um it's actually a great thing uh

1:37:20

and finally we're going to put the starting bid so start starting bid in uh

1:37:26

with 18 decimals so because of the M do value in the native coin right so if we

1:37:33

want to sell this for 100 augs that will be one and 20 zeros as a starting

1:37:38

bid and the rest is we're um just setting this flag to true and and Tim

1:37:46

stamp is from the current block time stamp plus 7 days so auction last for seven days and we're just throwing some

1:37:53

details about the token that is on auction the amount that is on auction of fractionalized asset the current highest

1:37:59

bidder and highest bid are just a starting bid and message. sender that means that if Alice is still the highest

1:38:06

bidder uh she will be able to just uh get her tokens back in return because

1:38:12

like no one she hasn't sold it to anyone right there is a view function to get

1:38:18

the current uh ID of a token that's on auction so you can interact with the real say token as well by yourself and

1:38:26

for example you might want to do something like this so uh let's collapse this oh expand this

1:38:35

sorry let's actually Zoom it a bit so this is real

1:38:40

estate token so here you might okay this is the one this token IDE is on auction

1:38:45

okay I want to see more about it so if I go here URI okay this is the ipfs hash

1:38:51

now I if you go to ipfs hash I can see details number of rooms bedrooms total

1:38:57

prices picture of that house whatever like you know like okay I want to bid

1:39:02

for this fraction of tokens this is interesting to me Etc how how can you

1:39:08

bid this is the implementation of a bid function and it's extremely simple first

1:39:14

we have some checks uh checks whether the auction is auction is in progress

1:39:19

weather is not ended right and like if it's past 7 days and whether your bid is

1:39:27

uh actually the high greater than the highest bid if not we'll just revert because we want you must bid with the

1:39:32

message. value amount that highest than the current highest bidder and this

1:39:38

function is payable because this function payable in solity means that this function can accept need coins the

1:39:44

rest of this function is extremely straightforward uh it just updates highest bider details and the current

1:39:50

total bids uh mapping and yeah that's that's pretty much it if you want to

1:39:57

withdraw bid if you're not the highest bidder so if you're highest bidder you cannot withdraw if you're not you're

1:40:02

just going to grab the total bids you placed so far so not like that's why we

1:40:07

have this mapping the total bits you play so far and we're going to delete

1:40:13

that mapping and send those coins back to you um this is the preferable way to

1:40:21

send coins native coins and solidity uh I think you can pretty easily find um on multiple different

1:40:28

places on internet why but this is how you you you should do it this is the safest way and if this failed we'll

1:40:36

revert finally for all final function is end auction as I said after seven days

1:40:43

anyone can call it and by calling this function uh D it will automatically

1:40:50

resolve to send uh irc1 55 tokens like fractional point of that house to the

1:40:56

highest bidder and highest bid back to Alice in in Native coin in aex in our

1:41:02

case and yeah that's pretty much it so

1:41:07

I'm going to deploy the smart contract I'm going to put it on auction I'm going to send the address so if you want you

1:41:14

can bid for a fraction of my real estate if if you want if you have time but um

1:41:22

for for homework you can just play with it deployed start auction try to buid with different wallet or whatever uh if

1:41:30

you you know like you can maybe play with your friend you can be or whatever

1:41:35

okay cool so let's compile first this smart

1:41:41

contract and the only address that I need to provide as a function argument

1:41:48

is the address of real estate token so I'm going to hit transact I'm going to deploy the

1:41:53

smart contract to a Fuji I'm going to hit confirm I'm going to wait for

1:41:59

transaction to

1:42:04

complete okay um there is a question

1:42:14

right token ID on auction have we updated that yet okay cool yes we did

1:42:20

okay so the question is the return by get token ID on auction is zero by default so you have to refer that a

1:42:27

token ID is available for auction by default no it will re return this

1:42:32

storage variable and I just search for it to see have I not forgot to put that but I haven't so when you start auction

1:42:39

you said I want to sell this token ID on auction and it will return that value

1:42:46

because that will be locked inside a contract in our case it will be like it's zero because we all have like to

1:42:53

the zeros but in general case does not doesn't need to be I hope that that does

1:42:58

not that answered your question okay so where is English auction it's over here let's hi this

1:43:06

comment okay so there is a bid function there is end auction withraw bit Etc I'm

1:43:12

going to So currently you know it's it's zero because there is no that's the

1:43:18

default value uh but uh I'm going to start the auction

1:43:24

so um before this this function will also revert if I don't approve this

1:43:31

smart contract to spend my tokens first so what I'm going to do here is I'm

1:43:37

going to go back to real estate. s smart contract and there

1:43:43

is um approval somewhere so that should

1:43:48

be burn burn batch set approv this

1:43:58

one yeah so I'm going to set that as a true

1:44:04

so this should work right if not I'm going to go back

1:44:10

uh okay so this will

1:44:17

allow yes I'm going to approve this I'm going to wait for transaction to

1:44:24

complete and here token ID I'm going to put five like 25% for data I'm going to

1:44:31

put empty and starting bid we can do we can do let's

1:44:41

say 0.1 aox okay so that me mean that I

1:44:47

need to provide how many zeros

1:44:54

this has 18 decimals anyone in the chat how many zeros for Z 0.1

1:45:11

aox there's a question by the way okay Valerio said 17 TBO 16 Ricardo 17

1:45:21

Mauricio 17 and yeah the the correct answer is 17 yes so one and 17 zeros okay let's

1:45:30

count that would be 1 2 3 4 5 6 7 8 9 10

1:45:36

11 12 13 14 15 16 17 okay so I'm going to put 0.1 aox as a high as a starting

1:45:45

bid and I'm going to hit transact so now you should see the metus pop up

1:45:56

a My remix froze Great Looks Like My remix has just froze

1:46:04

let's do one more time oh uh I have an error here okay

1:46:10

let's do it like this okay and yeah this will start my

1:46:20

Au uh and yeah that's that's pretty much it again you don't you can if you want

1:46:27

start the auction uh but uh what was in play with your friends but it's not necessary

1:46:34

again you can just deploy the smart contract and send the address of that smart contract because we have all this

1:46:40

issue with test Nets the LA the the we don't want to have a lot of transactions

1:46:47

with these gas uh gas prices so for you to complete the homework deploy auction

1:46:53

dosl and just submitted via this form but you can anyway like you can

1:47:01

play you can play uh with it and yeah that's that's pretty much it now I'm

1:47:08

going to answer some questions we're going to play some music and you will have exercise time so you can deploy

1:47:14

both RW landing and English auction. well on Fuji or other testet of choice

1:47:21

but it's more important that you understand how these use cases work and to be inspired of what can be

1:47:29

built with tokenized real estate so it can be much more than just lending and borrowing if you want to to practice a

1:47:37

bit you can Implement do auction instead of besides English auction from scratch

1:47:43

and solidity using the same the same contracts etc etc so yeah let's answer

1:47:49

some questions and let's play some music I'm going to play the same one from yesterday uh I hope that's

1:48:04

[Music]

1:48:11

fine if it's too loud or not great or whatever

1:48:18

uh uh that's just tell me in a chat

1:48:26

[Music] so now is officially exercise time we

1:48:33

have uh around 40 to 45 minutes for exercises and after that we will have a

1:48:40

talk with the bricken team specifically with their coo and co-founder advin so

1:48:48

uh I'm going to continue answering questions and after that we will have have admin joining us okay

1:48:59

questions let's see where we start well

1:49:04

we if someone was not the highest bidder and do not ask for the bid in return When the auction is finished they still

1:49:11

can ask for the funds to be returned okay let's see the actual implementation shall we so withdraw

1:49:19

bid says if if you're not the highest bidder you

1:49:24

cannot uh you cannot withdraw it if you are sorry if you are highest bidder this will revert otherwise it will grab your

1:49:33

all of your bids and if you haven't if you don't have any bids it will still revert but if you have it just going to

1:49:42

transfer back your coins to you so thus it's not it doesn't matter if the

1:49:48

auction has ended you can still withdraw your bids afterwards

1:49:53

so I hope that answers your question uh 17 17

1:50:00

[Music] 17 Andre are you deploying on Fuji as yesterday uh yes I'm deploying on Fuji

1:50:07

as yesterday because that's where my contracts are you can deploy to your Des network of choice but you need to deploy

1:50:14

everything and make sure that all of those four Training Services are available on that testet who validates

1:50:21

transactions here and where should we get the contract addresses for the homework uh for the homework you will

1:50:29

have this type form you'll click on it uh you'll you're going to take one

1:50:35

minute this is your email address and then you're going to enter token addresses for for each of contracts

1:50:43

you're going to enter contract addresses here uh it says an all Fu as you said

1:50:48

can be whatever test M of choice as as long as it's like that the same test net

1:50:54

so in my case actually okay let's I can fill this

1:51:01

so for my case that'll be this is my email my real estate token is addresses

1:51:09

this one real estate token address this one

1:51:14

so I'm going to hit enter my issuer smart contract is

1:51:24

is is is this one so I'm going to paste

1:51:29

that airw Landing this one this one enter and

1:51:39

English auction this one and this one

1:51:47

[Music] submit and congratulations I I submitted

1:51:54

okay so let me okay that's how you can submit

1:52:02

and who validates the transactions there that will be me so after that we going

1:52:08

to collect all your submissions and then I'll grab your addresses and then for example let's grab my real estate token

1:52:16

ASL once again and I'm going to grab

1:52:23

here and okay I I can see I have some transactions some contract okay you have

1:52:30

not uh I have not like uh verified on Explorer but I can

1:52:37

always load it in remix because I have a source code and I can expand and see all

1:52:42

of these transactions and I also have like an AI so I can easily go to tenderly and see what's going on and

1:52:48

after all that boring manual work I'll I'll confirm that you created function

1:52:54

subscription uh call the issue function call the update details function etc etc

1:52:59

so yeah that's how it's going to work it's going to be extremely manual work for me but it was the same as for CCP

1:53:07

boot camp so yeah it is what it is you're going to wait for a bit unfortunately but eventually we will

1:53:12

send you certificates uh music okay thanks a lot

1:53:18

for explation you're welcome I'm glad this was useful for

1:53:25

you um I don't need to remind everyone to pin their

1:53:31

contracts uh we're not dealing with CCAP so yeah uh

1:53:39

okay balance uh for the

1:53:45

homework for the homework can we deploy those contracts to networks other than sepolia yes to any dnet you'll find

1:53:53

convenient just make sure that these four uh features of chaining platform

1:53:59

services are available and you can grab them by go to Quick links anyone

1:54:06

wherever you land on a doc you can always click on quick links literally any page quick links is over there and

1:54:13

you need to make sure that CCP data fits functions and automation exist on the Tet there's like plenty of them and you

1:54:21

can use that test Network um can you share the link with

1:54:28

the music and playing I don't have it if I found it I'll share it maybe on

1:54:34

Twitter on Discord but I don't have it at the [Music]

1:54:41

moment uh if we all deploy toe Fuji to homework is it okay it's

1:54:46

okay um can we see the mintt nft on testet I yes but the metadata won't be

1:54:53

there until you publish uh to ipfs manually but

1:55:00

technically yes uh great finish thank you Andre thank you Gabriel nice job uh once we

1:55:07

review our homework we're going to issue uh on train certificate of completion and we're going to send it to your email

1:55:14

the unique link so you can

1:55:20

minted um why start auction is getting reverted

1:55:26

let's find out um there might be an error we can take a look at the code I'm

1:55:32

going to take it in a minute uh doing tomorrow all the

1:55:39

exercises then fill the form thanks yeah thank you you can do it until October

1:55:45

4th and I think yeah this is the deadline October 4th at 11:55

1:55:52

to 59 p.m. ET eastern

1:55:58

time um can you explain why you need to pin

1:56:06

with CCP yes so uh if you are working with

1:56:12

remix uh you can see here that I've connected to injected provider mamas

1:56:18

that means that if I switch you cannot see my mamas pop up now but if from my metamask I switch to different

1:56:25

network I will uh lose my deployed contracts over here because they not now

1:56:33

do not exist on that network if you want to avoid that from happening you just

1:56:38

click pin here and for each contract you want to

1:56:44

pin that means that when you switch to different test Network they will again be removed but when you go back to alen

1:56:53

Fuji switch again do something and then switch again here under pin contracts section over

1:57:00

here your contracts will be visible again and that's useful for CCP because

1:57:07

with CCP you switch between networks multiple times in

1:57:14

remix uh how would we receive the certification you will receive the

1:57:19

unique link and all the other details uh using emails uh like when you fill up

1:57:27

the form the first step is to provide your email to that email address we will send all the details Dio said thanks for the boot

1:57:34

camp all contracts deployed and tested congrats nice job thank you for joining

1:57:39

and I hope you're all going to fill the form so we can uh send you the

1:57:48

certificate thanks for the boot camp Andre you're welcome DL Tech is CP build on top of other technology like Cosmos

1:57:54

for inability or is it chain link native it's chain link native you can see uh

1:58:00

more details in the official docs so if you go to Doc chain. link and ccip there are a

1:58:07

bunch of concept conceptual overview architecture Etc a lot of stuff and we

1:58:13

also had CCP boot gamp recently so uh you might you can probably find the

1:58:20

gbook for that one and we also have had like four CP master classes so you can find bunch of details if you want to

1:58:27

really deep dive into it on both docs and previous boot camps and master classes but yeah short answer is it's uh

1:58:35

chain link native it doesn't have any external

1:58:43

dependency um yesterday you mentioned that you can transfer value between public blockchains and private

1:58:48

blockchains can you give an example for each of them so we can test those Solutions in real scenario so yeah CCP

1:58:57

is currently supported and uh for bunch of different private bank bank chains

1:59:04

both Main and test Nets and there's like a lot of testing over there Etc uh

1:59:10

however those config details are not live yet so in real scenario you can

1:59:16

just test between test Nets that are publicly available on the docs but uh

1:59:22

once once those private chains are uh are like details config details are

1:59:29

available and you know with whom you can interact with uh yeah you can you can use uh CCP for that but yeah various

1:59:36

different bank chains are already testing CCP uh with their own Tech and

1:59:42

their own data they're sending so yeah uh that's that's still a work in

1:59:50

progress and obviously in in the future there will be like non evm chains evm

1:59:55

chains and private and public everything's going to be interconnected but for now you can just test

2:00:01

with chains available over here or you can even test everything locally with

2:00:09

chain link local but that's another topic but you can test CCP locally using chain link local which is another tools

2:00:18

of ours and also you can find uh more Det details about training local over

2:00:23

here if you go to resources and there is a dedicated docs page for training local

2:00:29

that's me so yeah that's it share your playlist uh yeah once I

2:00:38

have it I don't know um thank you a lot for boot camp I've learned a lot thank you I'm glad to

2:00:44

hear that uh thank you for joining yeah and I hope uh I'll see your name uh on

2:00:52

or your email sorry under submissions for the homework uh yeah thank you thank you

2:00:57

you're welcome I I'm really glad to see that this was useful for you we try to make it

2:01:03

useful

2:01:10

um so yeah at the moment uh we have

2:01:16

exercise this in progress exercise number two and three if you have any

2:01:21

questions them I'll try to answer them debug them Etc and uh shortly we'll have a guest

2:01:30

lecture a talk with the bricken team with their own uh CEO and co-founder

2:01:36

advin so we'll still going to listen for a bit of Loi and answering questions uh

2:01:44

and after that we will see some real use case like this is uh all about tokenizing and real

2:01:52

world assets and digital Assets in production so you can see how these guys actually do stuff that are like more

2:01:58

advanced at what we than than than our mock examples for the past two

2:02:04

days um yeah thank you guys thank you very much for all the nice words that

2:02:11

means a lot

2:02:18

um okay oh I lost uh I lost uh my

2:02:24

questions uh let's see thank you so much apart from deploying the smart contract for day two do we need to interact with

2:02:30

them in any way to satisfy the homework so for homework you can just deploy them and they'll be fine and enough to me

2:02:37

it's more important to understand what's written there and how you can write your use cases and to inspire you um and

2:02:45

because we had all these issues with with gas and test Nets we want to minimize the the amount of transactions

2:02:52

because there's like a lot of you that sign up for this boot camp but if you want to play with you can but it's not

2:02:57

necessary for the for day two for X Series 2 and three just deployment is enough and as I said you can also if you

2:03:05

want to go beyond you can play with it and recreate Dodge auction from scratch

2:03:11

for this tokenized asset if you want it's not part of the homework it's not mandatory it's nothing you can tweet

2:03:18

about it you can put it on Discord you can say okay I follow this boot camp there was English auction but I went

2:03:24

beyond and I implemented this DOD auction because it SS seem seems really

2:03:30

fun or whatever but yeah that's uh that's that's it um for that

2:03:53

[Music]

2:03:58

okay cool thank you for this boot camp it was very informative and super practical

2:04:04

I'll keep working on experiment with the contracts thank you very much fraco for joining us I'm glad to see that was

2:04:09

useful for you and looking forward to your homeworks and maybe do auction implementation we'll see so yeah uh keep

2:04:18

keep practicing 10,000 hours that's all it needs to master a

2:04:26

topic uh okay tokenize the world yes uh what value did you provide for

2:04:33

set approval for all um token ID Zer and five I think for the

2:04:40

amount uh but yeah and address of English auction contract I

2:04:47

think uh D said thanks a million Andre great and valuable learning in the last two days thank you for joining I'm

2:04:54

really happy to see this positive feedback and as I said hopefully to see your email

2:05:00

amongst uh the ones that completed the homework and maybe you can Implement that auction as well we'll

2:05:07

see uh okay thank you thank you okay cool and as I said I'm

2:05:15

exercises two and three are currently in progress uh take your time the like for

2:05:22

homework purposes you will just need to deploy these two contracts and that's it there'll be aaable valid homework for

2:05:30

exercise for day two so uh take your time and afterwards we will have uh a

2:05:38

guest lecture from the brickin team so he will join us shortly and as I said you will hear more

2:05:46

about what brickin is and does and how they use real world asset in production

2:05:53

so more advanced contracts and content coming

2:05:59

soon again if you have any questions about any of anything that we covered

2:06:05

today feel free to drop them in a chat specifically about some technical

2:06:10

implementations I assume some stuff in RW lending uh

2:06:16

are are interesting at least so

2:06:32

yeah with the real estate tokens well with this mock minimal impementation it

2:06:38

will be just locked in a contract forever uh but in reality like you will

2:06:44

need to um have a first way to unlock them some somehow but essentially you

2:06:50

want to split the profit between the protocol itself and the Liquidator so you have like incentive

2:06:56

for people to liquidate

2:07:01

positions So yeah thank you thank you Ronnie very much uh one project I'm interested in is

2:07:10

energy airwa organization are there any projects focused around that and what are something you will recommend when

2:07:16

coming up with solution I don't know there there might be some build projects doing that but I'm not sure I don't have

2:07:23

any info at the moment I can though ask and try to find it and then maybe let

2:07:28

you know on on Discord uh but yeah that's that's a hard

2:07:34

problem to solve definitely so I don't have any technical recommendation on top of my hat but definitely doable uh so

2:07:42

yeah I'll need to think about it about the the implementation and yeah I'll need more details from you of course but

2:07:49

yeah [Music] uh

2:07:54

okay so we will soon have our guest lecture from the bricking team joining

2:08:01

us so you still have some some time to to finish uh to finish the exercise for

2:08:08

today if you don't finish in time doesn't matter until you have time uh

2:08:14

until October 4th to to finish and also you can ask questions on Discord

2:08:21

uh hey Andre sorry in case someone already ask is the certification a poop nft or different yeah it's it's it's a

2:08:27

pup it's going to be uh a PO on on D chain so you can Min it there for free

2:08:33

and then if you want you can migrate to ethereum main if you want it's not it's up to you at that point so yeah you we

2:08:41

will send you like the unique minting link to your email and then after that you are in try charger minting like same

2:08:47

as for pops uh pretty pretty standard stuff uh and yeah this is how it looks

2:08:53

like where is Itor yeah it has this nice animation so

2:08:59

it's pretty I like the design I like this design more than design for CCP Camp though so so yeah so yeah stick

2:09:07

around we're listening to some wfi music we're doing our exercises our for homework and soon we will uh we will

2:09:16

have uh Our Guest lecturer join us uh from the amican

2:09:23

team uh let's see keep getting uh oh two

2:09:28

two questions okay first one why CCP needed for liquidity other train abilities and after is tokenized then

2:09:35

the task ends there please enlighten yeah well thing is that uh to successfully tokenize your asset like

2:09:41

you can tokenize in one chain but if you cannot move it across blockchain sufficiently you're kind of missing out

2:09:48

because there might be a buyer over there a different protocol over there for landing borrowing whatever for

2:09:54

auction or you might want to interact with a private chain or they want to buy something for from you Etc so you know

2:10:03

technically yes it's possible it's just on one chain but in reality for production use cases you kind of want to

2:10:10

be on all chains using CCP uh in order to to get the most out of your tokenized

2:10:18

asset getting the error Contra creation code storage out of gas so you need to

2:10:26

enable compiler Optimizer sorry compiler to 200 runs you need to set even version

2:10:31

to Paris uh and you need to have enough of uh T net coins to cover for gas

2:10:41

fees um just to make sure I did deploy avalan Fuji there are but I will deploy English auction on seoa well I try to

2:10:48

deploy English auction on Fuji as well because you will need the address of real estate token. so smart contract so

2:10:56

you cannot just put an arbitrary address there to play all so you want to do it

2:11:02

on a testet where your tokenized real asset is essentially because all of these use cases are linked to your

2:11:08

tokenized real that's why on day one we spent all day like tokenizing it and

2:11:13

then on day two just creating multiple use cases out of which we we can come up

2:11:19

with more and more and more use cases after day one it's it's it's really not that hard but yeah just make sure to be

2:11:26

on the same blockchain whatever the blockchain do network [Music]

2:11:32

is you're welcome cool if you have if you have any

2:11:39

any questions about everything we covered during past two days feel free to drop them in a

2:11:47

chat uh uh we will uh uh we will also have as I said adwin from the bricking

2:11:54

team here joining us you can also ask question to him like he will have a Q&A session at the end so stick around if

2:12:01

you want to hear more about some some real stuff in production uh and until

2:12:08

then I'm going to answer any questions you might have help with debugging and we'll listen to uh this nice Loi

2:12:16

playlist okay this is a good question we can

2:12:22

tokenize a lot of offchain stuff but who is responsible for offchain documentation and yeah that's part of

2:12:28

the step five oranization as I think I shared here with this

2:12:34

page and yeah that's part of step five of inssurance and step number five is out of scope for this boot camp so yeah

2:12:42

out of scope for this boot camp uh and yeah it's it's a hard

2:12:49

problem to solve definitely uh uh but yeah it's not much of a technical

2:12:55

problem Al like Deco might help but

2:13:00

yeah so yeah I hope you you enjoy this playlist I certainly do

2:13:14

[Music]

2:13:23

[Music]

2:13:32

and I might actually cover this um while we're waiting for more questions this is

2:13:38

the last page of the G book with the next steps so this is also useful if you

2:13:45

want to continue your Learning Journey about chain link platform so the first

2:13:51

stop is you can join us at smartcon this is the Premier annual event this is the

2:13:57

annual training conference which is happening uh at the end of the October

2:14:03

in Hong Kong 30th and 31st October are the main conference days but on 28th and

2:14:09

29th we also have a hacker house so following this link and scanning this QR

2:14:16

code you can uh register for smaron following this link or this link you you can register for Hacker House so event

2:14:25

which is happening 2 days before the main thing during Hacker House this is event specifically crafted for

2:14:32

developers during hack Hacker House you will have these certifications uh in

2:14:37

progress uh in yeah training certifications in place so if you're

2:14:43

interested in obtaining training certifications uh we will have something

2:14:48

for you during hacker house so you can listen to the live classes about

2:14:53

certifications on the day one and then on day two you can take the exam take

2:14:59

the actual test in person on site in order to earn a certificate so there

2:15:06

will be some technical resarch a lot of workshops and and talks some happy hours

2:15:13

for networking and you will have the opportunity to connect with the

2:15:18

recruiting team from training clubs and some of our ecosystem P Partners at the

2:15:23

talent happy hour during the first day so at the end of the day one there will be an opportunity for this type of

2:15:31

networking which I think is highly valuable so we can see the whole schedule over here on day one after

2:15:37

rering ceremonies there will be some talks workshops and certification courses you will have lunch provided and

2:15:44

there will be more talks and certification courses again until 6:30 p.m. so all the content you need to pass

2:15:52

the certification then there will be this Talent happy hour and networking dinner so this is the time where you can

2:15:59

uh talk with the recruiters from the training clubs and some of our ecosystem partners and also there will be happy

2:16:06

hour where we can just network with all the other participants uh over there on

2:16:11

the day two there will be breakfast provided and then we will have the certification exam prep for blockchain

2:16:18

fundamentals and chaining fundamentals so there will be two uh certifications blockchain fundamentals and chaining

2:16:24

fundament fundamentals is nothing too hard like it's it's fundamentals no

2:16:30

worry guys like you you can pass that I'm sure uh but uh after after that prep

2:16:37

there will be a lot of talks and workshops just explaining all that stuff

2:16:42

after that there will be a lunch and then from 2 to 4:00 p.m. you will take the certification exams like in real

2:16:49

world you will take exam like there on

2:16:54

on on site uh in in Hong Kong and then there will be like closing remarks and

2:17:00

whatever but there will be like uh a reviewing of all your

2:17:06

exams and potential to get um to to get certificates so that

2:17:13

that's that's about Hacker House you can obviously sign off for CH developer newsletters to stay updated

2:17:21

and uh you can get in touch but more than that later as we promised we will

2:17:28

have uh talk with the bricking team so I'm going to quickly now um turn off this Loi playlist so uh

2:17:39

exercise time is done if you still haven't completed your exercises you have uh time until October 4th it's it's

2:17:47

not too hard and as I said it can be on whatever test that you find convenient

2:17:52

and now as I said multiple times we have a guest lecture the uh CEO and

2:17:57

co-founder of the bricken uh uh edin is here with us uh he will talk as I said

2:18:04

with you more about what bricken is and

2:18:09

how you can actually work and build with real world asset and tokenize asset in

2:18:14

production so these are the guys that like actually do some stuff in production with real world

2:18:21

and we just created mock versions uh for educational purposes over here you can

2:18:26

definitely connect with the brickin team and Edwin himself on Twitter and web page and now if Edwin is ready I would

2:18:34

like to bring him on stage so welcome Edwin can you hear us yeah

2:18:43

thank you very much for having me all right right yeah thank you very much for

2:18:48

for having me pleas sh my screen and I'm going to uh stop sharing like this I'm

2:18:56

going to add your screen to Stage I'm going to go back to the background the floor is yours and good

2:19:04

luck perfect so uh thank you very much for having me here an absolute pleasure

2:19:11

uh so yes my name is mat I'm the CEO brickin brickin it's a tokenization

2:19:16

platform that is under the build program of chain link we have been with the build program for a year and a half I

2:19:22

believe now so it's been an an absolute roller coaster to see how a lot of new

2:19:27

companies are jumping into the space Banks family offices asset managers real estate you name it right so it's all

2:19:34

about the digitization and tokenization of the space so I'm hoping that over the next half an hour I'm able to transfer

2:19:41

all of the excitement that Thrills here in bricket about the tokenization of rear wall assets but also to comprehend

2:19:48

what it's coming and why I mean the end as a builder you have to find a problem

2:19:53

that you want to solve and here in brickin we've been building our solution for over four years so it's an absolute

2:20:00

pleasure to share a little bit of the knowhow that we may have and I'm saying little knowhow and that's going to make

2:20:06

a lot of sense on my next slide right because uh real world asset came to be

2:20:11

as a term around I would say 2023 before that it was very diverse some will call

2:20:17

it just security token offering other will call it just crypto currencies or they will call them just digitized

2:20:23

assets so it was not well defined what a rear wall asset was and now it came to

2:20:29

be that it was what we call the offchain value right so if we were to understand

2:20:34

what is the total amount that is offline there's it's impossible to measure and

2:20:40

saying impossible seems like a very broad word but in the sense there's so many assets still out there that are not

2:20:47

even online so forget about the chain value right talk about all those assets

2:20:53

that have no value online so for example uh there's a lot of still real estate

2:21:00

streets in many countries that don't even have an address they're not in a registry land that has no ever been uh

2:21:07

value so it's impossible to comprehend how to put it online uh we have a lot of

2:21:13

exotic values out there J miral so if we were to amance all of the real world

2:21:18

value we're talking about trillions and trillions of lock value right so then we

2:21:26

have all of the big next Trend which is kind of like all the online value right so there's actually real estate that is

2:21:31

measurable there's stocks that are measurable because they're in a stock change but then there's private markets

2:21:37

that are not really fully online and not yet publicly disclosed value of companies who are not there so even in

2:21:45

the online World which is still a trillion more multi- trillion Euro

2:21:50

Market or dollar we still don't have a pure value right because the measurement

2:21:56

it's not so simple uh thinking about a startup who raises money the valuation is provided by the investor so you can

2:22:04

comprehend what is the value but that yet is not fully disclosed and it's a valuation made by the company itself but

2:22:11

then what about all those companies that don't have Founders or don't sorry don't have uh startup or capital or what about

2:22:18

the normal restaurant on the corner who provise value so even if you have a digitized asset still very hard to

2:22:25

measure so we come from a infinitive locked value who is not

2:22:31

online to trillions of lock value who is very hard to comprehend so this is where

2:22:37

the tokenization comes which is kind of like just the one less than 1% of the

2:22:43

total value of the world locked now comes into the tokenized version and why would you tokenize an asset because all

2:22:50

the pains that I've been speaking for the last three minutes are gone basically you do understand at all times

2:22:57

in real times what is the value of an asset where is it located there's a lot of transparency what are the moves who

2:23:04

is trying to allocate value is it locked in the chain is it locked like so many

2:23:10

questions that you may have when you go to an offline to an online in the

2:23:15

tokenized version there's a lot and obviously if information is symmetric that means between buyers and sellers

2:23:21

they both have the same information it becomes an efficient market and it becomes accessible so all of this is the

2:23:29

reason why we always hear or listen that it's becoming liquid so I want to be a

2:23:35

little bit Transcendent here because this is one of the biggest terms that is been thrown for real world asset but yet

2:23:41

it's one of the most dangerous ones in the sense that we're playing with information the the liquidity value is

2:23:49

because the the information between buyers and sellers so the market comprehends that there's value and

2:23:55

there's an exchange of value between Stables to the asset or between euro to

2:24:01

the asset I mean liquidity is not form for the digitization phase what you do

2:24:06

do when you tokenize an assets and we say it provides liquidity is because you

2:24:12

truly unlocked the value right so this is where chain excels with all the

2:24:17

oracles and being symmetric with information with the price fits trying to really comprehend what is the like

2:24:24

the microsc value of such assets because when you start playing with liquidity

2:24:30

you want to have the real time value of it and that's where liquidity and all

2:24:35

these things come but it will make sense over the most uh the next couple of slides but I really want to for you to

2:24:42

comprehend the magnitude of the things that we're talking about when we talk about rear wall assets so from a pure

2:24:50

offline lock value we go to a semick value between parties who sometimes is

2:24:56

public such as public traded markets like NASDAQ euron next whatever to the

2:25:02

tokenized version where everything just becomes purely transparent more

2:25:07

symmetric more efficient more accessible and all of these great characteristics

2:25:12

that blockchain by itself brings is the reason why liquidity is unlocked it's

2:25:17

easier to transact and for people to ENT enter into these markets just because they have more access to the information

2:25:24

so this is how markets are created all of times it's between one person telling the other one the value is a and the

2:25:31

buyer say fine I buy your buyer a but instead of the negotiation between just

2:25:36

two part is trying to digress it's between public markets and public information so it's easier to negotiate

2:25:43

and settle so that's kind of like how we we can understand markets and basically

2:25:49

that's why we decided to jump into the real W as tokenization phase there's two types of tokenization

2:25:57

that it's super important to understand there's the external tokenization in the sense that the real world asset per se

2:26:04

is not the asset tokenized right because for example there's a lot also in the marketing schemes that say like real

2:26:10

estate is getting tokenized in reality the real estate the heart asset is not

2:26:15

the one tokenized for various legal reasons that make it inefficient so if

2:26:20

we're talking about technology point pinpointing where is the efficiency optimization points we don't have to

2:26:27

change the rule of law what makes efficiency happens and real estate and

2:26:32

other terms are still not there so the asset is not the thing that gets fragmented the thing that gets

2:26:38

fragmented and optimized is the financial instrument C linked to the real world asset if we think of it

2:26:45

actually everything works like that except natural personals me the asset Direct so I m I own a house perfect but

2:26:52

the company usually is the one owner of the assets so that's where the investors come in investors coming to

2:27:00

companies exposing the financial instrument where a yielding or a revenue might happen for the retail so in that

2:27:08

sense I am a real estate company who wants to capitalize in order to exploit

2:27:13

or fund myself to create a new hotel so to speak then I can do a capital

2:27:19

increase and i s shares that's of shares is a financial instrument that I can shoot into the market and then I can

2:27:25

obtain funding for the for the real estate but I'm not tokenizing the hotel I'm tokenizing again a financial

2:27:31

instrument into the company same mechanism can be for the depth I'm a real estate company who wants to create

2:27:38

a loan so I can get investors buying part of the loan and I'm giving them a percentage of top going be a fix a short

2:27:46

term so I'm giving them apy so this revenue on them so loan the financial

2:27:52

instrument by which the company gets linked to the real estate but again it's not the real estate pure the one getting

2:27:59

tokenized and obviously we can go about that treasury bills the bonds profit sharing scheme convertible notes but

2:28:06

this is how crucial it is so when we start talking about organization yes

2:28:11

couple of years ago the marketing was mere at the asset level kind of like oh

2:28:16

you tokenize real estate but you don't really but it's easier as a marketing scheme for people to understand that the

2:28:22

hard asset is going but when you start getting into the specialization phase

2:28:28

financial instruments is the one getting toiz and thus this is the reason why we seeing a lot um of examples of why chain

2:28:36

link is working with banks is working with asset managers because the financial instruments is the one getting

2:28:43

tokenized that's why money got tokenized because it's the one giving you access to all of this so it's super important

2:28:50

for for us Educators so the ones working in the space people to understand that the mechanism for tokenizing real wall

2:28:57

asset comes at the financial instrument superseding the access to the real world

2:29:02

assets and if that is external company to the third parties then we can go to

2:29:08

the Circuit scheme which is internal companies can also start tokenizing and

2:29:14

we're starting to see a new trend with companies offering tokenized value to the employee or uh Freelancers or access

2:29:22

so Phantom shares we calling this restricted restricted units in the sense

2:29:28

that it's a company providing value to employees such as uh investing contracts

2:29:33

I give you shares in x amount of value but I do it in the tokenized version to be more transparent and you can add

2:29:39

value on the okay if you're three years into the company then it gets an unlock of the shares so it's a pure mechanism

2:29:46

that we're starting to see just because it's uh it's transparent it's accessible

2:29:52

it's optimizable and you can start playing with that but just wanted to throw as an example for us to understand

2:29:58

that external tokenization happens so company to third par is being investor

2:30:04

but we're seeing a trend that internal tokenization is happening so company to whoever they want to tokenize who is

2:30:11

providing value as a whole to the company right so as internal external

2:30:16

quite simple here so uh a chain link boot camp why

2:30:22

did we decided obviously to join build program and it's been a quite a journey because of the technology and one of the

2:30:28

things we Builders have to understand is you got the chain layer you may have the

2:30:34

infra the protocol but the application layer is crucial we've seen a lot of

2:30:39

Trends kind of or explanation saying what about the user experience right and

2:30:44

this is crucial because um when you are out of the tech initiatives of the blockchain you talk to people who might

2:30:52

not even be really good at technology or even turning on a computer because I've seen it all you cannot talk in the same

2:31:00

terms because the same reasoning that we have here saying oh what is the most uh TPS chain or what is the most with the

2:31:07

transaction value per day and all of the things that might worry us for us in the chain world the developing thing it

2:31:15

might not be the same situation or problems that they're trying to solve in let's say web two so one of the biggest

2:31:23

hustles that we had in the back in 2020 there were some initiatives but it was

2:31:28

still very much in the building phase multiple chains fragmentation um gotta

2:31:33

come here super clean and say I'm super against the diversification of chains and all the great things that are

2:31:40

happening l1s l2s l3s sub Nets and all of that because

2:31:46

that fragmentation is not needed I think optimization of some chains are good and

2:31:52

I think two three are going to make it but in the end it's it's all about if it's hard for us to bring assets to a

2:31:59

chain imagine us bringing multiple assets to multiple chains options if I

2:32:06

was to throw to a client the following slide and I give them 10 options to get

2:32:11

into a chain they will stop talking to me because they just have one problem

2:32:16

one solution so the abstraction of the chain it's crucial so I was in Paris when they

2:32:22

announced the ccip and I got super excited I was like if it works like they

2:32:27

say it's going to work is a game changer because I can abstract as the application layer the chain and it's

2:32:34

super crucial I can have my favorite chain I can choose steering for security I can choose base for the gasless here's

2:32:41

example because usdc is gasless so it's super efficient for my clients to operate in a gasless experience so they

2:32:47

don't have to pay that much on each transaction that they will perform so

2:32:52

the important thing is if I am a stct and I provide the same level of

2:32:58

opportunities then I can create a great product a client again real estate as an

2:33:03

example they issue the asset the tokenized asset on base without even

2:33:09

knowing base I'm throwing them the base layer just because usdc it's regulated

2:33:15

in Europe or whatever the format or because I just want to and in the back

2:33:20

it doesn't matter where the investors come because I'm going to tell you a problem that we started seeing here because I am in web 3 with my clients

2:33:27

and their investors come from a we to environment and it's like I go to for example two biggest

2:33:35

examples binance and Co if I go to binance and buy usdc they will drop me first on B&B

2:33:42

chain because they have the connection if I go to coinbase as a client retail and I bu usdc they will throw me back

2:33:48

into base as a fair why did they do that because obviously Association of chains and and whatever

2:33:54

but the retail investor of the new comr might not even know what's a chain right for them is I buy usdc because I have to

2:34:01

invest in usdc so usdc for them is usdc is usdc because if we were to think in

2:34:07

the real world how it we we would be saying like your euro is different from

2:34:12

the Euro that you received in Colombia why not right it wouldn't make sense or

2:34:17

the dollar that you got in China is different different of the dollar that got in United States and that makes

2:34:24

absolute no sense because for them it's kind of like a dollar issue officially it's a dollar issue officially

2:34:30

regardless of the where I receive it so if we were to put that perspective into

2:34:36

web three for them they got lost and we had a lot of drop downs just because people would be like wait but I'm trying

2:34:43

to pay with usdc and then we will have to come from support and say like yeah but you're in the wrong chain and then

2:34:49

that's kind of like a mind break for it's kind of like what are you saying I don't understand you pushed me to go and

2:34:56

buy usdc and my first and greatest enabler is still an exchange and then I

2:35:01

come to your platform to invest in this Global asset thrown by a client and I cannot even enter because you're telling

2:35:07

me I WR the I bought the run usdc so IM my the pains that are for the

2:35:13

application layer to start on boarding millions of users when we have so many options thus ccip giving you all the

2:35:22

problem because this is a great solution us as Builder we have to always find one great problem to find a better solution

2:35:28

right what happens with the abstraction of layers the issue or gets the asset on

2:35:34

the base layer and then whoever the investors come through ccip it always sends up in in the base and deployment

2:35:42

back can always happen in the layer of their choosing uh obviously for us it's still a work in progress we still have a

2:35:49

couple of Sprints before we actually deploy the full magnitude of ccip but so far our experiments are performing

2:35:55

exceptionally well because the only thing that we're pursuing on this end in brickin as a tokenization platform is

2:36:01

the absolute abstraction of of the chain because I think a lot of options are

2:36:07

what can make my clients lose and I just want them to sign in deploy get and good

2:36:14

to go all right so uh big fan of ccip

2:36:20

then if we're going to go more into the death of real wall asset there's another

2:36:25

thing that we should be discussing and it's the proof of reserves uh proof of reserves became a

2:36:31

big thing back in 2021 with the FDC love fall and many of the exchanges trying to

2:36:37

prove that they have enough assets on their balance to be able to be traded proof of the SES came to be we

2:36:44

abstracting that uh technology to be able to place it into the real wall

2:36:50

asset issuance and how does it work it's still uh it's not so it's quite simple

2:36:56

but I'm going to add the complexity of what it means but it's the same complexity that happens in real world

2:37:02

actually so if you have a the proof of res allows us to uh to stop the function

2:37:10

of mint right so if you say something is worth 1 million you cannot Over Me 1

2:37:16

million so there's a a connection between real world asset value and onchain value all of this it's the

2:37:24

foundation of trust right because people would like to enter into an asset that real value it's connected completely so

2:37:31

there's the function of proof reses at least that's how we we're we're starting to use proof of res in bricken uh

2:37:39

because we foresee that the trust Foundation is key so for example in real

2:37:45

estate again we don't we don't just do real estate I'm just saying for the marketing for the for the sake of the

2:37:51

explanation and not to fall trap into different kind of but this is applicable to anything that's what I wanted to say

2:37:58

actually so the the value that an appraisal of a real estate comes you

2:38:04

know this is think about forget about the CH let's talk about how real estate works you go you want to buy a house you

2:38:11

go and ask for appraisal right because if I tell you that my house is1 million EUR you will be like thank you very much

2:38:17

but who are you is said the you are the pure seller do I trust you I can say yes

2:38:23

I trust you but I rather have a third- party value the the the asset because

2:38:29

that's how a lot of things happen a lot of Auditors if not Auditors wouldn't even have a job economic Financial

2:38:34

Auditors Financial accounts Auditors there's so many Auditors just trying to prove that value does exist and

2:38:40

correspond to the asset itself in the case of real estate it's an appraisal so you will bring an appraisal to get to

2:38:47

the real estate and based on that appraisal will say the house is worth 920 so maybe a negotiation will happen

2:38:54

but at least I know what is the real value according to the city the meter Square the street the condition of the

2:39:02

house Model A lot of different variables so that happens in real world but now in

2:39:09

the onchain value we can say like oh look at these people saying that they want a loan for a hotel that they have

2:39:15

valued themselves in 10 million now a lot of people will be

2:39:20

asking what how do you get to that valuation so appraisals are still needed

2:39:26

one thing is that they're not provided by certain players which could happen in web two offline it can happen and in web

2:39:33

three it can happen but the radical importance is that the good players building the strong trust Foundation

2:39:40

they should like Knack something as a proof Reserve mechanism to Showcase that the value they're bringing on chain

2:39:47

corresponds to the offline value so an appraisal gets digitized it's a function

2:39:53

level that establish it that if 920 is what the appraisal said 920 is the total

2:39:59

value of the mean that you can create because that's the max offering you can offer because that's the max value of

2:40:05

the asset itself so the complication relies which is the same Offline that if

2:40:12

you are I don't know five years long into the last mechanism of

2:40:19

of value creation on chain you will need a new appraisal because values tend to

2:40:25

tend to change so for example if I live we're here in Barcelona for example and 10 years ago maybe you could buy a house

2:40:32

for 200k in 70 M Square Downtown 10 years later that's almost

2:40:38

impossible it's got double or triple the value so you will get a new appraisal that will mean you have to reignite your

2:40:46

function level because your value just got through but it can happen other way as well you know kind of like hey

2:40:51

there's a big burn in the building and or I don't know it got unsafe the area so the pr goes down so it's important

2:40:59

that we don't lock the value on one snapshot we we continuously provide

2:41:05

Snapchats along the way to be able to have a a correct value offline now this

2:41:10

is the complications of rear wall assets which is kind of like how you balance the offline value to the on online

2:41:18

because offline there's no such transparency so actually

2:41:24

there's not such movement so that's why markets are liquid it tends to be very peer-to-peer kind of like one person

2:41:31

selling to exactly the person of their choosing but when you go on chain and you start opening markets it's important

2:41:38

that all these transactions and the True Value gets locked and it's optimized throughout time so it may require for

2:41:45

you to get most various appraises of very measurements of value because you

2:41:52

always want to pinpoint what is the connection between the offline value and the online value because some things may

2:41:59

happen in the future which right now are not there yet because the markets are still getting but if we see Arbitrage

2:42:06

happening in online assets I can tell you that maybe in the near future when markets become more liquid at least in

2:42:12

the real world assets there's going to be a lot of Arbitrage opportunities so that's kind of like something that

2:42:18

through obviously the oracles price feds proof of reserves and all this we want to evate because arbitrate is good for

2:42:24

the Trader but it's never good for the asset itself so uh those are the kind of

2:42:29

like the two functions we we are very much excited obviously we just a lot of different price fits oracles being the

2:42:36

chain link top of the house uh best in best out there without doubt but I'm

2:42:42

going to really establish that if I can provide a really good uh uh what is

2:42:49

say advice studies C IP I think there's a lot of making here and I think the

2:42:55

abstraction of the chain it's actually one is going to bring millions of lock value just because people like one

2:43:02

option one solution and one click so uh that for us is how we doing everything

2:43:10

so um the new just wanted to end up saying that tokenization is definitely

2:43:15

creating new Frameworks um as we said external value being tokenized with

2:43:21

internal value so company looking for funding or Capital third parties then going back internally to employees

2:43:29

there's a lot of new interconnectivity between kind of like third parties internally which is happening and the

2:43:36

most important thing is that transparency uh can bring trust so you can provide trust to your investors you

2:43:43

can provide trust to your employees you can provide trust to whoever wants to go because you just become transparent in

2:43:49

the process so that's becoming more compliant there's a lot of things that legality wise even though it might seem

2:43:57

that it's uh it's one or the other blockchain or legal actually if we were

2:44:02

to really fully understand the power of blockchain and the public ledgers and how everything moves compliance can

2:44:09

definitely become simpler so it's it's all about like that process I've been here building for four years with

2:44:14

bricken I have no doubt we are better than yesterday we still have a long longterm to but I can definitely tell

2:44:21

you that the space that we are currently in 2024 I have never witnessed such growth and such let to say even the word

2:44:28

foral from bigger money institutional jumping in because they find this new uh

2:44:35

technology super efficient a lot of optimizations happening a lot of

2:44:41

trustworthiness so um yeah I wish you all the best on your journey and on my

2:44:46

side it's been an absolute pleasure uh talking to you you have any questions

2:44:51

there's my email uh yeah you can find me on Twitter ew ma or you can find me on

2:44:58

LinkedIn and it's been a pleasure thank you very

2:45:03

much thank you advin this was amazing thank you so much for sharing your real

2:45:09

world experience with real world assets as being mentioned if you have any questions for Edwin you can drop them in

2:45:15

chat now or there is his email and uh socials for the bricken over here

2:45:22

so you can find him and correct uh connect after wise and this uh talk

2:45:29

pretty much sums everything up uh this is it for this boot camp as we briefly

2:45:35

covered uh this page there's like these next steps that you can uh you can

2:45:40

follow along uh to stay in touch with us so uh we mentioned smarton and Hacker

2:45:46

House you definitely encourage to join us there you can always subscrib for for chaining developers newsletter to to

2:45:53

receive uh monthly updates about uh about everything what's what's new uh

2:45:58

inside the chaining ecosystem there is also our devhub on dev. chain. link with fresh new experience uh so I encourage

2:46:06

you to check that out you can also get in touch with our developer experts uh

2:46:12

obviously whenever you want to build something with chaining your first number one stop should always always

2:46:19

always be the official documentation so that's always up to date and available on dogs. chain. link and in general if

2:46:25

you want to learn more about chaining there is the official main website chain. link so yeah that was it um thank

2:46:32

you for joining us for these past two days uh uh and yeah uh keep working keep

2:46:40

studying deadline uh for homework is October 4th at midnight ET uh if if you

2:46:49

have any followup questions there is our Discord and if you have any followup

2:46:54

questions for edwiin there was his email and other contacts in the getbook thank

2:47:01

you and see you soon