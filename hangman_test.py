def game(string):

    word_to_guess = string.upper()
    second = []
    organ = ['arms', 'legs', 'dick', 'heart', 'head']
    user_input = []
    chances = 0
    while chances < 5:
        the_second_input_for_checking_value = []
        guess = input('Guess? ').upper()
        if guess in word_to_guess:
            for x in word_to_guess:
                for y in guess:
                    if x == ' ':
                        the_second_input_for_checking_value.append(' ')
                    elif x == y:
                        the_second_input_for_checking_value.append(x)
                    else:
                        the_second_input_for_checking_value.append('_')

            if user_input == []:
                user_input = the_second_input_for_checking_value

            for index_for_replacing_with_and_from in range(len(the_second_input_for_checking_value)):
                if the_second_input_for_checking_value[index_for_replacing_with_and_from] == '_':
                    second.append(user_input[index_for_replacing_with_and_from])
                else:
                    second.append(the_second_input_for_checking_value[index_for_replacing_with_and_from])

            user_input = second
            second = []
            return_list_as_string = ("".join(user_input))
            print(return_list_as_string)
            if return_list_as_string == word_to_guess:
                print(f'!!!!CONGRATULATIONS YOU WON!!!!')
                chances = 5

        else:
            if chances < 2:
                has_have = 'have'
            else:
                has_have = 'has'
            print(f'!!Your {organ[chances]} {has_have} been incinerated!!')
            chances = chances + 1
            if chances == 5:
                print(f'_______________YOU LOSE_______________')

#list_of_words = ['oven', 'supplement', 'random', 'suspect', 'quora','digital','central', 'undertaker', '']
game('apple')
