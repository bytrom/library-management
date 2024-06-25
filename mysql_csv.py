import mysql.connector as sq
from mysql.connector import Error as sqlerror


Books = ['Famous Five:Five go to demons rocks', 'The Vampire Diaries:The Compelled', 'Make Me', '61 Hours', 'My Days', 'Waiting for the Mahatma', 'Frankstein', 'The Hobbit', 'Aleph', 'The Secret', 'Wings of Fire: The Hidden Kingdom', 'Harry Potter And the Prisnor of Azkaben', 'Heroes of Olympus:The Demigod Diaries', 'Where Have All Leaders Gone',
         'Mighter than the Sword', 'Capital', 'Long walk to Freedom', 'Arise Awake', 'Sense and Sensibility', 'The Namesake', 'Sita:Warrrior of Mithila', 'A Short History of World', 'Panchatantra', 'The Davinci Code', 'Gone with the Wind', 'Pradyumna', 'The Trails of Apollo:The Dark Proplecy', 'The Shakespeare Mask', 'Murder on the orient express', 'The Throne of Fire']
Author = ['Enid Blyton', 'L.J.Smith', 'Lee Child', 'Lee Child', 'R K Narayan', 'R K Narayan', 'Mary Shelly', 'JRR Tolken', 'Paulo Coelho', 'Rhonda Byrne', 'Sutherland', 'J K Rowling', 'Rick Riordan', 'Lee Jacocca', 'Jeffrey Archer',
          'John Lance', 'Nelson Mandela', 'Rashmi Bansal', 'Jane Austen', 'Jhumpa Lahiri', 'Amish', 'H G Wells', 'Vishnu Sharma', 'Dan Brown', 'Margaret Mitchaell', 'Usha Narayanan', 'Rick Riordan', 'Frohlich', 'Agatha Christie', 'Rick Riordan']
Acc_No = [1686, 2732, 2512, 2511, 920, 1013, 1536, 1438, 1950, 1456, 3200, 1573, 1721, 1495,
          1407, 3032, 981, 965, 1991, 1355, 1755, 708, 1518, 1354, 1138, 926, 1115, 1774, 357, 1564]
Price = [369, 541, 100, 245, 635, 754, 412, 456, 126, 458, 365, 800, 451, 320,
         195, 713, 369, 145, 651, 500, 250, 300, 368, 345, 235, 456, 122, 678, 496, 438]
Catalouge = ['R1S1A', 'R1S4B', 'R3S1E', 'R1S2D', 'R4S1A', 'R4S2E', 'R3S2A', 'R1S1B', 'R1S4C', 'R1S2A', 'R3S2C',
             'R1S2C', 'R4S2C', 'R3S1C', 'R1S3D', 'R2S1A', 'R2S3B', 'R2S2C', 'R3S1D', 'R2S2B', 'R4S3B',
             'R2S4A', 'R1S3E', 'R2S3D', 'R2S2E', 'R3S4E', 'R2S2D', 'R4S4D', 'R2S4E', 'R4S1D']
Genre = ['Mystery', 'Fiction', 'Crime', 'Crime', 'Drama', 'Semi-Biography', 'Sci-Fi', 'Fantasy', 'Drama', 'Non-Fiction', 'Fantasy', 'Fantasy', 'Fantasy', 'Non-Fiction', 'Fiction', 'Non-Fiction',
         'Auto Biography', 'Non-Fiction', 'Romance', 'Fantasy', 'Mythical Fiction', 'Sci-Fi', 'Fiction', 'Thriller', 'Romance', 'Mythical-Fiction', 'Fantasy', 'Detective', 'Crime-Fiction', 'Fantasy']
ab = ['Pranav Sai', 'Mustaq', 'Vasanth', 'NONE', 'Mukesh', 'NONE',
      'NONE', 'Sandeep', 'Kalim', 'NONE', 'Saketh', 'Ranga', 'NONE',
      'NONE', 'Bhargav', 'Rahul', 'NONE', 'NONE', 'NONE', 'Prasad',
      'Akash', 'Sameer', 'Sai', 'NONE', 'Pranav', 'Abhiram', 'Tejus',
      'Abhishek', 'Sai Kiran', 'NONE']
Magazines = ['Pratiyogita Darpan(E)', 'Pratiyogita Darpan(H)', 'Competition Success Review', 'Outlook', 'Sports Star', 'Champak', 'Economic Political', 'Better Photography', 'Front Line', 'MGT Maths', 'MGT Physics', 'MGT CHemistry', 'Tell Me Why', 'The Week', 'Sanctuary Asia', 'Down To Earth',
             'Tinkle', 'Digital', 'Health', 'Science Reporter', 'Electronics For You', 'National Geography Magazine', 'National Geography Kids', 'Outlook Spotlight', 'Highlights Champs', 'World Focus', 'PC Quest', 'Gobar Times', 'Parent Edge', 'Biology Today', 'Current Science', 'Wisdom', 'TIME']
Magazines_ = ['GK & GA', 'GK & GA', 'GK & GA', 'Current Topics', 'Sports', 'Entertainment', 'Poilitics', 'Photography', 'Current Topics', 'Subject oriented', 'Subject oriented', 'Subject oriented', 'GK & GA', 'Current Awareness', 'Wildlife', 'Current Awareness',
              'Entertainment', 'Technology', 'Health', 'Science', 'Technology', 'Wildlife', 'Wildlife', 'Current Awareness', 'Entertainment', 'Political', 'Current Awareness', 'Political', 'Guidance', 'Subject Oriented', 'Science', 'Entertainment', 'Current Affairs']

Magazines_Quantity = [10, 4, 10, 6, 4, 8, 5, 9, 4, 5, 6, 7, 3,
                      2, 5, 6, 4, 6, 5, 3, 4, 2, 6, 6, 5, 4, 7, 5, 3, 9, 7, 8, 3]

New_Arrivals_Books = []
New_Arrivals_Authors = []
Order_Books = []
Total_Amount = 0

length = len(Magazines_)

conn = sq.connect(host='localhost', user='root',
                  password='student', database='library')
cursor = conn.cursor()

for i in range(length):
    zero = Magazines[i]
    one = Magazines_[i]
    two = Magazines_Quantity[i]
    l = [zero, one, two]

    cursor.execute(
        f"INSERT INTO magazines VALUES ('{l[0]}', '{l[1]}', {l[2]})")
    conn.commit()
