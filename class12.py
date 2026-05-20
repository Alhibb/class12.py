import matplotlib.pyplot as plt

prices = [
    87,    
    145,   
    145,  
    145,   
    145,   
    145,  
    165,   
    185,   
    617,   
    1030,  
    1100,  
    1150   
]
years = list(range(2015, 2027))

plt.plot(years, prices)

plt.show()