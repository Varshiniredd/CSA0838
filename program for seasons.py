month=input("input of the month(e.g.january,february etc.):")
day =int(input("input the day:"))
if month in ('january','february','march'):
    season='winter'
elif month in ('april','may','june'):
    season='spring'
elif month in('july','august','september'):
    season='summer'
else:
    season='autumn'
if(month=='march')and(day>19):
    season='spring'
elif(month=='june')and(day>20):
    season='summer'
elif(month=='september')and(day>21):
    season='autumn'
elif(month=='December')and(day>20):
    season='winter'
print("seasonis",season)
    

    