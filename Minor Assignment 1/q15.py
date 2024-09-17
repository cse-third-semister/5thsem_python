"""
15. Assume you start investing in Mutual Funds with Rs. 1000 and plan to leave your money invested.
 Calculate and display how much money you will have after 10, 20 and 30 years. Use the following
 formula for determining these amounts:
 a =p(1+r)n
 where p (principal) = Rs. 1000,
 r (annual rate of return) = 12
 n (number of years) = 10, 20, 30,
 a (amount on deposit at the end of the nth year).
 Disclaimer: Investing in Mutual Funds is subject to Market Risks. Do your due diligence before
 investing.
"""
p = 1000
r = 12
for i in [10,20,30]:
  
    print(f'money for {i}th year is ,{p*((1+r)**i)}')



# money for 10th year is ,137858491849000
# money for 20th year is ,19004963774880799438801000
# money for 30th year is ,2619995643649944960380551432833049000