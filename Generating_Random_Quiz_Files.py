"""Creates 35 different quizzes.
•	 Creates 50 multiple-choice questions for each quiz, in random order.
•	 Provides the correct answer and three random wrong answers for each
question, in random order.
•	 Writes the quizzes to 35 text files.
•	 Writes the answer keys to 35 text files.
This means the code will need to do the following:
•	 Store the states and their capitals in a dictionary.
•	 Call open(), write(), and close() for the quiz and answer key text files.
•	 Use random.shuffle() to randomize the order of the questions and
multiple-choice options."""


#! python  3
#step 1: Store the quiz data in a dictionary
capitals={'Abia':'Umuahia',
          'Adamawa':'Yola',
          'Akwa Ibom':'Uyo',
          'Anambra':'Awka',
          'Bauchi':'Bauchi',
          'Bayelsa':'Yenagoa',
          'Benue':'Makurdi',
          'Borno':'Maiduguri',
          'Cross River':'Calabar',
          'Delta':'Asaba',
          'Ebonyi':'Abakaliki',
          'Edo':'Benin',
          'Ekiti':'Ado Ekiti',
          'Enugu':'Enugu',
          'Gombe':'Gombe',
          'Imo':'Owerri',
          'Jigawa':'Dutse',
          'Kaduna':'Kaduna',
          'Kano':'Kano',
          'Kastina':'Kastina',
          'Kebbi':' Birnin Kebbi',
          'Kogi':'Lokoja',
          'Kwara':'Ilorin',
          'Lagos':'Ikeja',
          'Nasarawa':'Lafia',
          'Niger':'Minna',
          'Ogun':'Abeokuta',
          'Ondo':'Akure',
          'Osun':'Oshogbo',
          'Oyo':'Ibadan',
          'Plateau':'Jos',
          'Rivers':'Port Harcourt',
          'Sokoto':'Sokoto',
          'Taraba':'Jalingo',
          'Yobe':'Damaturu',
          'Zamfara':'Gusau',
          'FCT':'Abuja'}

