print('Hello, welcome to trivia!')

ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 20

if ans.lower() == 'yes':
    ans = input('1. Which Jamaican runner is an 11-time world champion and holds the record in the 100 and 200-meter race? ')
    if ans.lower() == 'usain bolt':
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is Usain Bolt')


    ans = input('2. How many soccer players should each team have on the field at the start of each match? ')
    if (ans == '11'or ans.lower() =='eleven'):
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is eleven or 11')


    ans = input('3. What year was the very first model of the iPhone released? ')
    if ans == '2007':
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is 2007')


    ans = input('4. What’s the shortcut for the “copy” function on most computers? ')
    if (ans.lower() == 'ctrl c' or ans.lower() == 'control c'):
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answers are either ctrl c or control c.')


    ans = input('6. What does “HTTP” stand for? ')
    if ans.lower() == 'hypertext transfer protocol':
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is Hypertext Transfer Protocol')


    ans = input('7. What is often seen as the smallest unit of memory? ')
    if (ans.lower() == 'kilobyte' or ans.lower() == 'kilobite'):
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is kilobyte.')


    ans = input('8. Is Java a type of Operating System?(yes/no) ')
    if ans.lower() == 'no':
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is no')


    ans = input('9. What is meteorology the study of? ')
    if ans.lower() == 'the weather' or ans.lower() == 'weather':
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is the weather')


    ans = input('10. Which planet is the hottest in the solar system? ')
    if ans.lower() == 'venus':
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is Venus')


    ans = input('11. What part of the atom has no electric charge? ')
    if ans.lower() == 'neutron':
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is neutron')


    ans = input('12. Which natural disaster is measured with a Richter scale? ')
    if ans.lower() == 'earthquakes' or ans.lower() == 'earthquake'):
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is earthquakes.')


    ans = input('13.  What is the symbol for potassium? ')
    if ans.lower() == 'k':
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is K.')


    ans = input('14. Which planet has the most gravity? ')
    if ans.lower() == 'jupiter':
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is Jupiter.')


    ans = input('15. Which animal can be seen on the Porsche logo? ')
    if ans.lower() == 'horse':
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is horse.')


    ans = input('16. Which kind of alcohol is Russia notoriously known for? ')
    if ans.lower() == 'vodka':
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is vodka.')


    ans = input('17. Which country is responsible for giving us pizza and pasta? ')
    if ans.lower() == 'italy':
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is Italy.')


    ans = input('18. Which cartoon character lives in a pineapple under the sea? ')
    if ans.lower() == 'spongebob squarepants':
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is Spongebob Squarepants.')


    ans = input('19. What was the name of the actor who played Jack Dawson in Titanic? ')
    if ans.lower() == 'leonardo dicaprio':
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is Leonardo DiCaprio.')


    ans = input('20. What does the square root of 144 equal? ')
    if (ans == '12' or ans.lower() == 'twelve'):
       score += 1
       print('Correct')
    else:
        print('Incorrect')
        print('The correct answer is 12.')

    print('Thank you for playing, you got', score, 'questions correct.')
    mark = (score/total_q) * 100

    print("Mark:", str(mark) + '%')
    print('Goodbye, Stay home and Stay Safe')
   
if ans.lower() == 'no':
    print('Goodbye, come back when you are ready :)')
