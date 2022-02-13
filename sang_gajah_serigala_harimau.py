def sgsh(cerita):
    result = []
    counter = 1
    for i in cerita:
        counter += 1
        if i == 'serigala':
            result.append(i)
        elif i == 'harimau':
            result.append(i)
        elif i == 'sang' and cerita[counter+1] == 'gajah':
            result.append('sang gajah')
            
    return result


if __name__ == "__main__":
    input = 'Berikut adalah kisah sang gajah. Sang gajah memiliki teman serigala bernama DoeSang. Gajah sering dibela oleh serigala ketika harimau mendekati gajah.'
    cerita = input.strip('.').strip(' ').split()
    print(sgsh(cerita))
