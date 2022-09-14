month=input("enter the month:")
day=int(input("enter the date:"))
if month in ('January', 'February','March'):
    season='summer'
elif month in ('April','May','June'):
    season='spring'
elif month in ('July','August','September'):
    season='fall'
else:
    season='autumn'

if month=='March' and day>20:
    season='summer'
elif month=='June' and day>21:
    season='spring'
elif month=='September' and day>22:
    season='fall'
elif season=='December' and day>21:
    season='winter'

    

print("the season on",month,day,"is",season)

    

