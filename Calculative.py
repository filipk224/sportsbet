## Calculative
def compare(response, high, low):
    print('### Entering: ', response.request.meta['allbets'][0]['Sport']+',', response.request.meta['allbets'][0]['League'])

    #print (response.request.meta['allbets'])
    #print (response.request.meta['ladder'])

    try:
        response.request.meta['ladder'][0]
    except:
        print('* ', response.request.meta['allbets'][0]['League'], 'ladder unaffirmed')
    else:
        for game in response.request.meta['allbets']:
            if response.request.meta['ladder'].index(game['Participant1']['Name'])<=high:
                if response.request.meta['ladder'].index(game['Participant2']['Name'])>=low:
                    print(game)
            elif response.request.meta['ladder'].index(game['Participant1']['Name'])>=low:
                if response.request.meta['ladder'].index(game['Participant2']['Name'])<=high:
                    print(game)

    ## Will find a suitable way to return/yield a key/list
    return None
