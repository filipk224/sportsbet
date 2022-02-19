## Calculative
from math import ceil

def compare(response, high, low):
    print('\n### Entering: ', response.request.meta['allbets'][0]['Sport']+',', response.request.meta['allbets'][0]['League'])

    results = []
    ladder=response.request.meta['ladder']

    try:
        ladder[0]
    except:
        print('* ', response.request.meta['allbets'][0]['League'], 'ladder unaffirmed')
    else:
        for game in response.request.meta['allbets']:
            
            # Participant Position
            index1, index2 = None, None
            for name in ladder:
                if index1 == None or index2 == None:
                    if game['Participant1']['Name'] in name:
                        index1=ladder.index(name)
                    elif game['Participant2']['Name'] in name:
                        index2=ladder.index(name)
                else:
                    break
            
            # Qualify
            try:
                if index1<=high and index2>=low:
                    # results.append(game)
                    print('\n', game)
                elif index1>=low and index2<=high:
                    # results.append(game)
                    print('\n', game)
            except:    
                if index1 == None or index2 == None:
                    print('\n', ladder, '\n')

                    # Participant 1
                    if index1 == None:
                        print(" : ['"+game['Participant1']['Name']+"'],", 'not in list')
                        
                        for participant_split in game['Participant1']['Name'].split(' '):
                            for position in ladder:
                                if len(position)!=1:
                                    for sub_position in position:
                                        for name in sub_position:
                                            for split in name.split(' '):
                                                if participant_split.lower() == split.lower():
                                                    print('  Suggestion: ', f"'{name}'")
                                                    continue
                                else:
                                    for name in position:
                                        for split in name.split(' '):
                                            if participant_split.lower() == split.lower():
                                                print('  Suggestion: ', f"'{name}'")
                                                continue
                    else:
                        print(" : ['"+game['Participant1']['Name']+"'],", 'IS in list')
                    
                    # Participant 2
                    if index2 == None:
                        print(" : ['"+game['Participant2']['Name']+"'],", 'not in list')

                        for participant_split in game['Participant2']['Name'].split(' '):
                            for position in ladder:
                                if len(position)!=1:
                                    for sub_position in position:
                                        for name in sub_position:
                                            for split in name.split(' '):
                                                if participant_split.lower() == split.lower():
                                                    print('  Suggestion: ', f"'{name}'")
                                                    continue
                                else:
                                    for name in position:
                                        for split in name.split(' '):
                                            if participant_split.lower() == split.lower():
                                                print('  Suggestion: ', f"'{name}'")
                                                continue
                    else:
                        print(" : ['"+game['Participant2']['Name']+"'],", 'IS in list')
                                

                    print('\n')

    # response.request.meta['results'] = results
    # return response  ## For when ready
    return None


def group_split(response, high, low, first='Group A', second='Group B', split='Even'):
    ladder=response.request.meta['ladder']

    print('# Splitting: ', response.request.meta['allbets'][0]['Sport']+',', response.request.meta['allbets'][0]['League'])
    
    if split == 'Even':
        split = int(len(ladder)/2)
    else:
        split=split[0]
    
    # Seperate
    bet_seperate={first: [], second: []}
    for bet in response.request.meta['allbets']:

        # First split in ladder
        for name in ladder[:split]:
            if (bet['Participant1']['Name'] in name) or (bet['Participant2']['Name'] in name):
                bet['League']=f'{bet["League"]}, {first}'
                bet_seperate[first].append(bet)
                break

        # Second split in ladder
        for name in ladder[split:]:
            if (bet['Participant1']['Name'] in name) or (bet['Participant2']['Name'] in name):
                bet['League']=f'{bet["League"]}, {second}'
                bet_seperate[second].append(bet)
                break
            
    # First Group Compare
    response.request.meta['ladder']=ladder[:split]
    response.request.meta['allbets']=bet_seperate[first]
    if response.request.meta['allbets']:
        compare(response, high, low)

    # Second Group Compare
    response.request.meta['ladder'] = ladder[split:]
    response.request.meta['allbets'] =bet_seperate[second]
    if response.request.meta['allbets']:
        compare(response, high, low)


def highlowTest(response):
    ## Calibrate the Sports

    Rating = 3.5
    print('**High Low Test:', response.request.url[36:])

    ladder = response.request.meta['ladder']
    split = len(ladder)//Rating
    high = ceil(split/2)-1
    low = len(ladder)-(split//2)

    print(len(ladder), high, low)