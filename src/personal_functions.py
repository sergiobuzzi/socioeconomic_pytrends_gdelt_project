def create_graphs(df):
    '''under construction''' 
    #plt.figure()
    dx = df.plot.line( figsize = (9,6), title ="ey")
    dx.set_xlabel('Date')
    dx.set_ylabel('Trends Index')
    dx.tick_params(axis='both', which='major', labelsize=13)
    plt.show()
