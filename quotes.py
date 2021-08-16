import random

quotes = [
  '“Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do.” ― Pelé, Brazillian pro footballer',
  '“There are no secrets to success. It is the result of preparation, hard work, and learning from failure.” ― General Colin Powell, former US Secretary of State',
  '“In order to succeed, your desire for success should be greater than your fear of failure.” ― Bill Cosby, stand-up comedian',
  '“Success consists of going from failure to failure without loss of enthusiasm.” ― Winston Churchill, former Prime Minister of the United Kingdom','“Striving for success without hard work is like trying to harvest where you haven’t planted.” ― David Bly, American politician','“Success is the sum of small efforts, repeated day in and day out.” ―  Robert Collier, self-help author','“Success isn’t overnight. It’s when every day you get a little better than the day before. It all adds up.” ― Dwayne Johnson, actor and former pro wrestler','The secret of success is to do the common things uncommonly well.” ― John D. Rockefeller, widely considered the richest man in modern history','“You may encounter many defeats but you must not be defeated. In fact, it may be necessary to encounter the defeats, so you can know who you are, what you can rise from, how you can still come out of it.” ― Maya Angelou, American civil rights activist and poet','“Failure is the opportunity to begin again more intelligently.” ― Henry Ford, industrialist founder of the Ford Motor Company','“And why do we fall, Bruce? So we can learn to pick ourselves up.” ― Thomas Wayne, Batman’s Dad, in ‘Batman Begins’','“Nothing is impossible. The word itself says ‘I’m Possible’.” ― Audrey Hepburn, actress and humanitarian','“There are two kinds of people in this world: those who want to get things done and those who don’t want to make mistakes.” ― John Maxwell, author and leadership expert','“The only place where success comes before work is in the dictionary.” ― Vidal Sassoon, hairstylist and philanthropist','“There are no shortcuts to any place worth going.” ― Beverly Sills, operatic soprano','“I find that the harder I work, the more luck I seem to have.” ― Thomas Jefferson, 3rd US president','“I’m not telling you it is going to be easy — I’m telling you it’s going to be worth it.” ― Art Williams, insurance billionaire','"A real ninja is one who endures no matter what gets thrown at him … All you do need, is the guts to never give up. - Jiraiya.','"A person grows up when he’s able to overcome hardships. Protection is important, but there are some things that a person must learn on his own." - Jiraiya.','"People who continue to put their lives on the line to defend their faith become heroes and continue to exist on in legend." - Naruto Uzumaki.', '"If you don’t like your destiny, don’t accept it. Instead have the courage to change it the way you want it to be." - Naruto Uzumaki.',
  '"Hard work is worthless for those that don’t believe in themselves." - Naruto Uzumaki.',
  '"Power is not will, it is the phenomenon of physically making things happen." - Madara Uchiha.',
  '"I won’t give up. I’ll never give up again. So I’ll win, no matter what! I’ll survive no matter what." - Mikasa Ackerman',
  '"People who can’t throw something important away, can never hope to change anything." - Armin Arlert.',
  '"If you win you live. If you lose you die. If you don’t fight, you can’t win." - Eren Jaeger.',
  '"You have to figure it out. Stand up and walk. Keep moving forward. You’ve got two good legs. So get up and use them. You’re strong enough to make your own path." - Edward Elric',
  '"Like I always say, can’t find a door? Make your own." - Edward Elric',
  '"A life that lives without doing anything is the same as a slow death." - Lelouch',
  '"Before creation there must be destruction. If my soul stands in the way, then I’ll toss it aside. Yes, I have no choice but to move forward." - Lelouch Lamperouge',
  '"Whether you win or lose, looking back and learning from your experience is a part of life." -All Might',
  '"Become the hero you want to be."  -Shoto Todoroki',
  '"No matter how scary it gets, you must always wear a smile that says... I’m fine!" -Nana Shimura',
  '"All men are not created equal. This was the reality I learned about society at the young age of four. And that was my first and last setback." -Izuku Midoriya'



]

def get_quote():
  return random.choice(quotes)