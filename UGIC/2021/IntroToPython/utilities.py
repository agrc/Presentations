def create_county_key(name, separator='_'):

    cleaned_name = name.split(separator)[-1].casefold().replace(' ',
                                                                '').replace(
                                                                    '.', '')

    if cleaned_name == 'richland':
        cleaned_name = 'rich'

    return cleaned_name


print(
    'This is from the script but will run any time the code is imported or run'
)
cleaned = create_county_key('UT_SANJUAN')
print(cleaned)

if __name__ == '__main__':
    print('This is from the script!')
    cleaned = create_county_key('UT_CACHE')
    print(cleaned)