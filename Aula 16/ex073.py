premier = ('Liverpool', 'Manchester City', 'Leicester', 'Chelsea', 'Manhchester United', 'Wolverhampton', 'Sheffield United',
           'Tottenham', 'Arsenal', 'Burnley', 'Crystal Palace', 'Everton', 'Newcastle', 'Southamptom', 'Brighton', 'West Ham',
           'Watford', 'Bournemouth', 'Aston Villa', 'Norwich')
print(f'Os 5 primeiros da Premier League são {premier[0:5]}')
print(f'Os 4 últimos da Premier League são {premier[16:]}')
print(sorted(premier))
print(f'A colocação do Leicester é {premier.index("Leicester")+1}')
